all_trio_morning_monday_=[]
all_trio_morning_tuesday_= []
all_trio_morning_wednesday_ = []
all_trio_morning_thursday_ = []
all_trio_morning_friday_ = []
all_trio_morning_saturday_ = []
all_trio_morning_days_ = []

def all_trio_mornings(x):  # x is all_trio_numbers
    for i in range(0,len(x),2):
        all_trio_morning_days_.append(x[i])
    return all_trio_morning_days_

def all_trio_monday_morning(x):
    for i in range(0, len(x), 12):
        all_trio_morning_monday_.append(x[i])
    return all_trio_morning_monday_

def all_trio_tuesday_morning(x):
    for i in range(2, len(x), 12):
        all_trio_morning_tuesday_.append(x[i])
    return all_trio_morning_tuesday_

def all_trio_wednesday_morning(x):
    for i in range(4, len(x), 12):
        all_trio_morning_wednesday_.append(x[i])
    return all_trio_morning_wednesday_

def all_trio_thursday_morning(x):
    for i in range(6, len(x), 12):
        all_trio_morning_thursday_.append(x[i])
    return all_trio_morning_thursday_

def all_trio_friday_morning(x):
    for i in range(8, len(x), 12):
        all_trio_morning_friday_.append(x[i])
    return all_trio_morning_friday_

def all_trio_saturday_morning(x):
    for i in range(10, len(x), 12):
        all_trio_morning_saturday_.append(x[i])
    return all_trio_morning_saturday_
