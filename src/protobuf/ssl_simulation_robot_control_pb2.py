# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssl_simulation_robot_control.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"ssl_simulation_robot_control.proto\x12\x06sslsim\"\x8d\x01\n\x0cRobotCommand\x12\n\n\x02id\x18\x01 \x02(\r\x12.\n\x0cmove_command\x18\x02 \x01(\x0b\x32\x18.sslsim.RobotMoveCommand\x12\x12\n\nkick_speed\x18\x03 \x01(\x02\x12\x15\n\nkick_angle\x18\x04 \x01(\x02:\x01\x30\x12\x16\n\x0e\x64ribbler_speed\x18\x05 \x01(\x02\"\xbe\x01\n\x10RobotMoveCommand\x12\x33\n\x0ewheel_velocity\x18\x01 \x01(\x0b\x32\x19.sslsim.MoveWheelVelocityH\x00\x12\x33\n\x0elocal_velocity\x18\x02 \x01(\x0b\x32\x19.sslsim.MoveLocalVelocityH\x00\x12\x35\n\x0fglobal_velocity\x18\x03 \x01(\x0b\x32\x1a.sslsim.MoveGlobalVelocityH\x00\x42\t\n\x07\x63ommand\"c\n\x11MoveWheelVelocity\x12\x13\n\x0b\x66ront_right\x18\x01 \x02(\x02\x12\x12\n\nback_right\x18\x02 \x02(\x02\x12\x11\n\tback_left\x18\x03 \x02(\x02\x12\x12\n\nfront_left\x18\x04 \x02(\x02\"C\n\x11MoveLocalVelocity\x12\x0f\n\x07\x66orward\x18\x01 \x02(\x02\x12\x0c\n\x04left\x18\x02 \x02(\x02\x12\x0f\n\x07\x61ngular\x18\x03 \x02(\x02\";\n\x12MoveGlobalVelocity\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\x0f\n\x07\x61ngular\x18\x03 \x02(\x02\"<\n\x0cRobotControl\x12,\n\x0erobot_commands\x18\x01 \x03(\x0b\x32\x14.sslsim.RobotCommand')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ssl_simulation_robot_control_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ROBOTCOMMAND']._serialized_start=47
  _globals['_ROBOTCOMMAND']._serialized_end=188
  _globals['_ROBOTMOVECOMMAND']._serialized_start=191
  _globals['_ROBOTMOVECOMMAND']._serialized_end=381
  _globals['_MOVEWHEELVELOCITY']._serialized_start=383
  _globals['_MOVEWHEELVELOCITY']._serialized_end=482
  _globals['_MOVELOCALVELOCITY']._serialized_start=484
  _globals['_MOVELOCALVELOCITY']._serialized_end=551
  _globals['_MOVEGLOBALVELOCITY']._serialized_start=553
  _globals['_MOVEGLOBALVELOCITY']._serialized_end=612
  _globals['_ROBOTCONTROL']._serialized_start=614
  _globals['_ROBOTCONTROL']._serialized_end=674
# @@protoc_insertion_point(module_scope)
