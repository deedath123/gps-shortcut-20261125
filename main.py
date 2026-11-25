import os

LINE = "Look, the map swore this cul-de-sac shaved nine minutes off your trip, so I trusted it, and now the bride is glaring at us through her veil while her wedding starts in four minutes."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(LINE)
