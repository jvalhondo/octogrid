# -*- coding: utf-8 -*-

"""
octogrid.utils.utils

This module implements some utility functions required by the package 
"""


def username_to_file(username):
	"""
	Return the network file name according to the username
	"""

	return '{0}.gml'.format(username)


def build_dependecies():
	"""
	Returns a list representing all the required packages
	"""

	package_list = []

	with open('requirements.txt', 'r') as f:
		lines = f.readlines()

	for line in lines:
		name, version = line.split('==')
		package_list.append('{0}>={1}'.format(name, version))

	return package_list