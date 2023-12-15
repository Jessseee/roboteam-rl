import protobuf.logfile_pb2 as _logfile_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FrameLookup(_message.Message):
    __slots__ = ("uid", "frame_number")
    UID_FIELD_NUMBER: _ClassVar[int]
    FRAME_NUMBER_FIELD_NUMBER: _ClassVar[int]
    uid: _logfile_pb2.UidEntry
    frame_number: int
    def __init__(self, uid: _Optional[_Union[_logfile_pb2.UidEntry, _Mapping]] = ..., frame_number: _Optional[int] = ...) -> None: ...

class FrameDescriptor(_message.Message):
    __slots__ = ("base_hash", "base_frame_number", "frame_infos")
    BASE_HASH_FIELD_NUMBER: _ClassVar[int]
    BASE_FRAME_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FRAME_INFOS_FIELD_NUMBER: _ClassVar[int]
    base_hash: str
    base_frame_number: int
    frame_infos: _containers.RepeatedCompositeFieldContainer[FrameLookup]
    def __init__(self, base_hash: _Optional[str] = ..., base_frame_number: _Optional[int] = ..., frame_infos: _Optional[_Iterable[_Union[FrameLookup, _Mapping]]] = ...) -> None: ...

class GameEvent(_message.Message):
    __slots__ = ("location", "progress", "random_id", "description", "tag", "assignee")
    class Progress(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Open: _ClassVar[GameEvent.Progress]
        Closed: _ClassVar[GameEvent.Progress]
        Postponed: _ClassVar[GameEvent.Progress]
        Resolved: _ClassVar[GameEvent.Progress]
        InProgress: _ClassVar[GameEvent.Progress]
        Info: _ClassVar[GameEvent.Progress]
        Merged: _ClassVar[GameEvent.Progress]
    Open: GameEvent.Progress
    Closed: GameEvent.Progress
    Postponed: GameEvent.Progress
    Resolved: GameEvent.Progress
    InProgress: GameEvent.Progress
    Info: GameEvent.Progress
    Merged: GameEvent.Progress
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RANDOM_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
    location: FrameDescriptor
    progress: GameEvent.Progress
    random_id: str
    description: str
    tag: _containers.RepeatedScalarFieldContainer[str]
    assignee: str
    def __init__(self, location: _Optional[_Union[FrameDescriptor, _Mapping]] = ..., progress: _Optional[_Union[GameEvent.Progress, str]] = ..., random_id: _Optional[str] = ..., description: _Optional[str] = ..., tag: _Optional[_Iterable[str]] = ..., assignee: _Optional[str] = ...) -> None: ...

class TimelineInit(_message.Message):
    __slots__ = ("primary", "secondary", "partially", "state")
    class Resolved(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Solved: _ClassVar[TimelineInit.Resolved]
        Conflicting: _ClassVar[TimelineInit.Resolved]
    Solved: TimelineInit.Resolved
    Conflicting: TimelineInit.Resolved
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_FIELD_NUMBER: _ClassVar[int]
    PARTIALLY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    primary: _logfile_pb2.UidEntry
    secondary: _containers.RepeatedCompositeFieldContainer[_logfile_pb2.UidEntry]
    partially: _containers.RepeatedCompositeFieldContainer[_logfile_pb2.UidEntry]
    state: TimelineInit.Resolved
    def __init__(self, primary: _Optional[_Union[_logfile_pb2.UidEntry, _Mapping]] = ..., secondary: _Optional[_Iterable[_Union[_logfile_pb2.UidEntry, _Mapping]]] = ..., partially: _Optional[_Iterable[_Union[_logfile_pb2.UidEntry, _Mapping]]] = ..., state: _Optional[_Union[TimelineInit.Resolved, str]] = ...) -> None: ...

class EventWrapper(_message.Message):
    __slots__ = ("tag", "conflicting")
    TAG_FIELD_NUMBER: _ClassVar[int]
    CONFLICTING_FIELD_NUMBER: _ClassVar[int]
    tag: str
    conflicting: _containers.RepeatedCompositeFieldContainer[GameEvent]
    def __init__(self, tag: _Optional[str] = ..., conflicting: _Optional[_Iterable[_Union[GameEvent, _Mapping]]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("wrapper", "game_event")
    WRAPPER_FIELD_NUMBER: _ClassVar[int]
    GAME_EVENT_FIELD_NUMBER: _ClassVar[int]
    wrapper: EventWrapper
    game_event: GameEvent
    def __init__(self, wrapper: _Optional[_Union[EventWrapper, _Mapping]] = ..., game_event: _Optional[_Union[GameEvent, _Mapping]] = ...) -> None: ...
