import unittest

from app import app


class AppTestSuit(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_unwanted_request_home(self):
        response = self.client.post("/", data={"content": "hello world"})
        assert response.status_code == 405

    def test_generic_error(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_security_error(self):
        response = self.client.get("/?dir=..&file=README.md")
        assert response.status_code == 403

    def test_file_not_found_error(self):
        response = self.client.get("/?dir=intentional_404&file=NO_README.md")
        assert response.text.find("Please select file from left side tree.") != -1

