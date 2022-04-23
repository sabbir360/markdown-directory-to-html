import unittest
import os

from app import directory_tree


class AppTestSuit(unittest.TestCase):
    path = None

    def setUp(self) -> None:
        self.path = f'{os.getcwd()}{os.sep}tests{os.sep}mock_directory'

    def test_directory_logic(self):
        dir_tree = len(directory_tree(self.path))
        assert dir_tree == 1430
