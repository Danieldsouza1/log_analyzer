from log_parser import parse_line
from detector import is_risky
from detector import is_risky, is_after_hours

# Initialize counters for the manager (the loop)
parsed = 0
skipped = 0
entries = []

# 3. THE LOOP: The "manager" that reads the file line-by-line and keeps score
with open("data/logs.log", "r", encoding="utf-8") as logs:
    for log in logs:
        result = parse_line(log)

        if result is None:
            skipped += 1
        else:
            parsed += 1
            entry = result
            entries.append(entry)  # 'entry' is now our LogEntry object
            

for entry in entries:
    if is_risky(entry):
        print(entry.user, entry.command)

print("After-hours activity:")
for entry in entries:
    if is_after_hours(entry):
        print(entry.timestamp, entry.user, entry.command)
        
# Print final tallies
print(f"Total parsed: {parsed}")
print(f"Total skipped: {skipped}")