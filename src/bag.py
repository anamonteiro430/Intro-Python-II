from item import Item

class Bag:
     def __init__(self, items, count):
          self.items = []
          self.count = len(self.items)
     
     def __str__(self):
          return f"You have {self.count} items in your bag: {self.items}"
          
     def pickup_item(self, item):
          self.items.append(item)

     def drop_item(self):
          items.remove(self) 

     def print_items(self):
          for i in self.items:
               print(i)