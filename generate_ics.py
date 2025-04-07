import json
from datetime import datetime
from ics import Calendar, Event
from zoneinfo import ZoneInfo  # Requires Python 3.9+

INPUT_FILE = "adult_basketball_events.json"
OUTPUT_FILE = "adult_basketball_events.ics"
LOCAL_TZ = ZoneInfo("America/Toronto")

def parse_datetime(raw):
    """
    Converts a string like 'Apr 10, 2025 8:00 PM - 10:00 PM' into (start, end) datetime objects with timezone.
    """
    try:
        parts = raw.split(" - ")
        start_str = parts[0]
        end_str = parts[1]

        # Start has full date
        start_dt = datetime.strptime(start_str, "%b %d, %Y %I:%M %p").replace(tzinfo=LOCAL_TZ)

        # End only has time, reuse start date
        end_time = datetime.strptime(end_str, "%I:%M %p")
        end_dt = start_dt.replace(hour=end_time.hour, minute=end_time.minute)

        return start_dt, end_dt
    except Exception as e:
        print(f"⚠️ Failed to parse datetime: {raw} — {e}")
        return None, None

def main():
    print("📂 Loading event data...")
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    calendar = Calendar()

    for item in data:
        title = item["title"]
        location = item["location"]
        raw_datetime = item["datetime"]
        community_centre = item["community_centre"]

        start, end = parse_datetime(raw_datetime)
        if not start or not end:
            continue

        event = Event()
        event.name = f"{title} @ {community_centre}"
        event.begin = start
        event.end = end
        event.location = location
        event.description = f"{title} at {location}"

        calendar.events.add(event)

    with open(OUTPUT_FILE, "w") as f:
        f.writelines(calendar)

    print(f"✅ iCalendar file saved as {OUTPUT_FILE} with Eastern Time zone.")

if __name__ == "__main__":
    main()
