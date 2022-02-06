import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # hides the dumb init log
import pygame.midi as midi
from time import sleep, time
from piano import octave, note, volume, sus
import keyboard
from keys import Keys
"""
m-audio midi interface

[keySet, keyNum, keyVal] - format

[144 - the piano keys], [(0 < x < 127) - piano key value]
[176 - volume knob], [7], [(0 < x < 127) - volume value]
[224 - pb id], [0 || 127 (at full)] , [(0 < x < 127) - pb val {rest - 64, left - 0, right - 127}]
[176 - mod id], [1], [(0 < x < 127) - mod value {rest - 0, full - 127}] 
[176 - sus id], [64], [(0 || 127) - toggle value]
"""

def main():
    print("Initializing MIDI Devices...")
    midi.init()
    print("Initialized MIDI Devices")
    d_id = midi.get_default_input_id()
    print(f"MIDI Device Found ID: {d_id}")
    if d_id == -1: # this is pointless
        for i in range(midi.get_count()):
            d = midi.get_device_info(i)
            if d is not None:
                if len(d) > 0:
                    if "Keystation Mini 32" in d[1].decode():
                        d_id = i
    device = midi.Input(d_id)
    volchange = False
    preVal = 127 # for utilizing velocity component
    timing = time() # VOLUME KNOB Timing
    actions = Keys
    print("Beginning Main Thread...")
    while True:
        sleep(0.01)
        deviceInput = device.read(1)
        if len(deviceInput) > 0:
            keys = deviceInput[0][0][:3]
            keySet, keyNum, keyVal = keys
            if keyVal > 0:
                preVal = keyVal
            if keyVal == 0 and keySet == 144: # piano keys (release -> [keyVal = 0])
                _key = note(keyNum)+str(octave(keyNum))
                print("Pressed Key: %s (id: %s)" % (_key, keyNum))
                actions.switch(_key, preVal) # client actions
            elif keySet == 176 and keyNum == 7: # vol knob
                vol = volume(keyVal)
                timing = time()
                volchange = True
                print(f"Volume Knob: {vol}% (val: {keyVal})")
            elif keySet == 176 and keyNum == 64: #sustain btn
                susToggle = sus(keyVal)
                keyboard.volume_mute() # Mute toggle
                print(f"Sustain Button: {'ON' if susToggle else 'OFF'}")
            elif keySet == 224: # pitch-bend btn
                print(f"PB Button: (val: {keyVal})")
        if volchange == True:
            if (time() - timing) > 0.279:
                volchange = False
                print(f"Volume Change: {vol}%")
                keyboard.set_volume(int(vol))

def init():
    try:
        return main()
    except Exception as e:
        print(f"Program crashed with the error: {str(e)}. Retrying in 5 seconds...")
        sleep(5)
        return init()

if __name__ == "__main__":
    init()