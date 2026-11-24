with open("data/logs.log", "r", encoding="utf-8") as logs:
    parsed = 0
    skipped = 0

    for log in logs:
        clean_log = log.strip()
 
        if not clean_log:
            skipped += 1
            continue

        parts = clean_log.split("|")
        try:
            user = parts[1].strip() 
            command = parts[4].strip()

        except IndexError as e:
            print(f"IndexError caught: {e}")
            skipped += 1
            continue

        if not user or not command:
            skipped += 1
            continue
        parsed += 1
        
        print(f"{user} -> {command}")
print(f"Total parsed: {parsed}")
print(f"Total skipped: {skipped}")
