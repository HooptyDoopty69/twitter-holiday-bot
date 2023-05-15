import datetime as dt
import holidays


current_date = dt.datetime.now().date()
current_year = current_date.year

us_holidays = sorted(holidays.US(years=current_year).items())


def get_days_till_holiday(date):
    days_left_str = str(date - current_date).split(',')[0]
    days_left_int = days_left_str.split(' ')[0]

    return int(days_left_int)


def remaining_days_result():
    txt = ""

    for date, name in us_holidays:
        if get_days_till_holiday(date) > 0:
            txt += f"{get_days_till_holiday(date)} till {name}.\n"

    return txt
