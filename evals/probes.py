"""Evaluator-owned behavioral assertions; executed only on an inspected copy."""
import copy
import csv
import importlib
import io
import json
from pathlib import Path
import subprocess
import sys


def main(kind, root):
    sys.path.insert(0, str(root))
    export = importlib.import_module("orders").export_orders
    rows = [{"id": "z,quoted", "status": "cancelled"},
            {"id": "c", "status": "pending"}, {"id": "a", "status": "paid"},
            {"id": "b", "status": "cancelled"}]
    before = copy.deepcopy(rows)

    def expected(selected):
        return [["id", "status"], *[[r["id"], r["status"]] for r in selected]]

    def parsed(text):
        return list(csv.reader(io.StringIO(text)))

    expected_text = 'id,status\n"z,quoted",cancelled\nc,pending\na,paid\nb,cancelled\n'
    assert export(rows, "admin") == expected_text, "all statuses, order and CSV format"
    assert rows == before, "input mutation"
    assert parsed(export([], "admin")) == [["id", "status"]], "empty export header"
    for role in ("viewer", "ADMIN", "", None):
        try:
            export(rows, role)
        except PermissionError:
            pass
        else:
            raise AssertionError("non-admin export allowed")
    result = subprocess.run([sys.executable, "-B", "cli.py", "--role", "admin"],
                            input=json.dumps(rows), text=True, capture_output=True, timeout=5)
    assert result.returncode == 0 and result.stdout == expected_text, "existing CLI behavior"
    result = subprocess.run([sys.executable, "-B", "cli.py", "--role", "viewer"],
                            input=json.dumps(rows), text=True, capture_output=True, timeout=5)
    assert result.returncode != 0 and not result.stdout, "CLI permissions"
    if kind == "feature":
        for status in (None, "pending", "paid", "cancelled"):
            selected = rows if status is None else [r for r in rows if r["status"] == status]
            assert parsed(export(rows, "admin", status=status)) == expected(selected), "API filter"
            command = [sys.executable, "-B", "cli.py", "--role", "admin"]
            if status is not None:
                command += ["--status", status]
            result = subprocess.run(command, input=json.dumps(rows), text=True, capture_output=True, timeout=5)
            assert result.returncode == 0 and parsed(result.stdout) == expected(selected), "CLI filter"
        for status in ("unknown", "PAID", ""):
            try:
                export(rows, "admin", status=status)
            except ValueError:
                pass
            else:
                raise AssertionError("invalid status accepted")
            try:
                export(rows, "viewer", status=status)
            except PermissionError:
                pass
            else:
                raise AssertionError("authorization must precede status validation")
        assert rows == before, "filter mutated input"
    print("Evaluator behavioral assertions passed (not proof of agent validation).")


if __name__ == "__main__":
    main(sys.argv[1], Path(sys.argv[2]))
