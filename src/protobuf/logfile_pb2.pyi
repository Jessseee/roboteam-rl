from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UidEntry(_message.Message):
    __slots__ = ("hash", "flags")
    HASH_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    hash: str
    flags: int
    def __init__(self, hash: _Optional[str] = ..., flags: _Optional[int] = ...) -> None: ...

class Uid(_message.Message):
    __slots__ = ("parts",)
    PARTS_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedCompositeFieldContainer[UidEntry]
    def __init__(self, parts: _Optional[_Iterable[_Union[UidEntry, _Mapping]]] = ...) -> None: ...

class LogRequest(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class LogOfferEntry(_message.Message):
    __slots__ = ("name", "quality", "uri")
    class QUALITY(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERFECT: _ClassVar[LogOfferEntry.QUALITY]
        UNKNOWN: _ClassVar[LogOfferEntry.QUALITY]
        UNREADABLE: _ClassVar[LogOfferEntry.QUALITY]
    PERFECT: LogOfferEntry.QUALITY
    UNKNOWN: LogOfferEntry.QUALITY
    UNREADABLE: LogOfferEntry.QUALITY
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    name: str
    quality: LogOfferEntry.QUALITY
    uri: LogRequest
    def __init__(self, name: _Optional[str] = ..., quality: _Optional[_Union[LogOfferEntry.QUALITY, str]] = ..., uri: _Optional[_Union[LogRequest, _Mapping]] = ...) -> None: ...

class LogOffer(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[LogOfferEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[LogOfferEntry, _Mapping]]] = ...) -> None: ...
