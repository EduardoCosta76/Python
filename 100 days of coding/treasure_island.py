

print('Welcome to Treasure Island game. In this game you will need to find the treasure, but be careful! Your choices will be very important here!')
crossroad = str(input('You are at a crossroad. Where do you want to go? Type "left" or "right": ')).lower().strip()
if crossroad == 'right':
    print('You have come to a lake. There is an island in the middle of the lake.', end=' ')
    swim = str(input('Type "wait" to wait for a boat, or type "swim" to swim across. ')).lower().strip()
    if swim == 'swim':
        print('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.', end=' ')
        color = str(input('''Which colour do you choose? 
        [R] - Red:  
        [Y] - Yellow: 
        [B] - Blue: ''')).lower().strip()
        if color == 'r':
            print('It is a room full of fire. Game over!')
        elif color == 'y':
            print('You found the treasure! You win!')
        elif color == 'b':
            print('You enter a room of beasts. Game over!')
        else:
            print('You chose a door that does not exist. Game over!')
    else:
        print('You get attacked by an angry trout. Game over!')
else:
    print('You fell into a hole. Game over!')