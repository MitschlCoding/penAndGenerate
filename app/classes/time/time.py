from typing import Optional

from app.classes.time.timeUnit import TimeUnit

class Time:
    def __init__(self, time: int, time_unit: Optional[TimeUnit]):
        if time_unit == TimeUnit.INSTANTANEOUS and time != None:
            raise ValueError("Time must be 0 for INSTANTANEOUS time unit")
        self.time = time
        self.time_unit = time_unit
        
    def __str__(self):
        if self.time_unit == TimeUnit.INSTANTANEOUS:
            return "Instantaneous"
        return f"{self.time} {self.time_unit.value}"
        
    def __eq__(self, other: 'Time'):
        # Calculate the time in seconds
        time = None
        if self.time_unit == TimeUnit.INSTANTANEOUS:
            time = 0
        elif self.time_unit == TimeUnit.SECONDS:
            time = self.time
        elif self.time_unit == TimeUnit.ROUND:
            time = self.time * 6
        elif self.time_unit == TimeUnit.MINUTES:
            time = self.time * 60
        elif self.time_unit == TimeUnit.HOURS:
            time = self.time * 3600
        
        other_time = None
        # Calculate the other time in seconds
        if other.time_unit == TimeUnit.INSTANTANEOUS:
            other_time = 0
        elif other.time_unit == TimeUnit.SECONDS:
            other_time = other.time
        elif other.time_unit == TimeUnit.ROUND:
            other_time = other.time * 6
        elif other.time_unit == TimeUnit.MINUTES:
            other_time = other.time * 60
        elif other.time_unit == TimeUnit.HOURS:
            other_time = other.time * 3600
           
        if time == None and other_time == None:
            raise ValueError("Time is not set")
        return time == other_time