def convert_to_military(num, tod):	
	if tod == 'PM':
		return 12 + num
	return num	
	

def add_hours(start_hours, add_hours):
	return start_hours + add_hours


def parse_string_to_num(string):
	split_string = string.split(':')
	parsed = dict()
	if split_string[1].find('PM') > -1:
		tod = split_string[1].split(' ')[1]	
		minutes = split_string[1].split(' ')[0]
		hours = split_string[0]	
		parsed['day_time'] = tod
	else:
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

def days_later(num_days, day_given):
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

	blah = week[0:day_given_index]
	print blah, week
	
	return day	

def add_time(start, duration, day = None):
# add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)
	start_time = parse_string_to_num(start)
	converted = convert_to_military(int(start_time['hours']), start_time['day_time'])
	given_time = parse_string_to_num(duration)
	total_hours = add_hours(converted, int(given_time['hours']))
	total_mins = add_mins(int(start_time['minutes']), int(given_time['minutes']))
	
	if 'add_one' in total_mins:
		total_hours = total_hours + total_mins['add_one']

	
	num_days = num_days_later(total_hours)
	total_hours_between_days = get_hours_between_days(num_days)
	
	new_time = total_hours - total_hours_between_days

	days = days_later(num_days, day)


	#print "new time", new_time, "total hours", total_hours, " total_mins", total_mins
	
    #return new_time


x = add_time("11:43 PM", "24:20", "tueSday")
y = add_time("6:30 PM", "205:12", "sunday")




