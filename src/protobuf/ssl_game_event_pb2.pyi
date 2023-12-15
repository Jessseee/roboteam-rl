from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Game_Event(_message.Message):
    __slots__ = ("gameEventType", "originator", "message")
    class GameEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Game_Event.GameEventType]
        CUSTOM: _ClassVar[Game_Event.GameEventType]
        NUMBER_OF_PLAYERS: _ClassVar[Game_Event.GameEventType]
        BALL_LEFT_FIELD: _ClassVar[Game_Event.GameEventType]
        GOAL: _ClassVar[Game_Event.GameEventType]
        KICK_TIMEOUT: _ClassVar[Game_Event.GameEventType]
        NO_PROGRESS_IN_GAME: _ClassVar[Game_Event.GameEventType]
        BOT_COLLISION: _ClassVar[Game_Event.GameEventType]
        MULTIPLE_DEFENDER: _ClassVar[Game_Event.GameEventType]
        MULTIPLE_DEFENDER_PARTIALLY: _ClassVar[Game_Event.GameEventType]
        ATTACKER_IN_DEFENSE_AREA: _ClassVar[Game_Event.GameEventType]
        ICING: _ClassVar[Game_Event.GameEventType]
        BALL_SPEED: _ClassVar[Game_Event.GameEventType]
        ROBOT_STOP_SPEED: _ClassVar[Game_Event.GameEventType]
        BALL_DRIBBLING: _ClassVar[Game_Event.GameEventType]
        ATTACKER_TOUCH_KEEPER: _ClassVar[Game_Event.GameEventType]
        DOUBLE_TOUCH: _ClassVar[Game_Event.GameEventType]
        ATTACKER_TO_DEFENCE_AREA: _ClassVar[Game_Event.GameEventType]
        DEFENDER_TO_KICK_POINT_DISTANCE: _ClassVar[Game_Event.GameEventType]
        BALL_HOLDING: _ClassVar[Game_Event.GameEventType]
        INDIRECT_GOAL: _ClassVar[Game_Event.GameEventType]
        BALL_PLACEMENT_FAILED: _ClassVar[Game_Event.GameEventType]
        CHIP_ON_GOAL: _ClassVar[Game_Event.GameEventType]
    UNKNOWN: Game_Event.GameEventType
    CUSTOM: Game_Event.GameEventType
    NUMBER_OF_PLAYERS: Game_Event.GameEventType
    BALL_LEFT_FIELD: Game_Event.GameEventType
    GOAL: Game_Event.GameEventType
    KICK_TIMEOUT: Game_Event.GameEventType
    NO_PROGRESS_IN_GAME: Game_Event.GameEventType
    BOT_COLLISION: Game_Event.GameEventType
    MULTIPLE_DEFENDER: Game_Event.GameEventType
    MULTIPLE_DEFENDER_PARTIALLY: Game_Event.GameEventType
    ATTACKER_IN_DEFENSE_AREA: Game_Event.GameEventType
    ICING: Game_Event.GameEventType
    BALL_SPEED: Game_Event.GameEventType
    ROBOT_STOP_SPEED: Game_Event.GameEventType
    BALL_DRIBBLING: Game_Event.GameEventType
    ATTACKER_TOUCH_KEEPER: Game_Event.GameEventType
    DOUBLE_TOUCH: Game_Event.GameEventType
    ATTACKER_TO_DEFENCE_AREA: Game_Event.GameEventType
    DEFENDER_TO_KICK_POINT_DISTANCE: Game_Event.GameEventType
    BALL_HOLDING: Game_Event.GameEventType
    INDIRECT_GOAL: Game_Event.GameEventType
    BALL_PLACEMENT_FAILED: Game_Event.GameEventType
    CHIP_ON_GOAL: Game_Event.GameEventType
    class Team(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEAM_UNKNOWN: _ClassVar[Game_Event.Team]
        TEAM_YELLOW: _ClassVar[Game_Event.Team]
        TEAM_BLUE: _ClassVar[Game_Event.Team]
    TEAM_UNKNOWN: Game_Event.Team
    TEAM_YELLOW: Game_Event.Team
    TEAM_BLUE: Game_Event.Team
    class Originator(_message.Message):
        __slots__ = ("team", "botId")
        TEAM_FIELD_NUMBER: _ClassVar[int]
        BOTID_FIELD_NUMBER: _ClassVar[int]
        team: Game_Event.Team
        botId: int
        def __init__(self, team: _Optional[_Union[Game_Event.Team, str]] = ..., botId: _Optional[int] = ...) -> None: ...
    GAMEEVENTTYPE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    gameEventType: Game_Event.GameEventType
    originator: Game_Event.Originator
    message: str
    def __init__(self, gameEventType: _Optional[_Union[Game_Event.GameEventType, str]] = ..., originator: _Optional[_Union[Game_Event.Originator, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...
