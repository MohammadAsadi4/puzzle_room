# global.py
floor_no = 0
floor_dim = [10, 10] #this is the dimention of a floor it's a 10*10 matris

 #here we define spcific rooms of a given floor
 ground_floor = ['hall', 'kitchen', 'bathroom']
 first_floor = ['bedroom', 'studyroom', 'balcony']
 basement = ['warehouse', 'facility', 'stairway']

 #these parts is not a room but exists in some floors
 floor_parts = ['balcony', 'facility', 'stairway']

 #definition of the dimention of diffrent rooms
 rooms_parts_dim = {'bedroom':[5,5], 'stydyroom':[7,7], 'kitchen':[6,4],
                     'hall':[5,10], 'bathroom':[3,3], 'warehouse':[6,5],
                     'balcony':[3,3], 'stairway':[2,10], 'facility':[4,4]}

 #four corners of a floor
 corners = {'topleft':[0,0], 'topright':[0,10], 'downleft':[10,0],
             'downright':[10,10]}

 rooms = ['bedroom', 'studyroom', 'kitchen', 'hall', 'bathroom', 'warehouse']

 room_position = dict(floor = [], room = [], positions = [])
