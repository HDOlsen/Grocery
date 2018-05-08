import unittest

class   ShopList:
      def __init__(self, grocery_store):
        self.grocery_store = grocery_store
        self.groceriesf = []
        self.groceriesw = []
        self.groceriess = []

      def add(self, item):
          self.groceriesf.append(item)
        
      def add2(self, item):
          self.groceriesw.append(item)

      def add3(self, item):
          self.groceriess.append(item)
          
User1 = ShopList("fiesta")
groceries = ["milk $1.85" , "soda $1.25", "fish $5.50"]
User1.add(groceries)

for item in User1.groceriesf:
    print(item)
for index in range(0, len(User1.groceriesf)):
    print(User1.groceriesf[index])

User1 = ShopList("walmart")
groceries = ["paper $2.85" , "napkins $2.25", "plate $5.50", "chips $2.42"]
User1.add2(groceries)

for item in User1.groceriesw:
    print(item)
for index2 in range(0, len(User1.groceriesw)):
    print(User1.groceriesw[index2])

User1 = ShopList("sams")
groceries = ["chicken $2.85" , "beef $2.25", "eggs $5.50", "sugar $2.42", "salt $1.15" , "pepper $1.22", "honey $2.05"]
User1.add3(groceries)

for item in User1.groceriess:
    print(item)
for index3 in range(0, len(User1.groceriess)):
    print(User1.groceriess[index3])






