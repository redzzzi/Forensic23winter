import winreg as reg

def find_display_name(registry_key, subkey_path):
    try:
        key = reg.OpenKey(registry_key, subkey_path)
        value_name, value_type, value_data = reg.QueryValue(key, "DisplayName")
        return value_data

    except FileNotFoundError:
        print(f"Error: The registry key '{subkey_path}' does not exist.")

    except Exception as e:
        print(f"Exception: {e}")


def main():
    registry_key = reg.HKEY_LOCAL_MACHINE
    subkey_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"

    display_name = find_display_name(registry_key, subkey_path)
    if display_name:
        print(display_name)
    else:
        print("No DisplayName found")


if __name__ == "__main__":
    main()
