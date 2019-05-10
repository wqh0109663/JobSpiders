import time
import os
import csv
import logging
from pprint import pprint
from collections import Counter
import numpy as np
import requests
import matplotlib.pyplot as plt
import matplotlib as mpl
import jieba
import pymysql
from gevent import monkey
from gevent.pool import Pool
from queue import Queue
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import synonyms