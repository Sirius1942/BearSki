from BearSki.install_data import testRun
# coding=utf-8
import time
import unittest
import logging


class TestSendMessage(unittest.TestCase):
    def setUp(self):
        self.logger=logging.getLogger("Test_install")
    def test_install(self):
        self.logger.info("I'm in  test_install")
        self.assertEqual(testRun(),"OK")
        