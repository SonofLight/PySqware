#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Retrieve individual store Categories.

'''
from sqware.catalog import ItmJson

class Sq_Products(object):
	'''
	'''
	def __init__(self):
		'''
		'''
		self.item_json = ItmJson()

	def __str__(self):
		return '{}'.format('Sq_Products Module')

	def get_category_items(self, category_id):
		'''
		'''
		self.json_data = self.item_json.retrieve_json()
		try:
			#products results list 
			category_items = []
			#loops through json data and returns associated items.
			for products in self.json_data['objects']:
				for key, value in products['item_data'].items():
					if category_id == value:
						category_items.append(products)

			#if products are placed in list, returns list
			if category_items:
				return category_items

		except TypeError as e:
			return str(e)



	


		