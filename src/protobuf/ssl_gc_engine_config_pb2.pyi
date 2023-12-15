from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ("game_event_behavior", "auto_ref_configs", "active_tracker_source", "teams")
    class Behavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BEHAVIOR_UNKNOWN: _ClassVar[Config.Behavior]
        BEHAVIOR_ACCEPT: _ClassVar[Config.Behavior]
        BEHAVIOR_ACCEPT_MAJORITY: _ClassVar[Config.Behavior]
        BEHAVIOR_PROPOSE_ONLY: _ClassVar[Config.Behavior]
        BEHAVIOR_LOG: _ClassVar[Config.Behavior]
        BEHAVIOR_IGNORE: _ClassVar[Config.Behavior]
    BEHAVIOR_UNKNOWN: Config.Behavior
    BEHAVIOR_ACCEPT: Config.Behavior
    BEHAVIOR_ACCEPT_MAJORITY: Config.Behavior
    BEHAVIOR_PROPOSE_ONLY: Config.Behavior
    BEHAVIOR_LOG: Config.Behavior
    BEHAVIOR_IGNORE: Config.Behavior
    class GameEventBehaviorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Config.Behavior
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Config.Behavior, str]] = ...) -> None: ...
    class AutoRefConfigsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AutoRefConfig
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AutoRefConfig, _Mapping]] = ...) -> None: ...
    GAME_EVENT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    AUTO_REF_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TRACKER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    game_event_behavior: _containers.ScalarMap[str, Config.Behavior]
    auto_ref_configs: _containers.MessageMap[str, AutoRefConfig]
    active_tracker_source: str
    teams: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, game_event_behavior: _Optional[_Mapping[str, Config.Behavior]] = ..., auto_ref_configs: _Optional[_Mapping[str, AutoRefConfig]] = ..., active_tracker_source: _Optional[str] = ..., teams: _Optional[_Iterable[str]] = ...) -> None: ...

class AutoRefConfig(_message.Message):
    __slots__ = ("game_event_behavior",)
    class Behavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BEHAVIOR_UNKNOWN: _ClassVar[AutoRefConfig.Behavior]
        BEHAVIOR_ACCEPT: _ClassVar[AutoRefConfig.Behavior]
        BEHAVIOR_LOG: _ClassVar[AutoRefConfig.Behavior]
        BEHAVIOR_IGNORE: _ClassVar[AutoRefConfig.Behavior]
    BEHAVIOR_UNKNOWN: AutoRefConfig.Behavior
    BEHAVIOR_ACCEPT: AutoRefConfig.Behavior
    BEHAVIOR_LOG: AutoRefConfig.Behavior
    BEHAVIOR_IGNORE: AutoRefConfig.Behavior
    class GameEventBehaviorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AutoRefConfig.Behavior
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AutoRefConfig.Behavior, str]] = ...) -> None: ...
    GAME_EVENT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    game_event_behavior: _containers.ScalarMap[str, AutoRefConfig.Behavior]
    def __init__(self, game_event_behavior: _Optional[_Mapping[str, AutoRefConfig.Behavior]] = ...) -> None: ...
