all_trio_monday_night_=[]
all_trio_tuesday_night_= []
all_trio_wednesday_night_ = []
all_trio_thursday_night_ = []
all_trio_friday_night_ = []
all_trio_saturday_night_ = []
all_trio_night_days_ = []

def all_trio_nights(x):  # x is all_trio_numbers
    for i in range(1,len(x),2):
        all_trio_night_days_.append(x[i])
    return all_trio_night_days_

def all_trio_monday_night(x):
    for i in range(1, len(x), 12):
        all_trio_monday_night_.append(x[i])
    return all_trio_monday_night_

def all_trio_tuesday_nigt(x):
    for i in range(3, len(x), 12):
        all_trio_tuesday_night_.append(x[i])
    return all_trio_tuesday_night_

def all_trio_wednesday_night(x):
    for i in range(5, len(x), 12):
        all_trio_wednesday_night_.append(x[i])
    return all_trio_wednesday_night_

def all_trio_thursday_night(x):
    for i in range(7, len(x), 12):
        all_trio_thursday_night_.append(x[i])
    return all_trio_thursday_night_

def all_trio_friday_night(x):
    for i in range(9, len(x), 12):
        all_trio_friday_night_.append(x[i])
    return all_trio_friday_night_

def all_trio_saturday_night(x):
    for i in range(11, len(x), 12):
        all_trio_saturday_night_.append(x[i])
    return all_trio_saturday_night_
