from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamPlan(_message.Message):
    __slots__ = ("plans",)
    PLANS_FIELD_NUMBER: _ClassVar[int]
    plans: _containers.RepeatedCompositeFieldContainer[RobotPlan]
    def __init__(self, plans: _Optional[_Iterable[_Union[RobotPlan, _Mapping]]] = ...) -> None: ...

class RobotPlan(_message.Message):
    __slots__ = ("robot_id", "role", "nav_target", "shot_target")
    class RobotRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Default: _ClassVar[RobotPlan.RobotRole]
        Goalie: _ClassVar[RobotPlan.RobotRole]
        Defense: _ClassVar[RobotPlan.RobotRole]
        Offense: _ClassVar[RobotPlan.RobotRole]
    Default: RobotPlan.RobotRole
    Goalie: RobotPlan.RobotRole
    Defense: RobotPlan.RobotRole
    Offense: RobotPlan.RobotRole
    ROBOT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    NAV_TARGET_FIELD_NUMBER: _ClassVar[int]
    SHOT_TARGET_FIELD_NUMBER: _ClassVar[int]
    robot_id: int
    role: RobotPlan.RobotRole
    nav_target: Pose
    shot_target: Location
    def __init__(self, robot_id: _Optional[int] = ..., role: _Optional[_Union[RobotPlan.RobotRole, str]] = ..., nav_target: _Optional[_Union[Pose, _Mapping]] = ..., shot_target: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class Pose(_message.Message):
    __slots__ = ("loc", "heading")
    LOC_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    loc: Location
    heading: float
    def __init__(self, loc: _Optional[_Union[Location, _Mapping]] = ..., heading: _Optional[float] = ...) -> None: ...
