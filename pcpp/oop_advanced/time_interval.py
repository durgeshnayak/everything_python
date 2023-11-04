class TimeInterval:

    def __init__(self, hours, minutes, seconds):
        if hours > 23 or minutes > 59 or seconds > 59:
            raise TypeError("invalid value supplied.")
        self.hour = hours
        self.minute = minutes
        self.second = seconds

    def __str__(self):
        str_hour = str(self.hour) if self.hour > 9 else "0" + str(self.hour)
        str_minute = str(self.minute) if self.minute > 9 else "0" + str(self.minute)
        str_second = str(self.second) if self.second > 9 else "0" + str(self.second)
        return str_hour + ":" + str_minute + ":" + str_second

    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Only time intervals can be added to other time intervals.")




time_interval = TimeInterval(11, 17, 00)
print(time_interval)
