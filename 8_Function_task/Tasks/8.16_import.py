import example
from example import show_message
from example import show_message as sm
import example as e
from example import *

message = ['hello', 'asd', 'dsa']

example.show_message(message)
show_message(message)
e.show_message(message)
sm(message)
show_message(message)

#192