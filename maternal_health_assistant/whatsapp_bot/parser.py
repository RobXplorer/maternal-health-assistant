import re

def parse_message(text):
    # Acceptable key aliases (e.g. "convulsion" maps to "convulsions")
    alias_map = {
        "bp": "bp", "b.p": "bp", "be": "bp",
        "fever": "fever",
        "bleed": "bleeding", "bleeding": "bleeding",
        "headache": "headache", "headaches": "headache",
        "convulsion": "convulsions", "convulsions": "convulsions",
    }

    expected_keys = {"bp", "fever", "bleeding", "headache", "convulsions"}
    data = {}
    found = set()

    words = text.lower().strip().split()

    i = 0
    while i < len(words):
        word = words[i]

        key = alias_map.get(word)
        if not key:
            i += 1
            continue

        # For blood pressure
        if key == "bp" and i + 1 < len(words):
            value = words[i + 1]
            if not re.match(r"^\d{2,3}/\d{2,3}$", value):
                raise ValueError(f"Invalid BP format: '{value}'. Use e.g. 120/80")
            data["bp"] = value
            found.add("bp")
            i += 2
            continue

        # For symptoms
        if key in expected_keys and i + 1 < len(words):
            value = words[i + 1]
            if value not in {"yes", "no"}:
                raise ValueError(f"Invalid response '{value}' for {key}. Use 'yes' or 'no'")
            data[key] = value
            found.add(key)
            i += 2
            continue

        i += 1

    # Check for any required fields still missing
    missing = expected_keys - found
    if "bp" not in found:
        raise ValueError("Missing BP. Please include something like 'bp 130/85'")

    # Fill missing symptoms with default "no"
    for key in expected_keys:
        if key not in data:
            data[key] = "no"

    return data
