class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, *args):
        self.hours = args[0]
        self.minutes = args[1]
        self.seconds = args[2]

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        if self.seconds + 1 > Time.max_seconds:
            self.seconds = 0

            if self.minutes + 1 > Time.max_minutes:
                self.minutes = 0

                if self.hours + 1 > Time.max_hours:
                    self.hours = 00
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

        self.set_time(self.hours, self.minutes, self.seconds)
        return self.get_time()

time = Time(9, 30, 59)
print(time.next_second())