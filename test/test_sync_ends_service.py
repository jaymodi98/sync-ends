import sys
import unittest
from unittest.mock import Mock
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))
from src.sync_ends_service import SyncEnd  # noqa: E402


class TestParser(unittest.TestCase):
    def setUp(self):
        self.sync_end = SyncEnd(
            "SAM-Key-123fg", "test server", 9, "sample channel", "123ff"
        )

    def test_get_newly_added_message(self):
        end_point_list = []
        endpoint1 = Mock()
        endpoint1.id = "385f7848-62db-4435-b7cf-820c3e7e5097"
        endpoint1.name = "Endpoint 1"
        endpoint1.authentication = None
        endpoint1.method = "POST"
        endpoint1.header = []
        endpoint1.url = "http://127.0.0.1:5002/endpoint?ep_id=1"
        endpoint1.query_parameters = [{"key": "ep_id", "value": "1"}]
        end_point_list.append(endpoint1)
        endpoint2 = Mock()
        endpoint2.id = "3234dt48-62db-4435-b7cf-820c3e7e5097"
        endpoint2.name = "Endpoint 2"
        endpoint2.authentication = None
        endpoint2.method = "POST"
        endpoint2.header = []
        endpoint2.url = "http://127.0.0.1:5003/endpoint?ep_id=2"
        endpoint2.query_parameters = [{"key": "ep_id", "value": "2"}]
        end_point_list.append(endpoint2)
        title = (
            "Following end points are newly added in the collection :: \n\n"
        )
        output = (
            "\t"
            + str(1)
            + ")  "
            + "Endpoint 1"
            + "\n"
            + "\t"
            + "URL: "
            + "http://127.0.0.1:5002/endpoint?ep_id=1"
            + "\n"
            + "\t"
            + "Request Method: "
            + "POST"
            + "\n\n"
            + "\t"
            + str(2)
            + ")  "
            + "Endpoint 2"
            + "\n"
            + "\t"
            + "URL: "
            + "http://127.0.0.1:5003/endpoint?ep_id=2"
            + "\n"
            + "\t"
            + "Request Method: "
            + "POST"
            + "\n\n"
        )
        result = self.sync_end.get_newly_added_message(end_point_list)
        print("actual:", result)
        print("expected", title + output)
        self.assertEqual(result, title + output)


if __name__ == "__main__":
    unittest.main()