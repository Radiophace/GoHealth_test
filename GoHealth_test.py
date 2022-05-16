import json
import re
from textwrap import indent
from datetime import datetime


with open('Plan.json') as f: 
	plan = json.load(f)
plannInfos = plan['planInfos']



for cname in plannInfos:
    cname = cname["carrierName"]
    if cname == 'Humana' or cname == 'WellCare' or cname == 'Anthem':
        print('Carrier Name is fine: ', cname)    
    else:
        print ('Carrier name is wrong! It should be HUMANA, WELLCARE or ANTHEM')



for date_time_str in plannInfos:
    date_time_str = date_time_str["effectiveDate"]

try:
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
    print ("DATE correct and it is", date_time_obj.date())
except ValueError:
    print(" ERROR : This is the incorrect date string format. It should be YYYY-MM-DD")
    


for planid in plannInfos:
    planid = planid['planId']
    #pattern = re.compile(r'\d{5}[-]\d{3}[-]\d')
    pattern = re.compile(r'[0-9]+\-[0-9]+\-[0-9]+')
    results = pattern.finditer(planid)
    for result in results:
       print('PLAN ID is OK ', result)
  


for planName in plannInfos:
    planName = planName['planName']
    print('Plan Name: ', planName)


    submattcount = plan["submissionAttemptCount"]
    if submattcount > 5 or submattcount < 1:
        print (' ERROR Submission Attampt Count: ', submattcount)
    else:
        print(' OK Submission Attampt Count: ', submattcount)