from datetime import datetime

class LogEntry:
    def __init__(self, timestamp, user, server, ip, command):
        self.timestamp = timestamp
        self.user = user
        self.server = server
        self.ip = ip
        self.command = command

# 1. THE CLASS: A blueprint that bundles all 5 fields into a single "box" (object)



# 2. THE FUNCTION: The "clerk" that inspects and validates one raw line at a time
def parse_line(line):
    clean_line = line.strip()
    
    # Skip empty lines
    if not clean_line:
        return None

    parts = clean_line.split("|")
    
    try:
        # Validate timestamp and save it
        timestamp_str = parts[0].strip()
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        
        # Extract the rest of the fields
        user = parts[1].strip() 
        server = parts[2].strip()
        ip = parts[3].strip()
        command = parts[4].strip()
        
    except (ValueError, IndexError):
        return None

    # Check if critical text fields are empty
    if not user or not command:
        return None

    # If it passes all checks, pack everything into a LogEntry box and return it
    return LogEntry(timestamp, user, server, ip, command)