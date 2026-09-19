from pathlib import Path
import subprocess
import sys


result = subprocess.run([sys.executable, "-B", "tests.py"], capture_output=True, text=True)
Path(".checks").mkdir(exist_ok=True)
Path(".checks/latest.txt").write_text(result.stdout + result.stderr)
print(result.stdout + result.stderr, end="")
raise SystemExit(result.returncode)
