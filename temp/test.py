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

print(aftv.available)