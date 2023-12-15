import protobuf.ssl_vision_wrapper_tracked_pb2 as _ssl_vision_wrapper_tracked_pb2
import protobuf.ssl_gc_api_pb2 as _ssl_gc_api_pb2
import protobuf.ssl_referee_pb2 as _ssl_referee_pb2
import protobuf.ssl_geometry_pb2 as _ssl_geometry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CiInput(_message.Message):
    __slots__ = ("timestamp", "tracker_packet", "api_inputs", "geometry")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACKER_PACKET_FIELD_NUMBER: _ClassVar[int]
    API_INPUTS_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    tracker_packet: _ssl_vision_wrapper_tracked_pb2.TrackerWrapperPacket
    api_inputs: _containers.RepeatedCompositeFieldContainer[_ssl_gc_api_pb2.Input]
    geometry: _ssl_geometry_pb2.SSL_GeometryData
    def __init__(self, timestamp: _Optional[int] = ..., tracker_packet: _Optional[_Union[_ssl_vision_wrapper_tracked_pb2.TrackerWrapperPacket, _Mapping]] = ..., api_inputs: _Optional[_Iterable[_Union[_ssl_gc_api_pb2.Input, _Mapping]]] = ..., geometry: _Optional[_Union[_ssl_geometry_pb2.SSL_GeometryData, _Mapping]] = ...) -> None: ...

class CiOutput(_message.Message):
    __slots__ = ("referee_msg",)
    REFEREE_MSG_FIELD_NUMBER: _ClassVar[int]
    referee_msg: _ssl_referee_pb2.SSL_Referee
    def __init__(self, referee_msg: _Optional[_Union[_ssl_referee_pb2.SSL_Referee, _Mapping]] = ...) -> None: ...
