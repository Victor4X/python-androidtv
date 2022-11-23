from androidtv import setup

from adb_shell.auth.keygen import keygen

adbkey = "adbkey"

from os.path import isfile

if not isfile(adbkey):
    # Generate ADB key files
    keygen(adbkey)

from androidtv.adb_manager.adb_manager_sync import ADBPythonSync, PythonRSASigner

signer = ADBPythonSync.load_adbkey(adbkey)
print(f"using Python ADB implementation with adbkey='{adbkey}'")

aftv = setup(
    host="192.168.88.243",
    device_class="androidtv",
    port=5555,
    adbkey=adbkey,
    signer=signer,
)

print(f"aftv.available: {aftv.available}")

print(f"aftv.device_properties: {aftv.device_properties}")

# print(aftv.adb_shell("input keyevent HOME"))

# print(aftv.adb_shell("dumpsys audio"))

print(aftv.update())
# print("screen and wake")
# print(aftv.screen_on_awake_wake_lock_size())
print("properties directly")
from androidtv import constants
# print(constants.CMD_SCREEN_ON_AWAKE_WAKE_LOCK_SIZE)
print(aftv.get_properties_dict(get_running_apps=True))