# You have a table with all available goods in the store. 
# The data is represented as a list of dicts

# Your mission here is to find the TOP most expensive goods. 
# The amount we are looking for will be given as a first argument and the whole data as the second one

# Input: int and list of dicts. Each dicts has two keys "name" and "price"

# Output: the same as the second Input argument.

# def bigger_price(limit: int, data: list) -> list:
#     """
#         TOP most expensive goods
#     """
#     # your code here
#     return None

limit = 2
data = [{"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}]

lst = sorted(data, key=lambda x: x['price'], reverse = True)[:limit]

print(lst)