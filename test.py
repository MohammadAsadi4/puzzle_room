from random import choice, choices, randint


room_name = ''
'''room_places devides room into a 5*5 matris(2d list). each item of matris
has a pair of (furniture,puzzle) element'''
pair = ['f','p']
rows, clos = (5,5)
room_places = [[pair]*clos]*rows

'''here we define diffrent kind of furniture for diffrent rooms'''
local_furniture = ['chair', 'table', 'sofa', 'lamp', 'plant', 'none']
bedroom_furniture = ['bed', 'side table', 'closet', 'dressing table', 'none']
kitchen_furniture = ['oven', 'fridge', 'dinnig table', 'washing machine',
                    'food processor', 'kettle', 'none']
studyroom_furniture = ['liberary', 'chair', 'office table', 'arm chair', 'none']
room_fur_pair = {'hall':'local_furniture', 'bedroom':'bedroom_furniture',
                 'kitchen':'kitchen_furniture', 'studyroom':'studyroom_furniture'}

'''this method gets the room's name and furnish it!(put furniture in room_places)'''
def room_furniture(r_name):
    if r_name in room_fur_pair:
        for i in range(25):
            room_places[randint(0,6)[choices(room_fur_pair.get(r_name),k = 5),'puzzle']][randint(0,6)]
        print(room_places)
    else:
        print('room\'s name is in incorrect.')
room_name = input('Enter room name:')
room_furniture(room_name)
