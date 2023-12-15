import protobuf.ssl_referee_game_event_pb2 as _ssl_referee_game_event_pb2
import protobuf.ssl_game_event_2019_pb2 as _ssl_game_event_2019_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SSL_Referee(_message.Message):
    __slots__ = ("packet_timestamp", "stage", "stage_time_left", "command", "command_counter", "command_timestamp", "yellow", "blue", "designated_position", "blueTeamOnPositiveHalf", "gameEvent", "next_command", "game_events_old", "game_events", "proposed_game_events", "game_event_proposals", "source_identifier", "current_action_time_remaining")
    class Stage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NORMAL_FIRST_HALF_PRE: _ClassVar[SSL_Referee.Stage]
        NORMAL_FIRST_HALF: _ClassVar[SSL_Referee.Stage]
        NORMAL_HALF_TIME: _ClassVar[SSL_Referee.Stage]
        NORMAL_SECOND_HALF_PRE: _ClassVar[SSL_Referee.Stage]
        NORMAL_SECOND_HALF: _ClassVar[SSL_Referee.Stage]
        EXTRA_TIME_BREAK: _ClassVar[SSL_Referee.Stage]
        EXTRA_FIRST_HALF_PRE: _ClassVar[SSL_Referee.Stage]
        EXTRA_FIRST_HALF: _ClassVar[SSL_Referee.Stage]
        EXTRA_HALF_TIME: _ClassVar[SSL_Referee.Stage]
        EXTRA_SECOND_HALF_PRE: _ClassVar[SSL_Referee.Stage]
        EXTRA_SECOND_HALF: _ClassVar[SSL_Referee.Stage]
        PENALTY_SHOOTOUT_BREAK: _ClassVar[SSL_Referee.Stage]
        PENALTY_SHOOTOUT: _ClassVar[SSL_Referee.Stage]
        POST_GAME: _ClassVar[SSL_Referee.Stage]
    NORMAL_FIRST_HALF_PRE: SSL_Referee.Stage
    NORMAL_FIRST_HALF: SSL_Referee.Stage
    NORMAL_HALF_TIME: SSL_Referee.Stage
    NORMAL_SECOND_HALF_PRE: SSL_Referee.Stage
    NORMAL_SECOND_HALF: SSL_Referee.Stage
    EXTRA_TIME_BREAK: SSL_Referee.Stage
    EXTRA_FIRST_HALF_PRE: SSL_Referee.Stage
    EXTRA_FIRST_HALF: SSL_Referee.Stage
    EXTRA_HALF_TIME: SSL_Referee.Stage
    EXTRA_SECOND_HALF_PRE: SSL_Referee.Stage
    EXTRA_SECOND_HALF: SSL_Referee.Stage
    PENALTY_SHOOTOUT_BREAK: SSL_Referee.Stage
    PENALTY_SHOOTOUT: SSL_Referee.Stage
    POST_GAME: SSL_Referee.Stage
    class Command(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HALT: _ClassVar[SSL_Referee.Command]
        STOP: _ClassVar[SSL_Referee.Command]
        NORMAL_START: _ClassVar[SSL_Referee.Command]
        FORCE_START: _ClassVar[SSL_Referee.Command]
        PREPARE_KICKOFF_YELLOW: _ClassVar[SSL_Referee.Command]
        PREPARE_KICKOFF_BLUE: _ClassVar[SSL_Referee.Command]
        PREPARE_PENALTY_YELLOW: _ClassVar[SSL_Referee.Command]
        PREPARE_PENALTY_BLUE: _ClassVar[SSL_Referee.Command]
        DIRECT_FREE_YELLOW: _ClassVar[SSL_Referee.Command]
        DIRECT_FREE_BLUE: _ClassVar[SSL_Referee.Command]
        INDIRECT_FREE_YELLOW: _ClassVar[SSL_Referee.Command]
        INDIRECT_FREE_BLUE: _ClassVar[SSL_Referee.Command]
        TIMEOUT_YELLOW: _ClassVar[SSL_Referee.Command]
        TIMEOUT_BLUE: _ClassVar[SSL_Referee.Command]
        GOAL_YELLOW: _ClassVar[SSL_Referee.Command]
        GOAL_BLUE: _ClassVar[SSL_Referee.Command]
        BALL_PLACEMENT_YELLOW: _ClassVar[SSL_Referee.Command]
        BALL_PLACEMENT_BLUE: _ClassVar[SSL_Referee.Command]
    HALT: SSL_Referee.Command
    STOP: SSL_Referee.Command
    NORMAL_START: SSL_Referee.Command
    FORCE_START: SSL_Referee.Command
    PREPARE_KICKOFF_YELLOW: SSL_Referee.Command
    PREPARE_KICKOFF_BLUE: SSL_Referee.Command
    PREPARE_PENALTY_YELLOW: SSL_Referee.Command
    PREPARE_PENALTY_BLUE: SSL_Referee.Command
    DIRECT_FREE_YELLOW: SSL_Referee.Command
    DIRECT_FREE_BLUE: SSL_Referee.Command
    INDIRECT_FREE_YELLOW: SSL_Referee.Command
    INDIRECT_FREE_BLUE: SSL_Referee.Command
    TIMEOUT_YELLOW: SSL_Referee.Command
    TIMEOUT_BLUE: SSL_Referee.Command
    GOAL_YELLOW: SSL_Referee.Command
    GOAL_BLUE: SSL_Referee.Command
    BALL_PLACEMENT_YELLOW: SSL_Referee.Command
    BALL_PLACEMENT_BLUE: SSL_Referee.Command
    class TeamInfo(_message.Message):
        __slots__ = ("name", "score", "red_cards", "yellow_card_times", "yellow_cards", "timeouts", "timeout_time", "goalie", "foul_counter", "ball_placement_failures", "can_place_ball", "max_allowed_bots", "bot_substitution_intent", "ball_placement_failures_reached")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        RED_CARDS_FIELD_NUMBER: _ClassVar[int]
        YELLOW_CARD_TIMES_FIELD_NUMBER: _ClassVar[int]
        YELLOW_CARDS_FIELD_NUMBER: _ClassVar[int]
        TIMEOUTS_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_TIME_FIELD_NUMBER: _ClassVar[int]
        GOALIE_FIELD_NUMBER: _ClassVar[int]
        FOUL_COUNTER_FIELD_NUMBER: _ClassVar[int]
        BALL_PLACEMENT_FAILURES_FIELD_NUMBER: _ClassVar[int]
        CAN_PLACE_BALL_FIELD_NUMBER: _ClassVar[int]
        MAX_ALLOWED_BOTS_FIELD_NUMBER: _ClassVar[int]
        BOT_SUBSTITUTION_INTENT_FIELD_NUMBER: _ClassVar[int]
        BALL_PLACEMENT_FAILURES_REACHED_FIELD_NUMBER: _ClassVar[int]
        name: str
        score: int
        red_cards: int
        yellow_card_times: _containers.RepeatedScalarFieldContainer[int]
        yellow_cards: int
        timeouts: int
        timeout_time: int
        goalie: int
        foul_counter: int
        ball_placement_failures: int
        can_place_ball: bool
        max_allowed_bots: int
        bot_substitution_intent: bool
        ball_placement_failures_reached: bool
        def __init__(self, name: _Optional[str] = ..., score: _Optional[int] = ..., red_cards: _Optional[int] = ..., yellow_card_times: _Optional[_Iterable[int]] = ..., yellow_cards: _Optional[int] = ..., timeouts: _Optional[int] = ..., timeout_time: _Optional[int] = ..., goalie: _Optional[int] = ..., foul_counter: _Optional[int] = ..., ball_placement_failures: _Optional[int] = ..., can_place_ball: bool = ..., max_allowed_bots: _Optional[int] = ..., bot_substitution_intent: bool = ..., ball_placement_failures_reached: bool = ...) -> None: ...
    class Point(_message.Message):
        __slots__ = ("x", "y")
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        x: float
        y: float
        def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...
    PACKET_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    STAGE_TIME_LEFT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    COMMAND_COUNTER_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    YELLOW_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    DESIGNATED_POSITION_FIELD_NUMBER: _ClassVar[int]
    BLUETEAMONPOSITIVEHALF_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENT_FIELD_NUMBER: _ClassVar[int]
    NEXT_COMMAND_FIELD_NUMBER: _ClassVar[int]
    GAME_EVENTS_OLD_FIELD_NUMBER: _ClassVar[int]
    GAME_EVENTS_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_GAME_EVENTS_FIELD_NUMBER: _ClassVar[int]
    GAME_EVENT_PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ACTION_TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
    packet_timestamp: int
    stage: SSL_Referee.Stage
    stage_time_left: int
    command: SSL_Referee.Command
    command_counter: int
    command_timestamp: int
    yellow: SSL_Referee.TeamInfo
    blue: SSL_Referee.TeamInfo
    designated_position: SSL_Referee.Point
    blueTeamOnPositiveHalf: bool
    gameEvent: _ssl_referee_game_event_pb2.SSL_Referee_Game_Event
    next_command: SSL_Referee.Command
    game_events_old: _containers.RepeatedCompositeFieldContainer[_ssl_game_event_2019_pb2.GameEvent]
    game_events: _containers.RepeatedCompositeFieldContainer[_ssl_game_event_2019_pb2.GameEvent]
    proposed_game_events: _containers.RepeatedCompositeFieldContainer[ProposedGameEvent]
    game_event_proposals: _containers.RepeatedCompositeFieldContainer[GameEventProposalGroup]
    source_identifier: str
    current_action_time_remaining: int
    def __init__(self, packet_timestamp: _Optional[int] = ..., stage: _Optional[_Union[SSL_Referee.Stage, str]] = ..., stage_time_left: _Optional[int] = ..., command: _Optional[_Union[SSL_Referee.Command, str]] = ..., command_counter: _Optional[int] = ..., command_timestamp: _Optional[int] = ..., yellow: _Optional[_Union[SSL_Referee.TeamInfo, _Mapping]] = ..., blue: _Optional[_Union[SSL_Referee.TeamInfo, _Mapping]] = ..., designated_position: _Optional[_Union[SSL_Referee.Point, _Mapping]] = ..., blueTeamOnPositiveHalf: bool = ..., gameEvent: _Optional[_Union[_ssl_referee_game_event_pb2.SSL_Referee_Game_Event, _Mapping]] = ..., next_command: _Optional[_Union[SSL_Referee.Command, str]] = ..., game_events_old: _Optional[_Iterable[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]]] = ..., game_events: _Optional[_Iterable[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]]] = ..., proposed_game_events: _Optional[_Iterable[_Union[ProposedGameEvent, _Mapping]]] = ..., game_event_proposals: _Optional[_Iterable[_Union[GameEventProposalGroup, _Mapping]]] = ..., source_identifier: _Optional[str] = ..., current_action_time_remaining: _Optional[int] = ...) -> None: ...

class ProposedGameEvent(_message.Message):
    __slots__ = ("valid_until", "proposer_id", "game_event")
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    valid_until: int
    proposer_id: str
    game_event: _ssl_game_event_2019_pb2.GameEvent
    def __init__(self, valid_until: _Optional[int] = ..., proposer_id: _Optional[str] = ..., game_event: _Optional[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]] = ...) -> None: ...

class GameEventProposalGroup(_message.Message):
    __slots__ = ("game_event", "accepted")
    GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    game_event: _containers.RepeatedCompositeFieldContainer[_ssl_game_event_2019_pb2.GameEvent]
    accepted: bool
    def __init__(self, game_event: _Optional[_Iterable[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]]] = ..., accepted: bool = ...) -> None: ...
