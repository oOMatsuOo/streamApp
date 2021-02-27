from datetime import datetime

from python_modules.src.update import update_all
from python_modules.src.rename import add_quality_in_all_file_name

print("Start Update on : " + datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
print("________________________")

path = 'media'

add_quality_in_all_file_name(path)

update_all(path)

print("________________________")
print("Update Finish on : " + datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))