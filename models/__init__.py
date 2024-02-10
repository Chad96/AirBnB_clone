#!/usr/bin/python3
"""Module for initializing the storage variable"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
