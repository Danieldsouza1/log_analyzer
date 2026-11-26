RISKY_COMMANDS = {"rm", "kill", "mv", "cp", "mkdir"}

def is_risky(entry):
    first_word = entry.command.split()[0]
    return first_word in RISKY_COMMANDS 

def is_after_hours(entry):
    hour = entry.timestamp.hour
    return hour < 6 or hour >= 22