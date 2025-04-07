# 🏀 Mississauga Adult Basketball Scraper

This project scrapes **Adult Drop-In Basketball** events from the [City of Mississauga ActiveMississauga site](https://anc.ca.apm.activecommunities.com/activemississauga/) and outputs the results into:

- A **structured JSON file** containing event details
- A **`.ics` calendar file** for importing into Google Calendar, Apple Calendar, Outlook, etc.

---

## 📸 Example Output

**`adult_basketball_events.json`**
```json
[
  {
    "title": "Drop In Adult Basketball",
    "location": "Clarkson CC Finch Auditorium/Gym",
    "datetime": "Apr 10, 2025 8:00 PM - 10:00 PM",
    "community_centre": "Clarkson Community Centre"
  },
  ...
]
