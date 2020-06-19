from BearSki.core import TD
from BearSki.core import DT
import unittest
import logging


class TestTestData(unittest.TestCase):

    def setUp(self):
        self.logger=logging.getLogger('TestTestData')
    def tearDown(self):
        pass
    # def test_getDefult_data(self):
    #     self.logger.info("I'm in test_getDefult_data")
    #     BASE_URL=TD.get_global_data("BASE_URL")
    #     self.assertEqual(BASE_URL,"http://www.agavetest.cn:8671")

    def test_setGlobalData(self):
        self.logger.info("I'm in test_getDefult_data")
        TD.add_global_data({"A1":"d1","A2":456})
        A1=TD.get_global_all_data()["A1"]
        A2=TD.get_global_all_data()["A2"]
        self.assertEqual(A1,"d1")
        self.assertEqual(A2,456)

    def test_getData(self):
        self.logger.info("in test_getData")
        name=TD.get_Data("login.admin.username")
        self.assertEqual(name['username'],"admin")
        admindata = TD.get_Data("login.admin")
        self.assertEqual(admindata['detail']['username'], "admin")
        admindata = TD.get_Data("login.admin",type='list')
        self.assertIn('admin',admindata)
        admindata = TD.get_Data("users.admin.mobile")
        self.logger.info(admindata)
        admindata = TD.get_Data("users.admin.time")
        self.logger.info(admindata)
        admindata = TD.get_Data("api_users_2_model.request",source_name='myJsonData')
        self.logger.info(admindata)

    def test_columns_data(self):
        self.logger.info("in test_columns_data ")
        data=TD.get_columns_data("users.DataID")
        self.logger.info(data)


