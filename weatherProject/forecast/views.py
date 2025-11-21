from django.shortcuts import render

# Create your views here.

import requests
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from datetime import datetime, timedelta
import pytz

def weather_view(request) :
    return HttpResponse('<h1>Weather Prediction App</h1>')