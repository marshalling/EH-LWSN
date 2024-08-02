# Generate a finite set of time periods from 7:30 to 16:30
def GetTime():
    # Initialization start time
    hour = 7
    minute = 30
#==========================
    # Generate array
    time_list = []

    # Loop generation time
    while hour < 16 or (hour == 16 and minute <= 30):  # From 7:30 to 16:30
        time_list.append(f"{hour:02d}:{minute:02d}")  # Add the current time to the array
        minute += 1  # Add minutes
        if minute == 60:  # When the minutes reaches 60
            hour += 1  # Round up hours
            minute = 0  # Reset minutes to 0
    return time_list


# print(GetTime())
