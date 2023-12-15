import protobuf.ssl_referee_pb2 as _ssl_referee_pb2
import protobuf.ssl_referee_game_event_pb2 as _ssl_referee_game_event_pb2
import protobuf.ssl_game_event_2019_pb2 as _ssl_game_event_2019_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GameState(_message.Message):
    __slots__ = ("stage", "stage_time_left", "state", "yellow", "blue", "designated_position", "game_event", "goals_flipped", "is_real_game_running", "current_action_time_remaining", "next_state", "game_event_2019")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Halt: _ClassVar[GameState.State]
        Stop: _ClassVar[GameState.State]
        Game: _ClassVar[GameState.State]
        GameForce: _ClassVar[GameState.State]
        KickoffYellowPrepare: _ClassVar[GameState.State]
        KickoffYellow: _ClassVar[GameState.State]
        PenaltyYellowPrepare: _ClassVar[GameState.State]
        PenaltyYellow: _ClassVar[GameState.State]
        PenaltyYellowRunning: _ClassVar[GameState.State]
        DirectYellow: _ClassVar[GameState.State]
        IndirectYellow: _ClassVar[GameState.State]
        BallPlacementYellow: _ClassVar[GameState.State]
        KickoffBluePrepare: _ClassVar[GameState.State]
        KickoffBlue: _ClassVar[GameState.State]
        PenaltyBluePrepare: _ClassVar[GameState.State]
        PenaltyBlue: _ClassVar[GameState.State]
        PenaltyBlueRunning: _ClassVar[GameState.State]
        DirectBlue: _ClassVar[GameState.State]
        IndirectBlue: _ClassVar[GameState.State]
        BallPlacementBlue: _ClassVar[GameState.State]
        TimeoutYellow: _ClassVar[GameState.State]
        TimeoutBlue: _ClassVar[GameState.State]
    Halt: GameState.State
    Stop: GameState.State
    Game: GameState.State
    GameForce: GameState.State
    KickoffYellowPrepare: GameState.State
    KickoffYellow: GameState.State
    PenaltyYellowPrepare: GameState.State
    PenaltyYellow: GameState.State
    PenaltyYellowRunning: GameState.State
    DirectYellow: GameState.State
    IndirectYellow: GameState.State
    BallPlacementYellow: GameState.State
    KickoffBluePrepare: GameState.State
    KickoffBlue: GameState.State
    PenaltyBluePrepare: GameState.State
    PenaltyBlue: GameState.State
    PenaltyBlueRunning: GameState.State
    DirectBlue: GameState.State
    IndirectBlue: GameState.State
    BallPlacementBlue: GameState.State
    TimeoutYellow: GameState.State
    TimeoutBlue: GameState.State
    STAGE_FIELD_NUMBER: _ClassVar[int]
    STAGE_TIME_LEFT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    YELLOW_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    DESIGNATED_POSITION_FIELD_NUMBER: _ClassVar[int]
    GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    GOALS_FLIPPED_FIELD_NUMBER: _ClassVar[int]
    IS_REAL_GAME_RUNNING_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ACTION_TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
    NEXT_STATE_FIELD_NUMBER: _ClassVar[int]
    GAME_EVENT_2019_FIELD_NUMBER: _ClassVar[int]
    stage: _ssl_referee_pb2.SSL_Referee.Stage
    stage_time_left: int
    state: GameState.State
    yellow: _ssl_referee_pb2.SSL_Referee.TeamInfo
    blue: _ssl_referee_pb2.SSL_Referee.TeamInfo
    designated_position: _ssl_referee_pb2.SSL_Referee.Point
    game_event: _ssl_referee_game_event_pb2.SSL_Referee_Game_Event
    goals_flipped: bool
    is_real_game_running: bool
    current_action_time_remaining: int
    next_state: GameState.State
    game_event_2019: _containers.RepeatedCompositeFieldContainer[_ssl_game_event_2019_pb2.GameEvent]
    def __init__(self, stage: _Optional[_Union[_ssl_referee_pb2.SSL_Referee.Stage, str]] = ..., stage_time_left: _Optional[int] = ..., state: _Optional[_Union[GameState.State, str]] = ..., yellow: _Optional[_Union[_ssl_referee_pb2.SSL_Referee.TeamInfo, _Mapping]] = ..., blue: _Optional[_Union[_ssl_referee_pb2.SSL_Referee.TeamInfo, _Mapping]] = ..., designated_position: _Optional[_Union[_ssl_referee_pb2.SSL_Referee.Point, _Mapping]] = ..., game_event: _Optional[_Union[_ssl_referee_game_event_pb2.SSL_Referee_Game_Event, _Mapping]] = ..., goals_flipped: bool = ..., is_real_game_running: bool = ..., current_action_time_remaining: _Optional[int] = ..., next_state: _Optional[_Union[GameState.State, str]] = ..., game_event_2019: _Optional[_Iterable[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]]] = ...) -> None: ...
