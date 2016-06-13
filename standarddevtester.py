# Authored by: John J. Zima
# Initial build date 12 Jun 2016
# Latest revision "A" 12 Jun 2016 by John J. Zima
# Written for Python 2.7.11
# This short app was developed to take an input set of numbers
# and provide some stastistical outputs.

# Initial user interaction section
print """
Welcome to the statistical computinator.

Please enter all numbers as an integer or floating point number, as indicated.
"""
number_of_inputs = int(raw_input("How many inputs shall we evaluate [integer]? "))

count = 0
data_set = []

while count < number_of_inputs:
	data_set.append(float(raw_input('Input [float]> ')))
	count += 1

# Basic Math Functions
def average(a):
	return sum(a) / len(a)
	
def average_less_one(a):
	return sum(a) / (len(a) - 1)
	
def sqrt(a):
	return a ** 0.5

# Standard Deviation for the whole population
def std_dev_p(a):
	mulist = average(a)
	sq_diff_avg = [(x - mulist) ** 2 for x in a]
	return sqrt(average(sq_diff_avg))
	
# Standard Deviation for a portion of the total population
def std_dev_s(a):
	mulist = average(a)
	sq_diff_avg = [(x - mulist) **2 for x in a]
	return sqrt(average_less_one(sq_diff_avg))
	
# Median calculations
def median(a):
	num_elements = len(a)
	addr1 = int(0.5 * (num_elements - 1))
	addr2 = int(0.5 * num_elements - 1)
	addr3 = addr2 + 1
	if num_elements % 2 == 0:
		middle_mat = [a[addr2], a[addr3]]
		print middle_mat
		return average(middle_mat)
	else:
		return a[addr1]

# Statistical calculations for this program
totals = sum(data_set)
lowest = min(data_set)
highest = max(data_set)
wholepop = std_dev_p(data_set)
partialpop = std_dev_s(data_set)
avgpop = average(data_set)
sorted_data_set = sorted(data_set)
medianlist = median(sorted_data_set)
	
# The results of what happens in this program
print "The data set we are evaluating is %s." % (data_set)
print "A sorted version of these data is %s." % (sorted_data_set)
print "The median of this list is %s." % (medianlist)
print "The lowest number in these data is %s." % (lowest)
print "The highest number in these data is %s." % (highest)
print "The sum of these data is %s." % (totals)
print "The average of these data is %s." % (avgpop)
print "The standard deviation if these data are the whole population %s." % (wholepop)
print "The standard deviation if these data are a sample of the whole population %s." % (partialpop)
