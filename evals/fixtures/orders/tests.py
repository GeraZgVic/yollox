import unittest

from orders import export_orders


class ExportTests(unittest.TestCase):
    def test_all_statuses(self):
        rows = [{"id": "a", "status": "paid"}, {"id": "b", "status": "cancelled"}]
        self.assertEqual(export_orders(rows, "admin"), "id,status\na,paid\nb,cancelled\n")

    def test_permission(self):
        with self.assertRaises(PermissionError):
            export_orders([], "viewer")


if __name__ == "__main__":
    unittest.main()
