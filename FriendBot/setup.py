from cx_Freeze import setup, Executable
import sys


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "FriendBot" , 
      version = "1.0" , 
      description = "FriendBot" ,
      
      executables = [Executable("FriendBot.py",base=base)]) 
