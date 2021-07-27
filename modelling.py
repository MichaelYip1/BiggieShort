import random, schedule, time
from biggieshort import *

def rng():
    x = random.randint(0,5)
    if x == 5:
        response = create_order('IYR','100','market','gtc')
        print(response)
        print("100 shares of IYR has been purchased, good choice investor")
    elif x == 0:
        response = liquidate_order('IYR','100','market','gtc')
        print(response)
        print("100 shares of IYR has been sold, enjoy the gainz")
    else:
        print('NOT BUYING, NOT SELLING')


schedule.every(4).seconds.do(rng)

while 1:
    schedule.run_pending()
    time.sleep(1)

# def buy_signal():
