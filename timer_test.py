import datetime, threading, time

def foo():
    next_call = time.time()
    while True:
        print(datetime.datetime.now())
        end = time.time()
        print("Elasped:{}".format(end - start))
        next_call = next_call+1;
        time.sleep(next_call - time.time())

timerThread = threading.Thread(target=foo)
start = time.time()
timerThread.start()

#start = time.time()
#print("started")
#foo()
