# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logfile.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rlogfile.proto\x12\x07logfile\"*\n\x08UidEntry\x12\x0c\n\x04hash\x18\x01 \x02(\t\x12\x10\n\x05\x66lags\x18\x02 \x01(\r:\x01\x30\"\'\n\x03Uid\x12 \n\x05parts\x18\x01 \x03(\x0b\x32\x11.logfile.UidEntry\"\x1a\n\nLogRequest\x12\x0c\n\x04path\x18\x01 \x02(\t\"\xa5\x01\n\rLogOfferEntry\x12\x0c\n\x04name\x18\x01 \x02(\t\x12/\n\x07quality\x18\x02 \x02(\x0e\x32\x1e.logfile.LogOfferEntry.QUALITY\x12 \n\x03uri\x18\x03 \x02(\x0b\x32\x13.logfile.LogRequest\"3\n\x07QUALITY\x12\x0b\n\x07PERFECT\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\x12\x0e\n\nUNREADABLE\x10\x03\"3\n\x08LogOffer\x12\'\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x16.logfile.LogOfferEntryB\x03\xf8\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'logfile_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001'
  _globals['_UIDENTRY']._serialized_start=26
  _globals['_UIDENTRY']._serialized_end=68
  _globals['_UID']._serialized_start=70
  _globals['_UID']._serialized_end=109
  _globals['_LOGREQUEST']._serialized_start=111
  _globals['_LOGREQUEST']._serialized_end=137
  _globals['_LOGOFFERENTRY']._serialized_start=140
  _globals['_LOGOFFERENTRY']._serialized_end=305
  _globals['_LOGOFFERENTRY_QUALITY']._serialized_start=254
  _globals['_LOGOFFERENTRY_QUALITY']._serialized_end=305
  _globals['_LOGOFFER']._serialized_start=307
  _globals['_LOGOFFER']._serialized_end=358
# @@protoc_insertion_point(module_scope)
