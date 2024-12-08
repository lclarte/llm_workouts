from typing import Deque, List, Optional, Tuple, Union
from pydantic import BaseModel

class Set(BaseModel):
    reps: int
    weight: Optional[float] = None
    rest: Optional[int] = 0  # Rest in seconds

class Exercise(BaseModel):
    name: str
    category: str
    equipment: Optional[str] = None
    sets: Optional[List[Set]] = None

class Superset(BaseModel):
    type: str = "superset"
    name: str
    exercises: List[Exercise]

class Dropset(BaseModel):
    type: str = "dropset"
    name: str
    equipment: Optional[str] = None
    sets: List[Set]

class HIITExercise(BaseModel):
    name: str
    category: str

class HIIT(BaseModel):
    type: str = "hiit"
    name: str
    rounds: int
    work_duration: int  # Seconds
    rest_duration: int  # Seconds
    exercises: List[HIITExercise]

class Workout(BaseModel):
    workout_name: str
    workout_type: str # what should this be ??? 
    exercises: List[Union[Exercise, Superset, Dropset, HIIT]]

#

# the workout from which we'll deviate

# TODO 1 : adapt the weights (at least at the beginning)

base_workout = Workout(
    workout_name="full body 5x5",
    workout_type="weights",

    exercises=[
        Exercise(name = "benchpress", category = "chest", equipment = "barbell", sets = [Set(reps = 5, weight = 100) for _ in range(5)]),
        Exercise(name = "squat", category = "legs", equipment = "barbell", sets = [Set(reps = 5, weight = 100) for _ in range(5)]),
        Exercise(name = "deadlift", category = "back", equipment = "barbell", sets = [Set(reps = 5, weight = 100) for _ in range(5)]),
    ]
)