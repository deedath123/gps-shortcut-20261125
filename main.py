import os

LINE = "Look, the map swore this cul-de-sac shaved nine minutes off your trip, so I trusted it, and now the bride is glaring at us through her veil while her wedding starts in four minutes."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

if not (1 <= len(LINE) <= 200) or not LINE.strip() or "\n" in LINE.strip():
    raise SystemExit("invalid entry")
print(LINE)
