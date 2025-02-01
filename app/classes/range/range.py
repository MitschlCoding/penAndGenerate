from typing import Optional

from app.classes.range.distanceType import DistanceType
from app.classes.range.distanceUnit import DistanceUnit

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