from random import shuffle
#pair = ['f','p']
#rows, clos = (5,5)
#room_places = [[pair]*clos]*rows
#print (room_places)
#for row in range(5):
    #for col in range(5):
    #    for k in range(2):
    #        print('(' + str(k) + ',' + str(col) + ',' + str(row) +')')
    #        '''print('------------------')
    #        print(col)
    #        print('*******************')
    #        print(row)
    #        print('###################')'''
    #        print(room_places[row][col][k])
#print(room_places)
# dict = {'a':[0,0], 'b':[1,1]}
# c = dict.get('a')
# print (c[0])
# print (dict.get('a')[0])
#from random import randint, shuffle
rooms_parts_dim = {'bedroom':[5,5], 'studyroom':[7,7], 'kitchen':[6,4],
                   'hall':[5,10], 'bathroom':[3,3], 'warehouse':[6,5],
                   'balcony':[3,3], 'stairway':[2,10], 'facility':[4,4]}
corners = [[0,0], [0,10], [10,0], [10,10]]
room_position = dict(floor = [], room = [], positions = [])


def create_floor(floor_name):

    shuffle(corners)#shufle the corners so evry room sets in random positions
    #these a,b,c and d points are the corners of a floor in clockwise order
    a = corners[0]
    b = corners[1]
    c = corners[2]
    d = corners[3]
    left_middle = [0,5]
    right_middle = [10,5]
    global room_position

    # start of making ground floor
    # start of making hall
    if (floor_name == 'ground_floor'):

        if (a[0] - left_middle[0] > 0) or (a[1] - left_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('hall')
            room_position.get('positions').append([a, [abs(a[0]-rooms_parts_dim.get('hall')[0]), a[1]],
            [abs(a[0]-rooms_parts_dim.get('hall')[0]), abs(a[1]-rooms_parts_dim.get('hall')[1])],
            [a[0], abs(a[1]-rooms_parts_dim.get('hall')[1])]])

        elif (a[0] - right_middle[0] > 0) or (a[1] - right_middle[1] > 0):

            room_position.get('floor').append(floor_name)
            room_position.get('room').append('hall')
            room_position.get('positions').append([a, [a[0], abs(a[1]-rooms_parts_dim.get('hall')[1])],
            [abs(a[0]-rooms_parts_dim.get('hall')[0]), abs(a[1]-rooms_parts_dim.get('hall')[1])],
            [a[0], abs(a[1]-rooms_parts_dim.get('hall')[1])]])

        elif (a[0] - left_middle[0] < 0) or (a[1] - left_middle[1] < 0):

            room_position.get('floor').append(floor_name)
            room_position.get('room').append('hall')
            room_position.get('positions').append([a, [a[0], a[1]+rooms_parts_dim.get('hall')[1]],
            [a[0]+rooms_parts_dim.get('hall')[0], a[1]+rooms_parts_dim.get('hall')[1]] ,
            [a[0]+rooms_parts_dim.get('hall')[0], a[1]]])

        elif (a[0] - right_middle[0] < 0) or (a[1] - right_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('hall')
            room_position.get('positions').append([a, [a[0], a[1]+rooms_parts_dim.get('hall')[1]],
            [a[0]+rooms_parts_dim.get('hall')[0], a[1]+rooms_parts_dim.get('hall')[1]] ,
            [a[0]+rooms_parts_dim.get('hall')[0], a[1]]])
        # end of creation of hall

        if (b[0] - left_middle[0] > 0) or (b[1] - left_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('kitchen')
            room_position.get('positions').append([b, [abs(b[0]-rooms_parts_dim.get('kitchen')[0]), b[1]],
            [abs(b[0]-rooms_parts_dim.get('kitchen')[0]), abs(b[1]-rooms_parts_dim.get('kitchen')[1])] ,
            [b[0], abs(b[1]-rooms_parts_dim.get('kitchen')[1])]])

        elif (b[0] - right_middle[0] > 0) or (b[1] - right_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('kitchen')
            room_position.get('positions').append([b, [b[0], abs(b[1]-rooms_parts_dim.get('kitchen')[1])],
            [abs(b[0]-rooms_parts_dim.get('kitchen')[0]), abs(b[1]-rooms_parts_dim.get('kitchen')[1])] ,
            [b[0], abs(b[1]-rooms_parts_dim.get('kitchen')[1])]])

        elif (b[0] - left_middle[0] < 0) or (b[1] - left_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('kitchen')
            room_position.get('positions').append([b, [b[0], b[1]+rooms_parts_dim.get('kitchen')[1]],
            [b[0]+rooms_parts_dim.get('kitchen')[0], b[1]+rooms_parts_dim.get('kitchen')[1]] ,
            [b[0]+rooms_parts_dim.get('kitchen')[0], b[1]]])

        elif (b[0] - right_middle[0] < 0) or (b[1] - right_middle[1] < 0):

            room_position.get('floor').append(floor_name)
            room_position.get('room').append('kitchen')
            room_position.get('positions').append([b, [b[0], a[1]+rooms_parts_dim.get('kitchen')[1]],
            [b[0]+rooms_parts_dim.get('kitchen')[0], b[1]+rooms_parts_dim.get('kitchen')[1]] ,
            [b[0]+rooms_parts_dim.get('kitchen')[0], b[1]]])
        # end of creation of kitchen

        if (c[0] - left_middle[0] > 0) or (c[1] - left_middle[1] > 0):

            room_position.get('floor').append(floor_name)
            room_position.get('room').append('bathroom')
            room_position.get('positions').append([c, [abs(c[0]-rooms_parts_dim.get('bathroom')[0]), c[1]],
            [abs(c[0]-rooms_parts_dim.get('bathroom')[0]), abs(c[1]-rooms_parts_dim.get('bathroom')[1])] ,
            [c[0], abs(c[1]-rooms_parts_dim.get('bathroom')[1])]])

        elif (c[0] - right_middle[0] > 0) or (c[1] - right_middle[1] > 0):

            room_position.get('floor').append(floor_name)
            room_position.get('room').append('bathroom')
            room_position.get('positions').append([c, [c[0], abs(c[1]-rooms_parts_dim.get('bathroom')[1])],
            [abs(c[0]-rooms_parts_dim.get('bathroom')[0]), abs(c[1]-rooms_parts_dim.get('bathroom')[1])] ,
            [c[0], abs(c[1]-rooms_parts_dim.get('bathroom')[1])]])

        elif (c[0] - left_middle[0] < 0) or (c[1] - left_middle[1] < 0):

            room_position.get('floor').append(floor_name)
            room_position.get('room').append('bathroom')
            room_position.get('positions').append([c, [c[0], c[1]+rooms_parts_dim.get('bathroom')[1]],
            [c[0]+rooms_parts_dim.get('bathroom')[0], c[1]+rooms_parts_dim.get('bathroom')[1]] ,
            [c[0]+rooms_parts_dim.get('bathroom')[0], c[1]]])

        elif (c[0] - right_middle[0] < 0) or (c[1] - right_middle[1] < 0):

            room_position.get('floor').append(floor_name)
            room_position.get('room').append('bathroom')
            room_position.get('positions').append([c, [c[0], c[1]+rooms_parts_dim.get('bathroom')[1]],
            [c[0]+rooms_parts_dim.get('bathroom')[0], c[1]+rooms_parts_dim.get('bathroom')[1]] ,
            [c[0]+rooms_parts_dim.get('bathroom')[0], c[1]]])
            # end of creation of bathroom
        #print (len(room_position.get('floor')))
    # end of making ground floor

    #start of making first floor
    shuffle(corners)
    a = corners[0]
    b = corners[1]
    c = corners[2]
    d = corners[3]
    if (floor_name == 'first_floor'):
        if (a[0] - left_middle[0] > 0) or (a[1] - left_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('bedroom')
            room_position.get('positions').append([a, [abs(a[0]-rooms_parts_dim.get('hall')[0]), a[1]],
            [abs(a[0]-rooms_parts_dim.get('bedroom')[0]), abs(a[1]-rooms_parts_dim.get('bedroom')[1])] ,
            [a[0], abs(a[1]-rooms_parts_dim.get('bedroom')[1])]])

        elif (a[0] - right_middle[0] > 0) or (a[1] - right_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('bedroom')
            room_position.get('positions').append([a, [a[0], abs(a[1]-rooms_parts_dim.get('bedroom')[1])],
            [abs(a[0]-rooms_parts_dim.get('bedroom')[0]), abs(a[1]-rooms_parts_dim.get('bedroom')[1])] ,
            [a[0], abs(a[1]-rooms_parts_dim.get('bedroom')[1])]])

        elif (a[0] - left_middle[0] < 0) or (a[1] - left_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('bedroom')
            room_position.get('positions').append([a, [a[0], a[1]+rooms_parts_dim.get('bedroom')[1]],
            [a[0]+rooms_parts_dim.get('bedroom')[0], a[1]+rooms_parts_dim.get('bedroom')[1]] ,
            [a[0]+rooms_parts_dim.get('bedroom')[0], a[1]]])

        elif (a[0] - right_middle[0] < 0) or (a[1] - right_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('bedroom')
            room_position.get('positions').append([a, [a[0], a[1]+rooms_parts_dim.get('bedroom')[1]],
            [a[0]+rooms_parts_dim.get('bedroom')[0], a[1]+rooms_parts_dim.get('bedroom')[1]] ,
            [a[0]+rooms_parts_dim.get('bedroom')[0], a[1]]])
        # end of creation of bedroom

        if (b[0] - left_middle[0] > 0) or (b[1] - left_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('studyroom')
            room_position.get('positions').append([b, [abs(b[0]-rooms_parts_dim.get('studyroom')[0]), b[1]],
            [abs(b[0]-rooms_parts_dim.get('studyroom')[0]), abs(b[1]-rooms_parts_dim.get('studyroom')[1])] ,
            [b[0], abs(b[1]-rooms_parts_dim.get('studyroom')[1])]])

        elif (b[0] - right_middle[0] > 0) or (b[1] - right_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('studyroom')
            room_position.get('positions').append([b, [b[0], abs(b[1]-rooms_parts_dim.get('studyroom')[1])],
            [abs(b[0]-rooms_parts_dim.get('studyroom')[0]), abs(b[1]-rooms_parts_dim.get('studyroom')[1])] ,
            [b[0], abs(b[1]-rooms_parts_dim.get('studyroom')[1])]])

        elif (b[0] - left_middle[0] < 0) or (b[1] - left_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('studyroom')
            room_position.get('positions').append([b, [b[0], b[1]+rooms_parts_dim.get('studyroom')[1]],
            [b[0]+rooms_parts_dim.get('studyroom')[0], b[1]+rooms_parts_dim.get('studyroom')[1]] ,
            [b[0]+rooms_parts_dim.get('studyroom')[0], b[1]]])

        elif (b[0] - right_middle[0] < 0) or (b[1] - right_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('studyroom')
            room_position.get('positions').append([b, [b[0], a[1]+rooms_parts_dim.get('studyroom')[1]],
            [b[0]+rooms_parts_dim.get('studyroom')[0], b[1]+rooms_parts_dim.get('studyroom')[1]] ,
            [b[0]+rooms_parts_dim.get('studyroom')[0], b[1]]])
        # end of creation of studyroom

        if (c[0] - left_middle[0] > 0) or (c[1] - left_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('balcony')
            room_position.get('positions').append([c, [abs(c[0]-rooms_parts_dim.get('bathroom')[0]), c[1]],
            [abs(c[0]-rooms_parts_dim.get('balcony')[0]), abs(c[1]-rooms_parts_dim.get('balcony')[1])] ,
            [c[0], abs(c[1]-rooms_parts_dim.get('bathroom')[1])]])

        elif (c[0] - right_middle[0] > 0) or (c[1] - right_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('balcony')
            room_position.get('positions').append([c, [c[0], abs(c[1]-rooms_parts_dim.get('balcony')[1])],
            [abs(c[0]-rooms_parts_dim.get('balcony')[0]), abs(c[1]-rooms_parts_dim.get('balcony')[1])] ,
            [c[0], abs(c[1]-rooms_parts_dim.get('balcony')[1])]])

        elif (c[0] - left_middle[0] < 0) or (c[1] - left_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('balcony')
            room_position.get('positions').append([c, [c[0], c[1]+rooms_parts_dim.get('balcony')[1]],
            [c[0]+rooms_parts_dim.get('balcony')[0], c[1]+rooms_parts_dim.get('balcony')[1]] ,
            [c[0]+rooms_parts_dim.get('balcony')[0], c[1]]])

        elif (c[0] - right_middle[0] < 0) or (c[1] - right_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('balcony')
            room_position.get('positions').append([c, [c[0], c[1]+rooms_parts_dim.get('balcony')[1]],
            [c[0]+rooms_parts_dim.get('balcony')[0], c[1]+rooms_parts_dim.get('balcony')[1]] ,
            [c[0]+rooms_parts_dim.get('balcony')[0], c[1]]])
        # end of creation of balcony
    # end of creation of first floor
    set_status()#save the curent room status in room_position dictionary

    # start of making basement
    shuffle(corners)
    a = corners[0]
    b = corners[1]
    c = corners[2]
    d = corners[3]
    if (floor_name == 'basement'):
        if (a[0] - left_middle[0] > 0) or (a[1] - left_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('warehouse')
            room_position.get('positions').append([a, [abs(a[0]-rooms_parts_dim.get('warehouse')[0]), a[1]],
            [abs(a[0]-rooms_parts_dim.get('warehouse')[0]), abs(a[1]-rooms_parts_dim.get('warehouse')[1])] ,
            [a[0], abs(a[1]-rooms_parts_dim.get('warehouse')[1])]])

        elif (a[0] - right_middle[0] > 0) or (a[1] - right_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('warehouse')
            room_position.get('positions').append([a, [a[0], abs(a[1]-rooms_parts_dim.get('warehouse')[1])],
            [abs(a[0]-rooms_parts_dim.get('warehouse')[0]), ab(a[1]-rooms_parts_dim.get('warehouse')[1])] ,
            [a[0], abs(a[1]-rooms_parts_dim.get('warehouse')[1])]])

        elif (a[0] - left_middle[0] < 0) or (a[1] - left_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('warehouse')
            room_position.get('positions').append([a, [a[0], a[1]+rooms_parts_dim.get('warehouse')[1]],
            [a[0]+rooms_parts_dim.get('warehouse')[0], a[1]+rooms_parts_dim.get('warehouse')[1]] ,
            [a[0]+rooms_parts_dim.get('warehouse')[0], a[1]]])

        elif (a[0] - right_middle[0] < 0) or (a[1] - right_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('warehouse')
            room_position.get('positions').append([a, [a[0], a[1]+rooms_parts_dim.get('warehouse')[1]],
            [a[0]+rooms_parts_dim.get('warehouse')[0], a[1]+rooms_parts_dim.get('warehouse')[1]] ,
            [a[0]+rooms_parts_dim.get('warehouse')[0], a[1]]])
        # end of creation of warehouse

        # start of creation of facility
        if (b[0] - left_middle[0] > 0) or (b[1] - left_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('facility')
            room_position.get('positions').append([b, [abs(b[0]-rooms_parts_dim.get('facility')[0]), b[1]],
            [abs(b[0]-rooms_parts_dim.get('facility')[0]), abs(b[1]-rooms_parts_dim.get('facility')[1])] ,
            [b[0], abs(b[1]-rooms_parts_dim.get('facility')[1])]])

        elif (b[0] - right_middle[0] > 0) or (b[1] - right_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('facility')
            room_position.get('positions').append([b, [b[0], abs(b[1]-rooms_parts_dim.get('facility')[1])],
            [abs(b[0]-rooms_parts_dim.get('facility')[0]), abs(b[1]-rooms_parts_dim.get('facility')[1])] ,
            [b[0], abs(b[1]-rooms_parts_dim.get('facility')[1])]])

        elif (b[0] - left_middle[0] < 0) or (b[1] - left_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('facility')
            room_position.get('positions').append([b, [b[0], b[1]+rooms_parts_dim.get('facility')[1]],
            [b[0]+rooms_parts_dim.get('facility')[0], b[1]+rooms_parts_dim.get('facility')[1]] ,
            [b[0]+rooms_parts_dim.get('facility')[0], b[1]]])

        elif (b[0] - right_middle[0] < 0) or (b[1] - right_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('facility')
            room_position.get('positions').append([b, [b[0], a[1]+rooms_parts_dim.get('facility')[1]],
            [b[0]+rooms_parts_dim.get('facility')[0], b[1]+rooms_parts_dim.get('facility')[1]] ,
            [b[0]+rooms_parts_dim.get('facility')[0], b[1]]])
        # end of creation of facility

        #start of creation of stairway
        if (c[0] - left_middle[0] > 0) or (c[1] - left_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('stairway')
            room_position.get('positions').append([c, [abs(c[0]-rooms_parts_dim.get('stairway')[0]), c[1]],
            [abs(c[0]-rooms_parts_dim.get('stairway')[0]), abs(c[1]-rooms_parts_dim.get('stairway')[1])] ,
            [c[0], abs(c[1]-rooms_parts_dim.get('stairway')[1])]])

        elif (c[0] - right_middle[0] > 0) or (c[1] - right_middle[1] > 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('stairway')
            room_position.get('positions').append([c, [c[0], abs(c[1]-rooms_parts_dim.get('stairway')[1])],
            [abs(c[0]-rooms_parts_dim.get('stairway')[0]), abs(c[1]-rooms_parts_dim.get('stairway')[1])] ,
            [c[0], abs(c[1]-rooms_parts_dim.get('stairway')[1])]])

        elif (c[0] - left_middle[0] < 0) or (c[1] - left_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('stairway')
            room_position.get('positions').append([c, [c[0], c[1]+rooms_parts_dim.get('stairway')[1]],
            [c[0]+rooms_parts_dim.get('stairway')[0], c[1]+rooms_parts_dim.get('stairway')[1]] ,
            [c[0]+rooms_parts_dim.get('stairway')[0], c[1]]])

        elif (c[0] - right_middle[0] < 0) or (c[1] - right_middle[1] < 0):
            room_position.get('floor').append(floor_name)
            room_position.get('room').append('stairway')
            room_position.get('positions').append([c, [c[0], c[1]+rooms_parts_dim.get('stairway')[1]],
            [c[0]+rooms_parts_dim.get('stairway')[0], c[1]+rooms_parts_dim.get('stairway')[1]] ,
            [c[0]+rooms_parts_dim.get('stairway')[0], c[1]]])
        # end of creation of stairway
    # end of creation of basement
    #set_status()
    print(room_position)

def set_status():# save the current floors and room status to statusfile
    status_file = open("/home/mohammad/projects/skeleton/puzzle_room"+
                        "/statusfile.txt", "w")
    status_file.write("positions of the rooms in floors of the building: \n")
    i = 0
    while i in range(len(room_position.get('floor'))):
        status_file.write(str(room_position.get('floor')[i]) + ', '
                          + str(room_position.get('room')[i]) + ', '
                          + str(room_position.get('positions')[i])+'\n')
        i+=1
    status_file.close()


def get_status():# recover room_position dictionary to the status before leaving game
    status_file = open("/home/mohammad/projects/skeleton/puzzle_room/"+
                        "statusfile.txt", "r")
    text = status_file.readlines()
    i = 0
    while i in range(1,len(text)):
        rp_part = text[i].splite(", ")
        room_position.get('floor')[i-1] = rp_part[0]
        room_position.get('room')[i-1] = rp_part[1]
        room_position.get('positions')[i-1] = rp_part[2]
        i+=1
    status_file.close()


create_floor('ground_floor')
#create_floor('first_floor')
#create_floor('basement')
#get_status()
