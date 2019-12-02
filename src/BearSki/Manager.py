import os
import shutil
import sys
from BearSki.testproject_template import BasicTestProject
from BearSki.utils.logger import SkiLogger
logger=SkiLogger("Manager")
def creat_test_project(projectname):
    BasicTestProject.create_testproject(projectname)
    
    



