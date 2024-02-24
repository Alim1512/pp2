from datetime import datetime, timedelta
#1
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print(new_date)

#2
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorow = current_date + timedelta(days=1)
print(yesterday, current_date, tomorow)

#3
#n = int(input())
current_date = datetime.now()
ans_time = current_date - timedelta(microseconds=n)
print(ans_time)

#4
current_date = datetime.now()
first_date = current_date - timedelta(seconds=5)
second_date = current_date + timedelta(seconds=5)
print(first_date, current_date, second_date)