import protobuf.ssl_game_controller_common_pb2 as _ssl_game_controller_common_pb2
import protobuf.ssl_game_controller_geometry_pb2 as _ssl_game_controller_geometry_pb2
import protobuf.ssl_game_event_2019_pb2 as _ssl_game_event_2019_pb2
import protobuf.ssl_referee_pb2 as _ssl_referee_pb2
from google.protobuf import proto.duration_pb2 as _duration_pb2
from google.protobuf import proto.timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class YellowCard(_message.Message):
    __slots__ = ("id", "caused_by_game_event", "time_remaining")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAUSED_BY_GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
    id: int
    caused_by_game_event: _ssl_game_event_2019_pb2.GameEvent
    time_remaining: _duration_pb2.Duration
    def __init__(self, id: _Optional[int] = ..., caused_by_game_event: _Optional[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]] = ..., time_remaining: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class RedCard(_message.Message):
    __slots__ = ("id", "caused_by_game_event")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAUSED_BY_GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    id: int
    caused_by_game_event: _ssl_game_event_2019_pb2.GameEvent
    def __init__(self, id: _Optional[int] = ..., caused_by_game_event: _Optional[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]] = ...) -> None: ...

class Foul(_message.Message):
    __slots__ = ("id", "caused_by_game_event", "timestamp")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAUSED_BY_GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: int
    caused_by_game_event: _ssl_game_event_2019_pb2.GameEvent
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., caused_by_game_event: _Optional[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ("type", "for_team")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Command.Type]
        HALT: _ClassVar[Command.Type]
        STOP: _ClassVar[Command.Type]
        NORMAL_START: _ClassVar[Command.Type]
        FORCE_START: _ClassVar[Command.Type]
        DIRECT: _ClassVar[Command.Type]
        INDIRECT: _ClassVar[Command.Type]
        KICKOFF: _ClassVar[Command.Type]
        PENALTY: _ClassVar[Command.Type]
        TIMEOUT: _ClassVar[Command.Type]
        BALL_PLACEMENT: _ClassVar[Command.Type]
    UNKNOWN: Command.Type
    HALT: Command.Type
    STOP: Command.Type
    NORMAL_START: Command.Type
    FORCE_START: Command.Type
    DIRECT: Command.Type
    INDIRECT: Command.Type
    KICKOFF: Command.Type
    PENALTY: Command.Type
    TIMEOUT: Command.Type
    BALL_PLACEMENT: Command.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FOR_TEAM_FIELD_NUMBER: _ClassVar[int]
    type: Command.Type
    for_team: _ssl_game_controller_common_pb2.Team
    def __init__(self, type: _Optional[_Union[Command.Type, str]] = ..., for_team: _Optional[_Union[_ssl_game_controller_common_pb2.Team, str]] = ...) -> None: ...

class GameState(_message.Message):
    __slots__ = ("type", "for_team")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[GameState.Type]
        HALT: _ClassVar[GameState.Type]
        STOP: _ClassVar[GameState.Type]
        RUNNING: _ClassVar[GameState.Type]
        FREE_KICK: _ClassVar[GameState.Type]
        KICKOFF: _ClassVar[GameState.Type]
        PENALTY: _ClassVar[GameState.Type]
        TIMEOUT: _ClassVar[GameState.Type]
        BALL_PLACEMENT: _ClassVar[GameState.Type]
    UNKNOWN: GameState.Type
    HALT: GameState.Type
    STOP: GameState.Type
    RUNNING: GameState.Type
    FREE_KICK: GameState.Type
    KICKOFF: GameState.Type
    PENALTY: GameState.Type
    TIMEOUT: GameState.Type
    BALL_PLACEMENT: GameState.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FOR_TEAM_FIELD_NUMBER: _ClassVar[int]
    type: GameState.Type
    for_team: _ssl_game_controller_common_pb2.Team
    def __init__(self, type: _Optional[_Union[GameState.Type, str]] = ..., for_team: _Optional[_Union[_ssl_game_controller_common_pb2.Team, str]] = ...) -> None: ...

class Proposal(_message.Message):
    __slots__ = ("timestamp", "game_event")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    game_event: _ssl_game_event_2019_pb2.GameEvent
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., game_event: _Optional[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]] = ...) -> None: ...

class ProposalGroup(_message.Message):
    __slots__ = ("proposals", "accepted")
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    proposals: _containers.RepeatedCompositeFieldContainer[Proposal]
    accepted: bool
    def __init__(self, proposals: _Optional[_Iterable[_Union[Proposal, _Mapping]]] = ..., accepted: bool = ...) -> None: ...

class TeamInfo(_message.Message):
    __slots__ = ("name", "goals", "goalkeeper", "yellow_cards", "red_cards", "timeouts_left", "timeout_time_left", "on_positive_half", "fouls", "ball_placement_failures", "ball_placement_failures_reached", "can_place_ball", "max_allowed_bots", "requests_bot_substitution_since", "requests_timeout_since", "requests_emergency_stop_since", "challenge_flags")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GOALS_FIELD_NUMBER: _ClassVar[int]
    GOALKEEPER_FIELD_NUMBER: _ClassVar[int]
    YELLOW_CARDS_FIELD_NUMBER: _ClassVar[int]
    RED_CARDS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUTS_LEFT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_TIME_LEFT_FIELD_NUMBER: _ClassVar[int]
    ON_POSITIVE_HALF_FIELD_NUMBER: _ClassVar[int]
    FOULS_FIELD_NUMBER: _ClassVar[int]
    BALL_PLACEMENT_FAILURES_FIELD_NUMBER: _ClassVar[int]
    BALL_PLACEMENT_FAILURES_REACHED_FIELD_NUMBER: _ClassVar[int]
    CAN_PLACE_BALL_FIELD_NUMBER: _ClassVar[int]
    MAX_ALLOWED_BOTS_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_BOT_SUBSTITUTION_SINCE_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_TIMEOUT_SINCE_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_EMERGENCY_STOP_SINCE_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    goals: int
    goalkeeper: int
    yellow_cards: _containers.RepeatedCompositeFieldContainer[YellowCard]
    red_cards: _containers.RepeatedCompositeFieldContainer[RedCard]
    timeouts_left: int
    timeout_time_left: _duration_pb2.Duration
    on_positive_half: bool
    fouls: _containers.RepeatedCompositeFieldContainer[Foul]
    ball_placement_failures: int
    ball_placement_failures_reached: bool
    can_place_ball: bool
    max_allowed_bots: int
    requests_bot_substitution_since: _timestamp_pb2.Timestamp
    requests_timeout_since: _timestamp_pb2.Timestamp
    requests_emergency_stop_since: _timestamp_pb2.Timestamp
    challenge_flags: int
    def __init__(self, name: _Optional[str] = ..., goals: _Optional[int] = ..., goalkeeper: _Optional[int] = ..., yellow_cards: _Optional[_Iterable[_Union[YellowCard, _Mapping]]] = ..., red_cards: _Optional[_Iterable[_Union[RedCard, _Mapping]]] = ..., timeouts_left: _Optional[int] = ..., timeout_time_left: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., on_positive_half: bool = ..., fouls: _Optional[_Iterable[_Union[Foul, _Mapping]]] = ..., ball_placement_failures: _Optional[int] = ..., ball_placement_failures_reached: bool = ..., can_place_ball: bool = ..., max_allowed_bots: _Optional[int] = ..., requests_bot_substitution_since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., requests_timeout_since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., requests_emergency_stop_since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., challenge_flags: _Optional[int] = ...) -> None: ...

class State(_message.Message):
    __slots__ = ("stage", "command", "game_state", "stage_time_elapsed", "stage_time_left", "match_time_start", "team_state", "placement_pos", "next_command", "current_action_time_remaining", "game_events", "proposal_groups", "division", "auto_continue", "first_kickoff_team")
    class TeamStateEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TeamInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TeamInfo, _Mapping]] = ...) -> None: ...
    STAGE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    GAME_STATE_FIELD_NUMBER: _ClassVar[int]
    STAGE_TIME_ELAPSED_FIELD_NUMBER: _ClassVar[int]
    STAGE_TIME_LEFT_FIELD_NUMBER: _ClassVar[int]
    MATCH_TIME_START_FIELD_NUMBER: _ClassVar[int]
    TEAM_STATE_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_POS_FIELD_NUMBER: _ClassVar[int]
    NEXT_COMMAND_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ACTION_TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
    GAME_EVENTS_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_GROUPS_FIELD_NUMBER: _ClassVar[int]
    DIVISION_FIELD_NUMBER: _ClassVar[int]
    AUTO_CONTINUE_FIELD_NUMBER: _ClassVar[int]
    FIRST_KICKOFF_TEAM_FIELD_NUMBER: _ClassVar[int]
    stage: _ssl_referee_pb2.SSL_Referee.Stage
    command: Command
    game_state: GameState
    stage_time_elapsed: _duration_pb2.Duration
    stage_time_left: _duration_pb2.Duration
    match_time_start: _timestamp_pb2.Timestamp
    team_state: _containers.MessageMap[str, TeamInfo]
    placement_pos: _ssl_game_controller_geometry_pb2.Vector2
    next_command: Command
    current_action_time_remaining: _duration_pb2.Duration
    game_events: _containers.RepeatedCompositeFieldContainer[_ssl_game_event_2019_pb2.GameEvent]
    proposal_groups: _containers.RepeatedCompositeFieldContainer[ProposalGroup]
    division: _ssl_game_controller_common_pb2.Division
    auto_continue: bool
    first_kickoff_team: _ssl_game_controller_common_pb2.Team
    def __init__(self, stage: _Optional[_Union[_ssl_referee_pb2.SSL_Referee.Stage, str]] = ..., command: _Optional[_Union[Command, _Mapping]] = ..., game_state: _Optional[_Union[GameState, _Mapping]] = ..., stage_time_elapsed: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., stage_time_left: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., match_time_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., team_state: _Optional[_Mapping[str, TeamInfo]] = ..., placement_pos: _Optional[_Union[_ssl_game_controller_geometry_pb2.Vector2, _Mapping]] = ..., next_command: _Optional[_Union[Command, _Mapping]] = ..., current_action_time_remaining: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., game_events: _Optional[_Iterable[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]]] = ..., proposal_groups: _Optional[_Iterable[_Union[ProposalGroup, _Mapping]]] = ..., division: _Optional[_Union[_ssl_game_controller_common_pb2.Division, str]] = ..., auto_continue: bool = ..., first_kickoff_team: _Optional[_Union[_ssl_game_controller_common_pb2.Team, str]] = ...) -> None: ...
