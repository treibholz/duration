#!/usr/bin/python3
import yaml
import os
import sys
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration
configfile = os.path.expanduser(os.getenv('DURATION_CONF','~/.duration.yaml'))
if os.path.isfile(configfile):
    data = yaml.load(open(configfile))
else:
    data =  { 'engine': 'google',
                'places': {
                    'home': 'Hauptstrasse 1, Neustadt',
                    'work': 'Kirchgasse 1, Neustadt' }}
    print("Writing stupid dummy configuration to {0}".format(configfile))
    f = open(configfile, 'w')
    yaml.dump(data, indent=2, default_flow_style=False, stream=f)
    f.close()

# opts (very primitive)
try:
    origin = data['places'][sys.argv[1]]
    destination = data['places'][sys.argv[2]]
except:
    if datetime.datetime.now().hour <= 12:
        origin = data['places']['home']
        destination = data['places']['work']
    else:
        origin = data['places']['work']
        destination = data['places']['home']

# Start the work!

print("From: {0}\n  To: {1}\n".format(origin, destination))

base_url = 'https://www.google.com/maps/dir/{0}/{1}'
url = base_url.format(origin, destination,)
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('temp-profile')
options.add_argument('incognito')
driver = webdriver.Chrome(options=options)
driver.get(url)

try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "section-directions-trip-description")
        )
    )
    elem = driver.find_element_by_class_name("section-directions-trip-description")

    print(elem.text)

except:
    # TODO: better exception handling
    print("OOPS: Something went wrong, try again! :-)")

driver.quit()
