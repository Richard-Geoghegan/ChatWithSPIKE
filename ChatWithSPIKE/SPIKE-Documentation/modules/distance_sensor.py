functions = {
    "clear": """
clear(port: int) -> None

Turns off all the lights in the Distance Sensor connected to port.

Parameters
port: int
A port from the port submodule in the hub module
""",

    "distance": """
distance(port: int) -> int

Retrieve the distance in millimetres captured by the Distance Sensor connected to port. If the Distance Sensor cannot read a valid distance it will return -1.

Parameters
port: int
A port from the port submodule in the hub module
""",

    "get_pixel": """
get_pixel(port: int, x: int, y: int) -> int

Retrieve the intensity of a specific light on the Distance Sensor connected to port.

Parameters
port: int
A port from the port submodule in the hub module

x: int
The X value (0 - 3)

y: int
The Y value, range (0 - 3)
""",

    "set_pixel": """
set_pixel(port: int, x: int, y: int, intensity: int) -> None

Changes the intensity of a specific light on the Distance Sensor connected to port.

Parameters
port: int
A port from the port submodule in the hub module

x: int
The X value (0 - 3)

y: int
The Y value, range (0 - 3)

intensity: int
How bright to light up the pixel
""",

    "show": """
show(port: int, pixels: list[int]) -> None

Change all the lights at the same time.


from hub import port
import distance_sensor

# Update all lights on Distance Sensor using the show function 

# Create a list with 4 identical intensity values 
pixels = [100] * 4 

# Update all pixels to show same intensity 
distance_sensor.show(port.A, pixels)
Parameters
port: int
A port from the port submodule in the hub module

pixels: bytes
A list containing intensity values for all 4 pixels.
"""
}
