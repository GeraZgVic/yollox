import csv
import io


def export_orders(rows, role):
    if role != "admin":
        raise PermissionError("admin required")
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["id", "status"])
    for row in rows:
        writer.writerow([row["id"], row["status"]])
    return output.getvalue()
