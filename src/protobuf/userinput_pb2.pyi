import protobuf.robot_pb2 as _robot_pb2
import protobuf.command_pb2 as _command_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserInput(_message.Message):
    __slots__ = ("radio_command", "move_command")
    RADIO_COMMAND_FIELD_NUMBER: _ClassVar[int]
    MOVE_COMMAND_FIELD_NUMBER: _ClassVar[int]
    radio_command: _containers.RepeatedCompositeFieldContainer[_robot_pb2.RadioCommand]
    move_command: _containers.RepeatedCompositeFieldContainer[_command_pb2.RobotMoveCommand]
    def __init__(self, radio_command: _Optional[_Iterable[_Union[_robot_pb2.RadioCommand, _Mapping]]] = ..., move_command: _Optional[_Iterable[_Union[_command_pb2.RobotMoveCommand, _Mapping]]] = ...) -> None: ...
