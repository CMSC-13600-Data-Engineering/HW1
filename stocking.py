'''
Program that analyzes whether Sakila is appropriately stocked.
'''
import sqlite3
import pandas as pd

#TODO fill in
def connect(filename):
	'''Returns a connection to the Sakila database refered
	   by the provided file name
	'''
	pass


#TODO fill in
def inventory_dataset(con):
	'''Returns a pandas dataframe where each row is a film and 
	   with the following attributes:
	   	* film name
	   	* number of copies in the inventory
	   	* number of times the film has been rented out
	   	* rental price
	   	* replacement pice
	'''
	pass


con = connect('sqlite-sakila.db')
df = inventory_dataset(con)
df.to_csv('inventory_dataset.csv')



