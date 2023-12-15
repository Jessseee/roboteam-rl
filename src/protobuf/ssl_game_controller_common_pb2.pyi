from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Team(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[Team]
    YELLOW: _ClassVar[Team]
    BLUE: _ClassVar[Team]

class Division(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIV_UNKNOWN: _ClassVar[Division]
    DIV_A: _ClassVar[Division]
    DIV_B: _ClassVar[Division]
UNKNOWN: Team
YELLOW: Team
BLUE: Team
DIV_UNKNOWN: Division
DIV_A: Division
DIV_B: Division

class BotId(_message.Message):
    __slots__ = ("id", "team")
    ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    id: int
    team: Team
    def __init__(self, id: _Optional[int] = ..., team: _Optional[_Union[Team, str]] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class ControllerReply(_message.Message):
    __slots__ = ("status_code", "reason", "next_token", "verification")
    class StatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS_CODE: _ClassVar[ControllerReply.StatusCode]
        OK: _ClassVar[ControllerReply.StatusCode]
        REJECTED: _ClassVar[ControllerReply.StatusCode]
    UNKNOWN_STATUS_CODE: ControllerReply.StatusCode
    OK: ControllerReply.StatusCode
    REJECTED: ControllerReply.StatusCode
    class Verification(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_VERIFICATION: _ClassVar[ControllerReply.Verification]
        VERIFIED: _ClassVar[ControllerReply.Verification]
        UNVERIFIED: _ClassVar[ControllerReply.Verification]
    UNKNOWN_VERIFICATION: ControllerReply.Verification
    VERIFIED: ControllerReply.Verification
    UNVERIFIED: ControllerReply.Verification
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    NEXT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    status_code: ControllerReply.StatusCode
    reason: str
    next_token: str
    verification: ControllerReply.Verification
    def __init__(self, status_code: _Optional[_Union[ControllerReply.StatusCode, str]] = ..., reason: _Optional[str] = ..., next_token: _Optional[str] = ..., verification: _Optional[_Union[ControllerReply.Verification, str]] = ...) -> None: ...

class Signature(_message.Message):
    __slots__ = ("token", "pkcs1v15")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PKCS1V15_FIELD_NUMBER: _ClassVar[int]
    token: str
    pkcs1v15: bytes
    def __init__(self, token: _Optional[str] = ..., pkcs1v15: _Optional[bytes] = ...) -> None: ...

class BallSpeedMeasurement(_message.Message):
    __slots__ = ("timestamp", "ball_speed", "initial_ball_speed")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BALL_SPEED_FIELD_NUMBER: _ClassVar[int]
    INITIAL_BALL_SPEED_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    ball_speed: float
    initial_ball_speed: float
    def __init__(self, timestamp: _Optional[int] = ..., ball_speed: _Optional[float] = ..., initial_ball_speed: _Optional[float] = ...) -> None: ...
