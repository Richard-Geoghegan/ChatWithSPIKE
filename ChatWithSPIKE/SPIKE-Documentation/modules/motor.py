functions = {
    "absolute_position": """
absolute_position(port: int) -> int

Get the absolute position of a motor

Parameters
port: int
A port from the port submodule in the hub module
""",

    "get_duty_cycle": """
get_duty_cycle(port: int) -> int

Get the PWM of a motor

Parameters
port: int
A port from the port submodule in the hub module
""",

    "relative_position": """
relative_position(port: int) -> int

Get the relative position of a motor

Parameters
port: int
A port from the port submodule in the hub module
""",

    "reset_relative_position": """
reset_relative_position(port: int, position: int) -> None

Change the position used as the offset when using the run_to_relative_position function.

Parameters
port: int
A port from the port submodule in the hub module

position: int
The degree of the motor
""",

    "run": """
run(port: int, velocity: int, *, acceleration: int = 1000) -> None

Start a motor at a constant speed

from hub import port
import motor, time

# Start motor 
motor.run(port.A, 1000)

Parameters
port: int
A port from the port submodule in the hub module

velocity: int
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050

Optional keyword arguments:
acceleration: int
The acceleration (deg/sec²) (0 - 10000)
""",

    "run_for_degrees": """
run_for_degrees(port: int, degrees: int, velocity: int, *, stop: int = BRAKE, 
acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

Turn a motor for a specific number of degrees
When awaited returns a status of the movement that corresponds to one of the following constants:

motor.READY
motor.RUNNING
motor.STALLED
motor.CANCELED
motor.ERROR
motor.DISCONNECTED

Parameters
port: int
A port from the port submodule in the hub module

degrees: int
The number of degrees

velocity: int
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050

Optional keyword arguments:
stop: int
The behaviour of the motor after it has stopped. Use the constants in the motor module.

Possible values are
motor.COAST to make the motor coast until a stop
motor.BREAK to brake and continue to brake after stop
motor.HOLD to tell the motor to hold it's position
motor.CONTINUE to tell the motor to keep running at whatever velocity it's running at until it gets another command
motor.SMART_COAST to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
motor.SMART_BRAKE to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command

acceleration: int
The acceleration (deg/sec²) (0 - 10000)

deceleration: int
The deceleration (deg/sec²) (0 - 10000)
""",

    "run_for_time": """
run_for_time(port: int, duration: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

Run a motor for a limited amount of time
When awaited returns a status of the movement that corresponds to one of the following constants:

motor.READY
motor.RUNNING
motor.STALLED
motor.ERROR
motor.DISCONNECTED


from hub import port
import runloop
import motor

async def main():
    # Run at 1000 velocity for 1 second 
    await motor.run_for_time(port.A, 1000, 1000)

    # Run at 280 velocity for 1 second 
    await motor_pair.run_for_time(port.A, 1000, 280)

    # Run at 280 velocity for 10 seconds with a slow deceleration 
    await motor_pair.run_for_time(port.A, 10000, 280, deceleration=10)

runloop.run(main())
Parameters
port: int
A port from the port submodule in the hub module

duration: int
The duration in milliseconds

velocity: int
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050

Optional keyword arguments:
stop: int
The behaviour of the motor after it has stopped. Use the constants in the motor module.

Possible values are
motor.COAST to make the motor coast until a stop
motor.BREAK to brake and continue to brake after stop
motor.HOLD to tell the motor to hold it's position
motor.CONTINUE to tell the motor to keep running at whatever velocity it's running at until it gets another command
motor.SMART_COAST to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
motor.SMART_BRAKE to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command

acceleration: int
The acceleration (deg/sec²) (0 - 10000)

deceleration: int
The deceleration (deg/sec²) (0 - 10000)
""",

    "run_to_absolute_position": """
run_to_absolute_position(port: int, position: int, velocity: int, *, direction: int, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

Turn a motor to an absolute position.
When awaited returns a status of the movement that corresponds to one of the following constants:

motor.READY
motor.RUNNING
motor.STALLED
motor.CANCELED
motor.ERROR
motor.DISCONNECTED

Parameters
port: int
A port from the port submodule in the hub module

position: int
The degree of the motor

velocity: int
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050

Optional keyword arguments:
direction: int
The direction to turn.
Options are:

motor.CLOCKWISE
motor.COUNTERCLOCKWISE
motor.SHORTEST_PATH
motor.LONGEST_PATH

stop: int
The behaviour of the motor after it has stopped. Use the constants in the motor module.

Possible values are
motor.COAST to make the motor coast until a stop
motor.BREAK to brake and continue to brake after stop
motor.HOLD to tell the motor to hold it's position
motor.CONTINUE to tell the motor to keep running at whatever velocity it's running at until it gets another command
motor.SMART_COAST to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
motor.SMART_BRAKE to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command

acceleration: int
The acceleration (deg/sec²) (0 - 10000)

deceleration: int
The deceleration (deg/sec²) (0 - 10000)
""",

    "run_to_relative_position": """
run_to_relative_position(port: int, position: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

Turn a motor to a position relative to the current position.
When awaited returns a status of the movement that corresponds to one of the following constants:

motor.READY
motor.RUNNING
motor.STALLED
motor.CANCELED
motor.ERROR
motor.DISCONNECTED

Parameters
port: int
A port from the port submodule in the hub module

position: int
The degree of the motor

velocity: int
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050

Optional keyword arguments:
stop: int
The behaviour of the motor after it has stopped. Use the constants in the motor module.

Possible values are
motor.COAST to make the motor coast until a stop
motor.BREAK to brake and continue to brake after stop
motor.HOLD to tell the motor to hold it's position
motor.CONTINUE to tell the motor to keep running at whatever velocity it's running at until it gets another command
motor.SMART_COAST to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
motor.SMART_BRAKE to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command

acceleration: int
The acceleration (deg/sec²) (0 - 10000)

deceleration: int
The deceleration (deg/sec²) (0 - 10000)
""",

    "set_duty_cycle": """
set_duty_cycle(port: int, pwm: int) -> None

Start a motor with a specific PWM

Parameters
port: int
A port from the port submodule in the hub module

pwm: int
The PWM value (-10000-10000)
""",

    "stop": """
stop(port: int, *, stop: int = BRAKE) -> None

Stops a motor


from hub import port
import motor, time

# Start motor 
motor.run(port.A, 1000)

# Wait for 2 seconds 
time.sleep_ms(2000)

# Stop motor 
motor.stop(port.A)
Parameters
port: int
A port from the port submodule in the hub module

Optional keyword arguments:
stop: int
The behaviour of the motor after it has stopped. Use the constants in the motor module.

Possible values are
motor.COAST to make the motor coast until a stop
motor.BREAK to brake and continue to brake after stop
motor.HOLD to tell the motor to hold it's position
motor.CONTINUE to tell the motor to keep running at whatever velocity it's running at until it gets another command
motor.SMART_COAST to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
motor.SMART_BRAKE to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command
""",

    "velocity": """
velocity(port: int) -> int

Get the velocity (deg/sec) of a Motor

Parameters
port: int
A port from the port submodule in the hub module
"""
}
