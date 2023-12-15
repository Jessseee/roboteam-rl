import protobuf.ssl_game_controller_geometry_pb2 as _ssl_game_controller_geometry_pb2
import protobuf.ssl_game_controller_common_pb2 as _ssl_game_controller_common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GcState(_message.Message):
    __slots__ = ("team_state", "auto_ref_state", "tracker_state", "tracker_state_gc", "ready_to_continue")
    class TeamStateEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: GcStateTeam
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[GcStateTeam, _Mapping]] = ...) -> None: ...
    class AutoRefStateEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: GcStateAutoRef
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[GcStateAutoRef, _Mapping]] = ...) -> None: ...
    class TrackerStateEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: GcStateTracker
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[GcStateTracker, _Mapping]] = ...) -> None: ...
    TEAM_STATE_FIELD_NUMBER: _ClassVar[int]
    AUTO_REF_STATE_FIELD_NUMBER: _ClassVar[int]
    TRACKER_STATE_FIELD_NUMBER: _ClassVar[int]
    TRACKER_STATE_GC_FIELD_NUMBER: _ClassVar[int]
    READY_TO_CONTINUE_FIELD_NUMBER: _ClassVar[int]
    team_state: _containers.MessageMap[str, GcStateTeam]
    auto_ref_state: _containers.MessageMap[str, GcStateAutoRef]
    tracker_state: _containers.MessageMap[str, GcStateTracker]
    tracker_state_gc: GcStateTracker
    ready_to_continue: bool
    def __init__(self, team_state: _Optional[_Mapping[str, GcStateTeam]] = ..., auto_ref_state: _Optional[_Mapping[str, GcStateAutoRef]] = ..., tracker_state: _Optional[_Mapping[str, GcStateTracker]] = ..., tracker_state_gc: _Optional[_Union[GcStateTracker, _Mapping]] = ..., ready_to_continue: bool = ...) -> None: ...

class GcStateTeam(_message.Message):
    __slots__ = ("connected", "connection_verified", "remote_control_connected", "remote_control_connection_verified")
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CONTROL_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CONTROL_CONNECTION_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    connected: bool
    connection_verified: bool
    remote_control_connected: bool
    remote_control_connection_verified: bool
    def __init__(self, connected: bool = ..., connection_verified: bool = ..., remote_control_connected: bool = ..., remote_control_connection_verified: bool = ...) -> None: ...

class GcStateAutoRef(_message.Message):
    __slots__ = ("connection_verified",)
    CONNECTION_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    connection_verified: bool
    def __init__(self, connection_verified: bool = ...) -> None: ...

class GcStateTracker(_message.Message):
    __slots__ = ("source_name", "uuid", "ball", "robots")
    SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    BALL_FIELD_NUMBER: _ClassVar[int]
    ROBOTS_FIELD_NUMBER: _ClassVar[int]
    source_name: str
    uuid: str
    ball: Ball
    robots: _containers.RepeatedCompositeFieldContainer[Robot]
    def __init__(self, source_name: _Optional[str] = ..., uuid: _Optional[str] = ..., ball: _Optional[_Union[Ball, _Mapping]] = ..., robots: _Optional[_Iterable[_Union[Robot, _Mapping]]] = ...) -> None: ...

class Ball(_message.Message):
    __slots__ = ("pos", "vel")
    POS_FIELD_NUMBER: _ClassVar[int]
    VEL_FIELD_NUMBER: _ClassVar[int]
    pos: _ssl_game_controller_geometry_pb2.Vector3
    vel: _ssl_game_controller_geometry_pb2.Vector3
    def __init__(self, pos: _Optional[_Union[_ssl_game_controller_geometry_pb2.Vector3, _Mapping]] = ..., vel: _Optional[_Union[_ssl_game_controller_geometry_pb2.Vector3, _Mapping]] = ...) -> None: ...

class Robot(_message.Message):
    __slots__ = ("id", "pos")
    ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    id: _ssl_game_controller_common_pb2.BotId
    pos: _ssl_game_controller_geometry_pb2.Vector2
    def __init__(self, id: _Optional[_Union[_ssl_game_controller_common_pb2.BotId, _Mapping]] = ..., pos: _Optional[_Union[_ssl_game_controller_geometry_pb2.Vector2, _Mapping]] = ...) -> None: ...
