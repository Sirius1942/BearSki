import argparse
import sys
sys.path.append('../')
from BearSki.Manager import create_project
from BearSki.gui.ApiTestGui import gui_start
from BearSki.utils.hartool import HarTool
import BearSki

def main():

  parser = argparse.ArgumentParser(description=BearSki.__description__+" version :"+BearSki.__version__)
  # parser.add_argument("commond",help="run commond",choices=['createproject','HarParser'])
  # parser.add_argument('-v', '--version',help="show version",action="store_true")
  parser.add_argument('commond', choices=['createproject','HarParser','tools','version'],help="CLI commond")

  group1=parser.add_argument_group('createproject','create templet testproject')
  group1.add_argument('-n', '--name',default='AgaveTestProject',help="yourproject name and your project root path")

  group2=parser.add_argument_group('HarParser','create testmodel and testcase from har file')
  group2.add_argument('-fp', '--harfilepath',help="parser har file path")
  group2.add_argument('-mp', '--modelpath',default="db/model",help="testmodel file path")
  group2.add_argument('-cp','--casepath',default='testcase',help='testcase file path')
  group2.add_argument('-cf','--configfile',default='config.json',help='config file path')

  group3=parser.add_argument_group('tools','test tools')
  group3.add_argument('-g', '--gui',help="api gui test tools",action="store_true")
  group3.add_argument('-gt', '--guitest',help="api gui test tools test mode",action="store_true")


  args = parser.parse_args()
 
  if args.commond:
      if args.commond=='createproject':
        create_project(args.name)
      if args.commond=='HarParser':
          if args.harfilepath:
            HarTool(args.harfilepath).createAllCase()
      if args.commond=='tools':
        if args.gui: 
          gui_start("")
        if args.guitest:
          gui_start("test")
      if args.commond=='version':
         print(BearSki.__version__)

