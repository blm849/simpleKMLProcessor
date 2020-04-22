########################################################################################
#
# processKMLfile.py                                 
#
# Description:
#  
#	This program will process a KML file downloaded from Google Maps. These files 
#   have a format this program recognizes, namely they have XML which contain name
#   and description information in a placemark block.
#
# History:
#
#       2020.03.17	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python processKMLfile.py inputKMLfile.ini 
#		where inputKMLfile contains the name of the KML file to process.
#
#######################################################################################

import ConfigParser				# needed to process the ini file
import sys						# needed to process input parameters in the ini file
from bs4 import BeautifulSoup	# needed to process the KML file


# Process the input parameters and get the name of the ini file

if len(sys.argv) == 2:
	iniFile = sys.argv[1]
else:
	print "you need to pass an ini file as input"
	sys.exit()

# The format of inputKMLfile.ini is like this (minus the #). 
# Note, no quote around the string
#[DEFAULT]
#inputKMLfile = KML file name

# Read the ini file

config = ConfigParser.ConfigParser()
config.read(iniFile)

# Get the name of the KML file from it and read the contents

inputKMLfile = config.get('DEFAULT', 'inputKMLfile')

iniFileContents = open(inputKMLfile,"r")
contents = iniFileContents.read()

# Process the contents of the KML file with Beautiful soup

soup = BeautifulSoup(contents,'html.parser')
placemarks = soup.find_all('placemark')

# Create output which is an ordered HTML list. The list items will contain the name
# and description of each entry in the KML file

print "<ol>"
for placemark in placemarks:

	name = placemark.find('name').string
	try:
		desc = placemark.find('description').string
	except:
		desc = "NA"
	outline = "<li><b>" + name + "</b>: " + desc + "</li>"
	print outline.encode('utf8')
	
print "</ol>"


   


