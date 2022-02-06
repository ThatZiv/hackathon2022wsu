# Some of this was taken from https://stackoverflow.com/questions/66274781/python-keyboard-input
import time
import ctypes
SendInput = ctypes.windll.user32.SendInput
# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBoardInput(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class HardwareInput(ctypes.Structure):
    _fields_ = [
        ("uMsg", ctypes.c_ulong),
        ("wParamL", ctypes.c_short),
        ("wParamH", ctypes.c_ushort)
    ]

class MouseInput(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time",ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class Input_I(ctypes.Union):
    _fields_ = [
        ("ki", KeyBoardInput),
        ("mi", MouseInput),
        ("hi", HardwareInput)
    ]

class Input(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("ii", Input_I)
    ]

# https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes 
# find more above

VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MENU = 0x12
VK_TAB = 0x09

def key_down(keyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBoardInput(keyCode, 0x48, 0, 0, ctypes.pointer(extra))
    x = Input( ctypes.c_ulong(1), ii_ )
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def key_up(keyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBoardInput(keyCode, 0x48, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def key(key_code, length = 0):    
    key_down(key_code)
    time.sleep(length)
    key_up(key_code)

def volume_up(inc=1):
    for _ in range(0, inc // 22 or 1):
        key(VK_VOLUME_UP)

def volume_up_1():
    key(VK_VOLUME_UP)

def volume_down_1():
    key(VK_VOLUME_DOWN)

def volume_down(inc=1):
    for _ in range(0, inc // 22 or 1):
        key(VK_VOLUME_DOWN)

def volume_mute():
    key(VK_VOLUME_MUTE)

def media_next():
    key(VK_MEDIA_NEXT_TRACK)

def media_prev():
    key(VK_MEDIA_PREV_TRACK)

def media_play_pause():
    key(VK_MEDIA_PLAY_PAUSE)

def a_key(): # mute
    key(0x6A, 0.1)

def b_key(): # deafen
    key(0x6D, 0.1)

def alt_tab():
    key_down(VK_MENU)
    time.sleep(0.1)
    key_down(VK_TAB)
    time.sleep(0.1)
    key_up(VK_MENU)
    key_up(VK_TAB)

def set_volume(num):
    for _ in range(0, 50):
        volume_down_1()
    for _ in range(num//2):
        volume_up_1()
