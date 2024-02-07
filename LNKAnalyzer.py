import winreg as reg
import sys
import os
import win32com.client

key = reg.HKEY_LOCAL_MACHINE
sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"

def print_subkeys(registry_key, subkey_path):
  try:
    key = reg.OpenKey(registry_key, subkey_path)
    print(f"\nSubkeys under '{subkey_path}'\n")
    count = 0
    for i in range(reg.QueryInfoKey(key)[0]):
      if count == 11:
        break
      subkey_name = reg.EnumKey(key, i)
      print(f"The name of subkey : {subkey_name}")
      subkey_full_path = f"{subkey_path}\\{subkey_name}"

      try:
        subkey = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, subkey_full_path, 0, reg.KEY_READ | reg.KEY_WOW64_64KEY)
        value = reg.QueryValueEx(subkey, "DisplayName")
        value2 = reg.QueryValueEx(subkey, "DisplayIcon")
        if value:
          count += 1
          print(f">>> program : {value[0]}")
          print(f">>> target : {value2[0]}\n")
      except FileNotFoundError:
        print(f"No DisplayName for {subkey_name}\n")
  except FileNotFoundError:
    print(f"Error: The registry key '{subkey_path}' does not exist.")
  except Exception as e:
    print(f"Exception: {e}")

test_home = r"C:\Users\hjado\Desktop\LNKtest"

def createLNK(name, target_path):
  shell = win32com.client.Dispatch("WScript.Shell")
  shortcut_path = os.path.join(test_home, f"{name}.lnk")
  shortcut = shell.CreateShortcut(shortcut_path)
  shortcut.TargetPath = target_path
  shortcut.Save()

# def changeLNK(changed, change):

while True:
  print("------------------------------------------")
  print("Enter a command 가 or 나 or 다")
  print("가) find out uninstalled programs (upto10)")
  print("나) make a lnk for uninstalled program")
  print("다) exit")
  print("------------------------------------------\n")
  command = input("your command is -> ")

  if (command == "가"):
    print_subkeys(key, sub_key)
  elif (command == "나"):
    lnkname = input("LNK name : ")
    lnkpath = input("LNK of : \n")
    createLNK(lnkname, lnkpath)
    print("Processed Successfully!")
  elif (command == "다"):
    print("exit")
    break
  else:
    print("check your command")

# print_subkeys(key, sub_key)