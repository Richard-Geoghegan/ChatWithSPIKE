functions = {
    "color": """
color(port: int) -> int

Returns the colour value of the detected colour. Use the color module to map the colour value to a specific colour.


import color_sensor
from hub import port
import color

if color_sensor.color(port.A) is color.RED:
    print("Red detected")
Parameters
port: int
A port from the port submodule in the hub module
""",

    "reflection": """
reflection(port: int) -> int

Retrieves the intensity of the reflected light (0-100%).

Parameters
port: int
A port from the port submodule in the hub module
""",

    "rgbi": """
rgbi(port: int) -> tuple[int, int, int, int]

Retrieves the overall colour intensity and intensity of red, green and blue.

Returns tuple[red: int, green: int, blue: int, intensity: int]

Parameters
port: int
A port from the port submodule in the hub module
"""
}
