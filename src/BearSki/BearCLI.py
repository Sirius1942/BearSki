import argparse
from BearSki.Manager import create_project
from BearSki.gui.ApiTestGui import gui_start
from BearSki.utils.arguments import runArg
from BearSki.utils.hartool import HarTool
import BearSki
import json

def main():

  rArg=runArg()
  
  parser = argparse.ArgumentParser(description=BearSki.__description__)
  # parser.add_argument("commond",help="run commond",choices=['createproject','HarParser'])
  parser.add_argument('-v', '--version',help="show version",action="store_true")
  parser.add_argument('commond', choices=['createproject','HarParser','tools'],help="CLI commond")

  group1=parser.add_argument_group('createproject','create templet testproject')
  group1.add_argument('-pn', '--projectname',default='AgaveTestProject',help="testcase file path")

  group2=parser.add_argument_group('HarParser','create testmodel and testcase from har file')
  group2.add_argument('-fp', '--harfilepath',help="parser har file path")
  group2.add_argument('-mp', '--modelpath',default="testdata/model",help="testmodel file path")
  group2.add_argument('-cp','--casepath',default='testcase',help='testcase file path')
  group2.add_argument('-cf','--configfile',default='config.json',help='config file path')

  group3=parser.add_argument_group('tools','test tools')
  group3.add_argument('-g', '--gui',help="api gui test tools",action="store_true")

  args = parser.parse_args()
  f= open(args.configfile)
  conf=json.load(f)
  rArg.setValueFromJson(conf)
  if args.commond:
      if args.commond=='createproject':
        create_project(args.projectname)
      if args.commond=='HarParser':
        if args.configfile:
          if args.harfilepath:
            HarTool(args.harfilepath).createAllCase()
      if args.commond=='tools':
        if args.gui: 
          gui_start()

  # if args.verbasity:
  #   print("打开 verbosity")
if __name__ == "__main__":
  main()

