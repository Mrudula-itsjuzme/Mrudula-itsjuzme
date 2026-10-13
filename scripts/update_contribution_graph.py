#!/usr/bin/env python3
"""Render the GitHub contribution calendar as a local SVG asset."""
import datetime as dt
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen
from html import escape

USER = "Mrudula-itsjuzme"
QUERY = """query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}"""

def main():
    token = os.environ["GH_TOKEN"]
    payload = json.dumps({"query": QUERY, "variables": {"login": USER}}).encode()
    request = Request(
        "https://api.github.com/graphql", data=payload,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "User-Agent": "profile-contribution-chart"},
    )
    with urlopen(request, timeout=30) as response:
        result = json.load(response)
    if result.get("errors"):
        raise RuntimeError(result["errors"])
    calendar = result["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = calendar["weeks"]
    cw, gap, left, top = 11, 3, 32, 58
    width = left + len(weeks) * (cw + gap) + 17
    height = 190
    colors = ["#19243A", "#29445C", "#246E83", "#1CA4B8", "#65E4D3"]
    def level(n):
        return 0 if n == 0 else 1 if n <= 2 else 2 if n <= 5 else 3 if n <= 9 else 4
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="GitHub contributions over the past year">',
        f'<rect width="{width}" height="{height}" fill="#0B1220" rx="12"/>',
        '<text x="20" y="28" fill="#DCE7F2" font-family="Arial,sans-serif" font-size="15" font-weight="600">contributions</text>',
        f'<text x="20" y="44" fill="#99A9C0" font-family="Arial,sans-serif" font-size="10">{calendar["totalContributions"]} contributions in the past year</text>',
    ]
    last_month = None
    for x, week in enumerate(weeks):
        days = week["contributionDays"]
        first = dt.date.fromisoformat(days[0]["date"])
        if first.month != last_month:
            if x % 2 == 0 or last_month is None:
                parts.append(f'<text x="{left + x * (cw + gap)}" y="54" fill="#8B9DB5" font-family="Arial,sans-serif" font-size="9">{escape(first.strftime("%b"))}</text>')
            last_month = first.month
        for day in days:
            day_date = dt.date.fromisoformat(day["date"])
            n = day["contributionCount"]
            y = top + (day_date.weekday() + 1) % 7 * (cw + gap)
            xx = left + x * (cw + gap)
            parts.append(f'<rect x="{xx}" y="{y}" width="{cw}" height="{cw}" rx="2" fill="{colors[level(n)]}"><title>{day["date"]}: {n} contributions</title></rect>')
    for weekday, idx in (("Mon", 1), ("Wed", 3), ("Fri", 5)):
        parts.append(f'<text x="7" y="{top + idx*(cw+gap) + 9}" fill="#8B9DB5" font-family="Arial,sans-serif" font-size="9">{weekday}</text>')
    legend_y = 168
    parts.append(f'<text x="{width-158}" y="{legend_y+9}" fill="#8B9DB5" font-family="Arial,sans-serif" font-size="10">less</text>')
    for i, color in enumerate(colors):
        parts.append(f'<rect x="{width-126+i*17}" y="{legend_y}" width="11" height="11" rx="2" fill="{color}"/>')
    parts.append(f'<text x="{width-32}" y="{legend_y+9}" fill="#8B9DB5" font-family="Arial,sans-serif" font-size="10">more</text>')
    parts.append("</svg>")
    target = Path("assets/contributions.svg")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(parts) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
