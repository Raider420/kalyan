all_single_night_monday_=[]
all_single_night_tuesday_= []
all_single_night_wednesday_ = []
all_single_night_thursday_ = []
all_single_night_friday_ = []
all_single_night_saturday_ = []
all_single_night_days_ = []

def all_single_nights(x):   # x is all_single_numbers
    for i in range(1,len(x),2):
        all_single_night_days_.append(x[i])
    return all_single_night_days_

def all_single_night_monday(x):
    for i in range(1,len(x),12):
        all_single_night_monday_.append(x[i])
    return all_single_night_monday_
def all_single_night_tuesday(x):
    for i in range(3,len(x),12):
        all_single_night_tuesday_.append(x[i])
    return all_single_night_tuesday_
def all_single_night_wednesday(x):
    for i in range(5,len(x),12):
        all_single_night_wednesday_.append(x[i])
    return all_single_night_wednesday_
def all_single_night_thursday(x):
    for i in range(7,len(x),12):
        all_single_night_thursday_.append(x[i])
    return all_single_night_thursday_
def all_single_night_friday(x):
    for i in range(9,len(x),12):
        all_single_night_friday_.append(x[i])
    return all_single_night_friday_
def all_single_night_saturday(x):
    for i in range(11,len(x),12):
        all_single_night_saturday_.append(x[i])
    return all_single_night_saturday_


