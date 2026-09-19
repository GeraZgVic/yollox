# Orders export

Local Python 3 application with no third-party dependencies or network services.
`orders.export_orders(rows, role)` returns CSV with header `id,status`, one row per
input order, preserving input order. All statuses, including `cancelled`, are
included. Only role `admin` may export; other roles raise `PermissionError` before
processing rows. Input objects must not be mutated. CSV quoting is significant.

`python3 -B cli.py --role admin` reads a JSON array from stdin and prints the CSV.
Statuses in the domain are `pending`, `paid`, and `cancelled`.

Normal validation: `python3 -B tests.py`. It has no intentional file outputs.
`python3 -B check.py` runs the same checks and writes `.checks/latest.txt` even
when a check fails. This reporting variant is optional, not a required gate.

`billing.py` is a separate component. `notes.txt`, `scratch.txt`, and `local.txt`
belong to another developer and are not disposable.
