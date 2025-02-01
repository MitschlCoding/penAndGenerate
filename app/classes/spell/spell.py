from typing import Optional

from app.classes.spell.spellComponent import SpellComponent
from app.classes.spell.spellSchool import SpellSchool
from app.classes.time.time import Time, TimeUnit
from app.classes.range.range import Range, DistanceUnit, DistanceType

class Range:
    def __init__(self, distance: Optional[int], distance_unit: Optional[DistanceUnit], distance_type: DistanceType):
        if distance_type == DistanceType.SELF or distance_type == DistanceType.TOUCH:
            if distance != None:
                raise ValueError("Distance must be 0 for SELF distance type")
            if distance_unit != None:
                raise ValueError("Distance unit must be None for SELF distance type")
        self.distance = distance
        self.distance_unit = distance_unit
        self.distance_type = distance_type
        
    def __str__(self):
        if self.distance_type == DistanceType.SELF:
            return "Self"
        elif self.distance_type == DistanceType.TOUCH:
            return "Touch"
        return f"{self.distance} {self.distance_unit.value}"
        
    def __eq__(self, other: 'Range'):
        if self.distance_type == DistanceType.SELF and other.distance_type == DistanceType.SELF:
            return True
        if self.distance_type == DistanceType.SELF or other.distance_type == DistanceType.SELF:
            return False
        
        distance = None
        # Calculate the distance in feet
        if self.distance_type == DistanceType.TOUCH:
            distance = 0
        elif self.distance_unit == DistanceUnit.FEET:
            distance = self.distance
        elif self.distance_unit == DistanceUnit.MILES:
            distance = self.distance * 5280
            
        other_distance = None
        # Calculate the other distance in feet
        if other.distance_type == DistanceType.TOUCH:
            other_distance = 0
        elif other.distance_unit == DistanceUnit.FEET:
            other_distance = other.distance
        elif other.distance_unit == DistanceUnit.MILES:
            other_distance = other.distance * 5280

        if distance == None and other_distance == None:
            raise ValueError("Distance is not set")
        return distance == other_distance

class Spell:
    def __init__(self, name: str, level: int, school: SpellSchool, casting_time: Time, range: Range, components: list[SpellComponent], duration: Time, description: str):
        self.name = name
        self.level = level
        self.school = school
        self.casting_time = casting_time
        self.range = range
        self.components = components
        self.duration = duration
        self.description = description
        
    def __str__(self):
        return f"{self.name} ({self.level}) - {self.school.value} - {self.casting_time} - {self.range} - {', '.join([component.value for component in self.components])} - {self.duration} - {self.description}"
        
    def __eq__(self, other: 'Spell'):
        return self.name == other.name and self.level == other.level and self.school == other.school and self.casting_time == other.casting_time and self.range == other.range and self.components == other.components and self.duration == other.duration and self.description == other.description