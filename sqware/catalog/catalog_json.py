#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from pathlib import Path
from sqware.connect import Sq_Connect



class ItmJson(object):
	'''
	Item/Products json Data.
	'''
	def __init__(self, directory_path):
		self.connect = Sq_Connect()
		self.dir_path = directory_path

	def __str__(self):
		return 'ItmJson path: {}'.format(self.dir_path)

	def __get_item_json(self):
		'''
		Retrieves JSON data for all items/products in square catalog. 
		'''
		#gets data from square catalog endpoint
		self.get_data = self.connect.get('/v2/catalog/list?types=item')
		#decodes json data
		self.retrieved_data = self.get_data.json()
		#prettifies json data
		self.json_data = json.dumps(self.retrieved_data, sort_keys=True, indent=4)
		return self.json_data

	def __directory_check(self):
		'''
		Checks if directory exists. If it doesn't creates directory in user supplied path.
		Creates a new directory if none exist. 

		*** mkdir flag - "exist_ok=False" prevents additional directories from being created. see documentation ***
		'''
		#set directory path
		self.dir_name = Path(self.dir_path + 'json')
		#tests if directory exists. creates new one if it doesnt.
		while not self.dir_name.exists():
			
			self.dir_name.mkdir(parents=True, exist_ok=False)
		else:
			return self.dir_name.exists()

	def __write_item_json(self, path_name, json_data):
		'''
		Checks if there is a json file exists.
		Creates file if none exists.
		Will overwrite any files that exists.

		*** May add a test for last time file modified and if any changes occured. ***
		'''
		self.directory = self.__directory_check()
		self.file_name = Path(path_name + 'json/items.json')
		try:
			#if directory exists.
			if self.directory:
				#creates file if none.
				while not self.file_name.exists():
					with open(self.file_name, 'w') as file:
						file.write(json_data)
			#overwrites file if exists.
			elif self.file_name.exists():
				with open(self.file_name, 'w') as file:
					file.write(json_data)
		except IOError as e:
			return(str(e))

	# def create_json(self):
	# 	'''
	# 	initiates the json retrieval and file writing class methods
	# 	'''
	# 	self.__write_item_json(self.dir_path, self.__get_item_json())

	def retrieve_json(self):
		'''
		Opens created json data file and returns it for iteration.
		'''
		#calls __write_item_json()
		self.create_json_file = self.__write_item_json(self.dir_path, self.__get_item_json())
		#calls __directory_check()
		self.directory = self.__directory_check()
		self.file_name = Path(self.dir_path +'json/items.json')
		try:

			if self.directory:
				if self.file_name.exists():
					with open(self.file_name, 'r') as json_file:
						json_data = json.load(json_file)
						return json_data
			else:
				return ('Directory not found. directory_check() returned : {}').format(self.directory)
		except OSError as e:
			return str(e)

class CategoryJson(object):
	'''
	Category Json Data.
	'''
	def __init__(self, directory_path):
		self.connect = Sq_Connect()
		self.items = ItmJson(directory_path=directory_path)
		self.dir_path = directory_path

	def __str__(self):
		return 'CategoryJson path: {}'.format(self.dir_path)

	def __get_category_json(self):
		self.get_cat_data = self.connect.get('/v1/' + self.connect.location_id + '/categories')
		#decodes json data
		self.retrieved_data = self.get_cat_data.json()
		#prettifies json data
		self.json_data = json.dumps(self.retrieved_data, sort_keys=True, indent=4)
		return self.json_data

	def __directory_check(self):
		'''
		Checks if directory exists. If it doesn't creates directory in user supplied path.
		Creates a new directory if none exist. 

		*** mkdir flag - "exist_ok=False" prevents additional directories from being created. see documentation ***
		'''
		#set directory path
		self.dir_name = Path(self.dir_path + 'json')
		#tests if directory exists. creates new one if it doesnt.
		while not self.dir_name.exists():
			
			self.dir_name.mkdir(parents=True, exist_ok=False)
		else:
			return self.dir_name.exists()

	def __write_category_json(self, path_name, json_data):
		'''
		Checks if there is a json file.
		Creates file if none exists.
		Will overwrite any files that exists.

		*** May add a test for last time file modified and if any changes occured. ***
		'''
		self.directory = self.__directory_check()
		self.file_name = Path(path_name + 'json/category.json')
		try:
			#if directory exists.
			if self.directory:
				while not self.file_name.exists():
					with open(self.file_name, 'w') as file:
						file.write(json_data)
			#overwrites file if exists.
			elif self.file_name.exists():
				with open(self.file_name, 'w') as file:
					file.write(json_data)
		except IOError as e:
			return(str(e))

	def retrieve_json(self):
		'''
		Opens created json data file and returns it for iteration.
		'''
		#calls __write_item_json()
		self.create_json_file = self.__write_category_json(self.dir_path, self.__get_category_json())
		#calls __directory_check()
		self.directory = self.__directory_check()
		self.file_name = Path(self.dir_path +'json/category.json')
		try:
			if self.directory:
				if self.file_name.exists():
					with open(self.file_name, 'r') as json_file:
						json_data = json.load(json_file)
						return json_data
			else:
				return ('Directory not found. directory_check() returned : {}').format(self.directory)
		except OSError as e:
			return str(e)



