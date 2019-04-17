#!/usr/bin/python
# MariaDB backup/restore helper
# Copyright 2019, Development Gateway, GPL3+, see LICENSE

from __future__ import print_function
import logging, sys, os, argparse

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

class FullBackup(Backup):
    def run(self):
        pass

class IncrementalBackup(Backup):
    def run(self):
        pass

class Schedule:
    def __init__(self, backup_dir, output_dir, retention_period):
        self._backup_dir = backup_dir
        self._output_dir = output_dir
        self._retention_period = retention_period

    def createBackup(self):
        pass

def get_logger():
    valid_levels = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]
    try:
        env_level = os.environ["LOG_LEVEL"]
        valid_levels.remove(env_level)
        level = getattr(logging, env_level)
    except KeyError:
        level = logging.WARNING
    except ValueError:
        msg = "Expected log level: %s, got: %s. Using default level WARNING." \
                % ("|".join(valid_levels), env_level)
        print(msg, file = sys.stderr)
        level = logging.WARNING

    logging.basicConfig(level = level)
    return logging.getLogger(__name__)

def main():
    log = get_logger()

    ap = argparse.ArgumentParser(description = "Run MariaDB backups and upload to Glacier")
    ap.add_argument("--retention",
            type = int,
            nargs = 1,
            required = True,
            metavar = "DAYS",
            help = "Retention period in days")

    args = ap.parse_args()

if __name__ == "__main__":
    main()
