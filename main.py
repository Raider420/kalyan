import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from bs4 import BeautifulSoup
from all_single_morning import  *
from all_trio_morning import  *
from all_double_days import *
from all_single_night import *
from all_trio_night import *
from single_numbers import *
from double_numbers import *
from trio_numbers import *
from frequency import *
import collections


url = "https://sattamatka.report/kalyan-matka-panel-chart"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html5lib')
single_numbers_= enumerate(soup.findAll('td', attrs={'class': 'border_left_right'}))
double_numbers_= enumerate(soup.findAll('td', attrs={'class': 'border_left_right'}))
trio_numbers_= enumerate(soup.findAll('td',attrs={'class':''}))

all_single_numbers_ = single(single_numbers_)
all_double_numbers_ = double(double_numbers_)
all_trio_numbers_ = trio(trio_numbers_)







