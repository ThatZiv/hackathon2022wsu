import math
def octave(key): # returns current piano key octave
    return math.floor((key)/12)

def note(key): # converts key id to actual piano key
    notes = [
        "C", "C#",
        "D", "D#",
        "E", "F",
        "F#", "G",
        "G#", "A",
        "A#", "B"
    ]
    return notes[key % 12]

def sus(val): # # returns boolean based on if the sustain button is toggled on or off
    return True if val == 127 else False

def volume(val): # converts volume knob ratio from 0-127 to 0-100
    return round((val/127)*100)
