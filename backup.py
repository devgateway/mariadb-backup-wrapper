#!/usr/bin/python
# MariaDB backup/restore helper
# Copyright 2019, Development Gateway, GPL3+, see LICENSE

from __future__ import print_function
import logging, sys, os, argparse

log = None

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

def parse_args():
    ap = argparse.ArgumentParser(description = "Run MariaDB backups and upload to Glacier")
    group = ap.add_mutually_exclusive_group(required = True)
    group.add_argument("--backup",
            type = int,
            nargs = 1,
            metavar = "DAYS",
            dest = "period",
            help = "Back up with full/incremental cycle of DAYS")
    group.add_argument("--restore",
            action = "store_true",
            help = "Prepare and restore the latest backup")

    return ap.parse_args()

def get_paths():
    paths = {
        "TEMP_ROOT": "/var/tmp/mariadb-backup",
        "OUTPUT_DIR": "/var/spool/backup"
    }

    for var_name in paths:
        try:
            paths[var_name] = os.environ[var_name]
        except KeyError:
            pass

    return paths

def main():
    global log
    log = get_logger()
    args = parse_args()
    paths = get_paths()

    schedule = Schedule(
        backup_dir = paths["TEMP_ROOT"],
        output_dir = paths["OUTPUT_DIR"],
        retention_period = args.period)

if __name__ == "__main__":
    main()
