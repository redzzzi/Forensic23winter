<<<<<<< HEAD
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()
=======
print("Hello World")
>>>>>>> 286a63bdc0cb5cc895a9a226dbe07df5bd54ea5f
