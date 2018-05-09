import unittest # UI tests require a unique framework for testing
from grocery import ShopList

class TestGroceryApp(unittest.TestCase):

    def setUp(self, grocery_store):
        print("SETUP")
        self.grocery = ShopList("fiesta")

    def test_add(self):
        grocery = ShopList("fiesta")
        print("test_add")
        groceries = ["milk $1.85" , "soda $1.25", "fish $5.50"]
        result = grocery.add(groceries)
        self.assertEqual(groceries ,result)

    def test_add2(self):
        grocery = ShopList("walmart")
        print("test_add2")
        groceries = ["paper $2.85" , "napkins $2.25", "plate $5.50", "chips $2.42"]
        result = grocery.add2(groceries)
        self.assertEqual(groceries,result)

    def test_add3(self):
        grocery = ShopList("sams")
        print("test_add3")
        groceries = ["chicken $2.85" , "beef $2.25", "eggs $5.50", "sugar $2.42", "salt $1.15" , "pepper $1.22", "honey $2.05"]
        result = grocery.add3(groceries)
        self.assertEqual(groceries, result)

    def tearDown(self):
        print("TEAR DOWN")


if __name__ == '__main__':
    unittest.main()