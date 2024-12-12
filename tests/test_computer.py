import unittest
from source.computer import computer_pon
from unittest.mock import patch

class TestComputer(unittest.TestCase):
    @patch("random.choice", return_value="グー")
    def test_computer1(self, mock_random):
        self.assertEqual(computer_pon(), "グー")
        
    @patch("random.choice", return_value="チョキ")
    def test_computer2(self, mock_random):
        self.assertEqual(computer_pon(), "チョキ")
        
    @patch("random.choice", return_value="パー")
    def test_computer3(self, mock_random):
        self.assertEqual(computer_pon(), "パー")
        
        