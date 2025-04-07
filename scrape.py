import json
import re
from playwright.sync_api import sync_playwright

# URL that includes all locations and filters for Adult Basketball
URL = "https://anc.ca.apm.activecommunities.com/activemississauga/calendars?onlineSiteId=0&no_scroll_top=true&defaultCalendarId=1&locationId=21,40,42,290,248,56,60,261,240,73,267,250,232,122,243,161,252,253,171,125,65,100,119,401,82,396,242,91,110,317,325,372,374&displayType=0&activityIds=90104,89535,89534,91079,75784,75954,76405,74464,106533,75953,76404,76406,105119&view=2"

def extract_event_info(event):
    aria_label = event.get_attribute("aria-label")
    if not aria_label or "Drop In Adult Basketball" not in aria_label:
        return None

    try:
        # Extract datetime
        datetime_match = re.search(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, 2025 \d{1,2}:\d{2} [AP]M - \d{1,2}:\d{2} [AP]M", aria_label)
        datetime_value = datetime_match.group(0) if datetime_match else "Unknown"

        # Extract location (everything after the title)
        location_part = aria_label.split("Drop In Adult Basketball")[-1].strip()

        # Extract cleaned community centre name
        centre_match = re.search(r"Center (.*?) Community Centre", aria_label)
        community_centre = f"{centre_match.group(1).strip()} Community Centre" if centre_match else "Unknown"

        return {
            "title": "Drop In Adult Basketball",
            "location": location_part,
            "datetime": datetime_value,
            "community_centre": community_centre
        }

    except Exception as e:
        print(f"⚠️ Failed to parse event: {e}")
        return None

def main():
    print("🚀 Launching browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)

        print("⏳ Waiting for event elements to load...")
        page.wait_for_selector("a.fc-timegrid-event", timeout=15000)

        events = page.query_selector_all("a.fc-timegrid-event")
        print(f"🔍 Found {len(events)} total events")

        basketball_events = []
        for event in events:
            result = extract_event_info(event)
            if result:
                basketball_events.append(result)

        print(f"🏀 Found {len(basketball_events)} adult basketball events")

        # Save results to JSON
        with open("adult_basketball_events.json", "w") as f:
            json.dump(basketball_events, f, indent=2)

        print("✅ Data saved to adult_basketball_events.json")

        browser.close()

if __name__ == "__main__":
    main()
