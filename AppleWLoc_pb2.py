# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AppleWLoc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AppleWLoc.proto',
  package='',
  serialized_pb=_b('\n\x0f\x41ppleWLoc.proto\"\x81\x03\n\nWifiDevice\x12\r\n\x05\x62ssid\x18\x01 \x02(\t\x12&\n\x08location\x18\x02 \x01(\x0b\x32\x14.WifiDevice.Location\x1a\xbb\x02\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x03\x12\x11\n\tlongitude\x18\x02 \x01(\x03\x12\x16\n\x0eunknown_value3\x18\x03 \x01(\x03\x12\x16\n\x0eunknown_value4\x18\x04 \x01(\x03\x12\x16\n\x0eunknown_value5\x18\x05 \x01(\x03\x12\x16\n\x0eunknown_value6\x18\x06 \x01(\x03\x12\x16\n\x0eunknown_value7\x18\x07 \x01(\x03\x12\x16\n\x0eunknown_value8\x18\x08 \x01(\x03\x12\x16\n\x0eunknown_value9\x18\t \x01(\x03\x12\x17\n\x0funknown_value10\x18\n \x01(\x03\x12\x17\n\x0funknown_value11\x18\x0b \x01(\x03\x12\x17\n\x0funknown_value12\x18\x0c \x01(\x03\x12\x17\n\x0funknown_value21\x18\x15 \x01(\x03\"\xa5\x01\n\tAppleWLoc\x12\x16\n\x0eunknown_value0\x18\x01 \x01(\x03\x12!\n\x0cwifi_devices\x18\x02 \x03(\x0b\x32\x0b.WifiDevice\x12\x16\n\x0eunknown_value1\x18\x03 \x01(\x05\x12\x1c\n\x14return_single_result\x18\x04 \x01(\x05\x12\x0f\n\x07\x41PIName\x18\x05 \x01(\t\x12\x16\n\x0eunknown_value2\x18\x06 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_WIFIDEVICE_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='WifiDevice.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='WifiDevice.Location.latitude', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='WifiDevice.Location.longitude', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value3', full_name='WifiDevice.Location.unknown_value3', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value4', full_name='WifiDevice.Location.unknown_value4', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value5', full_name='WifiDevice.Location.unknown_value5', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value6', full_name='WifiDevice.Location.unknown_value6', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value7', full_name='WifiDevice.Location.unknown_value7', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value8', full_name='WifiDevice.Location.unknown_value8', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value9', full_name='WifiDevice.Location.unknown_value9', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value10', full_name='WifiDevice.Location.unknown_value10', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value11', full_name='WifiDevice.Location.unknown_value11', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value12', full_name='WifiDevice.Location.unknown_value12', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value21', full_name='WifiDevice.Location.unknown_value21', index=12,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=405,
)

_WIFIDEVICE = _descriptor.Descriptor(
  name='WifiDevice',
  full_name='WifiDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bssid', full_name='WifiDevice.bssid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='WifiDevice.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WIFIDEVICE_LOCATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=405,
)


_APPLEWLOC = _descriptor.Descriptor(
  name='AppleWLoc',
  full_name='AppleWLoc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown_value0', full_name='AppleWLoc.unknown_value0', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wifi_devices', full_name='AppleWLoc.wifi_devices', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value1', full_name='AppleWLoc.unknown_value1', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='return_single_result', full_name='AppleWLoc.return_single_result', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='APIName', full_name='AppleWLoc.APIName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_value2', full_name='AppleWLoc.unknown_value2', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=408,
  serialized_end=573,
)

_WIFIDEVICE_LOCATION.containing_type = _WIFIDEVICE
_WIFIDEVICE.fields_by_name['location'].message_type = _WIFIDEVICE_LOCATION
_APPLEWLOC.fields_by_name['wifi_devices'].message_type = _WIFIDEVICE
DESCRIPTOR.message_types_by_name['WifiDevice'] = _WIFIDEVICE
DESCRIPTOR.message_types_by_name['AppleWLoc'] = _APPLEWLOC

WifiDevice = _reflection.GeneratedProtocolMessageType('WifiDevice', (_message.Message,), dict(

  Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
    DESCRIPTOR = _WIFIDEVICE_LOCATION,
    __module__ = 'AppleWLoc_pb2'
    # @@protoc_insertion_point(class_scope:WifiDevice.Location)
    ))
  ,
  DESCRIPTOR = _WIFIDEVICE,
  __module__ = 'AppleWLoc_pb2'
  # @@protoc_insertion_point(class_scope:WifiDevice)
  ))
_sym_db.RegisterMessage(WifiDevice)
_sym_db.RegisterMessage(WifiDevice.Location)

AppleWLoc = _reflection.GeneratedProtocolMessageType('AppleWLoc', (_message.Message,), dict(
  DESCRIPTOR = _APPLEWLOC,
  __module__ = 'AppleWLoc_pb2'
  # @@protoc_insertion_point(class_scope:AppleWLoc)
  ))
_sym_db.RegisterMessage(AppleWLoc)


# @@protoc_insertion_point(module_scope)