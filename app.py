
import streamlit as st
from parser import parse_availability
import streamlit.components.v1 as components

st.set_page_config(page_title="Availability Parser + Calendar", layout="wide")

st.title("📅 Teacher Availability Scheduler")

st.markdown("### Step 1: Paste your availability description below")

user_input = st.text_area("Enter your availability:", 
    "I’m available Monday mornings, Wednesday after 2pm, and Friday.")

if st.button("Parse and Show Calendar"):
    slots = parse_availability(user_input)

    if not slots:
        st.warning("No recognizable time slots found.")
    else:
        st.success("Parsed time slots:")
        st.write(slots)

        # Convert to FullCalendar format
        day_map = {
            "Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3,
            "Thursday": 4, "Friday": 5, "Saturday": 6
        }

        fullcalendar_events = []
        for day, start, end in slots:
            fullcalendar_events.append(f"""{{
                title: 'Available',
                daysOfWeek: [{day_map[day]}],
                startTime: '{start}',
                endTime: '{end}'
            }}""")

        calendar_code = f"""
        <link href='https://cdn.jsdelivr.net/npm/fullcalendar@5.10.1/main.min.css' rel='stylesheet' />
        <script src='https://cdn.jsdelivr.net/npm/fullcalendar@5.10.1/main.min.js'></script>
        <div id='calendar'></div>
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            var calendarEl = document.getElementById('calendar');
            var calendar = new FullCalendar.Calendar(calendarEl, {{
                initialView: 'timeGridWeek',
                slotMinTime: "08:00:00",
                slotMaxTime: "20:00:00",
                allDaySlot: false,
                events: [{','.join(fullcalendar_events)}]
            }});
            calendar.render();
        }});
        </script>
        <style>
            #calendar {{ max-width: 900px; margin: 40px auto; }}
        </style>
        """
        components.html(calendar_code, height=700)
