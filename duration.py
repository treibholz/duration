#!/usr/bin/python3
import yaml
import os
import sys
import distutils.spawn

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
                'google': {
                    'home': 'Hauptstrasse 1, Neustadt',
                    'work': 'Kirchgasse 1, Neustadt' }}
    print("Writing stupid dummy configuration to {0}".format(configfile))
    f = open(configfile, 'w')
    yaml.dump(data, indent=2, default_flow_style=False, stream=f)
    f.close()

engine = data['engine']
# opts (very primitive)
try:
    origin = data[engine][sys.argv[1]]
    destination = data[engine][sys.argv[2]]
except:
    if datetime.datetime.now().hour <= 12:
        origin = data[engine]['home']
        destination = data[engine]['work']
    else:
        origin = data[engine]['work']
        destination = data[engine]['home']

# Start the work!

print("From: {0}\n  To: {1}\n".format(origin, destination))

if engine == 'bing':
    # VERY experimentaö
    base_url = 'https://www.bing.com/maps?osid={0}&cp={1}'
    url = base_url.format(origin, destination,)
    info_class_name = 'directionsRouteLink'
else:
    base_url = 'https://www.google.com/maps/dir/{0}/{1}'
    url = base_url.format(origin, destination,)
    info_class_name = 'section-directions-trip-description'

options = webdriver.ChromeOptions()
# Use chromium instead of google-chrome, if available
options.binary_location = distutils.spawn.find_executable('chromium')
options.add_argument('headless')
options.add_argument('temp-profile')
options.add_argument('incognito')
driver = webdriver.Chrome(options=options)
driver.get(url)

try:
    WebDriverWait(driver, 300).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, info_class_name)
        )
    )
    elem = driver.find_element_by_class_name(info_class_name)

    print(elem.text)

except:
    # TODO: better exception handling
    print("OOPS: Something went wrong, try again! :-)")

#driver.quit()
