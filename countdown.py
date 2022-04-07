from dotenv import load_dotenv
import os
from datetime import datetime
from twitter_handler import update_displayname
import schedule
import time
from retry import retry
load_dotenv()


end_date = os.environ.get('end_date', None)
prefix = os.environ.get('prefix', None)
label = os.environ.get('label', None)

class CountDown:

    def __init__(self, end_date, label, prefix):
        self.end_date = end_date
        self.label = label
        self.prefix = prefix

    def _get_countdown(self): 

        def date_diff_in_seconds(dt2, dt1):
            timedelta = dt2 - dt1
            return timedelta.days * 24 * 3600 + timedelta.seconds

        def dhms_from_seconds(seconds):
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)
            return (days, hours, minutes)

        #Specified date
        date1 = datetime.strptime(self.end_date, '%Y-%m-%d')

        #Current date
        date2 = datetime.now()

        days, hours, mins = dhms_from_seconds(date_diff_in_seconds(date1, date2))

        message = f"{self.prefix} {days} dino, {hours} jam, {mins} menit nganti {self.label}."
        return message

    @retry(tries=3, delay=5)
    def main_task(self):
        message = self._get_countdown()
        update_displayname(name=message)


if __name__ == "__main__":

    print(f"scheduler countdown is now running")

    def job():
        CountDown(end_date, label, prefix).main_task()

    schedule.every().minute.at(":00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)