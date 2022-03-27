all_single_morning_monday_=[]
all_single_morning_tuesday_= []
all_single_morning_wednesday_ = []
all_single_morning_thursday_ = []
all_single_morning_friday_ = []
all_single_morning_saturday_ = []
all_single_morning_days_ = []

def all_single_morning_days(x):  # x is all_single_numbers
    for i in range(0,len(x),2):
        all_single_morning_days_.append(x[i])
    return all_single_morning_days_

def all_single_morning_monday(x): # x is all_single_numbers
    for i in range(0,len(x),12):
        all_single_morning_monday_.append(x[i])
    return all_single_morning_monday_

def all_single_morning_tuesday(x):
    for i in range(2,len(x),12):
        all_single_morning_tuesday_.append(x[i])
    return all_single_morning_tuesday_
def all_single_morning_wednesday(x):
    for i in range(4, len(x), 12):
        all_single_morning_wednesday_.append(x[i])
    return all_single_morning_wednesday_
def all_single_morning_thursday(x):
    for i in range(6, len(x), 12):
        all_single_morning_thursday_.append(x[i])
    return all_single_morning_thursday_
def all_single_morning_friday(x):
    for i in range(8, len(x), 12):
        all_single_morning_friday_.append(x[i])
    return all_single_morning_friday_
def all_single_morning_saturday(x):
    for i in range(10, len(x),12):
        all_single_morning_saturday_.append(x[i])
    return all_single_morning_saturday_


