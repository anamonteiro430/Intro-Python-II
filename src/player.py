# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
     def __init__(self, color, position):
          self.color = color
          self.position = position
          self.bag = []

     def __str__(self):
          return f"Your name is {self.color}."

     def move_to(self, direction, current_pos):
        attribute = direction + '_to'
        # if we can move in specified direction from our current location 
        if hasattr(current_pos, attribute):
            # get the room in the specified 
            return getattr(current_pos, attribute)
        
        # if we can't go that way 
        print("You hit a wall. Try again\n")

        return current_pos

     def pickup(self, item):
        self.bag.append(item)
        self.position.remove_item(item)

     def display_bag(self):
        message = "In your bag: "
        for item in self.backpack:
            message += f"{item.name}, "
        print(message)


