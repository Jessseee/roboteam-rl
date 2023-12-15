from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InputSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    None: _ClassVar[InputSourceType]
    AllSamplers: _ClassVar[InputSourceType]
    StandardSampler: _ClassVar[InputSourceType]
    EndInObstacleSampler: _ClassVar[InputSourceType]
    EscapeObstacleSampler: _ClassVar[InputSourceType]
None: InputSourceType
AllSamplers: InputSourceType
StandardSampler: InputSourceType
EndInObstacleSampler: InputSourceType
EscapeObstacleSampler: InputSourceType

class Vector(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class CircleObstacle(_message.Message):
    __slots__ = ("center",)
    CENTER_FIELD_NUMBER: _ClassVar[int]
    center: Vector
    def __init__(self, center: _Optional[_Union[Vector, _Mapping]] = ...) -> None: ...

class RectObstacle(_message.Message):
    __slots__ = ("bottom_left", "top_right")
    BOTTOM_LEFT_FIELD_NUMBER: _ClassVar[int]
    TOP_RIGHT_FIELD_NUMBER: _ClassVar[int]
    bottom_left: Vector
    top_right: Vector
    def __init__(self, bottom_left: _Optional[_Union[Vector, _Mapping]] = ..., top_right: _Optional[_Union[Vector, _Mapping]] = ...) -> None: ...

class TriangleObstacle(_message.Message):
    __slots__ = ("p1", "p2", "p3")
    P1_FIELD_NUMBER: _ClassVar[int]
    P2_FIELD_NUMBER: _ClassVar[int]
    P3_FIELD_NUMBER: _ClassVar[int]
    p1: Vector
    p2: Vector
    p3: Vector
    def __init__(self, p1: _Optional[_Union[Vector, _Mapping]] = ..., p2: _Optional[_Union[Vector, _Mapping]] = ..., p3: _Optional[_Union[Vector, _Mapping]] = ...) -> None: ...

class LineObstacle(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: Vector
    end: Vector
    def __init__(self, start: _Optional[_Union[Vector, _Mapping]] = ..., end: _Optional[_Union[Vector, _Mapping]] = ...) -> None: ...

class MovingCircleObstacle(_message.Message):
    __slots__ = ("start_pos", "speed", "acc", "start_time", "end_time")
    START_POS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    ACC_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_pos: Vector
    speed: Vector
    acc: Vector
    start_time: float
    end_time: float
    def __init__(self, start_pos: _Optional[_Union[Vector, _Mapping]] = ..., speed: _Optional[_Union[Vector, _Mapping]] = ..., acc: _Optional[_Union[Vector, _Mapping]] = ..., start_time: _Optional[float] = ..., end_time: _Optional[float] = ...) -> None: ...

class MovingLineObstacle(_message.Message):
    __slots__ = ("start_pos1", "speed1", "acc1", "start_pos2", "speed2", "acc2", "start_time", "end_time")
    START_POS1_FIELD_NUMBER: _ClassVar[int]
    SPEED1_FIELD_NUMBER: _ClassVar[int]
    ACC1_FIELD_NUMBER: _ClassVar[int]
    START_POS2_FIELD_NUMBER: _ClassVar[int]
    SPEED2_FIELD_NUMBER: _ClassVar[int]
    ACC2_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_pos1: Vector
    speed1: Vector
    acc1: Vector
    start_pos2: Vector
    speed2: Vector
    acc2: Vector
    start_time: float
    end_time: float
    def __init__(self, start_pos1: _Optional[_Union[Vector, _Mapping]] = ..., speed1: _Optional[_Union[Vector, _Mapping]] = ..., acc1: _Optional[_Union[Vector, _Mapping]] = ..., start_pos2: _Optional[_Union[Vector, _Mapping]] = ..., speed2: _Optional[_Union[Vector, _Mapping]] = ..., acc2: _Optional[_Union[Vector, _Mapping]] = ..., start_time: _Optional[float] = ..., end_time: _Optional[float] = ...) -> None: ...

class TrajectoryPoint(_message.Message):
    __slots__ = ("pos", "speed", "time")
    POS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    pos: Vector
    speed: Vector
    time: float
    def __init__(self, pos: _Optional[_Union[Vector, _Mapping]] = ..., speed: _Optional[_Union[Vector, _Mapping]] = ..., time: _Optional[float] = ...) -> None: ...

class FriendlyRobotObstacle(_message.Message):
    __slots__ = ("robot_trajectory",)
    ROBOT_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    robot_trajectory: _containers.RepeatedCompositeFieldContainer[TrajectoryPoint]
    def __init__(self, robot_trajectory: _Optional[_Iterable[_Union[TrajectoryPoint, _Mapping]]] = ...) -> None: ...

class OpponentRobotObstacle(_message.Message):
    __slots__ = ("start_pos", "speed")
    START_POS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    start_pos: Vector
    speed: Vector
    def __init__(self, start_pos: _Optional[_Union[Vector, _Mapping]] = ..., speed: _Optional[_Union[Vector, _Mapping]] = ...) -> None: ...

class Obstacle(_message.Message):
    __slots__ = ("name", "prio", "radius", "circle", "rectangle", "triangle", "line", "moving_circle", "moving_line", "friendly_robot", "opponent_robot")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIO_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    CIRCLE_FIELD_NUMBER: _ClassVar[int]
    RECTANGLE_FIELD_NUMBER: _ClassVar[int]
    TRIANGLE_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    MOVING_CIRCLE_FIELD_NUMBER: _ClassVar[int]
    MOVING_LINE_FIELD_NUMBER: _ClassVar[int]
    FRIENDLY_ROBOT_FIELD_NUMBER: _ClassVar[int]
    OPPONENT_ROBOT_FIELD_NUMBER: _ClassVar[int]
    name: str
    prio: int
    radius: float
    circle: CircleObstacle
    rectangle: RectObstacle
    triangle: TriangleObstacle
    line: LineObstacle
    moving_circle: MovingCircleObstacle
    moving_line: MovingLineObstacle
    friendly_robot: FriendlyRobotObstacle
    opponent_robot: OpponentRobotObstacle
    def __init__(self, name: _Optional[str] = ..., prio: _Optional[int] = ..., radius: _Optional[float] = ..., circle: _Optional[_Union[CircleObstacle, _Mapping]] = ..., rectangle: _Optional[_Union[RectObstacle, _Mapping]] = ..., triangle: _Optional[_Union[TriangleObstacle, _Mapping]] = ..., line: _Optional[_Union[LineObstacle, _Mapping]] = ..., moving_circle: _Optional[_Union[MovingCircleObstacle, _Mapping]] = ..., moving_line: _Optional[_Union[MovingLineObstacle, _Mapping]] = ..., friendly_robot: _Optional[_Union[FriendlyRobotObstacle, _Mapping]] = ..., opponent_robot: _Optional[_Union[OpponentRobotObstacle, _Mapping]] = ...) -> None: ...

class WorldState(_message.Message):
    __slots__ = ("obstacles", "out_of_field_priority", "boundary", "radius", "robot_id")
    OBSTACLES_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_FIELD_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    ROBOT_ID_FIELD_NUMBER: _ClassVar[int]
    obstacles: _containers.RepeatedCompositeFieldContainer[Obstacle]
    out_of_field_priority: int
    boundary: RectObstacle
    radius: float
    robot_id: int
    def __init__(self, obstacles: _Optional[_Iterable[_Union[Obstacle, _Mapping]]] = ..., out_of_field_priority: _Optional[int] = ..., boundary: _Optional[_Union[RectObstacle, _Mapping]] = ..., radius: _Optional[float] = ..., robot_id: _Optional[int] = ...) -> None: ...

class TrajectoryInput(_message.Message):
    __slots__ = ("v0", "v1", "s0", "s1", "max_speed", "acceleration")
    V0_FIELD_NUMBER: _ClassVar[int]
    V1_FIELD_NUMBER: _ClassVar[int]
    S0_FIELD_NUMBER: _ClassVar[int]
    S1_FIELD_NUMBER: _ClassVar[int]
    MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
    ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    v0: Vector
    v1: Vector
    s0: Vector
    s1: Vector
    max_speed: float
    acceleration: float
    def __init__(self, v0: _Optional[_Union[Vector, _Mapping]] = ..., v1: _Optional[_Union[Vector, _Mapping]] = ..., s0: _Optional[_Union[Vector, _Mapping]] = ..., s1: _Optional[_Union[Vector, _Mapping]] = ..., max_speed: _Optional[float] = ..., acceleration: _Optional[float] = ...) -> None: ...

class PathFindingTask(_message.Message):
    __slots__ = ("state", "input", "type")
    STATE_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    state: WorldState
    input: TrajectoryInput
    type: InputSourceType
    def __init__(self, state: _Optional[_Union[WorldState, _Mapping]] = ..., input: _Optional[_Union[TrajectoryInput, _Mapping]] = ..., type: _Optional[_Union[InputSourceType, str]] = ...) -> None: ...

class StandardSamplerPoint(_message.Message):
    __slots__ = ("time", "angle", "mid_speed_x", "mid_speed_y")
    TIME_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    MID_SPEED_X_FIELD_NUMBER: _ClassVar[int]
    MID_SPEED_Y_FIELD_NUMBER: _ClassVar[int]
    time: float
    angle: float
    mid_speed_x: float
    mid_speed_y: float
    def __init__(self, time: _Optional[float] = ..., angle: _Optional[float] = ..., mid_speed_x: _Optional[float] = ..., mid_speed_y: _Optional[float] = ...) -> None: ...

class StandardSamplerPrecomputationSegment(_message.Message):
    __slots__ = ("precomputed_points", "min_distance", "max_distance")
    PRECOMPUTED_POINTS_FIELD_NUMBER: _ClassVar[int]
    MIN_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    MAX_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    precomputed_points: _containers.RepeatedCompositeFieldContainer[StandardSamplerPoint]
    min_distance: float
    max_distance: float
    def __init__(self, precomputed_points: _Optional[_Iterable[_Union[StandardSamplerPoint, _Mapping]]] = ..., min_distance: _Optional[float] = ..., max_distance: _Optional[float] = ...) -> None: ...

class StandardSamplerPrecomputation(_message.Message):
    __slots__ = ("segments",)
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[StandardSamplerPrecomputationSegment]
    def __init__(self, segments: _Optional[_Iterable[_Union[StandardSamplerPrecomputationSegment, _Mapping]]] = ...) -> None: ...
