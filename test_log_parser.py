from log_parser import parse_line

def test_good_line_returns_entry():
    line = "2026-11-20 14:32:10 | alice | srv-db-01 | 10.0.0.5 | rm -rf /tmp/old"
    result = parse_line(line)

    assert result is not None
    assert result.user == "alice"
    assert result.command == "rm -rf /tmp/old"

def test_blank_line_returns_none():
    line = ""
    result = parse_line(line)

    assert result is None

def test_blank_line_space_returns_none():
    line = " "
    result = parse_line(line)

    assert result is None

def test_line_without_returns_entry():
    line = "2026-11-20 14:32:10 alice srv-db-01 10.0.0.5 rm -rf /tmp/old"
    result = parse_line(line)

    assert result is None

def test_line_withoutcommand_returns_entry():
    line = "2026-11-20 14:32:10 | alice | srv-db-01 | 10.0.0.5 |"
    result = parse_line(line)

    

def test_line_withoutuser_returns_entry():
    line = "2026-11-20 14:32:10 | | srv-db-01 | 10.0.0.5 | ls"
    result = parse_line(line)

    

def test_line_withoutserver_returns_entry():
    line = "2026-11-20 14:32:10 | alice | srv-db-01"
    result = parse_line(line)

    assert result is None
    

def test_line_withoutip_returns_entry():
    line = "2026-13-45 99:99:99 | erin | srv-db-03 | 10.0.4.14 | ls"
    result = parse_line(line)

    assert result is None
    
