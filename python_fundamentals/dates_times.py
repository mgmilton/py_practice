import datetime as dt
import time as tm

#time returns the current time in seconds since the Epoch (January 1st, 1970)
tn.time()

#Convert the timestampe to datetime
dt.now = dt.datetime.fromtimestamp(tm.time())
dtnow

#Useful datetime attributes
dtnow.year
dtnow.month
dtnow.day
dtnow.hour
dtnow.minute
dtnow.second

#timedelta is a duration expressing the difference btwn two dates

delta = dt.timedelta(days = 100) #create a timedelta of 100 days
delta

#date.today returns the current local date

today = dt.date.today()
today - delta # the date 100 days ago
today > today - delta # compare dates
