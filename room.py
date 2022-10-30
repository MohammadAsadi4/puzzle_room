from door import Door
from random import choice, choices, randint

class Room(floor):

    room_name = ''

    # room_places devides room into a 5*5 matris.each item of matris
    # has a pair of (furniture,puzzle) element(3-d list)
    pair = ['f','p']
    rows, clos = (5,5)
    room_places = [[pair]*clos]*rows

    # here we define diffrent kind of furniture for diffrent rooms
    local_furniture = ['chair', 'table', 'sofa', 'lamp', 'plant', 'none']
    bedroom_furniture = ['bed', 'side table', 'closet', 'dressing table', 'none']
    kitchen_furniture = ['oven', 'fridge', 'dinnig table', 'washing machine',
                        'food processor', 'kettle', 'none']
    studyroom_furniture = ['liberary', 'chair', 'office table', 'arm chair',
                        'none']
    room_fur_pair = {'hall':'local_furniture', 'bedroom':'bedroom_furniture',
                     'kitchen':'kitchen_furniture',
                     'studyroom':'studyroom_furniture'}

    # definition of puzzles
    math_puzzle = {'2':'1+1 =', '6':'2*3 =', '2':'square root of 4 =',
                    '8':'24 devide by 3 =', '9':'15-6 ='}
    text_puzzle = {'My son':'Brothers ans sister i have none but this man\'s father is my father\'s son.who is the man?',
                  'Nothing':'What is greater than God, more evil than devil, the poor have it, the rich need it, and if you eat it you will die',
                  'A coffin':'Who makes it, has no need of it.who buys it, has no use for it, who uses it can neither see nor feel it.what is that? ',
                  'A stamp':'What can travel around the world while staying in a corner?',
                  'An egg':'What has to be broken before you use it?',
                  'Piano':'What has many keys but can\'t open a single lock?',
                  'A fence':'What runs all around a backyard, yet never moves?'}
    puzzle = math_puzzle + text_puzzle

    # this method gets the room's name and furnish it whit furniture an puzzles!
    # (put room specific furniture and puzzle in room_placesand
    # creates a ['furniture','puzle'])
    def room_furniture(self, r_name):
        if r_name in room_fur_pair:
            for i in range(randint(1,5)):
                room_places[randrange(5)][randrange(5)][randrange(2)] =
                [choices(room_fur_pair.get(r_name), k=1),
                 choices(puzzle.items(randint(1,len(puzzle)), k=1)]
        else:
                print('room\'s name is in incorrect.')


    #this methode save the current state of the room after generating
    # room objects like furniture, puzzle, ...
    def room_set_status(self):
        status_file = open("/home/mohammad/projects/skeleton/puzzle_room/
                             statusfile.txt", "w")
        for row in range(5):
            for col in range(5):
                for k in range(2):
                    status_file.write(room_places[k][col][row]+"\n")
        status_file.close()

    def room_get_status(self):
        status_file = open("/home/mohammad/projects/skeleton/puzzle_room/
                            statusfile.txt", "r")
        for row in range(5):
            for col in range(5):
                for k in range(2):
                    room_places[k][col][row] = status_file.readline()
        status_file.close()
