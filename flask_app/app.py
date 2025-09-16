# app.py

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend before importing pyplot

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import io
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import mlflow
import numpy as np
import joblib
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from mlflow.tracking import MlflowClient
import matplotlib.dates as mdates
import traceback

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
# Temporary debug in predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        print("Received JSON:", data)
    except Exception as e:
        print("JSON parsing error:", e)

