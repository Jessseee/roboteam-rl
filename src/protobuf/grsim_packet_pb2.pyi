import protobuf.grsim_commands_pb2 as _grsim_commands_pb2
import protobuf.grsim_replacement_pb2 as _grsim_replacement_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class grSim_Packet(_message.Message):
    __slots__ = ("commands", "replacement")
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENT_FIELD_NUMBER: _ClassVar[int]
    commands: _grsim_commands_pb2.grSim_Commands
    replacement: _grsim_replacement_pb2.grSim_Replacement
    def __init__(self, commands: _Optional[_Union[_grsim_commands_pb2.grSim_Commands, _Mapping]] = ..., replacement: _Optional[_Union[_grsim_replacement_pb2.grSim_Replacement, _Mapping]] = ...) -> None: ...
