from BearSki.install_data import testRun
# coding=utf-8
import time
import unittest

class TestSendMessage(unittest.TestCase):
    def test_send(self):
        print("I'm in test_one test_send")
        self.assertEqual(testRun(),"OK")
        