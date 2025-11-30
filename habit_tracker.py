from datetime import datetime
from dataclasses import dataclass



@dataclass
class Habit:
    name: str
    time_since: str
    remaining_days: str
    minutes_saved: float
    money_saved: str



def track_habit(name:str, start: datetime, cost: float, minutes_used: float) -> Habit:
    goal: int = 60
    hourly_wage: int = 30

    time_elapsed: float = (datetime.now() - start).total_seconds()
    

