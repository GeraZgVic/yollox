import argparse
import json
import sys

from orders import export_orders


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--role", required=True)
    args = parser.parse_args()
    rows = json.load(sys.stdin)
    sys.stdout.write(export_orders(rows, args.role))


if __name__ == "__main__":
    main()
