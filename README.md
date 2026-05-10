# Tetris

This repo is something that I built back in 2022. The code is often pretty ugly but I decided to upload it anyway since this was one of my beginner projects. 

I basically built Tetris in both Python using pygame and in Javascript using the p5.js library. The python version also supports controller input.

## Controls

### Keyboard

```
LEFT/RIGHT -> move blocks left and right

UP -> immmediately bring blocks to the ground

DOWN -> move blocks one tile down

SPACE -> rotate blocks

C -> switch current blocks with the blocks in the HOLD window
```

### Controller

Controller inputs are only supported in the Python version. Not in the Javascript version.

All directional inputs should be done using the D-pad.

```
LEFT/RIGHT -> move blocks left and right

UP -> immmediately bring blocks to the ground

DOWN -> move blocks one tile down

A (X on Playstation) -> rotate blocks

LB (L1 on Playstation) -> switch current blocks with the blocks in the HOLD window
```

## Usage

### Python version

Simply run this command: 
```
python main.py
```

Make sure to download all needed python modules if you get any error.

### Javascript version

You need to start a server in the root directory and then request it in a browser.

#### Example 

Run this to start a server:
```
python -m http.server
```

Then simply request `http://localhost:8000` in a browser. 
