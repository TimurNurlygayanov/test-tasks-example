# The example of task was taken from
# https://www.youtube.com/watch?v=3Q_oYDQ2whs
# It took about 30 minutes for the solution #1
# and it took about 20 minutes for the solution #2
# after I read the comments

# Every calendar has sorted booked time slots in 24 hours format
# and we assume that both calendars have the same timezone

calendar1 = [['8:30', '10:00'], ['12:10', '15:00'], ['15:30', '18:00']]
calendar1_bounds = ['8:00', '18:00']

calendar2 = [['9:30', '11:00'], ['11:50', '16:00'], ['17:30', '19:00']]
calendar2_bounds = ['9:00', '20:00']

NEW_MEET_DURATION = 30  # meeting duration in minutes


def get_minutes(time_slot: list) -> list:
    res = []

    for time_str in time_slot:
        parts = time_str.split(':')
        minutes = int(parts[0])*60 + int(parts[1])
        res.append(minutes)

    return res


def get_time_str(time_slot: list) -> list:
    res = []

    for time_int in time_slot:
        hour = time_int // 60
        minute = time_int - hour*60
        res.append(f'{hour:02}:{minute:02}')

    return res


# Solution #1
def find_time_slot() -> list:
    results = []
    available1 = []
    available2 = []

    c1 = [get_minutes(c) for c in calendar1]
    c1b = get_minutes(calendar1_bounds)

    c2 = [get_minutes(c) for c in calendar2]
    c2b = get_minutes(calendar2_bounds)

    for i in range(len(c1) - 1):
        if c1[i+1][0] - c1[i][1] > NEW_MEET_DURATION:
            available1.append([c1[i][1], c1[i+1][0]])

    # add available slots from the beginning of the day
    # until the first meeting and from the last meeting until
    # the end of the day
    available1.insert(0, [c1b[0], c1[0][0]])
    available1.append([c1[-1][1], c1b[1]])

    for i in range(len(c2) - 1):
        if c2[i+1][0] - c2[i][1] > NEW_MEET_DURATION:
            available2.append([c2[i][1], c2[i+1][0]])

    available2.insert(0, [c2b[0], c2[0][0]])
    available2.append([c2[-1][1], c2b[1]])

    # Find available time slots:
    for slot in available1:
        for slot2 in available2:
            if min(slot[1], slot2[1]) - max(slot[0], slot2[0]) > NEW_MEET_DURATION:
                results.append([max(slot[0], slot2[0]),
                                max(slot[0], slot2[0]) + NEW_MEET_DURATION])

    # Convert int to string time format and
    # exclude duplicated slots if there any
    results = [get_time_str(e) for e in results
               if results.count(e) == 1]

    return results


# Solution #2
def find_time_slot2() -> list:
    results = []
    calendar = []

    # Combine all calendars and sort all events
    calendar_temp = calendar1 + calendar2
    calendar_temp = sorted([get_minutes(c) for c in calendar_temp])

    # Combine bounds (start and end of the day)
    c1b = get_minutes(calendar1_bounds)
    c2b = get_minutes(calendar2_bounds)
    bounds = [max(c1b[0], c2b[0]), min(c1b[1], c2b[1])]

    # Merge all events
    start_time = min(bounds[0], calendar_temp[0][0])
    end_time = max(bounds[0], calendar_temp[0][1])
    for i in range(0, len(calendar_temp) - 1):
        if calendar_temp[i][0] > end_time:
            calendar.append([start_time, end_time])
            start_time = calendar_temp[i][0]
            end_time = calendar_temp[i][1]
        else:
            end_time = calendar_temp[i][1]

    # Try to find the available slots
    for i in range(len(calendar) - 1):
        if calendar[i+1][0] - calendar[i][1] >= NEW_MEET_DURATION:
            if calendar[i][1] >= bounds[0] and calendar[i][1] + NEW_MEET_DURATION <= bounds[1]:
                results.append([calendar[i][1], calendar[i][1] + NEW_MEET_DURATION])

    # Convert int to string time format
    results = [get_time_str(e) for e in results]

    return results


result = find_time_slot()
print('Solution #1 result:', result)

result = find_time_slot2()
print('Solution #2 result:', result)
