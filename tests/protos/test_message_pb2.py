# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12test_message.proto\x12\x06mlflow\"\xb9\t\n\rSampleMessage\x12\x13\n\x0b\x66ield_int32\x18\x01 \x01(\x05\x12\x13\n\x0b\x66ield_int64\x18\x02 \x01(\x03\x12\x14\n\x0c\x66ield_uint32\x18\x03 \x01(\r\x12\x14\n\x0c\x66ield_uint64\x18\x04 \x01(\x04\x12\x14\n\x0c\x66ield_sint32\x18\x05 \x01(\x11\x12\x14\n\x0c\x66ield_sint64\x18\x06 \x01(\x12\x12\x15\n\rfield_fixed32\x18\x07 \x01(\x07\x12\x15\n\rfield_fixed64\x18\x08 \x01(\x06\x12\x16\n\x0e\x66ield_sfixed32\x18\t \x01(\x0f\x12\x16\n\x0e\x66ield_sfixed64\x18\n \x01(\x10\x12\x12\n\nfield_bool\x18\x0b \x01(\x08\x12\x14\n\x0c\x66ield_string\x18\x0c \x01(\t\x12 \n\x13\x66ield_with_default1\x18\r \x01(\x03:\x03\x31\x30\x30\x12 \n\x13\x66ield_with_default2\x18\x0e \x01(\x03:\x03\x32\x30\x30\x12\x1c\n\x14\x66ield_repeated_int64\x18\x0f \x03(\x03\x12\x34\n\nfield_enum\x18\x10 \x01(\x0e\x32 .mlflow.SampleMessage.SampleEnum\x12\x45\n\x13\x66ield_inner_message\x18\x11 \x03(\x0b\x32(.mlflow.SampleMessage.SampleInnerMessage\x12\x10\n\x06oneof1\x18\x12 \x01(\x03H\x00\x12\x10\n\x06oneof2\x18\x13 \x01(\x03H\x00\x12\x38\n\nfield_map1\x18\x14 \x03(\x0b\x32$.mlflow.SampleMessage.FieldMap1Entry\x12\x38\n\nfield_map2\x18\x15 \x03(\x0b\x32$.mlflow.SampleMessage.FieldMap2Entry\x12\x38\n\nfield_map3\x18\x16 \x03(\x0b\x32$.mlflow.SampleMessage.FieldMap3Entry\x12\x38\n\nfield_map4\x18\x17 \x03(\x0b\x32$.mlflow.SampleMessage.FieldMap4Entry\x1ao\n\x12SampleInnerMessage\x12\x19\n\x11\x66ield_inner_int64\x18\x01 \x01(\x03\x12\"\n\x1a\x66ield_inner_repeated_int64\x18\x02 \x03(\x03\x12\x1a\n\x12\x66ield_inner_string\x18\x03 \x01(\t\x1a\x30\n\x0e\x46ieldMap1Entry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x30\n\x0e\x46ieldMap2Entry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x30\n\x0e\x46ieldMap3Entry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1aZ\n\x0e\x46ieldMap4Entry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.mlflow.SampleMessage.SampleInnerMessage:\x02\x38\x01\"8\n\nSampleEnum\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0b\x45NUM_VALUE1\x10\x01\x12\x0f\n\x0b\x45NUM_VALUE2\x10\x02*\x06\x08\xe8\x07\x10\xd0\x0f\x42\x0e\n\x0csample_oneof\"H\n\x10\x45xtensionMessage24\n\x14\x66ield_extended_int64\x12\x15.mlflow.SampleMessage\x18\xe9\x07 \x01(\x03')



_SAMPLEMESSAGE = DESCRIPTOR.message_types_by_name['SampleMessage']
_SAMPLEMESSAGE_SAMPLEINNERMESSAGE = _SAMPLEMESSAGE.nested_types_by_name['SampleInnerMessage']
_SAMPLEMESSAGE_FIELDMAP1ENTRY = _SAMPLEMESSAGE.nested_types_by_name['FieldMap1Entry']
_SAMPLEMESSAGE_FIELDMAP2ENTRY = _SAMPLEMESSAGE.nested_types_by_name['FieldMap2Entry']
_SAMPLEMESSAGE_FIELDMAP3ENTRY = _SAMPLEMESSAGE.nested_types_by_name['FieldMap3Entry']
_SAMPLEMESSAGE_FIELDMAP4ENTRY = _SAMPLEMESSAGE.nested_types_by_name['FieldMap4Entry']
_EXTENSIONMESSAGE = DESCRIPTOR.message_types_by_name['ExtensionMessage']
_SAMPLEMESSAGE_SAMPLEENUM = _SAMPLEMESSAGE.enum_types_by_name['SampleEnum']
SampleMessage = _reflection.GeneratedProtocolMessageType('SampleMessage', (_message.Message,), {

  'SampleInnerMessage' : _reflection.GeneratedProtocolMessageType('SampleInnerMessage', (_message.Message,), {
    'DESCRIPTOR' : _SAMPLEMESSAGE_SAMPLEINNERMESSAGE,
    '__module__' : 'test_message_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.SampleMessage.SampleInnerMessage)
    })
  ,

  'FieldMap1Entry' : _reflection.GeneratedProtocolMessageType('FieldMap1Entry', (_message.Message,), {
    'DESCRIPTOR' : _SAMPLEMESSAGE_FIELDMAP1ENTRY,
    '__module__' : 'test_message_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.SampleMessage.FieldMap1Entry)
    })
  ,

  'FieldMap2Entry' : _reflection.GeneratedProtocolMessageType('FieldMap2Entry', (_message.Message,), {
    'DESCRIPTOR' : _SAMPLEMESSAGE_FIELDMAP2ENTRY,
    '__module__' : 'test_message_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.SampleMessage.FieldMap2Entry)
    })
  ,

  'FieldMap3Entry' : _reflection.GeneratedProtocolMessageType('FieldMap3Entry', (_message.Message,), {
    'DESCRIPTOR' : _SAMPLEMESSAGE_FIELDMAP3ENTRY,
    '__module__' : 'test_message_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.SampleMessage.FieldMap3Entry)
    })
  ,

  'FieldMap4Entry' : _reflection.GeneratedProtocolMessageType('FieldMap4Entry', (_message.Message,), {
    'DESCRIPTOR' : _SAMPLEMESSAGE_FIELDMAP4ENTRY,
    '__module__' : 'test_message_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.SampleMessage.FieldMap4Entry)
    })
  ,
  'DESCRIPTOR' : _SAMPLEMESSAGE,
  '__module__' : 'test_message_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.SampleMessage)
  })
_sym_db.RegisterMessage(SampleMessage)
_sym_db.RegisterMessage(SampleMessage.SampleInnerMessage)
_sym_db.RegisterMessage(SampleMessage.FieldMap1Entry)
_sym_db.RegisterMessage(SampleMessage.FieldMap2Entry)
_sym_db.RegisterMessage(SampleMessage.FieldMap3Entry)
_sym_db.RegisterMessage(SampleMessage.FieldMap4Entry)

ExtensionMessage = _reflection.GeneratedProtocolMessageType('ExtensionMessage', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONMESSAGE,
  '__module__' : 'test_message_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ExtensionMessage)
  })
_sym_db.RegisterMessage(ExtensionMessage)

if _descriptor._USE_C_DESCRIPTORS == False:
  SampleMessage.RegisterExtension(_EXTENSIONMESSAGE.extensions_by_name['field_extended_int64'])

  DESCRIPTOR._options = None
  _SAMPLEMESSAGE_FIELDMAP1ENTRY._options = None
  _SAMPLEMESSAGE_FIELDMAP1ENTRY._serialized_options = b'8\001'
  _SAMPLEMESSAGE_FIELDMAP2ENTRY._options = None
  _SAMPLEMESSAGE_FIELDMAP2ENTRY._serialized_options = b'8\001'
  _SAMPLEMESSAGE_FIELDMAP3ENTRY._options = None
  _SAMPLEMESSAGE_FIELDMAP3ENTRY._serialized_options = b'8\001'
  _SAMPLEMESSAGE_FIELDMAP4ENTRY._options = None
  _SAMPLEMESSAGE_FIELDMAP4ENTRY._serialized_options = b'8\001'
  _SAMPLEMESSAGE._serialized_start=31
  _SAMPLEMESSAGE._serialized_end=1240
  _SAMPLEMESSAGE_SAMPLEINNERMESSAGE._serialized_start=805
  _SAMPLEMESSAGE_SAMPLEINNERMESSAGE._serialized_end=916
  _SAMPLEMESSAGE_FIELDMAP1ENTRY._serialized_start=918
  _SAMPLEMESSAGE_FIELDMAP1ENTRY._serialized_end=966
  _SAMPLEMESSAGE_FIELDMAP2ENTRY._serialized_start=968
  _SAMPLEMESSAGE_FIELDMAP2ENTRY._serialized_end=1016
  _SAMPLEMESSAGE_FIELDMAP3ENTRY._serialized_start=1018
  _SAMPLEMESSAGE_FIELDMAP3ENTRY._serialized_end=1066
  _SAMPLEMESSAGE_FIELDMAP4ENTRY._serialized_start=1068
  _SAMPLEMESSAGE_FIELDMAP4ENTRY._serialized_end=1158
  _SAMPLEMESSAGE_SAMPLEENUM._serialized_start=1160
  _SAMPLEMESSAGE_SAMPLEENUM._serialized_end=1216
  _EXTENSIONMESSAGE._serialized_start=1242
  _EXTENSIONMESSAGE._serialized_end=1314
# @@protoc_insertion_point(module_scope)