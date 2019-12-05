import os
import shutil
import sys
from BearSki.testproject_template import BasicTestProject
from BearSki.utils.logger import SkiLogger
logger=SkiLogger("Manager")
def create_project(projectname):
    BasicTestProject.create_testproject(projectname)
    
    



