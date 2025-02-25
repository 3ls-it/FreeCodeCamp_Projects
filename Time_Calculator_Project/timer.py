
def add_time(start, duration, day=None):

    # Get all our input values 
    starting = start.split()
    begin = starting[0]
    meridiem = starting[1].upper()
    times = begin.split(':')
    start_hr = int(times[0])
    start_min = int(times[1])

    # Adjust for 24-hr clock 
    if meridiem == "PM":
        start_hr += 12

    # Calculate duration time, stop time, later day  
    durations = duration.split(':')
    duration_hr = int(durations[0])
    duration_min = int(durations[1])
    stop_min = start_min + duration_min
    stop_hr = start_hr + duration_hr + stop_min // 60
    later = stop_hr // 24
    stop_hr %= 24
    stop_min %= 60

    # Convert to 12-hr clock 
    if stop_hr >= 12:
        meridiem = "PM"
        stop_hr -= 12
    else:
        meridiem = "AM"

    if stop_hr == 0:
        stop_hr = 12

    # Get the day parts 
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day:
        idx = (days.index(day.capitalize()) + later) % 7
        later_day = days[idx]
        part = f", {later_day}"
    else:
        part = ""

    if later == 1:
        later_day_part = " (next day)"
    elif later > 1:
        later_day_part = f" ({later} days later)"
    else:
        later_day_part = ""

    # Put together the end time with days
    end_time = f"{stop_hr}:{stop_min:02} {meridiem}{part}{later_day_part}"

    return end_time

# Example usage
print(add_time("3:00 pm", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
