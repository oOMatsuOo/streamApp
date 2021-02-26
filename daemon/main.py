from datetime import datetime

from python_modules.src.update import update_all

print("Start Update on : " + datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
print("________________________")

update_all()

print("________________________")
print("Update Finish on : " + datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
