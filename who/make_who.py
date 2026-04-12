#!/usr/bin/env python3

import json


def sort_key(user):
    """Sort by end date, then start date, then username."""
    return (parse_date(user, "end"), parse_date(user, "start"), user["username"])


def parse_date(user, field):
    """Return a numeric sort key for a semester date string."""
    date = user.get(field, "")
    if not date or date == "???":
        return 0
    season = date.split()[0].lower()
    year = int(date.split()[-1])
    offsets = {"spring": 0.5, "winter": 0.25}
    return year + offsets.get(season, 0)


with open("./who.json") as f:
    who_data = json.load(f)["who"]

sorted_data = sorted(who_data, key=sort_key)

with open("./who.md", "w") as out:
    out.write("| Username | Name | Start | End | Coord? | Jobs | Link | Misc. |\n")
    out.write("| ---------|------|-------|-----|--------|------|------|------ |")

    for user in sorted_data:
        coord = ":white_check_mark:" if user.get("coord", False) else ":x:"
        cols = [
            f"`{user['username']}`",
            user["name"],
            user.get("start", "???"),
            user.get("end", "???"),
            coord,
            user.get("jobs", ""),
            user.get("link", ""),
            user.get("misc", ""),
        ]
        row = "| " + " | ".join(c.replace("|", "\\|") for c in cols) + " |"
        out.write(f"\n{row}")

    out.write("\n\n")
