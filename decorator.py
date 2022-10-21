from datetime import datetime


def log_datetime(func):
    '''Log the date and time of a function'''

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()

    return wrapper


@log_datetime
def daily_backup():
    print('Daily backup job has finished.')   

daily_backup()

def convert_upper(f):
    print("convert_upper")
    def wrap(*args, **kwargs):
        print("wrap")
        x = f(*args, **kwargs)
        return x.upper()
    return wrap

@convert_upper
def my_name(name):
    print("my_name")
    return name

teste = my_name('leonardo')
print(teste)


import time
def timed(function):
    def wrapper(*a, **ka):
        before = time.time()

        value = function(*a,**ka)
        after = time.time()
        fname = function.__name__
        print(f"{fname} too {after-before} seconds to execute!")
        return value        
    return wrapper
@timed
def myfunction(x):
    result = 1
    for i in range(1,x):
        result *= i
    return result

#timed(lambda: myfunction(100000))()
