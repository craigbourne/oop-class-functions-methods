from datetime import datetime

# Exercise 16.1
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

def mul_time(time, factor):
    total_seconds = time.hour * 3600 + time.minute * 60 + time.second
    new_seconds = total_seconds * factor
    hours = int(new_seconds // 3600)
    minutes = int((new_seconds % 3600) // 60)
    seconds = int(new_seconds % 60)
    return Time(hours, minutes, seconds)

def avg_pace(finish_time, distance):
    return mul_time(finish_time, 1/distance)

# Test Exercise 16.1
race_time = Time(1, 30, 0)  # 1 hour 30 minutes
distance = 5  # 5 miles

print("Exercise 16.1:")
print(f"Race time: {race_time}")
print(f"Pace per mile: {avg_pace(race_time, distance)}")

# Exercise 16.2
print("\nExercise 16.2:")
# Day of week
print(f"Current day: {datetime.now().strftime('%A')}")

# Birthday calculations
birthday = datetime(1990, 5, 15)
today = datetime.now()
next_birthday = datetime(today.year, birthday.month, birthday.day)
if next_birthday < today:
    next_birthday = datetime(today.year + 1, birthday.month, birthday.day)
age = today.year - birthday.year
if today < datetime(today.year, birthday.month, birthday.day):
    age -= 1
print(f"Age: {age}")
print(f"Days until next birthday: {(next_birthday - today).days}")

# Double Day calculation
birth1 = datetime(1990, 1, 1)
birth2 = datetime(1990, 12, 31)
diff = birth2 - birth1
double_day = birth2 + diff
triple_day = birth2 + (diff * 2)
print(f"Double Day: {double_day.date()}")
print(f"Triple Day: {triple_day.date()}")