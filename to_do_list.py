# A list of text items with a check box next to each one
# Items are stored in a hash with key as timestamp, value as user entered text
# e.g. { 2015110612320000 : "write notes on intelligent to do list app" }
# How to handle status, ie done or not done - in html?
# create hash to store to do
# user clicks an area at top of list, and that opens dialogue for them to enter new item
# onclick, or something
# 

# import time
import datetime

to_do_hash = {}

my_flag = "a"

while my_flag == "a":
	hash_item = raw_input("Type something to add to your list --> ")
	# this should append to existing hash?
	to_do_hash[str(datetime.datetime.utcnow())] = hash_item
	what_next = str(raw_input("Add something else or view your list? a/v --> "))
	if what_next == "v":
		my_flag = "v"
		print "Here's your list: ", to_do_hash.values()
		print "sorted(to_do_hash.values):,", sorted(to_do_hash.values())



# now, make it so that to_do_hash prints in order of datetime stamp
# get this on github
# what else