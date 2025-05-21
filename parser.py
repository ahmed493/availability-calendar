
import re

def parse_availability(text):
    text = text.lower()
    slots = []

    if "monday morning" in text:
        slots.append(("Monday", "08:00", "12:00"))
    if "monday afternoon" in text:
        slots.append(("Monday", "13:00", "17:00"))
    if "wednesday after 2" in text:
        slots.append(("Wednesday", "14:00", "18:00"))
    if "friday morning" in text:
        slots.append(("Friday", "08:00", "12:00"))
    elif "friday" in text:
        slots.append(("Friday", "10:00", "16:00"))

    return slots
