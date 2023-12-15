# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: world.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protobuf.robot_pb2 as robot__pb2
import protobuf.ssl_mixed_team_pb2 as ssl__mixed__team__pb2
import protobuf.ssl_wrapper_pb2 as ssl__wrapper__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bworld.proto\x12\x05world\x1a\x0brobot.proto\x1a\x14ssl_mixed_team.proto\x1a\x11ssl_wrapper.proto\"\x84\x05\n\x08Geometry\x12\x12\n\nline_width\x18\x01 \x02(\x02\x12\x13\n\x0b\x66ield_width\x18\x02 \x02(\x02\x12\x14\n\x0c\x66ield_height\x18\x03 \x02(\x02\x12\x16\n\x0e\x62oundary_width\x18\x04 \x02(\x02\x12\x12\n\ngoal_width\x18\x06 \x02(\x02\x12\x12\n\ngoal_depth\x18\x07 \x02(\x02\x12\x17\n\x0fgoal_wall_width\x18\x08 \x02(\x02\x12\x1c\n\x14\x63\x65nter_circle_radius\x18\t \x02(\x02\x12\x16\n\x0e\x64\x65\x66\x65nse_radius\x18\n \x02(\x02\x12\x17\n\x0f\x64\x65\x66\x65nse_stretch\x18\x0b \x02(\x02\x12#\n\x1b\x66ree_kick_from_defense_dist\x18\x0c \x02(\x02\x12)\n!penalty_spot_from_field_line_dist\x18\r \x02(\x02\x12#\n\x1bpenalty_line_from_spot_dist\x18\x0e \x02(\x02\x12\x13\n\x0bgoal_height\x18\x0f \x02(\x02\x12\x18\n\rdefense_width\x18\x10 \x01(\x02:\x01\x32\x12\x19\n\x0e\x64\x65\x66\x65nse_height\x18\x11 \x01(\x02:\x01\x31\x12\x35\n\x04type\x18\x12 \x01(\x0e\x32\x1c.world.Geometry.GeometryType:\tTYPE_2014\x12-\n\x08\x64ivision\x18\x13 \x01(\x0e\x32\x18.world.Geometry.Division:\x01\x41\x12$\n\nball_model\x18\x14 \x01(\x0b\x32\x10.world.BallModel\",\n\x0cGeometryType\x12\r\n\tTYPE_2014\x10\x01\x12\r\n\tTYPE_2018\x10\x02\"\x18\n\x08\x44ivision\x12\x05\n\x01\x41\x10\x01\x12\x05\n\x01\x42\x10\x02\"~\n\tBallModel\x12\x19\n\x11\x66\x61st_deceleration\x18\x01 \x01(\x02\x12\x19\n\x11slow_deceleration\x18\x02 \x01(\x02\x12\x14\n\x0cswitch_ratio\x18\x03 \x01(\x02\x12\x11\n\tz_damping\x18\x04 \x01(\x02\x12\x12\n\nxy_damping\x18\x05 \x01(\x02\"r\n\x12\x44ivisionDimensions\x12\x15\n\rfield_width_a\x18\x01 \x02(\x02\x12\x16\n\x0e\x66ield_height_a\x18\x02 \x02(\x02\x12\x15\n\rfield_width_b\x18\x03 \x02(\x02\x12\x16\n\x0e\x66ield_height_b\x18\x04 \x02(\x02\"\xd4\x01\n\x0c\x42\x61llPosition\x12\x0c\n\x04time\x18\x01 \x02(\x03\x12\x0b\n\x03p_x\x18\x02 \x02(\x02\x12\x0b\n\x03p_y\x18\x03 \x02(\x02\x12\x11\n\tderived_z\x18\n \x01(\x02\x12\x0b\n\x03v_x\x18\x05 \x01(\x02\x12\x0b\n\x03v_y\x18\x06 \x01(\x02\x12\x14\n\x0csystem_delay\x18\x07 \x01(\x02\x12\x18\n\x10time_diff_scaled\x18\x08 \x01(\x02\x12\x11\n\tcamera_id\x18\t \x01(\r\x12\x0c\n\x04\x61rea\x18\x0b \x01(\x02\x12\x1e\n\x16vision_processing_time\x18\x0c \x01(\x03\"\xc8\x01\n\x04\x42\x61ll\x12\x0b\n\x03p_x\x18\x01 \x02(\x02\x12\x0b\n\x03p_y\x18\x02 \x02(\x02\x12\x0b\n\x03p_z\x18\x06 \x01(\x02\x12\x0b\n\x03v_x\x18\x03 \x02(\x02\x12\x0b\n\x03v_y\x18\x04 \x02(\x02\x12\x0b\n\x03v_z\x18\x07 \x01(\x02\x12\x13\n\x0btouchdown_x\x18\x08 \x01(\x02\x12\x13\n\x0btouchdown_y\x18\t \x01(\x02\x12\x13\n\x0bis_bouncing\x18\n \x01(\x08\x12\x11\n\tmax_speed\x18\x0b \x01(\x02\x12 \n\x03raw\x18\x05 \x03(\x0b\x32\x13.world.BallPosition\"\xd0\x01\n\rRobotPosition\x12\x0c\n\x04time\x18\x01 \x02(\x03\x12\x0b\n\x03p_x\x18\x02 \x02(\x02\x12\x0b\n\x03p_y\x18\x03 \x02(\x02\x12\x0b\n\x03phi\x18\x04 \x02(\x02\x12\x0b\n\x03v_x\x18\x05 \x01(\x02\x12\x0b\n\x03v_y\x18\x06 \x01(\x02\x12\x14\n\x0csystem_delay\x18\x07 \x01(\x02\x12\x18\n\x10time_diff_scaled\x18\x08 \x01(\x02\x12\r\n\x05omega\x18\t \x01(\x02\x12\x11\n\tcamera_id\x18\n \x01(\r\x12\x1e\n\x16vision_processing_time\x18\x0b \x01(\x03\"\x86\x01\n\x05Robot\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0b\n\x03p_x\x18\x02 \x02(\x02\x12\x0b\n\x03p_y\x18\x03 \x02(\x02\x12\x0b\n\x03phi\x18\x04 \x02(\x02\x12\x0b\n\x03v_x\x18\x05 \x02(\x02\x12\x0b\n\x03v_y\x18\x06 \x02(\x02\x12\r\n\x05omega\x18\x07 \x02(\x02\x12!\n\x03raw\x18\x08 \x03(\x0b\x32\x14.world.RobotPosition\"=\n\x0bTrackingAOI\x12\n\n\x02x1\x18\x01 \x02(\x02\x12\n\n\x02y1\x18\x02 \x02(\x02\x12\n\n\x02x2\x18\x03 \x02(\x02\x12\n\n\x02y2\x18\x04 \x02(\x02\"\xcd\x04\n\x05State\x12\x0c\n\x04time\x18\x01 \x02(\x03\x12\x19\n\x04\x62\x61ll\x18\x02 \x01(\x0b\x32\x0b.world.Ball\x12\x1c\n\x06yellow\x18\x03 \x03(\x0b\x32\x0c.world.Robot\x12\x1a\n\x04\x62lue\x18\x04 \x03(\x0b\x32\x0c.world.Robot\x12,\n\x0eradio_response\x18\x05 \x03(\x0b\x32\x14.robot.RadioResponse\x12\x14\n\x0cis_simulated\x18\x06 \x01(\x08\x12\x17\n\x0fhas_vision_data\x18\x07 \x01(\x08\x12&\n\x0fmixed_team_info\x18\x08 \x01(\x0b\x32\r.ssl.TeamPlan\x12(\n\x0ctracking_aoi\x18\t \x01(\x0b\x32\x12.world.TrackingAOI\x12,\n\x16simple_tracking_yellow\x18\x0b \x03(\x0b\x32\x0c.world.Robot\x12*\n\x14simple_tracking_blue\x18\x0c \x03(\x0b\x32\x0c.world.Robot\x12)\n\x14simple_tracking_ball\x18\x11 \x01(\x0b\x32\x0b.world.Ball\x12&\n\x07reality\x18\r \x03(\x0b\x32\x15.world.SimulatorState\x12)\n\rvision_frames\x18\n \x03(\x0b\x32\x12.SSL_WrapperPacket\x12\x1a\n\x12vision_frame_times\x18\x0e \x03(\x03\x12\x14\n\x0csystem_delay\x18\x0f \x01(\x03\x12(\n\x0cworld_source\x18\x10 \x01(\x0e\x32\x12.world.WorldSource\"\x8a\x01\n\x0eSimulatorState\x12$\n\x0b\x62lue_robots\x18\x01 \x03(\x0b\x32\x0f.world.SimRobot\x12&\n\ryellow_robots\x18\x02 \x03(\x0b\x32\x0f.world.SimRobot\x12\x1c\n\x04\x62\x61ll\x18\x03 \x01(\x0b\x32\x0e.world.SimBall\x12\x0c\n\x04time\x18\x04 \x01(\x03\"\x90\x01\n\x07SimBall\x12\x0b\n\x03p_x\x18\x01 \x02(\x02\x12\x0b\n\x03p_y\x18\x02 \x02(\x02\x12\x0b\n\x03p_z\x18\x03 \x02(\x02\x12\x0b\n\x03v_x\x18\x04 \x02(\x02\x12\x0b\n\x03v_y\x18\x05 \x02(\x02\x12\x0b\n\x03v_z\x18\x06 \x02(\x02\x12\x11\n\tangular_x\x18\x07 \x01(\x02\x12\x11\n\tangular_y\x18\x08 \x01(\x02\x12\x11\n\tangular_z\x18\t \x01(\x02\";\n\nQuaternion\x12\t\n\x01i\x18\x01 \x02(\x02\x12\t\n\x01j\x18\x02 \x02(\x02\x12\t\n\x01k\x18\x03 \x02(\x02\x12\x0c\n\x04real\x18\x04 \x02(\x02\"\xc6\x01\n\x08SimRobot\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0b\n\x03p_x\x18\x02 \x02(\x02\x12\x0b\n\x03p_y\x18\x03 \x02(\x02\x12\x0b\n\x03p_z\x18\x04 \x02(\x02\x12#\n\x08rotation\x18\x05 \x02(\x0b\x32\x11.world.Quaternion\x12\x0b\n\x03v_x\x18\x06 \x02(\x02\x12\x0b\n\x03v_y\x18\x07 \x02(\x02\x12\x0b\n\x03v_z\x18\x08 \x02(\x02\x12\x0b\n\x03r_x\x18\t \x02(\x02\x12\x0b\n\x03r_y\x18\n \x02(\x02\x12\x0b\n\x03r_z\x18\x0b \x02(\x02\x12\x14\n\x0ctouches_ball\x18\x0c \x01(\x08*N\n\x0bWorldSource\x12\x17\n\x13INTERNAL_SIMULATION\x10\x01\x12\x17\n\x13\x45XTERNAL_SIMULATION\x10\x02\x12\r\n\tREAL_LIFE\x10\x03\x42\x03\xf8\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'world_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001'
  _globals['_WORLDSOURCE']._serialized_start=2938
  _globals['_WORLDSOURCE']._serialized_end=3016
  _globals['_GEOMETRY']._serialized_start=77
  _globals['_GEOMETRY']._serialized_end=721
  _globals['_GEOMETRY_GEOMETRYTYPE']._serialized_start=651
  _globals['_GEOMETRY_GEOMETRYTYPE']._serialized_end=695
  _globals['_GEOMETRY_DIVISION']._serialized_start=697
  _globals['_GEOMETRY_DIVISION']._serialized_end=721
  _globals['_BALLMODEL']._serialized_start=723
  _globals['_BALLMODEL']._serialized_end=849
  _globals['_DIVISIONDIMENSIONS']._serialized_start=851
  _globals['_DIVISIONDIMENSIONS']._serialized_end=965
  _globals['_BALLPOSITION']._serialized_start=968
  _globals['_BALLPOSITION']._serialized_end=1180
  _globals['_BALL']._serialized_start=1183
  _globals['_BALL']._serialized_end=1383
  _globals['_ROBOTPOSITION']._serialized_start=1386
  _globals['_ROBOTPOSITION']._serialized_end=1594
  _globals['_ROBOT']._serialized_start=1597
  _globals['_ROBOT']._serialized_end=1731
  _globals['_TRACKINGAOI']._serialized_start=1733
  _globals['_TRACKINGAOI']._serialized_end=1794
  _globals['_STATE']._serialized_start=1797
  _globals['_STATE']._serialized_end=2386
  _globals['_SIMULATORSTATE']._serialized_start=2389
  _globals['_SIMULATORSTATE']._serialized_end=2527
  _globals['_SIMBALL']._serialized_start=2530
  _globals['_SIMBALL']._serialized_end=2674
  _globals['_QUATERNION']._serialized_start=2676
  _globals['_QUATERNION']._serialized_end=2735
  _globals['_SIMROBOT']._serialized_start=2738
  _globals['_SIMROBOT']._serialized_end=2936
# @@protoc_insertion_point(module_scope)