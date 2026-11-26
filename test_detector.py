from datetime import datetime
from log_parser import LogEntry
from detector import is_risky, is_after_hours


def make_entry(command):
    return LogEntry(datetime(2026, 11, 20, 14, 0, 0), "alice", "srv-db-01", "10.0.0.5", command)


def test_rm_is_risky():
    assert is_risky(make_entry("rm -rf /tmp/x")) is True


def test_ls_is_not_risky():
    assert is_risky(make_entry("ls -la")) is False


def test_cpupower_is_not_risky():
    assert is_risky(make_entry("cpupower frequency-info")) is False

def make_entry(command, hour=14):
    return LogEntry(datetime(2026, 11, 20, hour, 0, 0), "alice", "srv-db-01", "10.0.0.5", command)

def test_3am_is_after_hours():
    assert is_after_hours(make_entry("ls", hour=3)) is True

def test_14am_is_after_hours():
    assert is_after_hours(make_entry("ls", hour=14)) is False

def test_23am_is_after_hours():
    assert is_after_hours(make_entry("ls", hour=23)) is True

def test_6am_is_after_hours():
    assert is_after_hours(make_entry("ls", hour=6)) is False

