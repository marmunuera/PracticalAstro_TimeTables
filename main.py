# IMPORTS
import os
from io import StringIO
import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import sgp4 as s4
from sgp4 import omm
from sgp4.api import Satrec
from sgp4.io import twoline2rv
from sgp4.api import jday
import datetime
import math
from math import trunc
import requests
import shutil
import sys
import getopt
from sgp4.api import WGS72OLD, WGS72, WGS84
import configparser
from mpl_toolkits.basemap import Basemap
import pandas as pd


# functions to download the tables

def get_table_correction_UT1(): # this function saves the most recent final.txt
    URL = "https://maia.usno.navy.mil/ser7/finals.daily"
    response = requests.get(URL)
    print("downloading final.dailys....")
    open("finals.daily.txt", "wb").write(response.content)
    return 0

def get_table_correction_GPS(): # this function saves the most recent leap seconds table
    URL = "https://maia.usno.navy.mil/ser7/tai-utc.dat"
    response = requests.get(URL)
    print("downloading /tai-utc....")
    open("leapSecondsTable.txt", "wb").write(response.content)
    return 0

def main():
    # definition of necessary constants:
    command= sys.argv[1]

    file_finals = os.path.exists("finals.daily.txt")
        if not file_finals:
            print("finals.daily.txt does not exist, it has to be downloaded")
            get_table_correction_UT1()

    file_leapSec = os.path.exists("leapSecondsTable.txt")
        if not file_finals:
            print("leapSecondsTable.txt does not exist, it has to be downloaded")
            get_table_correction_GPS()



if __name__ == "__main__":
    main()
