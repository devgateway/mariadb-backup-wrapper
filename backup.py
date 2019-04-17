#!/usr/bin/python
# MariaDB backup/restore helper
# Copyright 2019, Development Gateway, GPL3+, see LICENSE

class Backup:
    def __init__(self, directory, parent = None):
        self._directory = directory
        self._parent = parent

    def run(self):
        raise NotImplementedError()

    def upload(self, boto):
        pass

    def cleanUp(self):
        pass

    def delete(self):
        pass

    def prepare(self):
        pass

class Schedule:
    def __init__(self, backup_dir, output_dir, retention_period):
        self._backup_dir = backup_dir
        self._output_dir = output_dir
        self._retention_period = retention_period

    def createBackup(self):
        pass
