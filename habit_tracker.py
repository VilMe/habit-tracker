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
    hours: float = round(time_elapsed / 60 / 60, 1)
    days: float = round(hours / 24, 2)

    money_saved: float = cost * days
    minutes_used: float = round(days * minutes_used)
    total_money_saved: str = f'$({round(money_saved + (minutes_used / 60 * hourly_wage), 2)})'
