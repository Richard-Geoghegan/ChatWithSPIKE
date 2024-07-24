functions = {
    "force": """
force(port: int) -> int

Retrieves the measured force as decinewton. Values range from 0 to 100


from hub import port
import force_sensor


print(force_sensor.force(port.A))
Parameters
port: int
A port from the port submodule in the hub module
""",

    "pressed": """
pressed(port: int) -> bool

Tests whether the button on the sensor is pressed. Returns true if the force sensor connected to the port is pressed.


from hub import port
import force_sensor


print(force_sensor.pressed(port.A))
Parameters
port: int
A port from the port submodule in the hub module
""",

    "raw": """
raw(port: int) -> int

Returns the raw, uncalibrated force value of the force sensor connected on port port


from hub import port
import force_sensor


print(force_sensor.raw(port.A))
Parameters
port: int
A port from the port submodule in the hub module
"""

}