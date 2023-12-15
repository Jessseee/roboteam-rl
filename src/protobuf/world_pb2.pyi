import protobuf.robot_pb2 as _robot_pb2
import protobuf.ssl_mixed_team_pb2 as _ssl_mixed_team_pb2
import protobuf.ssl_wrapper_pb2 as _ssl_wrapper_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTERNAL_SIMULATION: _ClassVar[WorldSource]
    EXTERNAL_SIMULATION: _ClassVar[WorldSource]
    REAL_LIFE: _ClassVar[WorldSource]
INTERNAL_SIMULATION: WorldSource
EXTERNAL_SIMULATION: WorldSource
REAL_LIFE: WorldSource

class Geometry(_message.Message):
    __slots__ = ("line_width", "field_width", "field_height", "boundary_width", "goal_width", "goal_depth", "goal_wall_width", "center_circle_radius", "defense_radius", "defense_stretch", "free_kick_from_defense_dist", "penalty_spot_from_field_line_dist", "penalty_line_from_spot_dist", "goal_height", "defense_width", "defense_height", "type", "division", "ball_model")
    class GeometryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_2014: _ClassVar[Geometry.GeometryType]
        TYPE_2018: _ClassVar[Geometry.GeometryType]
    TYPE_2014: Geometry.GeometryType
    TYPE_2018: Geometry.GeometryType
    class Division(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        A: _ClassVar[Geometry.Division]
        B: _ClassVar[Geometry.Division]
    A: Geometry.Division
    B: Geometry.Division
    LINE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    FIELD_WIDTH_FIELD_NUMBER: _ClassVar[int]
    FIELD_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_WIDTH_FIELD_NUMBER: _ClassVar[int]
    GOAL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    GOAL_DEPTH_FIELD_NUMBER: _ClassVar[int]
    GOAL_WALL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    CENTER_CIRCLE_RADIUS_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_RADIUS_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_STRETCH_FIELD_NUMBER: _ClassVar[int]
    FREE_KICK_FROM_DEFENSE_DIST_FIELD_NUMBER: _ClassVar[int]
    PENALTY_SPOT_FROM_FIELD_LINE_DIST_FIELD_NUMBER: _ClassVar[int]
    PENALTY_LINE_FROM_SPOT_DIST_FIELD_NUMBER: _ClassVar[int]
    GOAL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DIVISION_FIELD_NUMBER: _ClassVar[int]
    BALL_MODEL_FIELD_NUMBER: _ClassVar[int]
    line_width: float
    field_width: float
    field_height: float
    boundary_width: float
    goal_width: float
    goal_depth: float
    goal_wall_width: float
    center_circle_radius: float
    defense_radius: float
    defense_stretch: float
    free_kick_from_defense_dist: float
    penalty_spot_from_field_line_dist: float
    penalty_line_from_spot_dist: float
    goal_height: float
    defense_width: float
    defense_height: float
    type: Geometry.GeometryType
    division: Geometry.Division
    ball_model: BallModel
    def __init__(self, line_width: _Optional[float] = ..., field_width: _Optional[float] = ..., field_height: _Optional[float] = ..., boundary_width: _Optional[float] = ..., goal_width: _Optional[float] = ..., goal_depth: _Optional[float] = ..., goal_wall_width: _Optional[float] = ..., center_circle_radius: _Optional[float] = ..., defense_radius: _Optional[float] = ..., defense_stretch: _Optional[float] = ..., free_kick_from_defense_dist: _Optional[float] = ..., penalty_spot_from_field_line_dist: _Optional[float] = ..., penalty_line_from_spot_dist: _Optional[float] = ..., goal_height: _Optional[float] = ..., defense_width: _Optional[float] = ..., defense_height: _Optional[float] = ..., type: _Optional[_Union[Geometry.GeometryType, str]] = ..., division: _Optional[_Union[Geometry.Division, str]] = ..., ball_model: _Optional[_Union[BallModel, _Mapping]] = ...) -> None: ...

class BallModel(_message.Message):
    __slots__ = ("fast_deceleration", "slow_deceleration", "switch_ratio", "z_damping", "xy_damping")
    FAST_DECELERATION_FIELD_NUMBER: _ClassVar[int]
    SLOW_DECELERATION_FIELD_NUMBER: _ClassVar[int]
    SWITCH_RATIO_FIELD_NUMBER: _ClassVar[int]
    Z_DAMPING_FIELD_NUMBER: _ClassVar[int]
    XY_DAMPING_FIELD_NUMBER: _ClassVar[int]
    fast_deceleration: float
    slow_deceleration: float
    switch_ratio: float
    z_damping: float
    xy_damping: float
    def __init__(self, fast_deceleration: _Optional[float] = ..., slow_deceleration: _Optional[float] = ..., switch_ratio: _Optional[float] = ..., z_damping: _Optional[float] = ..., xy_damping: _Optional[float] = ...) -> None: ...

class DivisionDimensions(_message.Message):
    __slots__ = ("field_width_a", "field_height_a", "field_width_b", "field_height_b")
    FIELD_WIDTH_A_FIELD_NUMBER: _ClassVar[int]
    FIELD_HEIGHT_A_FIELD_NUMBER: _ClassVar[int]
    FIELD_WIDTH_B_FIELD_NUMBER: _ClassVar[int]
    FIELD_HEIGHT_B_FIELD_NUMBER: _ClassVar[int]
    field_width_a: float
    field_height_a: float
    field_width_b: float
    field_height_b: float
    def __init__(self, field_width_a: _Optional[float] = ..., field_height_a: _Optional[float] = ..., field_width_b: _Optional[float] = ..., field_height_b: _Optional[float] = ...) -> None: ...

class BallPosition(_message.Message):
    __slots__ = ("time", "p_x", "p_y", "derived_z", "v_x", "v_y", "system_delay", "time_diff_scaled", "camera_id", "area", "vision_processing_time")
    TIME_FIELD_NUMBER: _ClassVar[int]
    P_X_FIELD_NUMBER: _ClassVar[int]
    P_Y_FIELD_NUMBER: _ClassVar[int]
    DERIVED_Z_FIELD_NUMBER: _ClassVar[int]
    V_X_FIELD_NUMBER: _ClassVar[int]
    V_Y_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_DELAY_FIELD_NUMBER: _ClassVar[int]
    TIME_DIFF_SCALED_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    VISION_PROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
    time: int
    p_x: float
    p_y: float
    derived_z: float
    v_x: float
    v_y: float
    system_delay: float
    time_diff_scaled: float
    camera_id: int
    area: float
    vision_processing_time: int
    def __init__(self, time: _Optional[int] = ..., p_x: _Optional[float] = ..., p_y: _Optional[float] = ..., derived_z: _Optional[float] = ..., v_x: _Optional[float] = ..., v_y: _Optional[float] = ..., system_delay: _Optional[float] = ..., time_diff_scaled: _Optional[float] = ..., camera_id: _Optional[int] = ..., area: _Optional[float] = ..., vision_processing_time: _Optional[int] = ...) -> None: ...

class Ball(_message.Message):
    __slots__ = ("p_x", "p_y", "p_z", "v_x", "v_y", "v_z", "touchdown_x", "touchdown_y", "is_bouncing", "max_speed", "raw")
    P_X_FIELD_NUMBER: _ClassVar[int]
    P_Y_FIELD_NUMBER: _ClassVar[int]
    P_Z_FIELD_NUMBER: _ClassVar[int]
    V_X_FIELD_NUMBER: _ClassVar[int]
    V_Y_FIELD_NUMBER: _ClassVar[int]
    V_Z_FIELD_NUMBER: _ClassVar[int]
    TOUCHDOWN_X_FIELD_NUMBER: _ClassVar[int]
    TOUCHDOWN_Y_FIELD_NUMBER: _ClassVar[int]
    IS_BOUNCING_FIELD_NUMBER: _ClassVar[int]
    MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
    RAW_FIELD_NUMBER: _ClassVar[int]
    p_x: float
    p_y: float
    p_z: float
    v_x: float
    v_y: float
    v_z: float
    touchdown_x: float
    touchdown_y: float
    is_bouncing: bool
    max_speed: float
    raw: _containers.RepeatedCompositeFieldContainer[BallPosition]
    def __init__(self, p_x: _Optional[float] = ..., p_y: _Optional[float] = ..., p_z: _Optional[float] = ..., v_x: _Optional[float] = ..., v_y: _Optional[float] = ..., v_z: _Optional[float] = ..., touchdown_x: _Optional[float] = ..., touchdown_y: _Optional[float] = ..., is_bouncing: bool = ..., max_speed: _Optional[float] = ..., raw: _Optional[_Iterable[_Union[BallPosition, _Mapping]]] = ...) -> None: ...

class RobotPosition(_message.Message):
    __slots__ = ("time", "p_x", "p_y", "phi", "v_x", "v_y", "system_delay", "time_diff_scaled", "omega", "camera_id", "vision_processing_time")
    TIME_FIELD_NUMBER: _ClassVar[int]
    P_X_FIELD_NUMBER: _ClassVar[int]
    P_Y_FIELD_NUMBER: _ClassVar[int]
    PHI_FIELD_NUMBER: _ClassVar[int]
    V_X_FIELD_NUMBER: _ClassVar[int]
    V_Y_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_DELAY_FIELD_NUMBER: _ClassVar[int]
    TIME_DIFF_SCALED_FIELD_NUMBER: _ClassVar[int]
    OMEGA_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    VISION_PROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
    time: int
    p_x: float
    p_y: float
    phi: float
    v_x: float
    v_y: float
    system_delay: float
    time_diff_scaled: float
    omega: float
    camera_id: int
    vision_processing_time: int
    def __init__(self, time: _Optional[int] = ..., p_x: _Optional[float] = ..., p_y: _Optional[float] = ..., phi: _Optional[float] = ..., v_x: _Optional[float] = ..., v_y: _Optional[float] = ..., system_delay: _Optional[float] = ..., time_diff_scaled: _Optional[float] = ..., omega: _Optional[float] = ..., camera_id: _Optional[int] = ..., vision_processing_time: _Optional[int] = ...) -> None: ...

class Robot(_message.Message):
    __slots__ = ("id", "p_x", "p_y", "phi", "v_x", "v_y", "omega", "raw")
    ID_FIELD_NUMBER: _ClassVar[int]
    P_X_FIELD_NUMBER: _ClassVar[int]
    P_Y_FIELD_NUMBER: _ClassVar[int]
    PHI_FIELD_NUMBER: _ClassVar[int]
    V_X_FIELD_NUMBER: _ClassVar[int]
    V_Y_FIELD_NUMBER: _ClassVar[int]
    OMEGA_FIELD_NUMBER: _ClassVar[int]
    RAW_FIELD_NUMBER: _ClassVar[int]
    id: int
    p_x: float
    p_y: float
    phi: float
    v_x: float
    v_y: float
    omega: float
    raw: _containers.RepeatedCompositeFieldContainer[RobotPosition]
    def __init__(self, id: _Optional[int] = ..., p_x: _Optional[float] = ..., p_y: _Optional[float] = ..., phi: _Optional[float] = ..., v_x: _Optional[float] = ..., v_y: _Optional[float] = ..., omega: _Optional[float] = ..., raw: _Optional[_Iterable[_Union[RobotPosition, _Mapping]]] = ...) -> None: ...

class TrackingAOI(_message.Message):
    __slots__ = ("x1", "y1", "x2", "y2")
    X1_FIELD_NUMBER: _ClassVar[int]
    Y1_FIELD_NUMBER: _ClassVar[int]
    X2_FIELD_NUMBER: _ClassVar[int]
    Y2_FIELD_NUMBER: _ClassVar[int]
    x1: float
    y1: float
    x2: float
    y2: float
    def __init__(self, x1: _Optional[float] = ..., y1: _Optional[float] = ..., x2: _Optional[float] = ..., y2: _Optional[float] = ...) -> None: ...

class State(_message.Message):
    __slots__ = ("time", "ball", "yellow", "blue", "radio_response", "is_simulated", "has_vision_data", "mixed_team_info", "tracking_aoi", "simple_tracking_yellow", "simple_tracking_blue", "simple_tracking_ball", "reality", "vision_frames", "vision_frame_times", "system_delay", "world_source")
    TIME_FIELD_NUMBER: _ClassVar[int]
    BALL_FIELD_NUMBER: _ClassVar[int]
    YELLOW_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    RADIO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    IS_SIMULATED_FIELD_NUMBER: _ClassVar[int]
    HAS_VISION_DATA_FIELD_NUMBER: _ClassVar[int]
    MIXED_TEAM_INFO_FIELD_NUMBER: _ClassVar[int]
    TRACKING_AOI_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_TRACKING_YELLOW_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_TRACKING_BLUE_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_TRACKING_BALL_FIELD_NUMBER: _ClassVar[int]
    REALITY_FIELD_NUMBER: _ClassVar[int]
    VISION_FRAMES_FIELD_NUMBER: _ClassVar[int]
    VISION_FRAME_TIMES_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_DELAY_FIELD_NUMBER: _ClassVar[int]
    WORLD_SOURCE_FIELD_NUMBER: _ClassVar[int]
    time: int
    ball: Ball
    yellow: _containers.RepeatedCompositeFieldContainer[Robot]
    blue: _containers.RepeatedCompositeFieldContainer[Robot]
    radio_response: _containers.RepeatedCompositeFieldContainer[_robot_pb2.RadioResponse]
    is_simulated: bool
    has_vision_data: bool
    mixed_team_info: _ssl_mixed_team_pb2.TeamPlan
    tracking_aoi: TrackingAOI
    simple_tracking_yellow: _containers.RepeatedCompositeFieldContainer[Robot]
    simple_tracking_blue: _containers.RepeatedCompositeFieldContainer[Robot]
    simple_tracking_ball: Ball
    reality: _containers.RepeatedCompositeFieldContainer[SimulatorState]
    vision_frames: _containers.RepeatedCompositeFieldContainer[_ssl_wrapper_pb2.SSL_WrapperPacket]
    vision_frame_times: _containers.RepeatedScalarFieldContainer[int]
    system_delay: int
    world_source: WorldSource
    def __init__(self, time: _Optional[int] = ..., ball: _Optional[_Union[Ball, _Mapping]] = ..., yellow: _Optional[_Iterable[_Union[Robot, _Mapping]]] = ..., blue: _Optional[_Iterable[_Union[Robot, _Mapping]]] = ..., radio_response: _Optional[_Iterable[_Union[_robot_pb2.RadioResponse, _Mapping]]] = ..., is_simulated: bool = ..., has_vision_data: bool = ..., mixed_team_info: _Optional[_Union[_ssl_mixed_team_pb2.TeamPlan, _Mapping]] = ..., tracking_aoi: _Optional[_Union[TrackingAOI, _Mapping]] = ..., simple_tracking_yellow: _Optional[_Iterable[_Union[Robot, _Mapping]]] = ..., simple_tracking_blue: _Optional[_Iterable[_Union[Robot, _Mapping]]] = ..., simple_tracking_ball: _Optional[_Union[Ball, _Mapping]] = ..., reality: _Optional[_Iterable[_Union[SimulatorState, _Mapping]]] = ..., vision_frames: _Optional[_Iterable[_Union[_ssl_wrapper_pb2.SSL_WrapperPacket, _Mapping]]] = ..., vision_frame_times: _Optional[_Iterable[int]] = ..., system_delay: _Optional[int] = ..., world_source: _Optional[_Union[WorldSource, str]] = ...) -> None: ...

class SimulatorState(_message.Message):
    __slots__ = ("blue_robots", "yellow_robots", "ball", "time")
    BLUE_ROBOTS_FIELD_NUMBER: _ClassVar[int]
    YELLOW_ROBOTS_FIELD_NUMBER: _ClassVar[int]
    BALL_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    blue_robots: _containers.RepeatedCompositeFieldContainer[SimRobot]
    yellow_robots: _containers.RepeatedCompositeFieldContainer[SimRobot]
    ball: SimBall
    time: int
    def __init__(self, blue_robots: _Optional[_Iterable[_Union[SimRobot, _Mapping]]] = ..., yellow_robots: _Optional[_Iterable[_Union[SimRobot, _Mapping]]] = ..., ball: _Optional[_Union[SimBall, _Mapping]] = ..., time: _Optional[int] = ...) -> None: ...

class SimBall(_message.Message):
    __slots__ = ("p_x", "p_y", "p_z", "v_x", "v_y", "v_z", "angular_x", "angular_y", "angular_z")
    P_X_FIELD_NUMBER: _ClassVar[int]
    P_Y_FIELD_NUMBER: _ClassVar[int]
    P_Z_FIELD_NUMBER: _ClassVar[int]
    V_X_FIELD_NUMBER: _ClassVar[int]
    V_Y_FIELD_NUMBER: _ClassVar[int]
    V_Z_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_X_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_Y_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_Z_FIELD_NUMBER: _ClassVar[int]
    p_x: float
    p_y: float
    p_z: float
    v_x: float
    v_y: float
    v_z: float
    angular_x: float
    angular_y: float
    angular_z: float
    def __init__(self, p_x: _Optional[float] = ..., p_y: _Optional[float] = ..., p_z: _Optional[float] = ..., v_x: _Optional[float] = ..., v_y: _Optional[float] = ..., v_z: _Optional[float] = ..., angular_x: _Optional[float] = ..., angular_y: _Optional[float] = ..., angular_z: _Optional[float] = ...) -> None: ...

class Quaternion(_message.Message):
    __slots__ = ("i", "j", "k", "real")
    I_FIELD_NUMBER: _ClassVar[int]
    J_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    REAL_FIELD_NUMBER: _ClassVar[int]
    i: float
    j: float
    k: float
    real: float
    def __init__(self, i: _Optional[float] = ..., j: _Optional[float] = ..., k: _Optional[float] = ..., real: _Optional[float] = ...) -> None: ...

class SimRobot(_message.Message):
    __slots__ = ("id", "p_x", "p_y", "p_z", "rotation", "v_x", "v_y", "v_z", "r_x", "r_y", "r_z", "touches_ball")
    ID_FIELD_NUMBER: _ClassVar[int]
    P_X_FIELD_NUMBER: _ClassVar[int]
    P_Y_FIELD_NUMBER: _ClassVar[int]
    P_Z_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    V_X_FIELD_NUMBER: _ClassVar[int]
    V_Y_FIELD_NUMBER: _ClassVar[int]
    V_Z_FIELD_NUMBER: _ClassVar[int]
    R_X_FIELD_NUMBER: _ClassVar[int]
    R_Y_FIELD_NUMBER: _ClassVar[int]
    R_Z_FIELD_NUMBER: _ClassVar[int]
    TOUCHES_BALL_FIELD_NUMBER: _ClassVar[int]
    id: int
    p_x: float
    p_y: float
    p_z: float
    rotation: Quaternion
    v_x: float
    v_y: float
    v_z: float
    r_x: float
    r_y: float
    r_z: float
    touches_ball: bool
    def __init__(self, id: _Optional[int] = ..., p_x: _Optional[float] = ..., p_y: _Optional[float] = ..., p_z: _Optional[float] = ..., rotation: _Optional[_Union[Quaternion, _Mapping]] = ..., v_x: _Optional[float] = ..., v_y: _Optional[float] = ..., v_z: _Optional[float] = ..., r_x: _Optional[float] = ..., r_y: _Optional[float] = ..., r_z: _Optional[float] = ..., touches_ball: bool = ...) -> None: ...
