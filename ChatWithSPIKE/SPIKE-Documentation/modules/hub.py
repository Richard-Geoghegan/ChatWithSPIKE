functions = {
    "device_uuid": """
device_uuid() -> str

Retrieve the device ID.

Parameters
""",

    "hardware_id": """
hardware_id() -> str

Retrieve the hardware ID.

Parameters
""",

    "power_off": """
power_off() -> int

Turns off the hub.

Parameters

""",

    "temperature": """
temperature() -> int

Retrieve the hub temperature. Measured in decidegrees Celsius (d°C) which is 1/10 of a degree Celsius (°C)

Parameters
""",

    "port": """
This module contains constants that enable easy access to the ports on the SPIKE Prime hub. Use the constants in all functions that take a port parameter.

To use the Port module add the following import statement to your project:


from hub import port
All functions in the module should be called inside the port module as a prefix like so:


port.A
Constants
hub.port Constants
A = 0
The Port that is labelled ‘A’ on the Hub.
B = 1
The Port that is labelled ‘B’ on the Hub.
C = 2
The Port that is labelled ‘C’ on the Hub.
D = 3
The Port that is labelled ‘D’ on the Hub.
E = 4
The Port that is labelled ‘E’ on the Hub.
F = 5
The Port that is labelled ‘F’ on the Hub.
""",

    "button": """
To use the Button module, add the following import statement to your project:

from hub import button

All functions in the module should be called inside the button module as a prefix like so:

button.pressed(button.LEFT)

Functions

pressed

Constants

hub.button Constants
LEFT = 1
Left button next to the power button on the SPIKE Prime hub
RIGHT = 2
Right button next to the power button on the SPIKE Prime hub
""",

    "light": """
The light module includes functions to change the colour of the light on the SPIKE Prime hub.

To use the Light module, add the following import statement to your project:

from hub import light
All functions in the module should be called inside the light module as a prefix like so:

light.color(color.RED)

Functions
color

Constants
hub.light Constants
POWER = 0
The power button. On SPIKE Prime it's the button between the left and right buttons.
CONNECT = 1
The light around the Bluetooth connect button on SPIKE Prime.
""",

    "light_matrix": """
To use the Light Matrix module, add the following import statement to your project:

from hub import light_matrix

All functions in the module should be called inside the light_matrix module as a prefix like so:

light_matrix.write("Hello World")

Functions
clear
get_orientation
get_pixel
set_orientation
set_pixel
show
show_image
write

Constants
hub.light_matrix Constants
IMAGE_HEART = 1
IMAGE_HEART_SMALL = 2
IMAGE_HAPPY = 3
IMAGE_SMILE = 4
IMAGE_SAD = 5
IMAGE_CONFUSED = 6
IMAGE_ANGRY = 7
IMAGE_ASLEEP = 8
IMAGE_SURPRISED = 9
IMAGE_SILLY = 10
IMAGE_FABULOUS = 11
IMAGE_MEH = 12
IMAGE_YES = 13
IMAGE_NO = 14
IMAGE_CLOCK12 = 15
IMAGE_CLOCK1 = 16
IMAGE_CLOCK2 = 17
IMAGE_CLOCK3 = 18
IMAGE_CLOCK4 = 19
IMAGE_CLOCK5 = 20
IMAGE_CLOCK6 = 21
IMAGE_CLOCK7 = 22
IMAGE_CLOCK8 = 23
IMAGE_CLOCK9 = 24
IMAGE_CLOCK10 = 25
IMAGE_CLOCK11 = 26
IMAGE_ARROW_N = 27
IMAGE_ARROW_NE = 28
IMAGE_ARROW_E = 29
IMAGE_ARROW_SE = 30
IMAGE_ARROW_S = 31
IMAGE_ARROW_SW = 32
IMAGE_ARROW_W = 33
IMAGE_ARROW_NW = 34
IMAGE_GO_RIGHT = 35
IMAGE_GO_LEFT = 36
IMAGE_GO_UP = 37
IMAGE_GO_DOWN = 38
IMAGE_TRIANGLE = 39
IMAGE_TRIANGLE_LEFT = 40
IMAGE_CHESSBOARD = 41
IMAGE_DIAMOND = 42
IMAGE_DIAMOND_SMALL = 43
IMAGE_SQUARE = 44
IMAGE_SQUARE_SMALL = 45
IMAGE_RABBIT = 46
IMAGE_COW = 47
IMAGE_MUSIC_CROTCHET = 48
IMAGE_MUSIC_QUAVER = 49
IMAGE_MUSIC_QUAVERS = 50
IMAGE_PITCHFORK = 51
IMAGE_XMAS = 52
IMAGE_PACMAN = 53
IMAGE_TARGET = 54
IMAGE_TSHIRT = 55
IMAGE_ROLLERSKATE = 56
IMAGE_DUCK = 57
IMAGE_HOUSE = 58
IMAGE_TORTOISE = 59
IMAGE_BUTTERFLY = 60
IMAGE_STICKFIGURE = 61
IMAGE_GHOST = 62
IMAGE_SWORD = 63
IMAGE_GIRAFFE = 64
IMAGE_SKULL = 65
IMAGE_UMBRELLA = 66
IMAGE_SNAKE = 67
"""
}