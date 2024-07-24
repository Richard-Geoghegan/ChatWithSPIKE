doc_data = {
    "motor": """
# Motor

To use a Motor add the following import statement to your project:
`import motor`

All functions in the module should be called inside the `motor` module as a prefix like so:
`motor.run(port.A, 1000)`

*Functions*

* `absolute_position`c
* `get_duty_cycle`
* `relative_position`
* `reset_relative_position`
* `run`
* `run_for_degrees`
* `run_for_time`
* `run_to_absolute_position`
* `run_to_relative_position`
* `set_duty_cycle`
* `stop`
* `velocity`

**Constants**

`motor` Constants:

* `READY = 0`
* `RUNNING = 1`
* `STALLED = 2`
* `CANCELLED = 3`
* `ERROR = 4`
* `DISCONNECTED = 5`
* `COAST = 0`
* `BRAKE = 1`
* `HOLD = 2`
* `CONTINUE = 3`
* `SMART_COAST = 4`
* `SMART_BRAKE = 5`
* `CLOCKWISE = 0`
* `COUNTERCLOCKWISE = 1`
* `SHORTEST_PATH = 2`
* `LONGEST_PATH = 3`
""",
    "motor_pair": """
# Motor Pair

The `motor_pair` module is used to run motors in a synchronized fashion. This mode is optimal for creating drivebases where you'd want a pair of motors to start and stop at the same time.

To use the `motor_pair` module simply import the module like so:

`import motor_pair`

All functions in the module should be called inside the motor_pair module as a prefix like so:

`motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)`

**Functions**

* `move`
* `move_for_degrees`
* `move_for_time`
* `move_tank`
* `move_tank_for_degrees`
* `move_tank_for_time`
* `pair`
* `stop`
* `unpair`

**Constants**

`motor_pair` Constants:

* `PAIR_1 = 0`: First Motor Pair
* `PAIR_2 = 1`: Second Motor Pair
* `PAIR_3 = 2`: Third Motor Pair
""",

    "distance_sensor": """
# Distance Sensor

The `distance_sensor` module enables you to write code that reacts to specific distances or light up the Distance Sensor in different ways.

To use the Distance Sensor module add the following import statement to your project:

`import distance_sensor`

All functions in the module should be called inside the `distance_sensor` module as a prefix like so:

`distance_sensor.distance(port.A)`

**Functions**

* `clear`
* `distance`
* `get_pixel`
* `set_pixel`
* `show`
""",

    "hub": """
# Hub

**Sub Modules**

* Button: `button`
* Light: `light`
* Light Matrix: `light_matrix`
* Motion Sensor: `motion_sensor`
* Port: `port`
* Sound: `sound`

**Functions**

* `device_uuid`
* `hardware_id`
* `power_off`
* `temperature`
""",

    "color_matrix": """
To use the Colour Matrix module, add the following import statement to your project:


import color_matrix
All functions in the module should be called inside the color_matrix module as a prefix like so:


color_matrix.set_pixel(port.A, 1, 1, (color.BLUE, 10))
Functions
clear
get_pixel
set_pixel
show
""",

    "color_sensor": """
The color_sensor module enables you to write code that reacts to specific colours or the intensity of the reflected light.

To use the Colour Sensor module, add the following import statement to your project:


import color_sensor
All functions in the module should be called inside the color_sensor module as a prefix like so:


color_sensor.reflection(port.A)
The Colour Sensor can recognise the following colours:

Red
Green
Blue
Magenta
Yellow
Orange
Azure
Black
White

Functions
color
reflection
rgbi
""",

    "force_sensor": """
The force_sensor module contains all functions and constants to use the Force Sensor.

To use the Force Sensor module, add the following import statement to your project:


import force_sensor
All functions in the module should be called inside the force_sensor module as a prefix like so:


force_sensor.force(port.A)
Functions
force
pressed
raw
""",

    "runloop": """
The runloop module contains all functions and constants to use the Runloop.

To use the Runloop module add the following import statement to your project:


import runloop
All functions in the module should be called inside the runloop module as a prefix like so:


runloop.run(some_async_function())
Functions
run
sleep_ms
until
"""
}