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

# Test
race_time = Time(1, 30, 0)  # 1 hour 30 minutes
distance = 5  # 5 miles

print(f"Race time: {race_time}")
print(f"Pace per mile: {avg_pace(race_time, distance)}")