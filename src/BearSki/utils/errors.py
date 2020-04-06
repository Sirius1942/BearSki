
#获取参数异常
class ArgmentError(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

#读取配置文件异常

class SettingFileError(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class DataBaseError(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
