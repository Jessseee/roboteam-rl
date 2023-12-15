import protobuf.ssl_game_controller_common_pb2 as _ssl_game_controller_common_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdvantageChoice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOP: _ClassVar[AdvantageChoice]
    CONTINUE: _ClassVar[AdvantageChoice]
STOP: AdvantageChoice
CONTINUE: AdvantageChoice

class TeamRegistration(_message.Message):
    __slots__ = ("team_name", "signature")
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    team_name: str
    signature: _ssl_game_controller_common_pb2.Signature
    def __init__(self, team_name: _Optional[str] = ..., signature: _Optional[_Union[_ssl_game_controller_common_pb2.Signature, _Mapping]] = ...) -> None: ...

class TeamToController(_message.Message):
    __slots__ = ("signature", "desired_keeper", "advantage_choice", "substitute_bot", "ping")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_KEEPER_FIELD_NUMBER: _ClassVar[int]
    ADVANTAGE_CHOICE_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTE_BOT_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    signature: _ssl_game_controller_common_pb2.Signature
    desired_keeper: int
    advantage_choice: AdvantageChoice
    substitute_bot: bool
    ping: bool
    def __init__(self, signature: _Optional[_Union[_ssl_game_controller_common_pb2.Signature, _Mapping]] = ..., desired_keeper: _Optional[int] = ..., advantage_choice: _Optional[_Union[AdvantageChoice, str]] = ..., substitute_bot: bool = ..., ping: bool = ...) -> None: ...

class ControllerToTeam(_message.Message):
    __slots__ = ("controller_reply",)
    CONTROLLER_REPLY_FIELD_NUMBER: _ClassVar[int]
    controller_reply: _ssl_game_controller_common_pb2.ControllerReply
    def __init__(self, controller_reply: _Optional[_Union[_ssl_game_controller_common_pb2.ControllerReply, _Mapping]] = ...) -> None: ...
