from datetime import datetime
from pytz import timezone
import pytz

events = [('01/29/2021 6:30 PM ', '11:30 PM MSK')]

date_format='%m/%d/%Y %I:%M %p %Z'

date = datetime.utcnow()
print(date.astimezone(timezone('Europe/London')).strftime(date_format))

moscow_time = date.astimezone(timezone('Europe/Moscow'))
san_francisco_time = moscow_time.astimezone(timezone('US/Pacific'))

print(moscow_time.strftime(date_format))
print(san_francisco_time.strftime(date_format))

