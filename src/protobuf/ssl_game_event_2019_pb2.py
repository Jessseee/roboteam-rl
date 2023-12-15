# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssl_game_event_2019.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protobuf.ssl_game_controller_common_pb2 as ssl__game__controller__common__pb2
import protobuf.ssl_game_controller_geometry_pb2 as ssl__game__controller__geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19ssl_game_event_2019.proto\x12\x0egameController\x1a ssl_game_controller_common.proto\x1a\"ssl_game_controller_geometry.proto\"\x83K\n\tGameEvent\x12,\n\x04type\x18( \x01(\x0e\x32\x1e.gameController.GameEvent.Type\x12\x0e\n\x06origin\x18) \x03(\t\x12M\n\x1a\x62\x61ll_left_field_touch_line\x18\x06 \x01(\x0b\x32\'.gameController.GameEvent.BallLeftFieldH\x00\x12L\n\x19\x62\x61ll_left_field_goal_line\x18\x07 \x01(\x0b\x32\'.gameController.GameEvent.BallLeftFieldH\x00\x12=\n\x0c\x61imless_kick\x18\x0b \x01(\x0b\x32%.gameController.GameEvent.AimlessKickH\x00\x12\x65\n\"attacker_too_close_to_defense_area\x18\x13 \x01(\x0b\x32\x37.gameController.GameEvent.AttackerTooCloseToDefenseAreaH\x00\x12S\n\x18\x64\x65\x66\x65nder_in_defense_area\x18\x1f \x01(\x0b\x32/.gameController.GameEvent.DefenderInDefenseAreaH\x00\x12G\n\x11\x62oundary_crossing\x18+ \x01(\x0b\x32*.gameController.GameEvent.BoundaryCrossingH\x00\x12\x44\n\x10keeper_held_ball\x18\r \x01(\x0b\x32(.gameController.GameEvent.KeeperHeldBallH\x00\x12T\n\x19\x62ot_dribbled_ball_too_far\x18\x11 \x01(\x0b\x32/.gameController.GameEvent.BotDribbledBallTooFarH\x00\x12@\n\x0e\x62ot_pushed_bot\x18\x18 \x01(\x0b\x32&.gameController.GameEvent.BotPushedBotH\x00\x12W\n\x1a\x62ot_held_ball_deliberately\x18\x1a \x01(\x0b\x32\x31.gameController.GameEvent.BotHeldBallDeliberatelyH\x00\x12\x42\n\x0f\x62ot_tipped_over\x18\x1b \x01(\x0b\x32\'.gameController.GameEvent.BotTippedOverH\x00\x12k\n%attacker_touched_ball_in_defense_area\x18\x0f \x01(\x0b\x32:.gameController.GameEvent.AttackerTouchedBallInDefenseAreaH\x00\x12R\n\x18\x62ot_kicked_ball_too_fast\x18\x12 \x01(\x0b\x32..gameController.GameEvent.BotKickedBallTooFastH\x00\x12\x44\n\x10\x62ot_crash_unique\x18\x16 \x01(\x0b\x32(.gameController.GameEvent.BotCrashUniqueH\x00\x12\x42\n\x0f\x62ot_crash_drawn\x18\x15 \x01(\x0b\x32\'.gameController.GameEvent.BotCrashDrawnH\x00\x12\x61\n defender_too_close_to_kick_point\x18\x1d \x01(\x0b\x32\x35.gameController.GameEvent.DefenderTooCloseToKickPointH\x00\x12J\n\x14\x62ot_too_fast_in_stop\x18\x1c \x01(\x0b\x32*.gameController.GameEvent.BotTooFastInStopH\x00\x12T\n\x18\x62ot_interfered_placement\x18\x14 \x01(\x0b\x32\x30.gameController.GameEvent.BotInterferedPlacementH\x00\x12\x37\n\rpossible_goal\x18\' \x01(\x0b\x32\x1e.gameController.GameEvent.GoalH\x00\x12.\n\x04goal\x18\x08 \x01(\x0b\x32\x1e.gameController.GameEvent.GoalH\x00\x12\x36\n\x0cinvalid_goal\x18, \x01(\x0b\x32\x1e.gameController.GameEvent.GoalH\x00\x12[\n\x1c\x61ttacker_double_touched_ball\x18\x0e \x01(\x0b\x32\x33.gameController.GameEvent.AttackerDoubleTouchedBallH\x00\x12K\n\x13placement_succeeded\x18\x05 \x01(\x0b\x32,.gameController.GameEvent.PlacementSucceededH\x00\x12J\n\x13penalty_kick_failed\x18- \x01(\x0b\x32+.gameController.GameEvent.PenaltyKickFailedH\x00\x12I\n\x13no_progress_in_game\x18\x02 \x01(\x0b\x32*.gameController.GameEvent.NoProgressInGameH\x00\x12\x45\n\x10placement_failed\x18\x03 \x01(\x0b\x32).gameController.GameEvent.PlacementFailedH\x00\x12\x41\n\x0emultiple_cards\x18  \x01(\x0b\x32\'.gameController.GameEvent.MultipleCardsH\x00\x12\x41\n\x0emultiple_fouls\x18\" \x01(\x0b\x32\'.gameController.GameEvent.MultipleFoulsH\x00\x12\x45\n\x10\x62ot_substitution\x18% \x01(\x0b\x32).gameController.GameEvent.BotSubstitutionH\x00\x12\x42\n\x0ftoo_many_robots\x18& \x01(\x0b\x32\'.gameController.GameEvent.TooManyRobotsH\x00\x12\x41\n\x0e\x63hallenge_flag\x18. \x01(\x0b\x32\'.gameController.GameEvent.ChallengeFlagH\x00\x12\x41\n\x0e\x65mergency_stop\x18/ \x01(\x0b\x32\'.gameController.GameEvent.EmergencyStopH\x00\x12V\n\x19unsporting_behavior_minor\x18# \x01(\x0b\x32\x31.gameController.GameEvent.UnsportingBehaviorMinorH\x00\x12V\n\x19unsporting_behavior_major\x18$ \x01(\x0b\x32\x31.gameController.GameEvent.UnsportingBehaviorMajorH\x00\x12\x36\n\x08prepared\x18\x01 \x01(\x0b\x32\".gameController.GameEvent.PreparedH\x00\x12?\n\rindirect_goal\x18\t \x01(\x0b\x32&.gameController.GameEvent.IndirectGoalH\x00\x12=\n\x0c\x63hipped_goal\x18\n \x01(\x0b\x32%.gameController.GameEvent.ChippedGoalH\x00\x12=\n\x0ckick_timeout\x18\x0c \x01(\x0b\x32%.gameController.GameEvent.KickTimeoutH\x00\x12s\n)attacker_touched_opponent_in_defense_area\x18\x10 \x01(\x0b\x32>.gameController.GameEvent.AttackerTouchedOpponentInDefenseAreaH\x00\x12{\n1attacker_touched_opponent_in_defense_area_skipped\x18* \x01(\x0b\x32>.gameController.GameEvent.AttackerTouchedOpponentInDefenseAreaH\x00\x12L\n\x18\x62ot_crash_unique_skipped\x18\x17 \x01(\x0b\x32(.gameController.GameEvent.BotCrashUniqueH\x00\x12H\n\x16\x62ot_pushed_bot_skipped\x18\x19 \x01(\x0b\x32&.gameController.GameEvent.BotPushedBotH\x00\x12\x66\n\"defender_in_defense_area_partially\x18\x1e \x01(\x0b\x32\x38.gameController.GameEvent.DefenderInDefenseAreaPartiallyH\x00\x12Z\n\x1bmultiple_placement_failures\x18! \x01(\x0b\x32\x33.gameController.GameEvent.MultiplePlacementFailuresH\x00\x1aq\n\rBallLeftField\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x1a\x9f\x01\n\x0b\x41imlessKick\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12.\n\rkick_location\x18\x04 \x01(\x0b\x32\x17.gameController.Vector2\x1a\xab\x02\n\x04Goal\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12*\n\x0ckicking_team\x18\x06 \x01(\x0e\x32\x14.gameController.Team\x12\x13\n\x0bkicking_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12.\n\rkick_location\x18\x04 \x01(\x0b\x32\x17.gameController.Vector2\x12\x17\n\x0fmax_ball_height\x18\x05 \x01(\x02\x12\x1a\n\x12num_robots_by_team\x18\x07 \x01(\r\x12\x1a\n\x12last_touch_by_team\x18\x08 \x01(\x04\x12\x0f\n\x07message\x18\t \x01(\t\x1a\xa0\x01\n\x0cIndirectGoal\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12.\n\rkick_location\x18\x04 \x01(\x0b\x32\x17.gameController.Vector2\x1a\xb8\x01\n\x0b\x43hippedGoal\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12.\n\rkick_location\x18\x04 \x01(\x0b\x32\x17.gameController.Vector2\x12\x17\n\x0fmax_ball_height\x18\x05 \x01(\x02\x1a\x83\x01\n\x10\x42otTooFastInStop\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12\r\n\x05speed\x18\x04 \x01(\x02\x1a\x91\x01\n\x1b\x44\x65\x66\x65nderTooCloseToKickPoint\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12\x10\n\x08\x64istance\x18\x04 \x01(\x02\x1a\x9e\x01\n\rBotCrashDrawn\x12\x12\n\nbot_yellow\x18\x01 \x01(\r\x12\x10\n\x08\x62ot_blue\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12\x13\n\x0b\x63rash_speed\x18\x04 \x01(\x02\x12\x12\n\nspeed_diff\x18\x05 \x01(\x02\x12\x13\n\x0b\x63rash_angle\x18\x06 \x01(\x02\x1a\xc2\x01\n\x0e\x42otCrashUnique\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x10\n\x08violator\x18\x02 \x01(\r\x12\x0e\n\x06victim\x18\x03 \x01(\r\x12)\n\x08location\x18\x04 \x01(\x0b\x32\x17.gameController.Vector2\x12\x13\n\x0b\x63rash_speed\x18\x05 \x01(\x02\x12\x12\n\nspeed_diff\x18\x06 \x01(\x02\x12\x13\n\x0b\x63rash_angle\x18\x07 \x01(\x02\x1a\x9b\x01\n\x0c\x42otPushedBot\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x10\n\x08violator\x18\x02 \x01(\r\x12\x0e\n\x06victim\x18\x03 \x01(\r\x12)\n\x08location\x18\x04 \x01(\x0b\x32\x17.gameController.Vector2\x12\x17\n\x0fpushed_distance\x18\x05 \x01(\x02\x1a\xa1\x01\n\rBotTippedOver\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12.\n\rball_location\x18\x04 \x01(\x0b\x32\x17.gameController.Vector2\x1a\x8b\x01\n\x15\x44\x65\x66\x65nderInDefenseArea\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12\x10\n\x08\x64istance\x18\x04 \x01(\x02\x1a\xc4\x01\n\x1e\x44\x65\x66\x65nderInDefenseAreaPartially\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12\x10\n\x08\x64istance\x18\x04 \x01(\x02\x12.\n\rball_location\x18\x05 \x01(\x0b\x32\x17.gameController.Vector2\x1a\x96\x01\n AttackerTouchedBallInDefenseArea\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12\x10\n\x08\x64istance\x18\x04 \x01(\x02\x1a\xa5\x01\n\x14\x42otKickedBallTooFast\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12\x1a\n\x12initial_ball_speed\x18\x04 \x01(\x02\x12\x0f\n\x07\x63hipped\x18\x05 \x01(\x08\x1a\x9c\x01\n\x15\x42otDribbledBallTooFar\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12&\n\x05start\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12$\n\x03\x65nd\x18\x04 \x01(\x0b\x32\x17.gameController.Vector2\x1a\x98\x01\n$AttackerTouchedOpponentInDefenseArea\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12\x0e\n\x06victim\x18\x04 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x1a}\n\x19\x41ttackerDoubleTouchedBall\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x1a\xc3\x01\n\x1d\x41ttackerTooCloseToDefenseArea\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12\x10\n\x08\x64istance\x18\x04 \x01(\x02\x12.\n\rball_location\x18\x05 \x01(\x0b\x32\x17.gameController.Vector2\x1a\x8d\x01\n\x17\x42otHeldBallDeliberately\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x12\x10\n\x08\x64uration\x18\x04 \x01(\x02\x1az\n\x16\x42otInterferedPlacement\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06\x62y_bot\x18\x02 \x01(\r\x12)\n\x08location\x18\x03 \x01(\x0b\x32\x17.gameController.Vector2\x1a\x36\n\rMultipleCards\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x1a\x36\n\rMultipleFouls\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x1a\x42\n\x19MultiplePlacementFailures\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x1am\n\x0bKickTimeout\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12)\n\x08location\x18\x02 \x01(\x0b\x32\x17.gameController.Vector2\x12\x0c\n\x04time\x18\x03 \x01(\x02\x1aK\n\x10NoProgressInGame\x12)\n\x08location\x18\x01 \x01(\x0b\x32\x17.gameController.Vector2\x12\x0c\n\x04time\x18\x02 \x01(\x02\x1aT\n\x0fPlacementFailed\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x1a\n\x12remaining_distance\x18\x02 \x01(\x02\x1aP\n\x17UnsportingBehaviorMinor\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06reason\x18\x02 \x02(\t\x1aP\n\x17UnsportingBehaviorMajor\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x0e\n\x06reason\x18\x02 \x02(\t\x1at\n\x0eKeeperHeldBall\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12)\n\x08location\x18\x02 \x01(\x0b\x32\x17.gameController.Vector2\x12\x10\n\x08\x64uration\x18\x03 \x01(\x02\x1at\n\x12PlacementSucceeded\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x12\n\ntime_taken\x18\x02 \x01(\x02\x12\x11\n\tprecision\x18\x03 \x01(\x02\x12\x10\n\x08\x64istance\x18\x04 \x01(\x02\x1a\x1e\n\x08Prepared\x12\x12\n\ntime_taken\x18\x01 \x01(\x02\x1a\x38\n\x0f\x42otSubstitution\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x1a\x36\n\rChallengeFlag\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x1a\x36\n\rEmergencyStop\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x1a\x9f\x01\n\rTooManyRobots\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12\x1a\n\x12num_robots_allowed\x18\x02 \x01(\x05\x12\x1b\n\x13num_robots_on_field\x18\x03 \x01(\x05\x12.\n\rball_location\x18\x04 \x01(\x0b\x32\x17.gameController.Vector2\x1a\x64\n\x10\x42oundaryCrossing\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12)\n\x08location\x18\x02 \x01(\x0b\x32\x17.gameController.Vector2\x1a\x65\n\x11PenaltyKickFailed\x12%\n\x07\x62y_team\x18\x01 \x02(\x0e\x32\x14.gameController.Team\x12)\n\x08location\x18\x02 \x01(\x0b\x32\x17.gameController.Vector2\"\xba\t\n\x04Type\x12\x1b\n\x17UNKNOWN_GAME_EVENT_TYPE\x10\x00\x12\x1e\n\x1a\x42\x41LL_LEFT_FIELD_TOUCH_LINE\x10\x06\x12\x1d\n\x19\x42\x41LL_LEFT_FIELD_GOAL_LINE\x10\x07\x12\x10\n\x0c\x41IMLESS_KICK\x10\x0b\x12&\n\"ATTACKER_TOO_CLOSE_TO_DEFENSE_AREA\x10\x13\x12\x1c\n\x18\x44\x45\x46\x45NDER_IN_DEFENSE_AREA\x10\x1f\x12\x15\n\x11\x42OUNDARY_CROSSING\x10)\x12\x14\n\x10KEEPER_HELD_BALL\x10\r\x12\x1d\n\x19\x42OT_DRIBBLED_BALL_TOO_FAR\x10\x11\x12\x12\n\x0e\x42OT_PUSHED_BOT\x10\x18\x12\x1e\n\x1a\x42OT_HELD_BALL_DELIBERATELY\x10\x1a\x12\x13\n\x0f\x42OT_TIPPED_OVER\x10\x1b\x12)\n%ATTACKER_TOUCHED_BALL_IN_DEFENSE_AREA\x10\x0f\x12\x1c\n\x18\x42OT_KICKED_BALL_TOO_FAST\x10\x12\x12\x14\n\x10\x42OT_CRASH_UNIQUE\x10\x16\x12\x13\n\x0f\x42OT_CRASH_DRAWN\x10\x15\x12$\n DEFENDER_TOO_CLOSE_TO_KICK_POINT\x10\x1d\x12\x18\n\x14\x42OT_TOO_FAST_IN_STOP\x10\x1c\x12\x1c\n\x18\x42OT_INTERFERED_PLACEMENT\x10\x14\x12\x11\n\rPOSSIBLE_GOAL\x10\'\x12\x08\n\x04GOAL\x10\x08\x12\x10\n\x0cINVALID_GOAL\x10*\x12 \n\x1c\x41TTACKER_DOUBLE_TOUCHED_BALL\x10\x0e\x12\x17\n\x13PLACEMENT_SUCCEEDED\x10\x05\x12\x17\n\x13PENALTY_KICK_FAILED\x10+\x12\x17\n\x13NO_PROGRESS_IN_GAME\x10\x02\x12\x14\n\x10PLACEMENT_FAILED\x10\x03\x12\x12\n\x0eMULTIPLE_CARDS\x10 \x12\x12\n\x0eMULTIPLE_FOULS\x10\"\x12\x14\n\x10\x42OT_SUBSTITUTION\x10%\x12\x13\n\x0fTOO_MANY_ROBOTS\x10&\x12\x12\n\x0e\x43HALLENGE_FLAG\x10,\x12\x12\n\x0e\x45MERGENCY_STOP\x10-\x12\x1d\n\x19UNSPORTING_BEHAVIOR_MINOR\x10#\x12\x1d\n\x19UNSPORTING_BEHAVIOR_MAJOR\x10$\x12\x0c\n\x08PREPARED\x10\x01\x12\x11\n\rINDIRECT_GOAL\x10\t\x12\x10\n\x0c\x43HIPPED_GOAL\x10\n\x12\x10\n\x0cKICK_TIMEOUT\x10\x0c\x12-\n)ATTACKER_TOUCHED_OPPONENT_IN_DEFENSE_AREA\x10\x10\x12\x35\n1ATTACKER_TOUCHED_OPPONENT_IN_DEFENSE_AREA_SKIPPED\x10(\x12\x1c\n\x18\x42OT_CRASH_UNIQUE_SKIPPED\x10\x17\x12\x1a\n\x16\x42OT_PUSHED_BOT_SKIPPED\x10\x19\x12&\n\"DEFENDER_IN_DEFENSE_AREA_PARTIALLY\x10\x1e\x12\x1f\n\x1bMULTIPLE_PLACEMENT_FAILURES\x10!B\x07\n\x05\x65vent')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ssl_game_event_2019_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GAMEEVENT']._serialized_start=116
  _globals['_GAMEEVENT']._serialized_end=9719
  _globals['_GAMEEVENT_BALLLEFTFIELD']._serialized_start=3616
  _globals['_GAMEEVENT_BALLLEFTFIELD']._serialized_end=3729
  _globals['_GAMEEVENT_AIMLESSKICK']._serialized_start=3732
  _globals['_GAMEEVENT_AIMLESSKICK']._serialized_end=3891
  _globals['_GAMEEVENT_GOAL']._serialized_start=3894
  _globals['_GAMEEVENT_GOAL']._serialized_end=4193
  _globals['_GAMEEVENT_INDIRECTGOAL']._serialized_start=4196
  _globals['_GAMEEVENT_INDIRECTGOAL']._serialized_end=4356
  _globals['_GAMEEVENT_CHIPPEDGOAL']._serialized_start=4359
  _globals['_GAMEEVENT_CHIPPEDGOAL']._serialized_end=4543
  _globals['_GAMEEVENT_BOTTOOFASTINSTOP']._serialized_start=4546
  _globals['_GAMEEVENT_BOTTOOFASTINSTOP']._serialized_end=4677
  _globals['_GAMEEVENT_DEFENDERTOOCLOSETOKICKPOINT']._serialized_start=4680
  _globals['_GAMEEVENT_DEFENDERTOOCLOSETOKICKPOINT']._serialized_end=4825
  _globals['_GAMEEVENT_BOTCRASHDRAWN']._serialized_start=4828
  _globals['_GAMEEVENT_BOTCRASHDRAWN']._serialized_end=4986
  _globals['_GAMEEVENT_BOTCRASHUNIQUE']._serialized_start=4989
  _globals['_GAMEEVENT_BOTCRASHUNIQUE']._serialized_end=5183
  _globals['_GAMEEVENT_BOTPUSHEDBOT']._serialized_start=5186
  _globals['_GAMEEVENT_BOTPUSHEDBOT']._serialized_end=5341
  _globals['_GAMEEVENT_BOTTIPPEDOVER']._serialized_start=5344
  _globals['_GAMEEVENT_BOTTIPPEDOVER']._serialized_end=5505
  _globals['_GAMEEVENT_DEFENDERINDEFENSEAREA']._serialized_start=5508
  _globals['_GAMEEVENT_DEFENDERINDEFENSEAREA']._serialized_end=5647
  _globals['_GAMEEVENT_DEFENDERINDEFENSEAREAPARTIALLY']._serialized_start=5650
  _globals['_GAMEEVENT_DEFENDERINDEFENSEAREAPARTIALLY']._serialized_end=5846
  _globals['_GAMEEVENT_ATTACKERTOUCHEDBALLINDEFENSEAREA']._serialized_start=5849
  _globals['_GAMEEVENT_ATTACKERTOUCHEDBALLINDEFENSEAREA']._serialized_end=5999
  _globals['_GAMEEVENT_BOTKICKEDBALLTOOFAST']._serialized_start=6002
  _globals['_GAMEEVENT_BOTKICKEDBALLTOOFAST']._serialized_end=6167
  _globals['_GAMEEVENT_BOTDRIBBLEDBALLTOOFAR']._serialized_start=6170
  _globals['_GAMEEVENT_BOTDRIBBLEDBALLTOOFAR']._serialized_end=6326
  _globals['_GAMEEVENT_ATTACKERTOUCHEDOPPONENTINDEFENSEAREA']._serialized_start=6329
  _globals['_GAMEEVENT_ATTACKERTOUCHEDOPPONENTINDEFENSEAREA']._serialized_end=6481
  _globals['_GAMEEVENT_ATTACKERDOUBLETOUCHEDBALL']._serialized_start=6483
  _globals['_GAMEEVENT_ATTACKERDOUBLETOUCHEDBALL']._serialized_end=6608
  _globals['_GAMEEVENT_ATTACKERTOOCLOSETODEFENSEAREA']._serialized_start=6611
  _globals['_GAMEEVENT_ATTACKERTOOCLOSETODEFENSEAREA']._serialized_end=6806
  _globals['_GAMEEVENT_BOTHELDBALLDELIBERATELY']._serialized_start=6809
  _globals['_GAMEEVENT_BOTHELDBALLDELIBERATELY']._serialized_end=6950
  _globals['_GAMEEVENT_BOTINTERFEREDPLACEMENT']._serialized_start=6952
  _globals['_GAMEEVENT_BOTINTERFEREDPLACEMENT']._serialized_end=7074
  _globals['_GAMEEVENT_MULTIPLECARDS']._serialized_start=7076
  _globals['_GAMEEVENT_MULTIPLECARDS']._serialized_end=7130
  _globals['_GAMEEVENT_MULTIPLEFOULS']._serialized_start=7132
  _globals['_GAMEEVENT_MULTIPLEFOULS']._serialized_end=7186
  _globals['_GAMEEVENT_MULTIPLEPLACEMENTFAILURES']._serialized_start=7188
  _globals['_GAMEEVENT_MULTIPLEPLACEMENTFAILURES']._serialized_end=7254
  _globals['_GAMEEVENT_KICKTIMEOUT']._serialized_start=7256
  _globals['_GAMEEVENT_KICKTIMEOUT']._serialized_end=7365
  _globals['_GAMEEVENT_NOPROGRESSINGAME']._serialized_start=7367
  _globals['_GAMEEVENT_NOPROGRESSINGAME']._serialized_end=7442
  _globals['_GAMEEVENT_PLACEMENTFAILED']._serialized_start=7444
  _globals['_GAMEEVENT_PLACEMENTFAILED']._serialized_end=7528
  _globals['_GAMEEVENT_UNSPORTINGBEHAVIORMINOR']._serialized_start=7530
  _globals['_GAMEEVENT_UNSPORTINGBEHAVIORMINOR']._serialized_end=7610
  _globals['_GAMEEVENT_UNSPORTINGBEHAVIORMAJOR']._serialized_start=7612
  _globals['_GAMEEVENT_UNSPORTINGBEHAVIORMAJOR']._serialized_end=7692
  _globals['_GAMEEVENT_KEEPERHELDBALL']._serialized_start=7694
  _globals['_GAMEEVENT_KEEPERHELDBALL']._serialized_end=7810
  _globals['_GAMEEVENT_PLACEMENTSUCCEEDED']._serialized_start=7812
  _globals['_GAMEEVENT_PLACEMENTSUCCEEDED']._serialized_end=7928
  _globals['_GAMEEVENT_PREPARED']._serialized_start=7930
  _globals['_GAMEEVENT_PREPARED']._serialized_end=7960
  _globals['_GAMEEVENT_BOTSUBSTITUTION']._serialized_start=7962
  _globals['_GAMEEVENT_BOTSUBSTITUTION']._serialized_end=8018
  _globals['_GAMEEVENT_CHALLENGEFLAG']._serialized_start=8020
  _globals['_GAMEEVENT_CHALLENGEFLAG']._serialized_end=8074
  _globals['_GAMEEVENT_EMERGENCYSTOP']._serialized_start=8076
  _globals['_GAMEEVENT_EMERGENCYSTOP']._serialized_end=8130
  _globals['_GAMEEVENT_TOOMANYROBOTS']._serialized_start=8133
  _globals['_GAMEEVENT_TOOMANYROBOTS']._serialized_end=8292
  _globals['_GAMEEVENT_BOUNDARYCROSSING']._serialized_start=8294
  _globals['_GAMEEVENT_BOUNDARYCROSSING']._serialized_end=8394
  _globals['_GAMEEVENT_PENALTYKICKFAILED']._serialized_start=8396
  _globals['_GAMEEVENT_PENALTYKICKFAILED']._serialized_end=8497
  _globals['_GAMEEVENT_TYPE']._serialized_start=8500
  _globals['_GAMEEVENT_TYPE']._serialized_end=9710
# @@protoc_insertion_point(module_scope)
