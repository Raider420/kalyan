all_double_monday_ = []
all_double_tuesday_  = []
all_double_wednesday_ = []
all_double_thursday_ = []
all_double_friday_ =[]
all_double_saturday_ = []

def all_double_monday(x): # x is list of all double numbers
    for i in range(0,len(x),6):
        all_double_monday_.append(x[i])
    return all_double_monday_

def all_double_tuesday(x):
    for i in range(1,len(x),6):
        all_double_tuesday_.append(x[i])
    return all_double_tuesday_

def all_double_wednesday(x):
    for i in range(2,len(x),6):
        all_double_wednesday_.append(x[i])
    return all_double_monday_

def all_double_thursday(x):
    for i in range(3,len(x),6):
        all_double_thursday_.append(x[i])
    return all_double_thursday_

def all_double_friday(x):
    for i in range(4,len(x),6):
        all_double_friday_.append(x[i])
    return all_double_friday_

def all_double_saturday(x):
    for i in range(5,len(x),6):
        all_double_saturday_.append(x[i])
    return all_double_saturday_






