import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KW_ROUTER={
        "userkw_sendmsg":"utest.keywords.send.askbaidu",
        "Create Session":"RequestsLibrary.RequestsLibrary.create_session",
        "Get Request":"RequestsLibrary.RequestsLibrary.get_request",
        "input text":"Selenium2Library.Selenium2Library.input_text",
        "click button":"Selenium2Library.Selenium2Library.click_button",
        "Open Browser":"Selenium2Library.Selenium2Library.open_browser",
        "requestFromModel":"utest.keywords.requestModel.runModel"
}
GLOBAL_VARIABLE={
        "BASE_URL":"http://www.agavetest.cn:8671",
    }
#原DataTable 配置，建议后续使用TEST_DATABASES 替换
DATATABLE={
        "db_excel_path":"./utest/db/testdata1.xlsx",
        "db_json_path":"./utest/db/model/"
    }

TEST_DATABASES = {
    'default': {
        'ENGINE': 'BearSki.db.Base.ExcelFile',
        'NAME': 'myDataTable', #连接的数据库名
        'PATH': './utest/testdata/testdata1.xlsx'
    },
    'myJsonData': {
        'ENGINE': 'Bearski.db.Base.JsonFile',
        'NAME': 'myJsonData', #连接的数据库名
        'PATH': './utest/db/model/'
    }
}
#当前先不提共 TEST_DATABASE_ROUTERS 扩展接口
#TEST_DATABASE_ROUTERS = ['myproject.database_router.DatabaseAppsRouter']
TEST_DATABASE_CASE_MAPPING = {
    'app01': 'default',
    'app02': 'mysql02',
}
INITDATA={
        "init_file_path":"utest.db.initdata"
}
