  
class command_parser(object):
  argument_array=[]
  def __init__(self):
    pass
  def add_argument(self,arg):
    self.argument_array.append(arg)
  def get_shot_arg(self):
    shot_arg=""
    for arg in self.argument_array:
      shot_arg=shot_arg+arg.shot_text+':'
    return shot_arg
  def get_long_arg(self):
    long_arg=[]
    for arg in self.argument_array:
      long_arg.append(arg.long_text)
    return long_arg
  def print_help_message(self):
    # print("Commands:")
    for arg in self.argument_array:
      message="  "+arg.shot_text
      for i in range(len(message),5):
        message=message+" "
      message=message+" --"+arg.long_text
      for i in range(len(message),30):
        message=message+" "
      # print(message+arg.helpmessage)

class base_command(object):
  shot_text=''
  long_text=''
  helpmessage=''
  def __init__(self,shot_text,long_text,helpmessage):
    self.shot_text=shot_text
    self.long_text=long_text
    self.helpmessage=helpmessage

