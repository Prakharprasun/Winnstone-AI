from calendar import month
from datetime import datetime
now=datetime.now()
year,mon,hour,min,sec=now.year,now.month,now.hour,now.minute,now.second
print(hour,":",min,":",sec)
print(month(year,mon))