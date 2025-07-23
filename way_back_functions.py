import pandas as pd
import numpy as np
from datetime import datetime as dt
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import os
import time
import codecs
from tqdm import tqdm
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

import requests

def get_closest_snapshots(domain, first_date, last_date):
    base_url = "https://web.archive.org/cdx/search/cdx"

    # Get latest snapshot BEFORE the date
    before_params = {
        "url": domain,
        "to": first_date,
        "limit": 1,
        "output": "json",
        "sort": "desc"
    }
    before_resp = requests.get(base_url, params=before_params)
    before = before_resp.json()[1] if len(before_resp.json()) > 1 else None

    # Get earliest snapshot AFTER the date
    after_params = {
        "url": domain,
        "from": last_date,
        "limit": 1,
        "output": "json",
        "sort": "asc"
    }
    after_resp = requests.get(base_url, params=after_params)
    after = after_resp.json()[1] if len(after_resp.json()) > 1 else None

    return {
        "before": before,
        "after": after
    }
