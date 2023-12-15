from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DebugSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    StrategyBlue: _ClassVar[DebugSource]
    StrategyYellow: _ClassVar[DebugSource]
    Controller: _ClassVar[DebugSource]
    Autoref: _ClassVar[DebugSource]
    Tracking: _ClassVar[DebugSource]
    RadioResponse: _ClassVar[DebugSource]
    ReplayBlue: _ClassVar[DebugSource]
    ReplayYellow: _ClassVar[DebugSource]
    NetworkTransceiver: _ClassVar[DebugSource]
    GameController: _ClassVar[DebugSource]
StrategyBlue: DebugSource
StrategyYellow: DebugSource
Controller: DebugSource
Autoref: DebugSource
Tracking: DebugSource
RadioResponse: DebugSource
ReplayBlue: DebugSource
ReplayYellow: DebugSource
NetworkTransceiver: DebugSource
GameController: DebugSource

class Color(_message.Message):
    __slots__ = ("red", "green", "blue", "alpha")
    RED_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    red: int
    green: int
    blue: int
    alpha: int
    def __init__(self, red: _Optional[int] = ..., green: _Optional[int] = ..., blue: _Optional[int] = ..., alpha: _Optional[int] = ...) -> None: ...

class Pen(_message.Message):
    __slots__ = ("style", "color")
    class Style(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DashLine: _ClassVar[Pen.Style]
        DotLine: _ClassVar[Pen.Style]
        DashDotLine: _ClassVar[Pen.Style]
        DashDotDotLine: _ClassVar[Pen.Style]
    DashLine: Pen.Style
    DotLine: Pen.Style
    DashDotLine: Pen.Style
    DashDotDotLine: Pen.Style
    STYLE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    style: Pen.Style
    color: Color
    def __init__(self, style: _Optional[_Union[Pen.Style, str]] = ..., color: _Optional[_Union[Color, _Mapping]] = ...) -> None: ...

class Circle(_message.Message):
    __slots__ = ("p_x", "p_y", "radius")
    P_X_FIELD_NUMBER: _ClassVar[int]
    P_Y_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    p_x: float
    p_y: float
    radius: float
    def __init__(self, p_x: _Optional[float] = ..., p_y: _Optional[float] = ..., radius: _Optional[float] = ...) -> None: ...

class Point(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class Polygon(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _containers.RepeatedCompositeFieldContainer[Point]
    def __init__(self, point: _Optional[_Iterable[_Union[Point, _Mapping]]] = ...) -> None: ...

class Path(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _containers.RepeatedCompositeFieldContainer[Point]
    def __init__(self, point: _Optional[_Iterable[_Union[Point, _Mapping]]] = ...) -> None: ...

class Rectangle(_message.Message):
    __slots__ = ("topleft", "bottomright")
    TOPLEFT_FIELD_NUMBER: _ClassVar[int]
    BOTTOMRIGHT_FIELD_NUMBER: _ClassVar[int]
    topleft: Point
    bottomright: Point
    def __init__(self, topleft: _Optional[_Union[Point, _Mapping]] = ..., bottomright: _Optional[_Union[Point, _Mapping]] = ...) -> None: ...

class ImageVisualization(_message.Message):
    __slots__ = ("width", "height", "data", "draw_area")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DRAW_AREA_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    data: bytes
    draw_area: Rectangle
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., data: _Optional[bytes] = ..., draw_area: _Optional[_Union[Rectangle, _Mapping]] = ...) -> None: ...

class Visualization(_message.Message):
    __slots__ = ("name", "pen", "brush", "width", "circle", "polygon", "path", "background", "image")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PEN_FIELD_NUMBER: _ClassVar[int]
    BRUSH_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    CIRCLE_FIELD_NUMBER: _ClassVar[int]
    POLYGON_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    pen: Pen
    brush: Color
    width: float
    circle: Circle
    polygon: Polygon
    path: Path
    background: bool
    image: ImageVisualization
    def __init__(self, name: _Optional[str] = ..., pen: _Optional[_Union[Pen, _Mapping]] = ..., brush: _Optional[_Union[Color, _Mapping]] = ..., width: _Optional[float] = ..., circle: _Optional[_Union[Circle, _Mapping]] = ..., polygon: _Optional[_Union[Polygon, _Mapping]] = ..., path: _Optional[_Union[Path, _Mapping]] = ..., background: bool = ..., image: _Optional[_Union[ImageVisualization, _Mapping]] = ...) -> None: ...

class DebugValue(_message.Message):
    __slots__ = ("key", "float_value", "bool_value", "string_value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    float_value: float
    bool_value: bool
    string_value: str
    def __init__(self, key: _Optional[str] = ..., float_value: _Optional[float] = ..., bool_value: bool = ..., string_value: _Optional[str] = ...) -> None: ...

class StatusLog(_message.Message):
    __slots__ = ("timestamp", "text")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    text: str
    def __init__(self, timestamp: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class PlotValue(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: float
    def __init__(self, name: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...

class RobotValue(_message.Message):
    __slots__ = ("generation", "id", "exchange")
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    generation: int
    id: int
    exchange: bool
    def __init__(self, generation: _Optional[int] = ..., id: _Optional[int] = ..., exchange: bool = ...) -> None: ...

class DebuggerOutput(_message.Message):
    __slots__ = ("line",)
    LINE_FIELD_NUMBER: _ClassVar[int]
    line: str
    def __init__(self, line: _Optional[str] = ...) -> None: ...

class DebugValues(_message.Message):
    __slots__ = ("source", "time", "value", "visualization", "log", "plot", "robot", "debugger_output")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VISUALIZATION_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    PLOT_FIELD_NUMBER: _ClassVar[int]
    ROBOT_FIELD_NUMBER: _ClassVar[int]
    DEBUGGER_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    source: DebugSource
    time: int
    value: _containers.RepeatedCompositeFieldContainer[DebugValue]
    visualization: _containers.RepeatedCompositeFieldContainer[Visualization]
    log: _containers.RepeatedCompositeFieldContainer[StatusLog]
    plot: _containers.RepeatedCompositeFieldContainer[PlotValue]
    robot: _containers.RepeatedCompositeFieldContainer[RobotValue]
    debugger_output: DebuggerOutput
    def __init__(self, source: _Optional[_Union[DebugSource, str]] = ..., time: _Optional[int] = ..., value: _Optional[_Iterable[_Union[DebugValue, _Mapping]]] = ..., visualization: _Optional[_Iterable[_Union[Visualization, _Mapping]]] = ..., log: _Optional[_Iterable[_Union[StatusLog, _Mapping]]] = ..., plot: _Optional[_Iterable[_Union[PlotValue, _Mapping]]] = ..., robot: _Optional[_Iterable[_Union[RobotValue, _Mapping]]] = ..., debugger_output: _Optional[_Union[DebuggerOutput, _Mapping]] = ...) -> None: ...
