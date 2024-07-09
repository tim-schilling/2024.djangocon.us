import datetime
import json
from pathlib import Path
import zoneinfo

REPO_ROOT = Path(__file__).parent.parent
SITE_JSON_FILE = REPO_ROOT / "src" / "_data" / "site.json"
SITE_JSON = json.loads(SITE_JSON_FILE.read_text())
CONFERENCE_TZ = zoneinfo.ZoneInfo(SITE_JSON["timezone"])
CONFERENCE_YEAR = SITE_JSON["conf_year"]

TUTORIAL_DAY = datetime.date(CONFERENCE_YEAR, 9, 22)
TALK_DAY_1 = datetime.date(CONFERENCE_YEAR, 9, 23)
TALK_DAY_2 = datetime.date(CONFERENCE_YEAR, 9, 24)
TALK_DAY_3 = datetime.date(CONFERENCE_YEAR, 9, 25)
SPRINTS_DAY_1 = datetime.date(CONFERENCE_YEAR, 9, 26)
SPRINTS_DAY_2 = datetime.date(CONFERENCE_YEAR, 9, 27)

SMALL_TALK_ROOM = "Grand Ballroom III"
LARGE_TALK_ROOM = "Junior Ballroom"

LUNCH_ROOM = "Grand Ballroom I/II"

LACTATION_ROOM = "Meeting Room 1"
QUIET_ROOM = "Meeting Room 4"
GREEN_ROOM = "Meeting Room 2"

TUTORIAL_TRACK_A_ROOM = "Tutorial Track A (TBD)"
TUTORIAL_TRACK_B_ROOM = "Tutorial Track B (TBD)"
TUTORIAL_TRACK_C_ROOM = "Tutorial Track C (TBD)"

# TODO once the childcare post is live: update this with the relative
# link to that post
LACTATION_BLOG_POST_LINK = None

# TODO once catering menus are live: update this with the blog post
CATERING_MENU_LINK = None

if CATERING_MENU_LINK:
    SUNDAY_BREAKFAST_LINK = f"{CATERING_MENU_LINK}/#sunday-breakfast"
    MONDAY_BREAKFAST_LINK = f"{CATERING_MENU_LINK}/#monday-breakfast"
    TUESDAY_BREAKFAST_LINK = f"{CATERING_MENU_LINK}/#tuesday-breakfast"
    WEDNESDAY_BREAKFAST_LINK = f"{CATERING_MENU_LINK}/#wednesday-breakfast"
    MONDAY_MORNING_BREAK_LINK = f"{CATERING_MENU_LINK}/#monday-morning-break"
    TUESDAY_MORNING_BREAK_LINK = f"{CATERING_MENU_LINK}/#tuesday-morning-break"
    WEDNESDAY_MORNING_BREAK_LINK = f"{CATERING_MENU_LINK}/#wednesday-morning-break"
    SUNDAY_LUNCH_LINK = f"{CATERING_MENU_LINK}/#sunday-lunch"
    MONDAY_LUNCH_LINK = f"{CATERING_MENU_LINK}/#monday-lunch"
    TUESDAY_LUNCH_LINK = f"{CATERING_MENU_LINK}/#tuesday-lunch"
    WEDNESDAY_LUNCH_LINK = f"{CATERING_MENU_LINK}/#wednesday-lunch"
    MONDAY_AFTERNOON_BREAK_LINK = f"{CATERING_MENU_LINK}/#monday-afternoon-break"
    TUESDAY_AFTERNOON_BREAK_LINK = f"{CATERING_MENU_LINK}/#tuesday-afternoon-break"
    WEDNESDAY_AFTERNOON_BREAK_LINK = f"{CATERING_MENU_LINK}/#wednesday-afternoon-break"
else:
    SUNDAY_BREAKFAST_LINK = None
    MONDAY_BREAKFAST_LINK = None
    TUESDAY_BREAKFAST_LINK = None
    WEDNESDAY_BREAKFAST_LINK = None
    MONDAY_MORNING_BREAK_LINK = None
    TUESDAY_MORNING_BREAK_LINK = None
    WEDNESDAY_MORNING_BREAK_LINK = None
    SUNDAY_LUNCH_LINK = None
    MONDAY_LUNCH_LINK = None
    TUESDAY_LUNCH_LINK = None
    WEDNESDAY_LUNCH_LINK = None
    MONDAY_AFTERNOON_BREAK_LINK = None
    TUESDAY_AFTERNOON_BREAK_LINK = None
    WEDNESDAY_AFTERNOON_BREAK_LINK = None
