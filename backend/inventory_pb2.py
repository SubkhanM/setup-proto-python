# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finventory.proto\"h\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x13\n\x0b\x65xpiry_date\x18\x05 \x01(\t\x12\r\n\x05price\x18\x06 \x01(\x03\" \n\x08ItemList\x12\x14\n\x05items\x18\x01 \x03(\x0b\x32\x05.Item\"\x14\n\x06ItemId\x12\n\n\x02id\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\xad\x01\n\x10InventoryService\x12\x19\n\x07\x41\x64\x64Item\x12\x05.Item\x1a\x05.Item\"\x00\x12\"\n\x0bGetAllItems\x12\x06.Empty\x1a\t.ItemList\"\x00\x12\x1b\n\x07GetItem\x12\x07.ItemId\x1a\x05.Item\"\x00\x12\x1c\n\nUpdateItem\x12\x05.Item\x1a\x05.Item\"\x00\x12\x1f\n\nDeleteItem\x12\x07.ItemId\x1a\x06.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ITEM']._serialized_start=19
  _globals['_ITEM']._serialized_end=123
  _globals['_ITEMLIST']._serialized_start=125
  _globals['_ITEMLIST']._serialized_end=157
  _globals['_ITEMID']._serialized_start=159
  _globals['_ITEMID']._serialized_end=179
  _globals['_EMPTY']._serialized_start=181
  _globals['_EMPTY']._serialized_end=188
  _globals['_INVENTORYSERVICE']._serialized_start=191
  _globals['_INVENTORYSERVICE']._serialized_end=364
# @@protoc_insertion_point(module_scope)
