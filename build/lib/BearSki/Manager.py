import shutil
import sys
from BearSki.template import BasicTestProject
# from BearSki.utils.logger import SkiLogger
# logger=SkiLogger("Manager")
def create_project(projectname):
    BasicTestProject.create_testproject(projectname)
    print("完成测试项目创建：{0}".format(projectname))
