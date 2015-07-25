# Simple Tornado Web Server

## Prerequisites

* Python Version 2.5, 2.6, and 2.7.

Check your version:

	$(which python) -V

If not installed:

	apt-get install python2.7

* simplejson IF Python 2.5

	sudo apt-get install python-simplejson

* PycURL (version 7.18.2 or higher)

Check your version:

	dpkg -s python-pycurl | grep Version

If not installed:

	sudo aptitude install python-pycurl

## Install

	sudo apt-get install pip
	sudo pip install tornado

## Run it:

	python server.py

## Navigate

	http://localhost:8080

