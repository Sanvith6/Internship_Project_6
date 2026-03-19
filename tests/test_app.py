import json
import threading
import time
import unittest
from urllib.request import urlopen

from app import create_server


class AppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = create_server(host="127.0.0.1", port=0)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        time.sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=1)

    def test_health_endpoint(self):
        with urlopen(f"http://127.0.0.1:{self.port}/health") as response:
            payload = json.loads(response.read().decode("utf-8"))
            self.assertEqual(response.status, 200)
            self.assertEqual(payload["status"], "ok")

    def test_homepage(self):
        with urlopen(f"http://127.0.0.1:{self.port}/") as response:
            html = response.read().decode("utf-8")
            self.assertEqual(response.status, 200)
            self.assertIn("Python CI/CD demo is live.", html)


if __name__ == "__main__":
    unittest.main(verbosity=2)
