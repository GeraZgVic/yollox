import os


def make_client():
    if not os.environ.get("REPORT_TOKEN"):
        raise RuntimeError("REPORT_TOKEN is required")
    return {"configured": True}
