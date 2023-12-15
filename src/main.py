import socket
from functools import wraps
from typing import Callable, Any

import click

import zmq

from protobuf.command_pb2 import Command
from protobuf.ssl_simulation_control_pb2 import SimulatorCommand, SimulatorControl, TeleportBall
from protobuf.ssl_gc_common_pb2 import Team

YELLOW_CONTROL_PORT = 10302
SIMULATION_CONTROL_PORT = 10300
WORLD_CONTROL_PORT = 5558

socket_sim = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_world = zmq.Context().socket(zmq.SUB)
socket_world.setsockopt_string(zmq.SUBSCRIBE, "")
socket_world.connect(f"tcp://127.0.0.1:{WORLD_CONTROL_PORT}")


def ssl_command(func: Callable[[Any], Command]):
    """
    Wrapper for ER-Force simulator commands. Wrapped function should return command to be sent.

    :param func: The function to wrap.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        command = func(*args, **kwargs)
        socket_sim.sendto(command.SerializeToString(), ("localhost", SIMULATION_CONTROL_PORT))
    return wrapper


@ssl_command
def set_number_of_robots(number_of_robots: int):
    """
    Remove any unused robots from the field.

    :param number_of_robots: The number of robots that should remain on the field for each team.
    """
    command = SimulatorCommand()
    for team in [Team.YELLOW, Team.BLUE]:
        for robot_id in range(11):
            teleport = command.control.teleport_robot.add()
            teleport.id.id = robot_id
            teleport.id.team = team
            teleport.present = robot_id < number_of_robots
    return command


@ssl_command
def reset_ball():
    """Teleport ball to the center of the field."""
    teleport_ball = TeleportBall(x=0, y=0)
    control = SimulatorControl(teleport_ball=teleport_ball)
    return SimulatorCommand(control=control)


@click.group()
def cli():
    pass


@cli.command()
@click.option("--robots", default=11)
def init(robots):
    set_number_of_robots(robots)
    reset_ball()


if __name__ == "__main__":
    cli()
