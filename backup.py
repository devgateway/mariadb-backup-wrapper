#!/usr/bin/python
# MariaDB backup/restore helper
# Copyright 2019, Development Gateway, GPL3+, see LICENSE

class Schedule:
    def __init__(self, backup_dir, output_dir, retention_period):
        self._backup_dir = backup_dir
        self._output_dir = output_dir
        self._retention_period = retention_period

    def createBackup(self):
        pass
