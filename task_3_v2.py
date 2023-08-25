# Генератор расписания
from datetime import datetime, timedelta


def schedule_generator(all_days, work_days, rest_days, start_date):
    schedule = []
    while all_days > 0:
        for _ in range(work_days):
            schedule.append(start_date)
            start_date += timedelta(days=1)
            all_days -= 1
            if all_days == 0:
                return schedule
        for _ in range(rest_days):
            start_date += timedelta(days=1)
            all_days -= 1
            if all_days == 0:
                return schedule


print(schedule_generator(5, 2, 1, datetime(2020, 1, 30)))


def test():
    res = schedule_generator(5, 2, 1, datetime(2020, 1, 30))
    assert res == [
                    datetime(2020, 1, 30, 0, 0),
                    datetime(2020, 1, 31, 0, 0),
                    datetime(2020, 2, 2, 0, 0),
                    datetime(2020, 2, 3, 0, 0)
                  ]
