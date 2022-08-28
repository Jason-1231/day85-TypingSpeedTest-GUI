# from words import WORDS
#
# x = 10
#
#
# def test():
#     y = WORDS[x]
#     print(y)
#     x += 1 # problem is here. Variable changed to local when newly assigned
#
#
# test()


# q_, rm_ = divmod(61, 60)
#
# print(q_, rm_)

from datetime import datetime
from datetime import timedelta


now = datetime.now()
future = now + timedelta(seconds=60)
remaining_secs = future - datetime.now()
while remaining_secs.seconds > 0:
    remaining_secs = future - datetime.now()
    print(remaining_secs.seconds)

print(now)
print(future)
