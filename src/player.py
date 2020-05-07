# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
     def __init__(self, room, color):
          self.room = room
          self.color = color

     def __str__(self):
          return f"<Your name is {self.color}, you are in room: {self.room}>"

     #Methods
     def select_color(self):
          print('Select a color')
          color = input("[r]ed \n [g]reen \n [b]lue")
          
          if color == 'r':
               Player.color = "red"
     


