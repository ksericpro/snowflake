from os import system
import time
import os
from timeloop import Timeloop
from datetime import timedelta

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print("current directory..{}".format(current_working_directory))

run_bat = "{}/run_connect.bat".format(current_working_directory)

TIME_INTERVAL=120

print("running at {}s interval".format(TIME_INTERVAL))
print("executing..{}".format(run_bat))

tl = Timeloop()

@tl.job(interval=timedelta(seconds=TIME_INTERVAL))
def trigger_snowflake():
    #print("Preparing Iteration #{}".format(ct))
    system(run_bat)

tl.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        tl.stop()
        break
