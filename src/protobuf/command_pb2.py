# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protobuf.world_pb2 as world__pb2
import protobuf.robot_pb2 as robot__pb2
import protobuf.logfile_pb2 as logfile__pb2
import protobuf.ssl_geometry_pb2 as ssl__geometry__pb2
import protobuf.ssl_simulation_control_pb2 as ssl__simulation__control__pb2
import protobuf.ssl_simulation_custom_erforce_realism_pb2 as ssl__simulation__custom__erforce__realism__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcommand.proto\x12\x04\x61mun\x1a\x0bworld.proto\x1a\x0brobot.proto\x1a\rlogfile.proto\x1a\x12ssl_geometry.proto\x1a\x1cssl_simulation_control.proto\x1a+ssl_simulation_custom_erforce_realism.proto\"8\n\x10RobotMoveCommand\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0b\n\x03p_x\x18\x02 \x01(\x02\x12\x0b\n\x03p_y\x18\x03 \x01(\x02\"i\n\x0eSimulatorSetup\x12!\n\x08geometry\x18\x01 \x02(\x0b\x32\x0f.world.Geometry\x12\x34\n\x0c\x63\x61mera_setup\x18\x02 \x03(\x0b\x32\x1e.SSL_GeometryCameraCalibration\"]\n\x18SimulatorWorstCaseVision\x12 \n\x18min_robot_detection_time\x18\x01 \x01(\x02\x12\x1f\n\x17min_ball_detection_time\x18\x02 \x01(\x02\"\x9e\x02\n\x10\x43ommandSimulator\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12-\n\x0fsimulator_setup\x18\x02 \x01(\x0b\x32\x14.amun.SimulatorSetup\x12\x39\n\x11vision_worst_case\x18\x03 \x01(\x0b\x32\x1e.amun.SimulatorWorstCaseVision\x12-\n\x0erealism_config\x18\x04 \x01(\x0b\x32\x15.RealismConfigErForce\x12\x32\n\x13set_simulator_state\x18\x05 \x01(\x0b\x32\x15.world.SimulatorState\x12-\n\x0bssl_control\x18\x06 \x01(\x0b\x32\x18.sslsim.SimulatorControl\"u\n\x0e\x43ommandReferee\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\x08\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\x0c\x12\x1c\n\x14use_internal_autoref\x18\x03 \x01(\x08\x12$\n\x1cuse_automatic_robot_exchange\x18\x04 \x01(\x08\"<\n\x13\x43ommandStrategyLoad\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x13\n\x0b\x65ntry_point\x18\x02 \x01(\t\"\x16\n\x14\x43ommandStrategyClose\" \n\x1e\x43ommandStrategyTriggerDebugger\"\xc2\x02\n\x0f\x43ommandStrategy\x12\'\n\x04load\x18\x01 \x01(\x0b\x32\x19.amun.CommandStrategyLoad\x12)\n\x05\x63lose\x18\x02 \x01(\x0b\x32\x1a.amun.CommandStrategyClose\x12\x0e\n\x06reload\x18\x03 \x01(\x08\x12\x13\n\x0b\x61uto_reload\x18\x04 \x01(\x08\x12\x14\n\x0c\x65nable_debug\x18\x05 \x01(\x08\x12\x33\n\x05\x64\x65\x62ug\x18\x06 \x01(\x0b\x32$.amun.CommandStrategyTriggerDebugger\x12\x18\n\x10performance_mode\x18\x07 \x01(\x08\x12\x17\n\x0fstart_profiling\x18\x08 \x01(\x08\x12\x1f\n\x17\x66inish_and_save_profile\x18\t \x01(\t\x12\x17\n\x0ftournament_mode\x18\n \x01(\x08\"7\n\x0e\x43ommandControl\x12%\n\x08\x63ommands\x18\x01 \x03(\x0b\x32\x13.robot.RadioCommand\"+\n\x18TransceiverConfiguration\x12\x0f\n\x07\x63hannel\x18\x01 \x02(\r\")\n\x0bHostAddress\x12\x0c\n\x04host\x18\x01 \x02(\t\x12\x0c\n\x04port\x18\x02 \x02(\r\"\x86\x01\n\x13SimulatorNetworking\x12\x19\n\x11\x63ontrol_simulator\x18\x01 \x02(\x08\x12\x14\n\x0c\x63ontrol_blue\x18\x02 \x02(\x08\x12\x16\n\x0e\x63ontrol_yellow\x18\x03 \x02(\x08\x12\x11\n\tport_blue\x18\x04 \x02(\r\x12\x13\n\x0bport_yellow\x18\x05 \x02(\r\"\xee\x01\n\x12\x43ommandTransceiver\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12\x0e\n\x06\x63harge\x18\x02 \x01(\x08\x12\x35\n\rconfiguration\x18\x03 \x01(\x0b\x32\x1e.amun.TransceiverConfiguration\x12\x30\n\x15network_configuration\x18\x04 \x01(\x0b\x32\x11.amun.HostAddress\x12\x13\n\x0buse_network\x18\x05 \x01(\x08\x12:\n\x17simulator_configuration\x18\x06 \x01(\x0b\x32\x19.amun.SimulatorNetworking\"m\n\x15VirtualFieldTransform\x12\x0b\n\x03\x61\x31\x31\x18\x01 \x02(\x02\x12\x0b\n\x03\x61\x31\x32\x18\x02 \x02(\x02\x12\x0b\n\x03\x61\x32\x31\x18\x03 \x02(\x02\x12\x0b\n\x03\x61\x32\x32\x18\x04 \x02(\x02\x12\x0f\n\x07offsetX\x18\x05 \x02(\x02\x12\x0f\n\x07offsetY\x18\x06 \x02(\x02\"\xb2\x02\n\x0f\x43ommandTracking\x12\x13\n\x0b\x61oi_enabled\x18\x01 \x01(\x08\x12\x1f\n\x03\x61oi\x18\x02 \x01(\x0b\x32\x12.world.TrackingAOI\x12\x14\n\x0csystem_delay\x18\x03 \x01(\x03\x12\r\n\x05reset\x18\x04 \x01(\x08\x12\x1c\n\x14\x65nable_virtual_field\x18\x05 \x01(\x08\x12\x34\n\x0f\x66ield_transform\x18\x06 \x01(\x0b\x32\x1b.amun.VirtualFieldTransform\x12)\n\x10virtual_geometry\x18\x07 \x01(\x0b\x32\x0f.world.Geometry\x12\x1f\n\x17tracking_replay_enabled\x18\x08 \x01(\x08\x12$\n\nball_model\x18\t \x01(\x0b\x32\x10.world.BallModel\":\n\x1b\x43ommandStrategyChangeOption\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\x08\"\x88\x01\n\x0b\x43ommandAmun\x12\x13\n\x0bvision_port\x18\x01 \x01(\r\x12\x14\n\x0creferee_port\x18\x02 \x01(\r\x12\x14\n\x0ctracker_port\x18\x04 \x01(\r\x12\x38\n\rchange_option\x18\x03 \x01(\x0b\x32!.amun.CommandStrategyChangeOption\"\x1d\n\x1b\x43ommandDebuggerInputDisable\"(\n\x18\x43ommandDebuggerInputLine\x12\x0c\n\x04line\x18\x01 \x01(\t\"\xb0\x01\n\x14\x43ommandDebuggerInput\x12\x30\n\rstrategy_type\x18\x01 \x02(\x0e\x32\x19.amun.DebuggerInputTarget\x12\x32\n\x07\x64isable\x18\x02 \x01(\x0b\x32!.amun.CommandDebuggerInputDisable\x12\x32\n\nqueue_line\x18\x03 \x01(\x0b\x32\x1e.amun.CommandDebuggerInputLine\"b\n\x15PauseSimulatorCommand\x12*\n\x06reason\x18\x01 \x02(\x0e\x32\x1a.amun.PauseSimulatorReason\x12\r\n\x05pause\x18\x02 \x01(\x08\x12\x0e\n\x06toggle\x18\x03 \x01(\x08\"\xbb\x01\n\rCommandReplay\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12\x1c\n\x14\x65nable_blue_strategy\x18\x02 \x01(\x08\x12,\n\rblue_strategy\x18\x03 \x01(\x0b\x32\x15.amun.CommandStrategy\x12\x1e\n\x16\x65nable_yellow_strategy\x18\x04 \x01(\x08\x12.\n\x0fyellow_strategy\x18\x05 \x01(\x0b\x32\x15.amun.CommandStrategy\"\x06\n\x04\x46lag\"\xd8\x02\n\x0f\x43ommandPlayback\x12\x11\n\tseek_time\x18\x01 \x01(\x05\x12\x13\n\x0bseek_packet\x18\x02 \x01(\x05\x12\x1b\n\x13seek_time_backwards\x18\x03 \x01(\x05\x12\x16\n\x0eplayback_speed\x18\x04 \x01(\x05\x12!\n\rtoggle_paused\x18\x05 \x01(\x0b\x32\n.amun.Flag\x12\x14\n\x0crun_playback\x18\x06 \x01(\x08\x12%\n\x08log_path\x18\x07 \x01(\x0b\x32\x13.logfile.LogRequest\x12\"\n\x0einstant_replay\x18\x08 \x01(\x0b\x32\n.amun.Flag\x12\x19\n\x11\x65xport_vision_log\x18\t \x01(\t\x12\x1b\n\x07get_uid\x18\n \x01(\x0b\x32\n.amun.Flag\x12\x14\n\x0c\x66ind_logfile\x18\x0b \x01(\t\x12\x16\n\x0eplayback_limit\x18\x0c \x01(\x05\"\xb4\x01\n\rCommandRecord\x12\x1c\n\x14use_logfile_location\x18\x01 \x01(\x08\x12 \n\x0csave_backlog\x18\x02 \x01(\x0b\x32\n.amun.Flag\x12\x13\n\x0brun_logging\x18\x03 \x01(\x08\x12\x12\n\nfor_replay\x18\x04 \x01(\x08\x12\x17\n\x0frequest_backlog\x18\x05 \x01(\x05\x12!\n\x19overwrite_record_filename\x18\x06 \x01(\t\"\xc8\x06\n\x07\x43ommand\x12)\n\tsimulator\x18\x01 \x01(\x0b\x32\x16.amun.CommandSimulator\x12%\n\x07referee\x18\x02 \x01(\x0b\x32\x14.amun.CommandReferee\x12\"\n\rset_team_blue\x18\x03 \x01(\x0b\x32\x0b.robot.Team\x12$\n\x0fset_team_yellow\x18\x04 \x01(\x0b\x32\x0b.robot.Team\x12,\n\rstrategy_blue\x18\x05 \x01(\x0b\x32\x15.amun.CommandStrategy\x12.\n\x0fstrategy_yellow\x18\x06 \x01(\x0b\x32\x15.amun.CommandStrategy\x12/\n\x10strategy_autoref\x18\x07 \x01(\x0b\x32\x15.amun.CommandStrategy\x12%\n\x07\x63ontrol\x18\x08 \x01(\x0b\x32\x14.amun.CommandControl\x12-\n\x0btransceiver\x18\t \x01(\x0b\x32\x18.amun.CommandTransceiver\x12\'\n\x08tracking\x18\x0b \x01(\x0b\x32\x15.amun.CommandTracking\x12\x1f\n\x04\x61mun\x18\x0c \x01(\x0b\x32\x11.amun.CommandAmun\x12\x31\n\x16mixed_team_destination\x18\r \x01(\x0b\x32\x11.amun.HostAddress\x12/\n\x0frobot_move_blue\x18\x0e \x03(\x0b\x32\x16.amun.RobotMoveCommand\x12\x31\n\x11robot_move_yellow\x18\x0f \x03(\x0b\x32\x16.amun.RobotMoveCommand\x12\x32\n\x0e\x64\x65\x62ugger_input\x18\x10 \x01(\x0b\x32\x1a.amun.CommandDebuggerInput\x12\x34\n\x0fpause_simulator\x18\x11 \x01(\x0b\x32\x1b.amun.PauseSimulatorCommand\x12#\n\x06replay\x18\x12 \x01(\x0b\x32\x13.amun.CommandReplay\x12\'\n\x08playback\x18\x13 \x01(\x0b\x32\x15.amun.CommandPlayback\x12#\n\x06record\x18\x14 \x01(\x0b\x32\x13.amun.CommandRecord*Q\n\x13\x44\x65\x62uggerInputTarget\x12\x15\n\x11\x44ITStrategyYellow\x10\x00\x12\x13\n\x0f\x44ITStrategyBlue\x10\x01\x12\x0e\n\nDITAutoref\x10\x02*\x95\x01\n\x14PauseSimulatorReason\x12\x06\n\x02Ui\x10\x01\x12\x0f\n\x0bWindowFocus\x10\x02\x12\x15\n\x11\x44\x65\x62ugBlueStrategy\x10\x03\x12\x17\n\x13\x44\x65\x62ugYellowStrategy\x10\x04\x12\x10\n\x0c\x44\x65\x62ugAutoref\x10\x05\x12\n\n\x06Replay\x10\x06\x12\t\n\x05Horus\x10\x07\x12\x0b\n\x07Logging\x10\x08\x42\x03\xf8\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001'
  _globals['_DEBUGGERINPUTTARGET']._serialized_start=4337
  _globals['_DEBUGGERINPUTTARGET']._serialized_end=4418
  _globals['_PAUSESIMULATORREASON']._serialized_start=4421
  _globals['_PAUSESIMULATORREASON']._serialized_end=4570
  _globals['_ROBOTMOVECOMMAND']._serialized_start=159
  _globals['_ROBOTMOVECOMMAND']._serialized_end=215
  _globals['_SIMULATORSETUP']._serialized_start=217
  _globals['_SIMULATORSETUP']._serialized_end=322
  _globals['_SIMULATORWORSTCASEVISION']._serialized_start=324
  _globals['_SIMULATORWORSTCASEVISION']._serialized_end=417
  _globals['_COMMANDSIMULATOR']._serialized_start=420
  _globals['_COMMANDSIMULATOR']._serialized_end=706
  _globals['_COMMANDREFEREE']._serialized_start=708
  _globals['_COMMANDREFEREE']._serialized_end=825
  _globals['_COMMANDSTRATEGYLOAD']._serialized_start=827
  _globals['_COMMANDSTRATEGYLOAD']._serialized_end=887
  _globals['_COMMANDSTRATEGYCLOSE']._serialized_start=889
  _globals['_COMMANDSTRATEGYCLOSE']._serialized_end=911
  _globals['_COMMANDSTRATEGYTRIGGERDEBUGGER']._serialized_start=913
  _globals['_COMMANDSTRATEGYTRIGGERDEBUGGER']._serialized_end=945
  _globals['_COMMANDSTRATEGY']._serialized_start=948
  _globals['_COMMANDSTRATEGY']._serialized_end=1270
  _globals['_COMMANDCONTROL']._serialized_start=1272
  _globals['_COMMANDCONTROL']._serialized_end=1327
  _globals['_TRANSCEIVERCONFIGURATION']._serialized_start=1329
  _globals['_TRANSCEIVERCONFIGURATION']._serialized_end=1372
  _globals['_HOSTADDRESS']._serialized_start=1374
  _globals['_HOSTADDRESS']._serialized_end=1415
  _globals['_SIMULATORNETWORKING']._serialized_start=1418
  _globals['_SIMULATORNETWORKING']._serialized_end=1552
  _globals['_COMMANDTRANSCEIVER']._serialized_start=1555
  _globals['_COMMANDTRANSCEIVER']._serialized_end=1793
  _globals['_VIRTUALFIELDTRANSFORM']._serialized_start=1795
  _globals['_VIRTUALFIELDTRANSFORM']._serialized_end=1904
  _globals['_COMMANDTRACKING']._serialized_start=1907
  _globals['_COMMANDTRACKING']._serialized_end=2213
  _globals['_COMMANDSTRATEGYCHANGEOPTION']._serialized_start=2215
  _globals['_COMMANDSTRATEGYCHANGEOPTION']._serialized_end=2273
  _globals['_COMMANDAMUN']._serialized_start=2276
  _globals['_COMMANDAMUN']._serialized_end=2412
  _globals['_COMMANDDEBUGGERINPUTDISABLE']._serialized_start=2414
  _globals['_COMMANDDEBUGGERINPUTDISABLE']._serialized_end=2443
  _globals['_COMMANDDEBUGGERINPUTLINE']._serialized_start=2445
  _globals['_COMMANDDEBUGGERINPUTLINE']._serialized_end=2485
  _globals['_COMMANDDEBUGGERINPUT']._serialized_start=2488
  _globals['_COMMANDDEBUGGERINPUT']._serialized_end=2664
  _globals['_PAUSESIMULATORCOMMAND']._serialized_start=2666
  _globals['_PAUSESIMULATORCOMMAND']._serialized_end=2764
  _globals['_COMMANDREPLAY']._serialized_start=2767
  _globals['_COMMANDREPLAY']._serialized_end=2954
  _globals['_FLAG']._serialized_start=2956
  _globals['_FLAG']._serialized_end=2962
  _globals['_COMMANDPLAYBACK']._serialized_start=2965
  _globals['_COMMANDPLAYBACK']._serialized_end=3309
  _globals['_COMMANDRECORD']._serialized_start=3312
  _globals['_COMMANDRECORD']._serialized_end=3492
  _globals['_COMMAND']._serialized_start=3495
  _globals['_COMMAND']._serialized_end=4335
# @@protoc_insertion_point(module_scope)
