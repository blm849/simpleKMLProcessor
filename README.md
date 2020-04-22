# simpleKMLProcessor
This repo contains software to process KML files

Currently it consists of two files:

- processKMLfile.py: a python program to process a KML file
- processKMLfile.ini: the input parameters for processKMLfile.py. Currently this ini file has one parameter:
	- inputKMLFile: the full name of the KML file you will process with processKMLfile.py
	
Some background: I wanted to take a KML map from Google Maps, extract key information from it
and then output it as an HTML ordered list. I would then manually take that HTML and put it
into a full HTML web page.

If you enter: python processKMLfile.py, it will read the processKMLfile.ini and then process the KML file referred to in the ini file.
