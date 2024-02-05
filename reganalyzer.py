import subprocess
import winreg as reg
import sys
# import os
# import win32com.shell.shell as shell

# if sys.argv[-1] != 'asadmin':
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
#     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
#     sys.exit(0)

key = reg.HKEY_LOCAL_MACHINE
sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"

def print_subkeys(registry_key, subkey_path):
    try:
        key = reg.OpenKey(registry_key, subkey_path)
        print(f"\nSubkeys under '{subkey_path}'\n")
        for i in range(reg.QueryInfoKey(key)[0]):
            subkey_name = reg.EnumKey(key, i)
            print(subkey_name)
            subkey_full_path = f"{subkey_path}\\{subkey_name}"

            try:
                subkey = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, subkey_full_path, 0, reg.KEY_READ | reg.KEY_WOW64_64KEY)
                value = reg.QueryValueEx(subkey, "DisplayName")
                if value:
                    print(f">>> {value[0]}\n")
            except FileNotFoundError:
                print(f"No DisplayName for {subkey_name}\n")
            # for j in range(50):
            #     try:
            #         n, v, t = reg.EnumValue(subkey, j)
            #         if "DisplayName" in n:
            #             print(f"{subkey_name} - DisplayName: {v}")
            #     except EnvironmentError:
            #         print("No DisplayName")  # 더 이상 값이 없으면 루프 종료

            # print("\nValues:")
            # for i in range(reg.QueryInfoKey(key)[1]):
            #     value_name, value_data, value_type = reg.EnumValue(key, i)
            #     print(f"{value_name}: {value_data} (Type: {value_type})")

    except FileNotFoundError:
        print(f"Error: The registry key '{subkey_path}' does not exist.")

    except Exception as e:
        print(f"Exception: {e}")

def uninstall_program(display_name):
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"

    try:
        uninstall_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_READ | reg.KEY_WOW64_64KEY)
        for i in range(reg.QueryInfoKey(uninstall_key)[0]):
            subkey_name = reg.EnumKey(uninstall_key, i)
            subkey_full_path = f"{key_path}\\{subkey_name}"

            try:
                subkey = reg.OpenKey(uninstall_key, subkey_full_path, 0, reg.KEY_READ | reg.KEY_WOW64_64KEY)
                try:
                    value, _ = reg.QueryValueEx(subkey, "DisplayName")
                    if value == display_name:
                        uninstall_string, _ = reg.QueryValueEx(subkey, "UninstallString")
                        if uninstall_string:
                            print(f"Uninstalling {display_name}...")
                            subprocess.run(uninstall_string, shell=True, check=True)
                            print(f"{display_name} has been uninstalled.")
                            return
                except FileNotFoundError:
                    pass
                finally:
                    reg.CloseKey(subkey)

            except FileNotFoundError:
                pass

        print(f"\nError: No program with DisplayName '{display_name}' found.\n")

    except FileNotFoundError:
        print(f"\nError: The registry key '{key_path}' does not exist.\n")
    except Exception as e:
        print(f"\nException: {e}\n")


# print(f"Subkeys under '{sub_key}':")
# print("Enter a command among (a), (b), (c)")
# print("(a) Find out uninstalled programs.")
# print("(b) Delete the program perfectly.")
# print("(c) exit")

# command = input()

while True:
    print("Enter a command among (a), (b), (c)")
    print("(a) Find out uninstalled programs.")
    print("(b) Delete the program perfectly.")
    print("(c) EXIT")
    print("\n")
    command = input("Your command : ")

    if (command == "a"):
        print_subkeys(key, sub_key)
    elif (command == "b"):
        dp = input("Enter the name of program you want to delete permanently.")
        uninstall_program(dp)
    elif (command == "c"):
        print("Exit.")
        break
    else:
        print("Enter the correct command.")
# reg.CreateKey(key, sub_key)

# winreg.OpenKey(key, sub_key, reserved=0, access=KEY_READ) : 지정된 키를 열고, 핸들 객체 반환
# reserved=0은 예약된 정수이므로, 0이 무조건 들어가야 함.
# open = reg.OpenKey(key, sub_key, 0, reg.KEY_ALL_ACCESS)

# winreg.QueryValueEx(key, value_name) : 해당 레지스트리의 지정된 값의 타입과 데이터 가져옴
# value, type = reg.QueryValueEx(open, "Uninstall")
# print(value, "Type: ", type)

# reg.CloseKey(open)
=======
## Ex 3-1. 창 띄우기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
