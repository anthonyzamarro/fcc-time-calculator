def convert_to_military(num, tod):	
	if tod == 'PM':
		return 12 + num
	return num	
	

def add_hours(start_hours, add_hours):
	return start_hours + add_hours


def parse_string_to_num(string):
	split_string = string.split(':')
	parsed = dict()
	# if string is start time AKA has AM or PM
	if split_string[1].find('PM') > -1 or split_string[1].find('AM') > -1:
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
	return total_hours / 24

def get_hours_between_days(days):
	return days * 24	

def days_later(num_days, day_given = ''):
	day = day_given.lower()
	# create an array that contains all the days of the week
	# from this, create a new array that starts on the day given
	# loop through the array num_days times. 
	# if num_days > array length, then append x days to end of array starting with day_given and ending on num_days - array.length after days given
	week = [
	'sunday',
	'monday',
	'tuesday',
	'wednesday',
	'thursday', 
	'friday',
	'saturday'
	] 
	
	day_given_index = week.index(day)

	days_before_start = week[0:day_given_index]

	#diff = None
	#if num_days > len(week):
	new_week_start = week[day_given_index:]
	new_week_days = week * -(-num_days // len(week))
	new_week = new_week_start + new_week_days
	return new_week[num_days]
		## num_days = 20
		#diff = num_days - len(week)
		#week = week[day_given_index:] + week[0:diff]
		#print 'output: ', week[day_given_index:], week
		#return week[num_days - 1]
	#else:
		#print 'line 73: num_days = ', num_days, ' week = ', week
		#del week[:day_given_index]
		#print 'line 75: num_days = ', num_days, ' week = ', week
		#print num_days, day_given_index, week, week[:num_days]
		#return week[num_days]

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
	if num_days == 0:
		return ''
	elif num_days == 1:
		return ' (next day)'
	else:
		return ' (' + str(num_days) + ' days later)'

	
def add_time(start, duration, day_given = ''):
	start_time = parse_string_to_num(start)
	converted = convert_to_military(int(start_time['hours']), start_time['day_time'])
	given_time = parse_string_to_num(duration)
	total_hours = add_hours(converted, int(given_time['hours']))
	total_mins = add_mins(int(start_time['minutes']), int(given_time['minutes']))

	if 'add_one' in total_mins:
		total_hours = total_hours + total_mins['add_one']

	num_days = num_days_later(total_hours)
	total_hours_between_days = get_hours_between_days(num_days)
	
	new_hours = total_hours - total_hours_between_days

	hours = format_hours(new_hours)

	minutes = format_mins(total_mins['minutes'])

	am_pm = format_am_pm(new_hours)

	fnum_days = format_num_days(num_days)

	days = ''
	if day_given:	
		days = days_later(num_days, day_given)
		days  = ', ' + days.capitalize()
	
	new_time  = str(hours) + ':' + str(minutes) + ' ' + str(am_pm) + str(days) + fnum_days
	return new_time
	
#a = add_time("3:00 PM", "3:10")
## Returns: 6:10 PM
#
#b = add_time("11:30 AM", "2:32", "Monday")
## Returns: 2:02 PM, Monday
#
#c = add_time("11:43 AM", "00:20")
## Returns: 12:03 PM
#
#d = add_time("10:10 PM", "3:30")
## Returns: 1:40 AM (next day)
#
#e = add_time("11:43 PM", "24:20", "tueSday")
## Returns: 12:03 AM, Thursday (2 days later)
#
#f = add_time("6:30 PM", "205:12")
## Returns: 7:42 AM (9 days later)
#
#g = add_time("6:30 PM", "205:12", 'sunday')
## Returns: 7:42 AM, Monday (9 days later)

#h = add_time("2:59 AM", "24:00", "saturDay")
#i = add_time("8:16 PM", "466:02", "tuesday")

#j = add_time("3:30 PM", "2:12", "Monday")
#k = add_time("2:59 AM", "24:00", "saturDay")
#l = add_time("11:59 PM", "24:05", "Wednesday")
#
#print a, "\nReturns: 6:10 PM\n"
#print b, "\nReturns: 2:02 PM, Monday\n"
#print c, "\nReturns: 12:03 PM\n"
#print d, "\nReturns: 1:40 AM (next day)\n"
#print e, "\nReturns: 12:03 AM, Thursday (2 days later)\n"
#print f, "\nReturns: 7:42 AM (9 days later)\n"
#print g, "\nReturns: 7:42 AM, Monday (9 days later)\n"

#print j, "\nreturn 5:42 PM, Monday\n"
#print k, "\nreturn 2:59 AM, Sunday (next day)\n"
#print l, "\nreturn 12:04 AM, Friday (2 days later)\n"



