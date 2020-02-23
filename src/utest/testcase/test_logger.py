# coding=utf-8
import unittest
import logging

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger=logging.getLogger("TestLogger")
    def tearDown(self):
        pass
    def test_log(self):
        self.logger.info("info logger is ok!")
        self.logger.warn("warn logger is ok!")
        self.logger.error("error logger is ok!")
        self.logger.critical("critical logger is ok!")
        self.logger.debug("debug logger is ok!")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()