import datetime
import pytz

def IST():
    current_IST = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    return current_IST.year, current_IST.month, current_IST.date, current_IST.hour, current_IST.minute, current_IST.second

