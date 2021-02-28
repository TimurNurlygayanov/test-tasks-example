# The example of task was taken from
# https://www.youtube.com/watch?v=3Q_oYDQ2whs
#

calendar1 = [['8:30', '10:00'], ['12:10', '15:00'], ['15:30', '18:00']]
calendar1_bounds = ['8:00', '18:00']

calendar2 = [['9:30', '11:00'], ['11:50', '16:00'], ['17:30', '19:00']]
calendar2_bounds = ['9:00', '20:00']

NEW_MEET_DURATION = 30  # new meeting duration in minutes


def get_minutes(time_str: str) -> int:
    hours, minutes = ((int(k) for k in time_str.split(':')))
    return hours * 60 + minutes


def merge_bounds(calendar: list, bounds: list) -> list:
    # Add bounds to the events list:
    calendar = [['0:00', bounds[0]]] + calendar
    calendar.append([bounds[1], '24:00'])

    return calendar


def merge_events(c1: list) -> list:
    start = c1[0][0]
    end = c1[0][1]
    i = 1
    new_calendar = []

    while i < len(c1):
        if c1[i][0] <= end:
            if c1[i][1] > end:
                end = c1[i][1]
            i += 1
        else:
            new_calendar.append([start, end])
            start = c1[i][0]
            end = c1[i][1]

    new_calendar.append([start, end])

    return new_calendar


def get_slot(c1, c2, c1_bounds, c2_bounds, minutes) -> str:
    c1 = merge_bounds(c1, c1_bounds)
    c2 = merge_bounds(c2, c2_bounds)

    # Convert all timestamps into integers
    c1 = [[get_minutes(x[0]), get_minutes(x[1])] for x in c1]
    c2 = [[get_minutes(x[0]), get_minutes(x[1])] for x in c2]

    events = sorted(c1 + c2)    # here we can apply merge sort
                                # to get O(N) time for sorting

    events = merge_events(events)

    time_slot = None
    for i, event in enumerate(events):
        if i < len(events)-1 and minutes <= events[i+1][0] - event[1]:
            time_slot = '{0:02d}:{1:02d}'.format(event[1] // 60,
                                                 event[1] % 60)

    return time_slot


suggested_time_slot = get_slot(calendar1, calendar2,
                               calendar1_bounds, calendar2_bounds,
                               NEW_MEET_DURATION)
print('Suggested time slot is', suggested_time_slot)
