import protobuf.ssl_gc_state_pb2 as _ssl_gc_state_pb2
import protobuf.ssl_game_controller_common_pb2 as _ssl_game_controller_common_pb2
import protobuf.ssl_game_controller_geometry_pb2 as _ssl_game_controller_geometry_pb2
import protobuf.ssl_game_event_2019_pb2 as _ssl_game_event_2019_pb2
import protobuf.ssl_referee_pb2 as _ssl_referee_pb2
from google.protobuf import proto.timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StateChange(_message.Message):
    __slots__ = ("id", "state_pre", "state", "change", "timestamp")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_PRE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: int
    state_pre: _ssl_gc_state_pb2.State
    state: _ssl_gc_state_pb2.State
    change: Change
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., state_pre: _Optional[_Union[_ssl_gc_state_pb2.State, _Mapping]] = ..., state: _Optional[_Union[_ssl_gc_state_pb2.State, _Mapping]] = ..., change: _Optional[_Union[Change, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Change(_message.Message):
    __slots__ = ("origin", "revertible", "new_command", "change_stage", "set_ball_placement_pos", "add_yellow_card", "add_red_card", "yellow_card_over", "add_game_event", "add_passive_game_event", "add_proposal", "start_ball_placement", "update_config", "update_team_state", "switch_colors", "revert", "new_game_state", "accept_proposal_group")
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    REVERTIBLE_FIELD_NUMBER: _ClassVar[int]
    NEW_COMMAND_FIELD_NUMBER: _ClassVar[int]
    CHANGE_STAGE_FIELD_NUMBER: _ClassVar[int]
    SET_BALL_PLACEMENT_POS_FIELD_NUMBER: _ClassVar[int]
    ADD_YELLOW_CARD_FIELD_NUMBER: _ClassVar[int]
    ADD_RED_CARD_FIELD_NUMBER: _ClassVar[int]
    YELLOW_CARD_OVER_FIELD_NUMBER: _ClassVar[int]
    ADD_GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    ADD_PASSIVE_GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    ADD_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    START_BALL_PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TEAM_STATE_FIELD_NUMBER: _ClassVar[int]
    SWITCH_COLORS_FIELD_NUMBER: _ClassVar[int]
    REVERT_FIELD_NUMBER: _ClassVar[int]
    NEW_GAME_STATE_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_PROPOSAL_GROUP_FIELD_NUMBER: _ClassVar[int]
    origin: str
    revertible: bool
    new_command: NewCommand
    change_stage: ChangeStage
    set_ball_placement_pos: SetBallPlacementPos
    add_yellow_card: AddYellowCard
    add_red_card: AddRedCard
    yellow_card_over: YellowCardOver
    add_game_event: AddGameEvent
    add_passive_game_event: AddPassiveGameEvent
    add_proposal: AddProposal
    start_ball_placement: StartBallPlacement
    update_config: UpdateConfig
    update_team_state: UpdateTeamState
    switch_colors: SwitchColors
    revert: Revert
    new_game_state: NewGameState
    accept_proposal_group: AcceptProposalGroup
    def __init__(self, origin: _Optional[str] = ..., revertible: bool = ..., new_command: _Optional[_Union[NewCommand, _Mapping]] = ..., change_stage: _Optional[_Union[ChangeStage, _Mapping]] = ..., set_ball_placement_pos: _Optional[_Union[SetBallPlacementPos, _Mapping]] = ..., add_yellow_card: _Optional[_Union[AddYellowCard, _Mapping]] = ..., add_red_card: _Optional[_Union[AddRedCard, _Mapping]] = ..., yellow_card_over: _Optional[_Union[YellowCardOver, _Mapping]] = ..., add_game_event: _Optional[_Union[AddGameEvent, _Mapping]] = ..., add_passive_game_event: _Optional[_Union[AddPassiveGameEvent, _Mapping]] = ..., add_proposal: _Optional[_Union[AddProposal, _Mapping]] = ..., start_ball_placement: _Optional[_Union[StartBallPlacement, _Mapping]] = ..., update_config: _Optional[_Union[UpdateConfig, _Mapping]] = ..., update_team_state: _Optional[_Union[UpdateTeamState, _Mapping]] = ..., switch_colors: _Optional[_Union[SwitchColors, _Mapping]] = ..., revert: _Optional[_Union[Revert, _Mapping]] = ..., new_game_state: _Optional[_Union[NewGameState, _Mapping]] = ..., accept_proposal_group: _Optional[_Union[AcceptProposalGroup, _Mapping]] = ..., **kwargs) -> None: ...

class NewCommand(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: _ssl_gc_state_pb2.Command
    def __init__(self, command: _Optional[_Union[_ssl_gc_state_pb2.Command, _Mapping]] = ...) -> None: ...

class ChangeStage(_message.Message):
    __slots__ = ("new_stage",)
    NEW_STAGE_FIELD_NUMBER: _ClassVar[int]
    new_stage: _ssl_referee_pb2.SSL_Referee.Stage
    def __init__(self, new_stage: _Optional[_Union[_ssl_referee_pb2.SSL_Referee.Stage, str]] = ...) -> None: ...

class SetBallPlacementPos(_message.Message):
    __slots__ = ("pos",)
    POS_FIELD_NUMBER: _ClassVar[int]
    pos: _ssl_game_controller_geometry_pb2.Vector2
    def __init__(self, pos: _Optional[_Union[_ssl_game_controller_geometry_pb2.Vector2, _Mapping]] = ...) -> None: ...

class AddYellowCard(_message.Message):
    __slots__ = ("for_team", "caused_by_game_event")
    FOR_TEAM_FIELD_NUMBER: _ClassVar[int]
    CAUSED_BY_GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    for_team: _ssl_game_controller_common_pb2.Team
    caused_by_game_event: _ssl_game_event_2019_pb2.GameEvent
    def __init__(self, for_team: _Optional[_Union[_ssl_game_controller_common_pb2.Team, str]] = ..., caused_by_game_event: _Optional[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]] = ...) -> None: ...

class AddRedCard(_message.Message):
    __slots__ = ("for_team", "caused_by_game_event")
    FOR_TEAM_FIELD_NUMBER: _ClassVar[int]
    CAUSED_BY_GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    for_team: _ssl_game_controller_common_pb2.Team
    caused_by_game_event: _ssl_game_event_2019_pb2.GameEvent
    def __init__(self, for_team: _Optional[_Union[_ssl_game_controller_common_pb2.Team, str]] = ..., caused_by_game_event: _Optional[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]] = ...) -> None: ...

class YellowCardOver(_message.Message):
    __slots__ = ("for_team",)
    FOR_TEAM_FIELD_NUMBER: _ClassVar[int]
    for_team: _ssl_game_controller_common_pb2.Team
    def __init__(self, for_team: _Optional[_Union[_ssl_game_controller_common_pb2.Team, str]] = ...) -> None: ...

class AddGameEvent(_message.Message):
    __slots__ = ("game_event",)
    GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    game_event: _ssl_game_event_2019_pb2.GameEvent
    def __init__(self, game_event: _Optional[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]] = ...) -> None: ...

class AddPassiveGameEvent(_message.Message):
    __slots__ = ("game_event",)
    GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    game_event: _ssl_game_event_2019_pb2.GameEvent
    def __init__(self, game_event: _Optional[_Union[_ssl_game_event_2019_pb2.GameEvent, _Mapping]] = ...) -> None: ...

class AddProposal(_message.Message):
    __slots__ = ("proposal",)
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    proposal: _ssl_gc_state_pb2.Proposal
    def __init__(self, proposal: _Optional[_Union[_ssl_gc_state_pb2.Proposal, _Mapping]] = ...) -> None: ...

class AcceptProposalGroup(_message.Message):
    __slots__ = ("group_id", "accepted_by")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_BY_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    accepted_by: str
    def __init__(self, group_id: _Optional[int] = ..., accepted_by: _Optional[str] = ...) -> None: ...

class StartBallPlacement(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Continue(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateConfig(_message.Message):
    __slots__ = ("division", "first_kickoff_team", "auto_continue")
    DIVISION_FIELD_NUMBER: _ClassVar[int]
    FIRST_KICKOFF_TEAM_FIELD_NUMBER: _ClassVar[int]
    AUTO_CONTINUE_FIELD_NUMBER: _ClassVar[int]
    division: _ssl_game_controller_common_pb2.Division
    first_kickoff_team: _ssl_game_controller_common_pb2.Team
    auto_continue: bool
    def __init__(self, division: _Optional[_Union[_ssl_game_controller_common_pb2.Division, str]] = ..., first_kickoff_team: _Optional[_Union[_ssl_game_controller_common_pb2.Team, str]] = ..., auto_continue: bool = ...) -> None: ...

class UpdateTeamState(_message.Message):
    __slots__ = ("for_team", "team_name", "goals", "goalkeeper", "timeouts_left", "timeout_time_left", "on_positive_half", "ball_placement_failures", "can_place_ball", "challenge_flags_left", "requests_bot_substitution", "requests_timeout", "requests_challenge", "requests_emergency_stop", "yellow_card", "red_card", "foul", "remove_yellow_card", "remove_red_card", "remove_foul")
    FOR_TEAM_FIELD_NUMBER: _ClassVar[int]
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    GOALS_FIELD_NUMBER: _ClassVar[int]
    GOALKEEPER_FIELD_NUMBER: _ClassVar[int]
    TIMEOUTS_LEFT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_TIME_LEFT_FIELD_NUMBER: _ClassVar[int]
    ON_POSITIVE_HALF_FIELD_NUMBER: _ClassVar[int]
    BALL_PLACEMENT_FAILURES_FIELD_NUMBER: _ClassVar[int]
    CAN_PLACE_BALL_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FLAGS_LEFT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_BOT_SUBSTITUTION_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_EMERGENCY_STOP_FIELD_NUMBER: _ClassVar[int]
    YELLOW_CARD_FIELD_NUMBER: _ClassVar[int]
    RED_CARD_FIELD_NUMBER: _ClassVar[int]
    FOUL_FIELD_NUMBER: _ClassVar[int]
    REMOVE_YELLOW_CARD_FIELD_NUMBER: _ClassVar[int]
    REMOVE_RED_CARD_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FOUL_FIELD_NUMBER: _ClassVar[int]
    for_team: _ssl_game_controller_common_pb2.Team
    team_name: str
    goals: int
    goalkeeper: int
    timeouts_left: int
    timeout_time_left: str
    on_positive_half: bool
    ball_placement_failures: int
    can_place_ball: bool
    challenge_flags_left: int
    requests_bot_substitution: bool
    requests_timeout: bool
    requests_challenge: bool
    requests_emergency_stop: bool
    yellow_card: _ssl_gc_state_pb2.YellowCard
    red_card: _ssl_gc_state_pb2.RedCard
    foul: _ssl_gc_state_pb2.Foul
    remove_yellow_card: int
    remove_red_card: int
    remove_foul: int
    def __init__(self, for_team: _Optional[_Union[_ssl_game_controller_common_pb2.Team, str]] = ..., team_name: _Optional[str] = ..., goals: _Optional[int] = ..., goalkeeper: _Optional[int] = ..., timeouts_left: _Optional[int] = ..., timeout_time_left: _Optional[str] = ..., on_positive_half: bool = ..., ball_placement_failures: _Optional[int] = ..., can_place_ball: bool = ..., challenge_flags_left: _Optional[int] = ..., requests_bot_substitution: bool = ..., requests_timeout: bool = ..., requests_challenge: bool = ..., requests_emergency_stop: bool = ..., yellow_card: _Optional[_Union[_ssl_gc_state_pb2.YellowCard, _Mapping]] = ..., red_card: _Optional[_Union[_ssl_gc_state_pb2.RedCard, _Mapping]] = ..., foul: _Optional[_Union[_ssl_gc_state_pb2.Foul, _Mapping]] = ..., remove_yellow_card: _Optional[int] = ..., remove_red_card: _Optional[int] = ..., remove_foul: _Optional[int] = ...) -> None: ...

class SwitchColors(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Revert(_message.Message):
    __slots__ = ("change_id",)
    CHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    change_id: int
    def __init__(self, change_id: _Optional[int] = ...) -> None: ...

class NewGameState(_message.Message):
    __slots__ = ("game_state",)
    GAME_STATE_FIELD_NUMBER: _ClassVar[int]
    game_state: _ssl_gc_state_pb2.GameState
    def __init__(self, game_state: _Optional[_Union[_ssl_gc_state_pb2.GameState, _Mapping]] = ...) -> None: ...
