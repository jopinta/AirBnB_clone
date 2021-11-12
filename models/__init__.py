#!/usr/bin/python3
""" add the init storage"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
