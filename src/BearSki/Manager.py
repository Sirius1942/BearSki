
from BearSki.template import BasicTestProject
def create_project(projectname):
    BasicTestProject.create_testproject(projectname)
    print("完成测试项目创建：{0}".format(projectname))
