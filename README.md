# 🏀 Mississauga Community Centre Basketball Scraper

This project scrapes **Adult Drop-In Basketball** events from the [City of Mississauga Active Mississauga site](https://anc.ca.apm.activecommunities.com/activemississauga/calendars?onlineSiteId=0&no_scroll_top=true&defaultCalendarId=1&locationId=21,40,42,290,248,56,60,261,240,73,267,250,232,122,243,161,252,253,171,125,65,100,119,401,82,396,242,91,110,317,325,372,374&displayType=0&activityIds=90104,89535,89534,91079,75784,75954,76405,74464,106533,75953,76404,76406,105119&view=2) and outputs the results into:

- A **structured JSON file** containing event details
- A **`.ics` calendar file** for importing into Google Calendar, Apple Calendar, Outlook, etc.

---

## 📸 Example Output

```
[
  {
    "title": "Drop In Adult Basketball",
    "location": "Clarkson CC Finch Auditorium/Gym",
    "datetime": "Apr 10, 2025 8:00 PM - 10:00 PM",
    "community_centre": "Clarkson Community Centre"
  },
  ...
]
```

**`adult_basketball_events.ics`**
- Fully compatible iCalendar file with correctly formatted event times in **America/Toronto (Eastern Time)**.

---

## ⚙️ Requirements

- Python 3.9+
- [Playwright](https://playwright.dev/python/)
- [ics](https://pypi.org/project/ics/)

### Install Dependencies

```bash
# 1. Set up a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# 2. Install required packages
pip install playwright ics
playwright install
```

---

## 🏃‍♂️ Usage

### 1. Scrape Events

```bash
python scrape.py
```

This will generate `adult_basketball_events.json` with all Adult Basketball events from selected Mississauga community centres.

### 2. Generate Calendar

```bash
python generate_ics.py
```

This will produce `adult_basketball_events.ics`.

You can now import this file into your calendar app of choice.

---

## 🧠 How It Works

- Uses Playwright to dynamically load calendar pages for all Mississauga community centres.
- Filters for events with the title **"Drop In Adult Basketball"**.
- Parses event details (title, time, location, community centre).
- Outputs clean JSON and iCalendar files.

---

## 🗺️ Community Centres Covered

The script scrapes all major Mississauga recreation centres, including:

- Clarkson Community Centre
- Churchill Meadows CC
- Carmen Corbasson CC
- Meadowvale CC
- Mississauga Valley Gymnasium
- Malton CC
- Frank McKechnie CC
- Huron Park RC

…and many more!
