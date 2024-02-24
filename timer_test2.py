import datetime, threading, time
from threading import Timer


def hello():
    print("hello, world")

t = Timer(20.0, hello)
t.start()