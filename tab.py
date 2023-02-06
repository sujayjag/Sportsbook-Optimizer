# import the module 
import pandas 
from tabulate import tabulate

# consider the food data 
food_input={'id':['foo-23','foo-13','foo-02','foo-31'], 
            'name':['ground-nut oil','almonds','flour','cereals'], 
            'cost':[567.00,562.56,67.00,76.09], 
            'quantity':[1,2,3,2]}

# pass this food to the dataframe by specifying rows
dataframe=pandas.DataFrame(food_input,index = ['item-1', 'item-2', 'item-3', 'item-4']) 

# dispay the entire dataframe in github format
print(tabulate(dataframe, headers='keys', tablefmt='github'))

