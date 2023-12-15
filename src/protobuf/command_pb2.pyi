import protobuf.world_pb2 as _world_pb2
import protobuf.robot_pb2 as _robot_pb2
import protobuf.logfile_pb2 as _logfile_pb2
import protobuf.ssl_geometry_pb2 as _ssl_geometry_pb2
import protobuf.ssl_simulation_control_pb2 as _ssl_simulation_control_pb2
import protobuf.ssl_simulation_custom_erforce_realism_pb2 as _ssl_simulation_custom_erforce_realism_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DebuggerInputTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DITStrategyYellow: _ClassVar[DebuggerInputTarget]
    DITStrategyBlue: _ClassVar[DebuggerInputTarget]
    DITAutoref: _ClassVar[DebuggerInputTarget]

class PauseSimulatorReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Ui: _ClassVar[PauseSimulatorReason]
    WindowFocus: _ClassVar[PauseSimulatorReason]
    DebugBlueStrategy: _ClassVar[PauseSimulatorReason]
    DebugYellowStrategy: _ClassVar[PauseSimulatorReason]
    DebugAutoref: _ClassVar[PauseSimulatorReason]
    Replay: _ClassVar[PauseSimulatorReason]
    Horus: _ClassVar[PauseSimulatorReason]
    Logging: _ClassVar[PauseSimulatorReason]
DITStrategyYellow: DebuggerInputTarget
DITStrategyBlue: DebuggerInputTarget
DITAutoref: DebuggerInputTarget
Ui: PauseSimulatorReason
WindowFocus: PauseSimulatorReason
DebugBlueStrategy: PauseSimulatorReason
DebugYellowStrategy: PauseSimulatorReason
DebugAutoref: PauseSimulatorReason
Replay: PauseSimulatorReason
Horus: PauseSimulatorReason
Logging: PauseSimulatorReason

class RobotMoveCommand(_message.Message):
    __slots__ = ("id", "p_x", "p_y")
    ID_FIELD_NUMBER: _ClassVar[int]
    P_X_FIELD_NUMBER: _ClassVar[int]
    P_Y_FIELD_NUMBER: _ClassVar[int]
    id: int
    p_x: float
    p_y: float
    def __init__(self, id: _Optional[int] = ..., p_x: _Optional[float] = ..., p_y: _Optional[float] = ...) -> None: ...

class SimulatorSetup(_message.Message):
    __slots__ = ("geometry", "camera_setup")
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    CAMERA_SETUP_FIELD_NUMBER: _ClassVar[int]
    geometry: _world_pb2.Geometry
    camera_setup: _containers.RepeatedCompositeFieldContainer[_ssl_geometry_pb2.SSL_GeometryCameraCalibration]
    def __init__(self, geometry: _Optional[_Union[_world_pb2.Geometry, _Mapping]] = ..., camera_setup: _Optional[_Iterable[_Union[_ssl_geometry_pb2.SSL_GeometryCameraCalibration, _Mapping]]] = ...) -> None: ...

class SimulatorWorstCaseVision(_message.Message):
    __slots__ = ("min_robot_detection_time", "min_ball_detection_time")
    MIN_ROBOT_DETECTION_TIME_FIELD_NUMBER: _ClassVar[int]
    MIN_BALL_DETECTION_TIME_FIELD_NUMBER: _ClassVar[int]
    min_robot_detection_time: float
    min_ball_detection_time: float
    def __init__(self, min_robot_detection_time: _Optional[float] = ..., min_ball_detection_time: _Optional[float] = ...) -> None: ...

class CommandSimulator(_message.Message):
    __slots__ = ("enable", "simulator_setup", "vision_worst_case", "realism_config", "set_simulator_state", "ssl_control")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    SIMULATOR_SETUP_FIELD_NUMBER: _ClassVar[int]
    VISION_WORST_CASE_FIELD_NUMBER: _ClassVar[int]
    REALISM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SET_SIMULATOR_STATE_FIELD_NUMBER: _ClassVar[int]
    SSL_CONTROL_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    simulator_setup: SimulatorSetup
    vision_worst_case: SimulatorWorstCaseVision
    realism_config: _ssl_simulation_custom_erforce_realism_pb2.RealismConfigErForce
    set_simulator_state: _world_pb2.SimulatorState
    ssl_control: _ssl_simulation_control_pb2.SimulatorControl
    def __init__(self, enable: bool = ..., simulator_setup: _Optional[_Union[SimulatorSetup, _Mapping]] = ..., vision_worst_case: _Optional[_Union[SimulatorWorstCaseVision, _Mapping]] = ..., realism_config: _Optional[_Union[_ssl_simulation_custom_erforce_realism_pb2.RealismConfigErForce, _Mapping]] = ..., set_simulator_state: _Optional[_Union[_world_pb2.SimulatorState, _Mapping]] = ..., ssl_control: _Optional[_Union[_ssl_simulation_control_pb2.SimulatorControl, _Mapping]] = ...) -> None: ...

class CommandReferee(_message.Message):
    __slots__ = ("active", "command", "use_internal_autoref", "use_automatic_robot_exchange")
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    USE_INTERNAL_AUTOREF_FIELD_NUMBER: _ClassVar[int]
    USE_AUTOMATIC_ROBOT_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    active: bool
    command: bytes
    use_internal_autoref: bool
    use_automatic_robot_exchange: bool
    def __init__(self, active: bool = ..., command: _Optional[bytes] = ..., use_internal_autoref: bool = ..., use_automatic_robot_exchange: bool = ...) -> None: ...

class CommandStrategyLoad(_message.Message):
    __slots__ = ("filename", "entry_point")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    ENTRY_POINT_FIELD_NUMBER: _ClassVar[int]
    filename: str
    entry_point: str
    def __init__(self, filename: _Optional[str] = ..., entry_point: _Optional[str] = ...) -> None: ...

class CommandStrategyClose(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommandStrategyTriggerDebugger(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommandStrategy(_message.Message):
    __slots__ = ("load", "close", "reload", "auto_reload", "enable_debug", "debug", "performance_mode", "start_profiling", "finish_and_save_profile", "tournament_mode")
    LOAD_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    RELOAD_FIELD_NUMBER: _ClassVar[int]
    AUTO_RELOAD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DEBUG_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_MODE_FIELD_NUMBER: _ClassVar[int]
    START_PROFILING_FIELD_NUMBER: _ClassVar[int]
    FINISH_AND_SAVE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    load: CommandStrategyLoad
    close: CommandStrategyClose
    reload: bool
    auto_reload: bool
    enable_debug: bool
    debug: CommandStrategyTriggerDebugger
    performance_mode: bool
    start_profiling: bool
    finish_and_save_profile: str
    tournament_mode: bool
    def __init__(self, load: _Optional[_Union[CommandStrategyLoad, _Mapping]] = ..., close: _Optional[_Union[CommandStrategyClose, _Mapping]] = ..., reload: bool = ..., auto_reload: bool = ..., enable_debug: bool = ..., debug: _Optional[_Union[CommandStrategyTriggerDebugger, _Mapping]] = ..., performance_mode: bool = ..., start_profiling: bool = ..., finish_and_save_profile: _Optional[str] = ..., tournament_mode: bool = ...) -> None: ...

class CommandControl(_message.Message):
    __slots__ = ("commands",)
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[_robot_pb2.RadioCommand]
    def __init__(self, commands: _Optional[_Iterable[_Union[_robot_pb2.RadioCommand, _Mapping]]] = ...) -> None: ...

class TransceiverConfiguration(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: int
    def __init__(self, channel: _Optional[int] = ...) -> None: ...

class HostAddress(_message.Message):
    __slots__ = ("host", "port")
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    def __init__(self, host: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class SimulatorNetworking(_message.Message):
    __slots__ = ("control_simulator", "control_blue", "control_yellow", "port_blue", "port_yellow")
    CONTROL_SIMULATOR_FIELD_NUMBER: _ClassVar[int]
    CONTROL_BLUE_FIELD_NUMBER: _ClassVar[int]
    CONTROL_YELLOW_FIELD_NUMBER: _ClassVar[int]
    PORT_BLUE_FIELD_NUMBER: _ClassVar[int]
    PORT_YELLOW_FIELD_NUMBER: _ClassVar[int]
    control_simulator: bool
    control_blue: bool
    control_yellow: bool
    port_blue: int
    port_yellow: int
    def __init__(self, control_simulator: bool = ..., control_blue: bool = ..., control_yellow: bool = ..., port_blue: _Optional[int] = ..., port_yellow: _Optional[int] = ...) -> None: ...

class CommandTransceiver(_message.Message):
    __slots__ = ("enable", "charge", "configuration", "network_configuration", "use_network", "simulator_configuration")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    USE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    SIMULATOR_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    charge: bool
    configuration: TransceiverConfiguration
    network_configuration: HostAddress
    use_network: bool
    simulator_configuration: SimulatorNetworking
    def __init__(self, enable: bool = ..., charge: bool = ..., configuration: _Optional[_Union[TransceiverConfiguration, _Mapping]] = ..., network_configuration: _Optional[_Union[HostAddress, _Mapping]] = ..., use_network: bool = ..., simulator_configuration: _Optional[_Union[SimulatorNetworking, _Mapping]] = ...) -> None: ...

class VirtualFieldTransform(_message.Message):
    __slots__ = ("a11", "a12", "a21", "a22", "offsetX", "offsetY")
    A11_FIELD_NUMBER: _ClassVar[int]
    A12_FIELD_NUMBER: _ClassVar[int]
    A21_FIELD_NUMBER: _ClassVar[int]
    A22_FIELD_NUMBER: _ClassVar[int]
    OFFSETX_FIELD_NUMBER: _ClassVar[int]
    OFFSETY_FIELD_NUMBER: _ClassVar[int]
    a11: float
    a12: float
    a21: float
    a22: float
    offsetX: float
    offsetY: float
    def __init__(self, a11: _Optional[float] = ..., a12: _Optional[float] = ..., a21: _Optional[float] = ..., a22: _Optional[float] = ..., offsetX: _Optional[float] = ..., offsetY: _Optional[float] = ...) -> None: ...

class CommandTracking(_message.Message):
    __slots__ = ("aoi_enabled", "aoi", "system_delay", "reset", "enable_virtual_field", "field_transform", "virtual_geometry", "tracking_replay_enabled", "ball_model")
    AOI_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AOI_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_DELAY_FIELD_NUMBER: _ClassVar[int]
    RESET_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VIRTUAL_FIELD_FIELD_NUMBER: _ClassVar[int]
    FIELD_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    TRACKING_REPLAY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BALL_MODEL_FIELD_NUMBER: _ClassVar[int]
    aoi_enabled: bool
    aoi: _world_pb2.TrackingAOI
    system_delay: int
    reset: bool
    enable_virtual_field: bool
    field_transform: VirtualFieldTransform
    virtual_geometry: _world_pb2.Geometry
    tracking_replay_enabled: bool
    ball_model: _world_pb2.BallModel
    def __init__(self, aoi_enabled: bool = ..., aoi: _Optional[_Union[_world_pb2.TrackingAOI, _Mapping]] = ..., system_delay: _Optional[int] = ..., reset: bool = ..., enable_virtual_field: bool = ..., field_transform: _Optional[_Union[VirtualFieldTransform, _Mapping]] = ..., virtual_geometry: _Optional[_Union[_world_pb2.Geometry, _Mapping]] = ..., tracking_replay_enabled: bool = ..., ball_model: _Optional[_Union[_world_pb2.BallModel, _Mapping]] = ...) -> None: ...

class CommandStrategyChangeOption(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: bool
    def __init__(self, name: _Optional[str] = ..., value: bool = ...) -> None: ...

class CommandAmun(_message.Message):
    __slots__ = ("vision_port", "referee_port", "tracker_port", "change_option")
    VISION_PORT_FIELD_NUMBER: _ClassVar[int]
    REFEREE_PORT_FIELD_NUMBER: _ClassVar[int]
    TRACKER_PORT_FIELD_NUMBER: _ClassVar[int]
    CHANGE_OPTION_FIELD_NUMBER: _ClassVar[int]
    vision_port: int
    referee_port: int
    tracker_port: int
    change_option: CommandStrategyChangeOption
    def __init__(self, vision_port: _Optional[int] = ..., referee_port: _Optional[int] = ..., tracker_port: _Optional[int] = ..., change_option: _Optional[_Union[CommandStrategyChangeOption, _Mapping]] = ...) -> None: ...

class CommandDebuggerInputDisable(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommandDebuggerInputLine(_message.Message):
    __slots__ = ("line",)
    LINE_FIELD_NUMBER: _ClassVar[int]
    line: str
    def __init__(self, line: _Optional[str] = ...) -> None: ...

class CommandDebuggerInput(_message.Message):
    __slots__ = ("strategy_type", "disable", "queue_line")
    STRATEGY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FIELD_NUMBER: _ClassVar[int]
    QUEUE_LINE_FIELD_NUMBER: _ClassVar[int]
    strategy_type: DebuggerInputTarget
    disable: CommandDebuggerInputDisable
    queue_line: CommandDebuggerInputLine
    def __init__(self, strategy_type: _Optional[_Union[DebuggerInputTarget, str]] = ..., disable: _Optional[_Union[CommandDebuggerInputDisable, _Mapping]] = ..., queue_line: _Optional[_Union[CommandDebuggerInputLine, _Mapping]] = ...) -> None: ...

class PauseSimulatorCommand(_message.Message):
    __slots__ = ("reason", "pause", "toggle")
    REASON_FIELD_NUMBER: _ClassVar[int]
    PAUSE_FIELD_NUMBER: _ClassVar[int]
    TOGGLE_FIELD_NUMBER: _ClassVar[int]
    reason: PauseSimulatorReason
    pause: bool
    toggle: bool
    def __init__(self, reason: _Optional[_Union[PauseSimulatorReason, str]] = ..., pause: bool = ..., toggle: bool = ...) -> None: ...

class CommandReplay(_message.Message):
    __slots__ = ("enable", "enable_blue_strategy", "blue_strategy", "enable_yellow_strategy", "yellow_strategy")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BLUE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    BLUE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_YELLOW_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    YELLOW_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    enable_blue_strategy: bool
    blue_strategy: CommandStrategy
    enable_yellow_strategy: bool
    yellow_strategy: CommandStrategy
    def __init__(self, enable: bool = ..., enable_blue_strategy: bool = ..., blue_strategy: _Optional[_Union[CommandStrategy, _Mapping]] = ..., enable_yellow_strategy: bool = ..., yellow_strategy: _Optional[_Union[CommandStrategy, _Mapping]] = ...) -> None: ...

class Flag(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommandPlayback(_message.Message):
    __slots__ = ("seek_time", "seek_packet", "seek_time_backwards", "playback_speed", "toggle_paused", "run_playback", "log_path", "instant_replay", "export_vision_log", "get_uid", "find_logfile", "playback_limit")
    SEEK_TIME_FIELD_NUMBER: _ClassVar[int]
    SEEK_PACKET_FIELD_NUMBER: _ClassVar[int]
    SEEK_TIME_BACKWARDS_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_SPEED_FIELD_NUMBER: _ClassVar[int]
    TOGGLE_PAUSED_FIELD_NUMBER: _ClassVar[int]
    RUN_PLAYBACK_FIELD_NUMBER: _ClassVar[int]
    LOG_PATH_FIELD_NUMBER: _ClassVar[int]
    INSTANT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    EXPORT_VISION_LOG_FIELD_NUMBER: _ClassVar[int]
    GET_UID_FIELD_NUMBER: _ClassVar[int]
    FIND_LOGFILE_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_LIMIT_FIELD_NUMBER: _ClassVar[int]
    seek_time: int
    seek_packet: int
    seek_time_backwards: int
    playback_speed: int
    toggle_paused: Flag
    run_playback: bool
    log_path: _logfile_pb2.LogRequest
    instant_replay: Flag
    export_vision_log: str
    get_uid: Flag
    find_logfile: str
    playback_limit: int
    def __init__(self, seek_time: _Optional[int] = ..., seek_packet: _Optional[int] = ..., seek_time_backwards: _Optional[int] = ..., playback_speed: _Optional[int] = ..., toggle_paused: _Optional[_Union[Flag, _Mapping]] = ..., run_playback: bool = ..., log_path: _Optional[_Union[_logfile_pb2.LogRequest, _Mapping]] = ..., instant_replay: _Optional[_Union[Flag, _Mapping]] = ..., export_vision_log: _Optional[str] = ..., get_uid: _Optional[_Union[Flag, _Mapping]] = ..., find_logfile: _Optional[str] = ..., playback_limit: _Optional[int] = ...) -> None: ...

class CommandRecord(_message.Message):
    __slots__ = ("use_logfile_location", "save_backlog", "run_logging", "for_replay", "request_backlog", "overwrite_record_filename")
    USE_LOGFILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SAVE_BACKLOG_FIELD_NUMBER: _ClassVar[int]
    RUN_LOGGING_FIELD_NUMBER: _ClassVar[int]
    FOR_REPLAY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BACKLOG_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_RECORD_FILENAME_FIELD_NUMBER: _ClassVar[int]
    use_logfile_location: bool
    save_backlog: Flag
    run_logging: bool
    for_replay: bool
    request_backlog: int
    overwrite_record_filename: str
    def __init__(self, use_logfile_location: bool = ..., save_backlog: _Optional[_Union[Flag, _Mapping]] = ..., run_logging: bool = ..., for_replay: bool = ..., request_backlog: _Optional[int] = ..., overwrite_record_filename: _Optional[str] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ("simulator", "referee", "set_team_blue", "set_team_yellow", "strategy_blue", "strategy_yellow", "strategy_autoref", "control", "transceiver", "tracking", "amun", "mixed_team_destination", "robot_move_blue", "robot_move_yellow", "debugger_input", "pause_simulator", "replay", "playback", "record")
    SIMULATOR_FIELD_NUMBER: _ClassVar[int]
    REFEREE_FIELD_NUMBER: _ClassVar[int]
    SET_TEAM_BLUE_FIELD_NUMBER: _ClassVar[int]
    SET_TEAM_YELLOW_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_BLUE_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_YELLOW_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_AUTOREF_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    TRANSCEIVER_FIELD_NUMBER: _ClassVar[int]
    TRACKING_FIELD_NUMBER: _ClassVar[int]
    AMUN_FIELD_NUMBER: _ClassVar[int]
    MIXED_TEAM_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ROBOT_MOVE_BLUE_FIELD_NUMBER: _ClassVar[int]
    ROBOT_MOVE_YELLOW_FIELD_NUMBER: _ClassVar[int]
    DEBUGGER_INPUT_FIELD_NUMBER: _ClassVar[int]
    PAUSE_SIMULATOR_FIELD_NUMBER: _ClassVar[int]
    REPLAY_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    simulator: CommandSimulator
    referee: CommandReferee
    set_team_blue: _robot_pb2.Team
    set_team_yellow: _robot_pb2.Team
    strategy_blue: CommandStrategy
    strategy_yellow: CommandStrategy
    strategy_autoref: CommandStrategy
    control: CommandControl
    transceiver: CommandTransceiver
    tracking: CommandTracking
    amun: CommandAmun
    mixed_team_destination: HostAddress
    robot_move_blue: _containers.RepeatedCompositeFieldContainer[RobotMoveCommand]
    robot_move_yellow: _containers.RepeatedCompositeFieldContainer[RobotMoveCommand]
    debugger_input: CommandDebuggerInput
    pause_simulator: PauseSimulatorCommand
    replay: CommandReplay
    playback: CommandPlayback
    record: CommandRecord
    def __init__(self, simulator: _Optional[_Union[CommandSimulator, _Mapping]] = ..., referee: _Optional[_Union[CommandReferee, _Mapping]] = ..., set_team_blue: _Optional[_Union[_robot_pb2.Team, _Mapping]] = ..., set_team_yellow: _Optional[_Union[_robot_pb2.Team, _Mapping]] = ..., strategy_blue: _Optional[_Union[CommandStrategy, _Mapping]] = ..., strategy_yellow: _Optional[_Union[CommandStrategy, _Mapping]] = ..., strategy_autoref: _Optional[_Union[CommandStrategy, _Mapping]] = ..., control: _Optional[_Union[CommandControl, _Mapping]] = ..., transceiver: _Optional[_Union[CommandTransceiver, _Mapping]] = ..., tracking: _Optional[_Union[CommandTracking, _Mapping]] = ..., amun: _Optional[_Union[CommandAmun, _Mapping]] = ..., mixed_team_destination: _Optional[_Union[HostAddress, _Mapping]] = ..., robot_move_blue: _Optional[_Iterable[_Union[RobotMoveCommand, _Mapping]]] = ..., robot_move_yellow: _Optional[_Iterable[_Union[RobotMoveCommand, _Mapping]]] = ..., debugger_input: _Optional[_Union[CommandDebuggerInput, _Mapping]] = ..., pause_simulator: _Optional[_Union[PauseSimulatorCommand, _Mapping]] = ..., replay: _Optional[_Union[CommandReplay, _Mapping]] = ..., playback: _Optional[_Union[CommandPlayback, _Mapping]] = ..., record: _Optional[_Union[CommandRecord, _Mapping]] = ...) -> None: ...
