import numpy as np
from datetime import datetime, timedelta


def predict(stats, predict_days):
    latest_date = datetime(1970, 1, 1)

    dates = [(__get_datetime(date), date) for date in list(stats.keys())]
    dates = sorted(dates, key=lambda d: d[0])

    timestamps = []
    values = []

    for date in dates:
        latest_date = max(latest_date, date[0])

        timestamps.append(__get_timestamp(date[0]))
        values.append(stats[date[1]])

    order = 1
    predict_f = np.poly1d(np.polyfit(timestamps, values, order))

    predict_days = [__get_timestamp(latest_date + timedelta(days=i)) for i in range(1, predict_days + 1, 1)]

    return list(predict_f(predict_days))


def __get_datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')


def __get_timestamp(datetime):
    return datetime.timestamp()
