def parse_line(line):
    """Takes a single raw log line, validates it, and returns 
       (user, command) if valid, or None if invalid."""
    clean_line = line.strip()
    
    # 1. Skip empty lines
    if not clean_line:
        return None

    parts = clean_line.split("|")
    
    try:
        # 2. Validate timestamp format
        timestamp_str = parts[0].strip()
        datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        
        # 3. Extract fields
        user = parts[1].strip() 
        server = parts[2].strip()
        ip = parts[3].strip()
        command = parts[4].strip()
        
    except ValueError, IndexError:
        return None

    # 4. Check if extracted fields are empty strings
    if not user or not command:
        return None

    # If it passes everything, return the valid data tuple
    return LogEntry(timestamp, user, server, ip, command)


# Initialize counters
parsed = 0
skipped = 0

# Process the log file
with open("data/logs.log", "r", encoding="utf-8") as logs:
    for log in logs:
        result = parse_line(log)

        if result is None:
            skipped += 1
        else:
            parsed += 1
            entry = result
            print(f"{entry.user} -> {entry.command}")

# Print final tallies
print(f"Total parsed: {parsed}")
print(f"Total skipped: {skipped}")

class LogEntry:
    def __init__(self, timestamp, user, server, ip, command):
        self.timestamp = timestamp
        self.user = user
        self.server = server
        self.ip = ip
        self.command = command  
        pass