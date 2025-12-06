import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit


def main():
    habits: list[Habit] = [
        track_habit('Voyager', datetime(2025, 12, 4, 8), cost=10, minutes_used=60)
    ]

    df = pd.DataFrame(habits)
    print(tabulate(df, headers='keys', tablefmt='psql'))