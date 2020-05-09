from room import Room
from player import Player
from item import Item
from bag import Bag
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "0", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "0", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "0", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "0",[] ),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "0", []),
}


items = {
    'outside':  [Item("rock","North of you, the cave mount beckons"), Item("car","North of you, the cave mount beckons")],

    'overlook': Item("spider", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Item("cat", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ),

    'treasure': Item("mouse trap", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

'treasure': Item("paper", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

'treasure': Item("paper", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),


}

# Link rooms together


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

""" # Link items to rooms
room['outside'].has = 'rock'
room['outside'].has = 'car'
room['foyer'].has = 'spider'
room['foyer'].has = 'cat'
room['foyer'].has = 'mouse trap'
room['overlook'].has = 'paper'
room['overlook'].has = 'another rock'
room['narrow'].has = 'skeletons'
room['narrow'].has = 'eyeball'
room['treasure'].has = 'gold'
room['treasure'].has = '50 bucks'
 """

rock = Item("Rock", "heavy")
car = Item("Car", "You can go far away")

room["outside"].add_item(rock)
room["outside"].add_item(car)

# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("random_name", room["outside"])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
user_quits = False

print("**** WELCOME TO MY ADVENTURE GAME ****")
start = input("***** Press [s] to start, [q] to quit or [h] for help *****")
   
if start == "s":
    ### select color name
    print('***** Select a Color *****')
    color = input("[red], [green} or [blue] ")
    if color == "red" or color == "green" or color == "blue":
        player = Player(color, player.position)
        print('here')
        print(player)
    else:
        print("That's not a color!")
    while not user_quits:
        #Player first position
        print(player.position)
        print(player.position.print_description())
        print("\n")
        print(player.position.print_items())
        
        print("\n")
        print("***** What do you want to do *****")
        move = input('[l]ook around], [n]orth , [s]outh, [e]ast, [w]est\n')
        if move in ['n', 's', 'e', 'w']:
            player.position = player.move_to(move, player.position)
        elif move == "pickup":
            item_name = ' '.join(move[1:])
            for item in player.position.items:
                if item_name == item-name:
                    player.pickup(item)
            player.display_bag()
        else:
            print("That's not a direction")
elif start == "h":
    print('helping')
    print('help menu')
    help = input("[i]nstructions\n[B]ag\n[M]ap\n[I]nfo\n\n")
    if help == 'i':
        print("Use [n], [s], [e] and [w] keys to move around the game. You're going to hit walls but you'll fint the hidden treasure!")
        
elif start == "q":
    quit = input('Do you want to exit the game? [y]/[n]')
    if quit == "y":
        
        #close game
        print('closing....')
        user_quits = True
    elif quit == "n":
        pass
else:
    print('Invalid key')




