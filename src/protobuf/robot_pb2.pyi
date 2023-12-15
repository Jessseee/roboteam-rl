from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LimitParameters(_message.Message):
    __slots__ = ("a_speedup_f_max", "a_speedup_s_max", "a_speedup_phi_max", "a_brake_f_max", "a_brake_s_max", "a_brake_phi_max")
    A_SPEEDUP_F_MAX_FIELD_NUMBER: _ClassVar[int]
    A_SPEEDUP_S_MAX_FIELD_NUMBER: _ClassVar[int]
    A_SPEEDUP_PHI_MAX_FIELD_NUMBER: _ClassVar[int]
    A_BRAKE_F_MAX_FIELD_NUMBER: _ClassVar[int]
    A_BRAKE_S_MAX_FIELD_NUMBER: _ClassVar[int]
    A_BRAKE_PHI_MAX_FIELD_NUMBER: _ClassVar[int]
    a_speedup_f_max: float
    a_speedup_s_max: float
    a_speedup_phi_max: float
    a_brake_f_max: float
    a_brake_s_max: float
    a_brake_phi_max: float
    def __init__(self, a_speedup_f_max: _Optional[float] = ..., a_speedup_s_max: _Optional[float] = ..., a_speedup_phi_max: _Optional[float] = ..., a_brake_f_max: _Optional[float] = ..., a_brake_s_max: _Optional[float] = ..., a_brake_phi_max: _Optional[float] = ...) -> None: ...

class SimulationLimits(_message.Message):
    __slots__ = ("a_speedup_wheel_max", "a_brake_wheel_max")
    A_SPEEDUP_WHEEL_MAX_FIELD_NUMBER: _ClassVar[int]
    A_BRAKE_WHEEL_MAX_FIELD_NUMBER: _ClassVar[int]
    a_speedup_wheel_max: float
    a_brake_wheel_max: float
    def __init__(self, a_speedup_wheel_max: _Optional[float] = ..., a_brake_wheel_max: _Optional[float] = ...) -> None: ...

class Specs(_message.Message):
    __slots__ = ("generation", "year", "id", "type", "radius", "height", "mass", "angle", "v_max", "omega_max", "shot_linear_max", "shot_chip_max", "dribbler_width", "acceleration", "strategy", "ir_param", "shoot_radius", "dribbler_height", "simulation_limits")
    class GenerationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Regular: _ClassVar[Specs.GenerationType]
        Ally: _ClassVar[Specs.GenerationType]
    Regular: Specs.GenerationType
    Ally: Specs.GenerationType
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MASS_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    V_MAX_FIELD_NUMBER: _ClassVar[int]
    OMEGA_MAX_FIELD_NUMBER: _ClassVar[int]
    SHOT_LINEAR_MAX_FIELD_NUMBER: _ClassVar[int]
    SHOT_CHIP_MAX_FIELD_NUMBER: _ClassVar[int]
    DRIBBLER_WIDTH_FIELD_NUMBER: _ClassVar[int]
    ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    IR_PARAM_FIELD_NUMBER: _ClassVar[int]
    SHOOT_RADIUS_FIELD_NUMBER: _ClassVar[int]
    DRIBBLER_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_LIMITS_FIELD_NUMBER: _ClassVar[int]
    generation: int
    year: int
    id: int
    type: Specs.GenerationType
    radius: float
    height: float
    mass: float
    angle: float
    v_max: float
    omega_max: float
    shot_linear_max: float
    shot_chip_max: float
    dribbler_width: float
    acceleration: LimitParameters
    strategy: LimitParameters
    ir_param: float
    shoot_radius: float
    dribbler_height: float
    simulation_limits: SimulationLimits
    def __init__(self, generation: _Optional[int] = ..., year: _Optional[int] = ..., id: _Optional[int] = ..., type: _Optional[_Union[Specs.GenerationType, str]] = ..., radius: _Optional[float] = ..., height: _Optional[float] = ..., mass: _Optional[float] = ..., angle: _Optional[float] = ..., v_max: _Optional[float] = ..., omega_max: _Optional[float] = ..., shot_linear_max: _Optional[float] = ..., shot_chip_max: _Optional[float] = ..., dribbler_width: _Optional[float] = ..., acceleration: _Optional[_Union[LimitParameters, _Mapping]] = ..., strategy: _Optional[_Union[LimitParameters, _Mapping]] = ..., ir_param: _Optional[float] = ..., shoot_radius: _Optional[float] = ..., dribbler_height: _Optional[float] = ..., simulation_limits: _Optional[_Union[SimulationLimits, _Mapping]] = ...) -> None: ...

class Generation(_message.Message):
    __slots__ = ("default", "robot")
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ROBOT_FIELD_NUMBER: _ClassVar[int]
    default: Specs
    robot: _containers.RepeatedCompositeFieldContainer[Specs]
    def __init__(self, default: _Optional[_Union[Specs, _Mapping]] = ..., robot: _Optional[_Iterable[_Union[Specs, _Mapping]]] = ...) -> None: ...

class Team(_message.Message):
    __slots__ = ("robot",)
    ROBOT_FIELD_NUMBER: _ClassVar[int]
    robot: _containers.RepeatedCompositeFieldContainer[Specs]
    def __init__(self, robot: _Optional[_Iterable[_Union[Specs, _Mapping]]] = ...) -> None: ...

class Polynomial(_message.Message):
    __slots__ = ("a0", "a1", "a2", "a3")
    A0_FIELD_NUMBER: _ClassVar[int]
    A1_FIELD_NUMBER: _ClassVar[int]
    A2_FIELD_NUMBER: _ClassVar[int]
    A3_FIELD_NUMBER: _ClassVar[int]
    a0: float
    a1: float
    a2: float
    a3: float
    def __init__(self, a0: _Optional[float] = ..., a1: _Optional[float] = ..., a2: _Optional[float] = ..., a3: _Optional[float] = ...) -> None: ...

class Spline(_message.Message):
    __slots__ = ("t_start", "t_end", "x", "y", "phi")
    T_START_FIELD_NUMBER: _ClassVar[int]
    T_END_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    PHI_FIELD_NUMBER: _ClassVar[int]
    t_start: float
    t_end: float
    x: Polynomial
    y: Polynomial
    phi: Polynomial
    def __init__(self, t_start: _Optional[float] = ..., t_end: _Optional[float] = ..., x: _Optional[_Union[Polynomial, _Mapping]] = ..., y: _Optional[_Union[Polynomial, _Mapping]] = ..., phi: _Optional[_Union[Polynomial, _Mapping]] = ...) -> None: ...

class ControllerInput(_message.Message):
    __slots__ = ("spline",)
    SPLINE_FIELD_NUMBER: _ClassVar[int]
    spline: _containers.RepeatedCompositeFieldContainer[Spline]
    def __init__(self, spline: _Optional[_Iterable[_Union[Spline, _Mapping]]] = ...) -> None: ...

class SpeedVector(_message.Message):
    __slots__ = ("v_s", "v_f", "omega")
    V_S_FIELD_NUMBER: _ClassVar[int]
    V_F_FIELD_NUMBER: _ClassVar[int]
    OMEGA_FIELD_NUMBER: _ClassVar[int]
    v_s: float
    v_f: float
    omega: float
    def __init__(self, v_s: _Optional[float] = ..., v_f: _Optional[float] = ..., omega: _Optional[float] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ("controller", "v_f", "v_s", "omega", "kick_style", "kick_power", "dribbler", "local", "standby", "strategy_controlled", "force_kick", "network_controlled", "eject_sdcard", "cur_v_f", "cur_v_s", "cur_omega", "output0", "output1", "output2")
    class KickStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Linear: _ClassVar[Command.KickStyle]
        Chip: _ClassVar[Command.KickStyle]
    Linear: Command.KickStyle
    Chip: Command.KickStyle
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    V_F_FIELD_NUMBER: _ClassVar[int]
    V_S_FIELD_NUMBER: _ClassVar[int]
    OMEGA_FIELD_NUMBER: _ClassVar[int]
    KICK_STYLE_FIELD_NUMBER: _ClassVar[int]
    KICK_POWER_FIELD_NUMBER: _ClassVar[int]
    DRIBBLER_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    STANDBY_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_CONTROLLED_FIELD_NUMBER: _ClassVar[int]
    FORCE_KICK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONTROLLED_FIELD_NUMBER: _ClassVar[int]
    EJECT_SDCARD_FIELD_NUMBER: _ClassVar[int]
    CUR_V_F_FIELD_NUMBER: _ClassVar[int]
    CUR_V_S_FIELD_NUMBER: _ClassVar[int]
    CUR_OMEGA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT0_FIELD_NUMBER: _ClassVar[int]
    OUTPUT1_FIELD_NUMBER: _ClassVar[int]
    OUTPUT2_FIELD_NUMBER: _ClassVar[int]
    controller: ControllerInput
    v_f: float
    v_s: float
    omega: float
    kick_style: Command.KickStyle
    kick_power: float
    dribbler: float
    local: bool
    standby: bool
    strategy_controlled: bool
    force_kick: bool
    network_controlled: bool
    eject_sdcard: bool
    cur_v_f: float
    cur_v_s: float
    cur_omega: float
    output0: SpeedVector
    output1: SpeedVector
    output2: SpeedVector
    def __init__(self, controller: _Optional[_Union[ControllerInput, _Mapping]] = ..., v_f: _Optional[float] = ..., v_s: _Optional[float] = ..., omega: _Optional[float] = ..., kick_style: _Optional[_Union[Command.KickStyle, str]] = ..., kick_power: _Optional[float] = ..., dribbler: _Optional[float] = ..., local: bool = ..., standby: bool = ..., strategy_controlled: bool = ..., force_kick: bool = ..., network_controlled: bool = ..., eject_sdcard: bool = ..., cur_v_f: _Optional[float] = ..., cur_v_s: _Optional[float] = ..., cur_omega: _Optional[float] = ..., output0: _Optional[_Union[SpeedVector, _Mapping]] = ..., output1: _Optional[_Union[SpeedVector, _Mapping]] = ..., output2: _Optional[_Union[SpeedVector, _Mapping]] = ...) -> None: ...

class RadioCommand(_message.Message):
    __slots__ = ("generation", "id", "is_blue", "command", "command_time")
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_BLUE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TIME_FIELD_NUMBER: _ClassVar[int]
    generation: int
    id: int
    is_blue: bool
    command: Command
    command_time: int
    def __init__(self, generation: _Optional[int] = ..., id: _Optional[int] = ..., is_blue: bool = ..., command: _Optional[_Union[Command, _Mapping]] = ..., command_time: _Optional[int] = ...) -> None: ...

class SpeedStatus(_message.Message):
    __slots__ = ("v_f", "v_s", "omega")
    V_F_FIELD_NUMBER: _ClassVar[int]
    V_S_FIELD_NUMBER: _ClassVar[int]
    OMEGA_FIELD_NUMBER: _ClassVar[int]
    v_f: float
    v_s: float
    omega: float
    def __init__(self, v_f: _Optional[float] = ..., v_s: _Optional[float] = ..., omega: _Optional[float] = ...) -> None: ...

class ExtendedError(_message.Message):
    __slots__ = ("motor_1_error", "motor_2_error", "motor_3_error", "motor_4_error", "dribbler_error", "kicker_error", "kicker_break_beam_error", "motor_encoder_error", "main_sensor_error", "temperature")
    MOTOR_1_ERROR_FIELD_NUMBER: _ClassVar[int]
    MOTOR_2_ERROR_FIELD_NUMBER: _ClassVar[int]
    MOTOR_3_ERROR_FIELD_NUMBER: _ClassVar[int]
    MOTOR_4_ERROR_FIELD_NUMBER: _ClassVar[int]
    DRIBBLER_ERROR_FIELD_NUMBER: _ClassVar[int]
    KICKER_ERROR_FIELD_NUMBER: _ClassVar[int]
    KICKER_BREAK_BEAM_ERROR_FIELD_NUMBER: _ClassVar[int]
    MOTOR_ENCODER_ERROR_FIELD_NUMBER: _ClassVar[int]
    MAIN_SENSOR_ERROR_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    motor_1_error: bool
    motor_2_error: bool
    motor_3_error: bool
    motor_4_error: bool
    dribbler_error: bool
    kicker_error: bool
    kicker_break_beam_error: bool
    motor_encoder_error: bool
    main_sensor_error: bool
    temperature: int
    def __init__(self, motor_1_error: bool = ..., motor_2_error: bool = ..., motor_3_error: bool = ..., motor_4_error: bool = ..., dribbler_error: bool = ..., kicker_error: bool = ..., kicker_break_beam_error: bool = ..., motor_encoder_error: bool = ..., main_sensor_error: bool = ..., temperature: _Optional[int] = ...) -> None: ...

class RadioResponse(_message.Message):
    __slots__ = ("time", "generation", "id", "battery", "packet_loss_rx", "packet_loss_tx", "estimated_speed", "ball_detected", "cap_charged", "error_present", "radio_rtt", "extended_error", "is_blue")
    TIME_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    PACKET_LOSS_RX_FIELD_NUMBER: _ClassVar[int]
    PACKET_LOSS_TX_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_SPEED_FIELD_NUMBER: _ClassVar[int]
    BALL_DETECTED_FIELD_NUMBER: _ClassVar[int]
    CAP_CHARGED_FIELD_NUMBER: _ClassVar[int]
    ERROR_PRESENT_FIELD_NUMBER: _ClassVar[int]
    RADIO_RTT_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_BLUE_FIELD_NUMBER: _ClassVar[int]
    time: int
    generation: int
    id: int
    battery: float
    packet_loss_rx: float
    packet_loss_tx: float
    estimated_speed: SpeedStatus
    ball_detected: bool
    cap_charged: bool
    error_present: bool
    radio_rtt: float
    extended_error: ExtendedError
    is_blue: bool
    def __init__(self, time: _Optional[int] = ..., generation: _Optional[int] = ..., id: _Optional[int] = ..., battery: _Optional[float] = ..., packet_loss_rx: _Optional[float] = ..., packet_loss_tx: _Optional[float] = ..., estimated_speed: _Optional[_Union[SpeedStatus, _Mapping]] = ..., ball_detected: bool = ..., cap_charged: bool = ..., error_present: bool = ..., radio_rtt: _Optional[float] = ..., extended_error: _Optional[_Union[ExtendedError, _Mapping]] = ..., is_blue: bool = ...) -> None: ...
