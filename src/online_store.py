###Online Store
from datetime import datetime

#List of objects to model
""" 
Users
          Customers
          Vendors
          Admin
Products
Purchases 
"""

#Attributes for each object
"""
Users
     Attributes
          name
          is the user an admin?
     Customers
          Attributes
               name
               a collection of purchases
     Vendors
          Attributes
               name
               a collection of products
     Admin
          name
          a flag that the user is an admin
Products
     Attributes
          name
          price
          vendor
Purchases
     Attributes
          product
          customer
          price
          date and time info about when the purchase was completed
"""

#Relationships between the objects
""" Sellers have products (one to many)
Customers have purchases (one to many)
Purchases have products (one to many) """

#User Class - Base class that all user types will inherit from
class User:
     def __init__(self, name, is_admin=False):
          self.name = name
          self.is_admin = is_admin

##Users
class Admin(User):
    def __init__(self, name):
        super().__init__(name, is_admin=True)

class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.purchases = []
    #customer purchases a product~
    def purchase_product(self, product):
         purchase = Purchase(product, self)
         self.purchases.append(purchase)

class Vendor(User):
    def __init__(self, name):
        super().__init__(name)
        self.products = []
    ##vendor creates a product
    def create_product(self, product_name, product_price):
         product = Product(product_name, product_price, self)
         self.products.append(product)

#These don't inherit from other classes
class Product:
    def __init__(self, name, price, vendor):
        self.name = name
        self.price = price
        self.vendor = vendor

class Purchase:
    def __init__(self, product, customer):
        self.product = product
        self.customer = customer
        self.purchase_price = product.price
        self.purchase_data = datetime.now()





