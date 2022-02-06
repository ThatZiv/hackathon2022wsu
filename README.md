
# `MIDI Macros` - Hackathon 2022 WSU

`MIDI Macros` allows users to bind efficient shortcuts/macros to their MIDI keyboard and increase productivity while working at home. 

[![Click Me](https://img.youtube.com/vi/MZsUFm2aQ58/0.jpg)](https://www.youtube.com/watch?v=MZsUFm2aQ58)

## Contributor:
 * [@thatziv](https://github.com/thatziv)

## Problem
When working at home, menial tasks, such as opening specific files or playing music can be less of a burden to do. With `MIDI Macros,` the program utilizes the MIDI protocol to do such tasks at ease. In doing so, certain actions can be performed with a press of a button, and with over 128 keys to use (on a traditional MIDI Piano), the possibilities are endless. All in all, The amount of time saved looking for that specific folder, or any other redundant task is paramount.

## Technicalities
* Language: `Python`
* Libraries: `pygame, subprocess, ctypes`

## Progression
The project was completed during the hackathon. The parsing of MIDI values was done first using the `pygame.midi` library. Then the research of what values meant what was done. After, the formulas of the key values were then completed. Once the values were entirely parsed, the linking of actions and macros was done (what key did what action/function) using `subprocesses` for opening programs and `ctypes` for keyboard input emulation. The volume knob was done last using a timeout/flag based-logic. The outcome was a versatile program that utilizes any MIDI keyboard as a way for many macros and automations on your PC.

## Navigation

* `main.py` is the main file that runs as the index of the project. It houses the logic for reading input and passing its data to other files.
* `piano.py` houses the formulas for parsing data from the MIDI interface. This includes logic like what note is played, the status of the sustain button, octave calculation, and volume knob ratio conversation.
* `keyboard.py` has the keyboard functionality; it emulates keyboard input and functionalities like: volume up/down, play/pause media, mute, and set volume.
* `keys.py` is the output of the program. The data fed from `main.py` goes to this file and runs whatever it needs based on the data from the main thread. The main function houses the switch case logic to execute respective functionalities like: opening programs, multi-media controls, starting websites, and more.

## Reproduction

1. Clone repo
```bash
git clone https://github.com/ThatZiv/hackathon2022wsu
```

2.  Install dependencies
```bash
python3 -m pip install pygame ctypes
```
3. Configure directories
	* Change the constant values in `keys.py` to your liking, not my values.
4. Run file
```bash
python3 main.py
```


## Demo

[https://www.youtube.com/watch?v=MZsUFm2aQ58](https://www.youtube.com/watch?v=MZsUFm2aQ58)
