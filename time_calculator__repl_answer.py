def convert_to_military(num, tod):
    if tod == 'PM':
        return 12 + num
    return num


def add_hours(start_hours, add_hours):
    return start_hours + add_hours


def parse_string_to_num(string):
    split_string = string.split(':')
    parsed = dict()  # if string is start time AKA has AM or PM
    if split_string[1].find('PM') > -1 or split_string[1].find('AM') \
        > -1:
        tod = split_string[1].split(' ')[1]
        minutes = split_string[1].split(' ')[0]
        hours = split_string[0]
        parsed['day_time'] = tod
    else:

          # otherwise, string is duration time

        hours = split_string[0]
        minutes = split_string[1]

    parsed['hours'] = hours
    parsed['minutes'] = minutes

    return parsed


def add_mins(start_mins, given_mins):
    total = start_mins + given_mins
    mins = dict()
    if total >= 60:
        mins['add_one'] = 1
        mins['minutes'] = total - 60
    else:
        mins['minutes'] = total

    return mins


def num_days_later(total_hours):
    if total_hours / 24 < 1:
      return 0
    else:
      return total_hours / 24


def get_hours_between_days(days):
    return days * 24


def days_later(num_days, day_given=''):
    day = day_given.lower()
    week = [
        'sunday',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        ]

    day_given_index = week.index(day)

    new_week_start = week[day_given_index:]
    new_week_days = week * int(-(-num_days // len(week)))
    new_week = new_week_start + new_week_days

    return new_week[int(num_days)]


def format_hours(hours):
    if hours > 12:
        hours = hours - 12
    if hours == 0:
        hours = 12
    return hours


def format_am_pm(hours):
    if hours >= 12:
        return 'PM'
    return 'AM'


def format_mins(mins):
    if mins < 10:
        return '0' + str(mins)
    return str(mins)


def format_num_days(num_days):
    num_days = int(num_days)
    if num_days == 0:
        return ''
    elif num_days == 1:
        return ' (next day)'
    else:
        return ' (' + str(num_days) + ' days later)'


def add_time(start, duration, day_given=''):
    start_time = parse_string_to_num(start)
    converted = convert_to_military(int(start_time['hours']),
                                    start_time['day_time'])
    given_time = parse_string_to_num(duration)
    total_hours = add_hours(converted, int(given_time['hours']))
    total_mins = add_mins(int(start_time['minutes']),
                          int(given_time['minutes']))

    if 'add_one' in total_mins:
        total_hours = total_hours + total_mins['add_one']

    num_days = int(num_days_later(total_hours))

    total_hours_between_days = get_hours_between_days(num_days)

    new_hours = total_hours - int(total_hours_between_days)

    hours = format_hours(new_hours)

    minutes = format_mins(total_mins['minutes'])

    am_pm = format_am_pm(new_hours)

    fnum_days = format_num_days(num_days)

    days = ''
    if day_given:
        days = days_later(num_days, day_given)
        days = ', ' + days.capitalize()

    new_time = str(hours) + ':' + str(minutes) + ' ' + str(am_pm) \
        + str(days) + fnum_days
    return new_time


# l = add_time('11:55 AM', '3:12')
j = add_time("2:59 AM", "24:00", "saturDay")
print (j, '''
return: 2:59 AM, Sunday (next day)
''')
# print (l, '''
# return 3:07 PM 
# ''')

