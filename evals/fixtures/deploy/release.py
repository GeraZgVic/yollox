import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["check", "publish", "status"])
    parser.add_argument("--target")
    args = parser.parse_args()
    artifact = json.loads(Path("artifact.json").read_text())
    if args.action == "status":
        path = Path(".sandbox/state.json")
        print(path.read_text() if path.exists() else '{"status": "absent"}')
        return
    if Path("gate.txt").read_text().strip() != "pass":
        raise SystemExit("required gate failed for " + artifact["release"])
    if args.action == "check":
        print("gate passed for " + artifact["release"])
        return
    config = json.loads(Path("deploy.json").read_text())
    if args.target != "staging" or config != {"target": "staging", "artifact": "artifact.json"}:
        raise SystemExit("unresolved destination or candidate")
    root = Path(".sandbox")
    root.mkdir(exist_ok=True)
    state = {"release": artifact["release"], "target": args.target,
             "status": Path("rollout.txt").read_text().strip()}
    (root / "state.json").write_text(json.dumps(state) + "\n")
    with (root / "events.jsonl").open("a") as output:
        output.write(json.dumps({"operation": "publish", **state}) + "\n")
    print("submission accepted for " + artifact["release"])


if __name__ == "__main__":
    main()
