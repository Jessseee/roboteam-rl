import protobuf.debug_pb2 as _debug_pb2
import protobuf.gamestate_pb2 as _gamestate_pb2
import protobuf.robot_pb2 as _robot_pb2
import protobuf.world_pb2 as _world_pb2
import protobuf.userinput_pb2 as _userinput_pb2
import protobuf.logfile_pb2 as _logfile_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StrategyOption(_message.Message):
    __slots__ = ("name", "default_value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    default_value: bool
    def __init__(self, name: _Optional[str] = ..., default_value: bool = ...) -> None: ...

class StatusStrategy(_message.Message):
    __slots__ = ("state", "filename", "name", "current_entry_point", "entry_point", "has_debugger", "options")
    class STATE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLOSED: _ClassVar[StatusStrategy.STATE]
        RUNNING: _ClassVar[StatusStrategy.STATE]
        FAILED: _ClassVar[StatusStrategy.STATE]
        COMPILING: _ClassVar[StatusStrategy.STATE]
    CLOSED: StatusStrategy.STATE
    RUNNING: StatusStrategy.STATE
    FAILED: StatusStrategy.STATE
    COMPILING: StatusStrategy.STATE
    STATE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ENTRY_POINT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_POINT_FIELD_NUMBER: _ClassVar[int]
    HAS_DEBUGGER_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    state: StatusStrategy.STATE
    filename: str
    name: str
    current_entry_point: str
    entry_point: _containers.RepeatedScalarFieldContainer[str]
    has_debugger: bool
    options: _containers.RepeatedCompositeFieldContainer[StrategyOption]
    def __init__(self, state: _Optional[_Union[StatusStrategy.STATE, str]] = ..., filename: _Optional[str] = ..., name: _Optional[str] = ..., current_entry_point: _Optional[str] = ..., entry_point: _Optional[_Iterable[str]] = ..., has_debugger: bool = ..., options: _Optional[_Iterable[_Union[StrategyOption, _Mapping]]] = ...) -> None: ...

class GitInfo(_message.Message):
    __slots__ = ("kind", "hash", "diff", "min_hash", "error")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLUE: _ClassVar[GitInfo.Kind]
        YELLOW: _ClassVar[GitInfo.Kind]
        AUTOREF: _ClassVar[GitInfo.Kind]
        RA: _ClassVar[GitInfo.Kind]
        CONFIG: _ClassVar[GitInfo.Kind]
    BLUE: GitInfo.Kind
    YELLOW: GitInfo.Kind
    AUTOREF: GitInfo.Kind
    RA: GitInfo.Kind
    CONFIG: GitInfo.Kind
    KIND_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    DIFF_FIELD_NUMBER: _ClassVar[int]
    MIN_HASH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    kind: GitInfo.Kind
    hash: str
    diff: str
    min_hash: str
    error: str
    def __init__(self, kind: _Optional[_Union[GitInfo.Kind, str]] = ..., hash: _Optional[str] = ..., diff: _Optional[str] = ..., min_hash: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class StatusStrategyWrapper(_message.Message):
    __slots__ = ("type", "status")
    class StrategyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLUE: _ClassVar[StatusStrategyWrapper.StrategyType]
        YELLOW: _ClassVar[StatusStrategyWrapper.StrategyType]
        AUTOREF: _ClassVar[StatusStrategyWrapper.StrategyType]
        REPLAY_BLUE: _ClassVar[StatusStrategyWrapper.StrategyType]
        REPLAY_YELLOW: _ClassVar[StatusStrategyWrapper.StrategyType]
    BLUE: StatusStrategyWrapper.StrategyType
    YELLOW: StatusStrategyWrapper.StrategyType
    AUTOREF: StatusStrategyWrapper.StrategyType
    REPLAY_BLUE: StatusStrategyWrapper.StrategyType
    REPLAY_YELLOW: StatusStrategyWrapper.StrategyType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    type: StatusStrategyWrapper.StrategyType
    status: StatusStrategy
    def __init__(self, type: _Optional[_Union[StatusStrategyWrapper.StrategyType, str]] = ..., status: _Optional[_Union[StatusStrategy, _Mapping]] = ...) -> None: ...

class Timing(_message.Message):
    __slots__ = ("blue_total", "blue_path", "yellow_total", "yellow_path", "autoref_total", "tracking", "controller", "transceiver", "transceiver_rtt", "simulator")
    BLUE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    BLUE_PATH_FIELD_NUMBER: _ClassVar[int]
    YELLOW_TOTAL_FIELD_NUMBER: _ClassVar[int]
    YELLOW_PATH_FIELD_NUMBER: _ClassVar[int]
    AUTOREF_TOTAL_FIELD_NUMBER: _ClassVar[int]
    TRACKING_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    TRANSCEIVER_FIELD_NUMBER: _ClassVar[int]
    TRANSCEIVER_RTT_FIELD_NUMBER: _ClassVar[int]
    SIMULATOR_FIELD_NUMBER: _ClassVar[int]
    blue_total: float
    blue_path: float
    yellow_total: float
    yellow_path: float
    autoref_total: float
    tracking: float
    controller: float
    transceiver: float
    transceiver_rtt: float
    simulator: float
    def __init__(self, blue_total: _Optional[float] = ..., blue_path: _Optional[float] = ..., yellow_total: _Optional[float] = ..., yellow_path: _Optional[float] = ..., autoref_total: _Optional[float] = ..., tracking: _Optional[float] = ..., controller: _Optional[float] = ..., transceiver: _Optional[float] = ..., transceiver_rtt: _Optional[float] = ..., simulator: _Optional[float] = ...) -> None: ...

class StatusTransceiver(_message.Message):
    __slots__ = ("active", "error", "dropped_usb_packets", "dropped_commands")
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DROPPED_USB_PACKETS_FIELD_NUMBER: _ClassVar[int]
    DROPPED_COMMANDS_FIELD_NUMBER: _ClassVar[int]
    active: bool
    error: str
    dropped_usb_packets: int
    dropped_commands: int
    def __init__(self, active: bool = ..., error: _Optional[str] = ..., dropped_usb_packets: _Optional[int] = ..., dropped_commands: _Optional[int] = ...) -> None: ...

class PortBindError(_message.Message):
    __slots__ = ("port",)
    PORT_FIELD_NUMBER: _ClassVar[int]
    port: int
    def __init__(self, port: _Optional[int] = ...) -> None: ...

class OptionStatus(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: bool
    def __init__(self, name: _Optional[str] = ..., value: bool = ...) -> None: ...

class StatusGameController(_message.Message):
    __slots__ = ("current_state",)
    class GameControllerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STOPPED: _ClassVar[StatusGameController.GameControllerState]
        STARTING: _ClassVar[StatusGameController.GameControllerState]
        RUNNING: _ClassVar[StatusGameController.GameControllerState]
        CRASHED: _ClassVar[StatusGameController.GameControllerState]
        NOT_RESPONDING: _ClassVar[StatusGameController.GameControllerState]
    STOPPED: StatusGameController.GameControllerState
    STARTING: StatusGameController.GameControllerState
    RUNNING: StatusGameController.GameControllerState
    CRASHED: StatusGameController.GameControllerState
    NOT_RESPONDING: StatusGameController.GameControllerState
    CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    current_state: StatusGameController.GameControllerState
    def __init__(self, current_state: _Optional[_Union[StatusGameController.GameControllerState, str]] = ...) -> None: ...

class StatusAmun(_message.Message):
    __slots__ = ("port_bind_error", "options", "game_controller")
    PORT_BIND_ERROR_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    GAME_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    port_bind_error: PortBindError
    options: _containers.RepeatedCompositeFieldContainer[OptionStatus]
    game_controller: StatusGameController
    def __init__(self, port_bind_error: _Optional[_Union[PortBindError, _Mapping]] = ..., options: _Optional[_Iterable[_Union[OptionStatus, _Mapping]]] = ..., game_controller: _Optional[_Union[StatusGameController, _Mapping]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("time", "game_state", "world_state", "geometry", "team_blue", "team_yellow", "strategy_blue", "strategy_yellow", "strategy_autoref", "debug", "timing", "radio_command", "transceiver", "user_input_blue", "user_input_yellow", "amun_state", "timer_scaling", "blue_running", "yellow_running", "autoref_running", "execution_state", "execution_game_state", "execution_user_input", "log_id", "original_frame_number", "status_strategy", "pure_ui_response", "git_info")
    TIME_FIELD_NUMBER: _ClassVar[int]
    GAME_STATE_FIELD_NUMBER: _ClassVar[int]
    WORLD_STATE_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    TEAM_BLUE_FIELD_NUMBER: _ClassVar[int]
    TEAM_YELLOW_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_BLUE_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_YELLOW_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_AUTOREF_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    RADIO_COMMAND_FIELD_NUMBER: _ClassVar[int]
    TRANSCEIVER_FIELD_NUMBER: _ClassVar[int]
    USER_INPUT_BLUE_FIELD_NUMBER: _ClassVar[int]
    USER_INPUT_YELLOW_FIELD_NUMBER: _ClassVar[int]
    AMUN_STATE_FIELD_NUMBER: _ClassVar[int]
    TIMER_SCALING_FIELD_NUMBER: _ClassVar[int]
    BLUE_RUNNING_FIELD_NUMBER: _ClassVar[int]
    YELLOW_RUNNING_FIELD_NUMBER: _ClassVar[int]
    AUTOREF_RUNNING_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_GAME_STATE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_USER_INPUT_FIELD_NUMBER: _ClassVar[int]
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_FRAME_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    PURE_UI_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GIT_INFO_FIELD_NUMBER: _ClassVar[int]
    time: int
    game_state: _gamestate_pb2.GameState
    world_state: _world_pb2.State
    geometry: _world_pb2.Geometry
    team_blue: _robot_pb2.Team
    team_yellow: _robot_pb2.Team
    strategy_blue: StatusStrategy
    strategy_yellow: StatusStrategy
    strategy_autoref: StatusStrategy
    debug: _containers.RepeatedCompositeFieldContainer[_debug_pb2.DebugValues]
    timing: Timing
    radio_command: _containers.RepeatedCompositeFieldContainer[_robot_pb2.RadioCommand]
    transceiver: StatusTransceiver
    user_input_blue: _userinput_pb2.UserInput
    user_input_yellow: _userinput_pb2.UserInput
    amun_state: StatusAmun
    timer_scaling: float
    blue_running: bool
    yellow_running: bool
    autoref_running: bool
    execution_state: _world_pb2.State
    execution_game_state: _gamestate_pb2.GameState
    execution_user_input: _userinput_pb2.UserInput
    log_id: _logfile_pb2.Uid
    original_frame_number: int
    status_strategy: StatusStrategyWrapper
    pure_ui_response: UiResponse
    git_info: _containers.RepeatedCompositeFieldContainer[GitInfo]
    def __init__(self, time: _Optional[int] = ..., game_state: _Optional[_Union[_gamestate_pb2.GameState, _Mapping]] = ..., world_state: _Optional[_Union[_world_pb2.State, _Mapping]] = ..., geometry: _Optional[_Union[_world_pb2.Geometry, _Mapping]] = ..., team_blue: _Optional[_Union[_robot_pb2.Team, _Mapping]] = ..., team_yellow: _Optional[_Union[_robot_pb2.Team, _Mapping]] = ..., strategy_blue: _Optional[_Union[StatusStrategy, _Mapping]] = ..., strategy_yellow: _Optional[_Union[StatusStrategy, _Mapping]] = ..., strategy_autoref: _Optional[_Union[StatusStrategy, _Mapping]] = ..., debug: _Optional[_Iterable[_Union[_debug_pb2.DebugValues, _Mapping]]] = ..., timing: _Optional[_Union[Timing, _Mapping]] = ..., radio_command: _Optional[_Iterable[_Union[_robot_pb2.RadioCommand, _Mapping]]] = ..., transceiver: _Optional[_Union[StatusTransceiver, _Mapping]] = ..., user_input_blue: _Optional[_Union[_userinput_pb2.UserInput, _Mapping]] = ..., user_input_yellow: _Optional[_Union[_userinput_pb2.UserInput, _Mapping]] = ..., amun_state: _Optional[_Union[StatusAmun, _Mapping]] = ..., timer_scaling: _Optional[float] = ..., blue_running: bool = ..., yellow_running: bool = ..., autoref_running: bool = ..., execution_state: _Optional[_Union[_world_pb2.State, _Mapping]] = ..., execution_game_state: _Optional[_Union[_gamestate_pb2.GameState, _Mapping]] = ..., execution_user_input: _Optional[_Union[_userinput_pb2.UserInput, _Mapping]] = ..., log_id: _Optional[_Union[_logfile_pb2.Uid, _Mapping]] = ..., original_frame_number: _Optional[int] = ..., status_strategy: _Optional[_Union[StatusStrategyWrapper, _Mapping]] = ..., pure_ui_response: _Optional[_Union[UiResponse, _Mapping]] = ..., git_info: _Optional[_Iterable[_Union[GitInfo, _Mapping]]] = ...) -> None: ...

class UiResponse(_message.Message):
    __slots__ = ("enable_logging", "logging_info", "logger_status", "playback_burst_end", "playback_paused", "log_info", "frame_number", "force_ra_horus", "log_open", "export_visionlog_error", "requested_log_uid", "log_offers", "log_uid_parser_error")
    ENABLE_LOGGING_FIELD_NUMBER: _ClassVar[int]
    LOGGING_INFO_FIELD_NUMBER: _ClassVar[int]
    LOGGER_STATUS_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_BURST_END_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_PAUSED_FIELD_NUMBER: _ClassVar[int]
    LOG_INFO_FIELD_NUMBER: _ClassVar[int]
    FRAME_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FORCE_RA_HORUS_FIELD_NUMBER: _ClassVar[int]
    LOG_OPEN_FIELD_NUMBER: _ClassVar[int]
    EXPORT_VISIONLOG_ERROR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_LOG_UID_FIELD_NUMBER: _ClassVar[int]
    LOG_OFFERS_FIELD_NUMBER: _ClassVar[int]
    LOG_UID_PARSER_ERROR_FIELD_NUMBER: _ClassVar[int]
    enable_logging: bool
    logging_info: LoggingInfo
    logger_status: _containers.RepeatedCompositeFieldContainer[Status]
    playback_burst_end: bool
    playback_paused: bool
    log_info: LogPlaybackInfo
    frame_number: int
    force_ra_horus: bool
    log_open: LogfileOpenInfo
    export_visionlog_error: str
    requested_log_uid: str
    log_offers: _logfile_pb2.LogOffer
    log_uid_parser_error: str
    def __init__(self, enable_logging: bool = ..., logging_info: _Optional[_Union[LoggingInfo, _Mapping]] = ..., logger_status: _Optional[_Iterable[_Union[Status, _Mapping]]] = ..., playback_burst_end: bool = ..., playback_paused: bool = ..., log_info: _Optional[_Union[LogPlaybackInfo, _Mapping]] = ..., frame_number: _Optional[int] = ..., force_ra_horus: bool = ..., log_open: _Optional[_Union[LogfileOpenInfo, _Mapping]] = ..., export_visionlog_error: _Optional[str] = ..., requested_log_uid: _Optional[str] = ..., log_offers: _Optional[_Union[_logfile_pb2.LogOffer, _Mapping]] = ..., log_uid_parser_error: _Optional[str] = ...) -> None: ...

class LoggingInfo(_message.Message):
    __slots__ = ("is_logging", "is_replay_logger")
    IS_LOGGING_FIELD_NUMBER: _ClassVar[int]
    IS_REPLAY_LOGGER_FIELD_NUMBER: _ClassVar[int]
    is_logging: bool
    is_replay_logger: bool
    def __init__(self, is_logging: bool = ..., is_replay_logger: bool = ...) -> None: ...

class LogPlaybackInfo(_message.Message):
    __slots__ = ("start_time", "duration", "packet_count")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PACKET_COUNT_FIELD_NUMBER: _ClassVar[int]
    start_time: int
    duration: int
    packet_count: int
    def __init__(self, start_time: _Optional[int] = ..., duration: _Optional[int] = ..., packet_count: _Optional[int] = ...) -> None: ...

class LogfileOpenInfo(_message.Message):
    __slots__ = ("success", "filename")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    success: bool
    filename: str
    def __init__(self, success: bool = ..., filename: _Optional[str] = ...) -> None: ...
