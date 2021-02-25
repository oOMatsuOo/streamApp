from apscheduler.schedulers.blocking import BlockingScheduler

from python_modules.src.update import update_all

sched = BlockingScheduler()


@sched.scheduled_job('interval', hour=1)

def scheduled_job():
    update_all()


sched.start()