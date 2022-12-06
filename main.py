# IMPORTS
import os
from io import StringIO
import numpy as np
import requests
import shutil
import sys
import getopt



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

def check_for_Tables():
    file_finals = os.path.exists("finals.daily.txt")
    if not file_finals:
        print("File finals.daily.txt does not exist, it has to be downloaded")
        get_table_correction_UT1()
        print("File downloaded!")

    file_leapSec = os.path.exists("leapSecondsTable.txt")
    if not file_finals:
        print("File leapSecondsTable.txt does not exist, it has to be downloaded")
        get_table_correction_GPS()
        print("File downloaded !")

    print("All necessary tables are present in your directory.")
    return 0

def get_DUT1(): # get lists with MDJ and DUT1=UT1-UTC from the tables (UTC_to_UT1)

    # open text file in read mode
    text_file = open("finals.daily.txt", "r")
    # read whole file to a string
    data = []
    data = text_file.read().split('\n')
    text_file.close()

    if data[-1]=="":
        del data[-1]

    MJD=[0]*len(data)
    DUT1 = [0]*len(data)

    for i in range(len(data)):
        MJD[i]= float(data[i][7:14])
        DUT1[i]=float(data[i][58:67])

    return MJD, DUT1


def get_TAI_UTC(): # get lists with MDJ and errors

    # open text file in read mode
    text_file = open("leapSecondsTable.txt", "r")
    # read whole file to a string
    data = []
    data = text_file.read().split('\n')

    if data[-1]=="":
        del data[-1]

    text_file.close()

    MJD=[0]*len(data)
    TAI_UTC_1=[0]*len(data)
    TAI_UTC_2=[0]*len(data)
    TAI_UTC_3=[0]*len(data)

    for i in range(len(data)):
        MJD[i] = float(data[i][17:26])
        TAI_UTC_1[i]= float(data[i][38:42])
        TAI_UTC_2[i]= float(data[i][59:65])
        TAI_UTC_3[i]= float(data[i][70:78])

    return MJD, TAI_UTC_1, TAI_UTC_2,TAI_UTC_3


def main():
    # definition of necessary constants:

    #First I check that I have the tables in my directory or I download them
    check_for_Tables()

    # Get MJD and DUT1 lists
    MJD_1, DUT1 = get_DUT1()

    # get lists with MDJ and errors
    MJD_2, TAI_UTC_1, TAI_UTC_2,TAI_UTC_3 = get_TAI_UTC()

    # EXAMPLE OF HOW TO USE THE DATA:
    print("\nI want to know the last DUT1 and for what MJD it is:")
    print("MDJ: " + str(MJD_1[-1]) + " ; DUT1: " + str(DUT1[-1]))

    print("\nI want to know the last MDJ for which there is a correction in leap seconds:")
    print("MDJ: " + str(MJD_2[-1]) )

    print("Done.")



if __name__ == "__main__":
    main()