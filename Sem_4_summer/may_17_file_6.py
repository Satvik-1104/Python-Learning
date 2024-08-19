# ******************************************************************
import time
# ******************************************************************

# print((time.ctime(0)))          convert a time expressed in seconds since epoch to a readable string
#                                 epoch = when your computer thinks time began (reference point)
# print(time.time())              return current seconds since epoch
# print(time.ctime(time.time()))  will get current time.
# time.strftime - time object to readable format
# time.strptime - readable format to time object
# time.asctime - time tuple to time string
# time.mktime - time tuple to seconds since epoch

print(time.ctime(0))
print(time.time())
print(time.ctime(time.time()))

time_object = time.localtime()
time_obj_global = time.gmtime()
print(time_object)
print(time_obj_global)
time_format = "%B %d %Y %H:%M:%S"
local_time = time.strftime(time_format, time_object)
global_time = time.strftime(time_format, time_obj_global)
print(local_time)
print(global_time)

time_string = "11 October, 2004"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)

# (year, month, day, hours, minutes, secs, #day of the  week, #day of the year, dst)
time_tuple = (2004, 11, 10, 22, 53, 18, 0, 0, 0)
time_asc = time.asctime(time_tuple)
print(time_asc)

time_tuple = (2004, 11, 10, 22, 53, 18, 0, 0, 0)
time_mk = time.mktime(time_tuple)
print(time_mk)
