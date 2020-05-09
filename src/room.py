# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
from item import Item

class Room():
     def __init__(self, name, description, occupants, items=[]):
          self.name = name
          self.description = description
          self.occupants = occupants
          self.items = [Item(*i) for i in items]
     
     def __str__(self):
        return f"{self.name}"

     def print_description(self):
        return f"{self.description}"
     

     def print_items(self):
         for i in self.items:
              print(i)

     def remove_item(self, item):
        for i in self.items:
            if item.name == i.name:
                self.items.remove(i)

     def add_item(self, item):
        self.items.append(item)