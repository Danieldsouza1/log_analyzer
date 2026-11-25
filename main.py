from log_parser import parse_line
 
# Initialize counters for the manager (the loop)
parsed = 0
skipped = 0

# 3. THE LOOP: The "manager" that reads the file line-by-line and keeps score
with open("data/logs.log", "r", encoding="utf-8") as logs:
    for log in logs:
        result = parse_line(log)

        if result is None:
            skipped += 1
        else:
            parsed += 1
            entry = result  # 'entry' is now our LogEntry object
            print(f"{entry.user} -> {entry.command}")

# Print final tallies
print(f"Total parsed: {parsed}")
print(f"Total skipped: {skipped}")