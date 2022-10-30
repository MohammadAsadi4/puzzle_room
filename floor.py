from door import Door
from random import shuffle, randint

class Floor(map):

    global room_position, ground_floor, first_floor, basement, rooms_parts_dim

    room_position = {'floor':[], 'room':[], 'positions':[]}

    #here we define spcific rooms of a given floor
    ground_floor = (['kitchen', 'bathroom', 'hall'])
    first_floor = (['bedroom', 'studyroom', 'balcony'])
    basement = (['warehouse', 'facility', 'stairway'])

    #definition of the dimention of diffrent rooms
    rooms_parts_dim = ({'bedroom':[5,5], 'studyroom':[6,5], 'kitchen':[6,4],
                       'hall':[5,10], 'bathroom':[3,3], 'warehouse':[5,6],
                       'balcony':[3,3], 'stairway':[2,10], 'facility':[4,5]})

    def __init__(self):
        pass

    def set_room_position(rp, key, value):
        rp.get(key).append(value)

    def get_room_position(rp, key = None):
        if not key :
            return rp
        else:
            return rp.get(key)


    def create_floor(floor_name):
    # This method generates floor structure based on floor name and its rooms
    # first we create a set of randomly chosen point from corners then we put
    # them on 4 side of our floor and begin to position rooms of the given
    # floor based on those points.at last save positions in room_position dictionary

        rooms = [] #list of sorted room based on room`s area will store here
        #four corners of a floor
        corners = [[0,0], [0,10], [10,0], [10,10]]
        room_whole_inside_points = {'room':[], 'walls':[], 'inside_points':[], 'whole_points':[]}

        shuffle(corners)#shufle the corners so each room will place in random positions

        def update_corners(rp): # update corners after placing a room in floor
            i = 0
            nonlocal corners

            ix = Floor.get_room_position(room_position,'room').index(rp)
            pos = Floor.get_room_position(room_position,'positions')
            room_corners = pos[ix]
            i = 0
            while i < (len(room_corners)):
                if room_corners[i] not in corners:
                    corners.append(room_corners[i])
                else:
                    corners.remove(room_corners[i])
                i+=1


        def check_room_fit (floor, room):
        #check if current room fits in lefted_space of floor after placing previous rooms

            chk = []
            i = 0
            j = 1
            equal_length = list()
            equal_width = list()
            nonlocal corners
            length = list()
            width = list()
            l_mul_w = {'index' : [], 'data' :[], 'mul' :[]}
            left_space = {'index' : [], 'data': [], 'pack':[]}

            for i in range(len(corners)):
                for j in range(len(corners)):
                    if (corners[i][0] == corners[j][0]) and corners[j] not in equal_length:
                            equal_length.append(corners[j])
                    if (corners[i][1] == corners[j][1]) and corners[j] not in equal_width:
                            equal_width.append(corners[j])
            i = 0
            # print(f"equal width : {equal_width}\n")
            # print(f"equal length : {equal_length}\n")
            for i in range(0 , len(equal_length), 2):# calculatin all sides of lefted space
                length.append(abs(equal_width[i][0] - equal_width[i+1][0]))
            i = 0
            for i in range(0, len(equal_width), 2):
                width.append(abs(equal_length[i][1] - equal_length[i+1][1]))
            i = 0
            j = 0
            for i in range(len(length)):# calculates all possible forms of deviding irregular left space into regular shapes(squre or rectangle)
                for j in range(len(width)):
                    l_mul_w.get('index').append([i, j])
                    l_mul_w.get('data').append([length[i], width[j]])
                    l_mul_w.get('mul').append(length[i] * width[j])

            created_rooms = Floor.get_room_position(room_position, 'room')
            created_floor = Floor.get_room_position(room_position, 'floor')
            floor_rooms = []
            i = 0
            for i in range(len(created_rooms)):# choses rooms that belongs to current floor
                if created_floor[i] == floor :
                    floor_rooms.append(created_rooms[i])
            # print(f"rooms in {floor} are {floor_rooms}\n")
            i = 0
            f_used_area = 0
            for i in range(len(floor_rooms)):# calculating used space of current floor after placing rooms
                f_used_area = f_used_area + rooms_parts_dim.get(floor_rooms[i])[0] * rooms_parts_dim.get(floor_rooms[i])[1]
            f_remain_area = 100 - f_used_area
            # print(f"remaining area is {f_remain_area}\n")
            # print(f"l*w details: {l_mul_w}\n")
            i = 0
            for i in range(len(l_mul_w.get('index'))):# makes sets of lefted space shapes that their area are equal to remaining area of the floor
                j = 1
                for j in range(len(l_mul_w.get('index'))):
                    k = 2
                    for k in range(len(l_mul_w.get('index'))):
                        if l_mul_w.get('mul')[i] == f_remain_area or l_mul_w.get('mul')[i] + l_mul_w.get('mul')[j] == f_remain_area or l_mul_w.get('mul')[i] + l_mul_w.get('mul')[j] + l_mul_w.get('mul')[k] == f_remain_area :
                            if (l_mul_w.get('data')[i]  or l_mul_w.get('data')[j] or l_mul_w.get('data')[k]) not in left_space.get('data') :
                                left_space.get('index').append(l_mul_w.get('index')[l_mul_w.get('data').index(l_mul_w.get('data')[i])])
                                left_space.get('data').append(l_mul_w.get('data')[i])
                                left_space.get('pack').append([l_mul_w.get('data')[i], l_mul_w.get('data')[j], l_mul_w.get('data')[k]])

            #print(f"left space details: {left_space}\n")
            i = 0
            for i in range(len(left_space.get('index'))):#checks wether current room dimentions fits in atleast one of the possible lefted space regular shapes
                #print(f"x of {room} is :{rooms_parts_dim.get(room)[0]}\ny of {room} is :{rooms_parts_dim.get(room)[1]}\nx of devided left space is {left_space.get('data')[i][0]}\ny of devided left space is {left_space.get('data')[i][1]}\n")
                if (rooms_parts_dim.get(room)[0] <= left_space.get('data')[i][0] and rooms_parts_dim.get(room)[1] <= left_space.get('data')[i][1]) or (rooms_parts_dim.get(room)[1] <= left_space.get('data')[i][0] and rooms_parts_dim.get(room)[0] <= left_space.get('data')[i][1]):
                    chk.append(True)
                else:
                    chk.append(False)

            if True in chk:
                return True
            else:
                # if room in Floor.get_room_position(room_position, 'room'):
                #     Floor.get_room_position(room_position, 'room').remove(room)# removing collided room from room position dict
                return False


        def room_points(room):
        # categorizing all of the points of the  given room in 3 groups: whole, inside and wall points

            whole_points = [] # whole points of the given room includind walls
            inside_points = [] # all of the points inside current room stores here
            walls = [] # wall points of the room
            ix = Floor.get_room_position(room_position,'room').index(room)# index of the given room in room section of room_position dictionary
            pos = Floor.get_room_position(room_position,'positions')# all positions of created rooms -- pos[ix] are dimentions of current room
            i = 1
            min = pos[ix][0]
            for i in range(4):
                if pos[ix][i][0] <= min[0] and pos[ix][i][1] <= min[1] :
                    min = pos[ix][i]
            # whole points of the given room(with walls)
            i = min[0]
            j = min[1]
            for i in range(i, min[0] + rooms_parts_dim[room][0] + 1) :
                j = min[1]
                for j in range(j, min[1] + rooms_parts_dim[room][1] + 1):
                    whole_points.append([i, j])
            # all points inside the given room(without walls)
            i = min[0] + 1
            j = min[1] + 1
            for i in range(i, min[0] + rooms_parts_dim[room][0]) :
                j = min[1] + 1
                for j in range(j, min[1] + rooms_parts_dim[room][1]):
                    inside_points.append([i, j])
            # walls of the given room
            i = 0
            for i in range(len(whole_points)):
                if whole_points[i] not in inside_points :
                    walls.append(whole_points[i])
            #print(f"walls of {room} are ", walls, "\n")

            return walls, inside_points, whole_points


        def collide_check(room, whole_points):
        # check if current room dimentions conflict with other rooms created before.

            chk = []
            chk.clear()
            collision_points = {'collision' : [] , 'whole_collision' : [], 'wall_collision' : []}# here we store collision point and points that collision point  collide with
            collision_points.get('collision').clear()
            collision_points.get('whole_collision').clear()
            collision_points.get('wall_collision').clear()

            ix = whole_points.get('room').index(room)# index of the given room in room_whole_inside_points dictionary
            wh_points = whole_points.get('whole_points')# all inside points of created rooms -- wh_points[ix] are inside points of current room
            wall_points = whole_points.get('walls')# all wall points of created rooms -- wall_poin[ix] are walls of current room
            # print(f"all walls in room_whole_inside_points dict are {wall_points} \n")
            # print(f"wall of the {room} in room_whole_inside_points dict are {wall_points[ix]} \n")
            # print(f"whole points in room_whole_inside_points dict are {wh_points} \n")
            # print(f"whole points of {room} in room_whole_inside_points dict are {wh_points[ix]} \n")

            i = 0
            #(we lower end of range by one unit to eliminate checking a room with intself (in every for loop))
            for i in range(len(wall_points[ix]) - 1):#check if walls of current room collides with other walls in the floor
                j = 0
                for j in range(len(wall_points) - 1):
                    if wall_points[ix][i] in wall_points[j] :
                        if (wall_points[ix][i] not in collision_points.get('collision')) and (wall_points[j] not in collision_points.get('wall_collision')):
                            collision_points.get('collision').append(wall_points[ix][i])
                            collision_points.get('wall_collision').append(wall_points[j])
            #print(f"checking wall collision of {room} : {collision_points}\n")
            i = 0
            for i in range(len(wh_points[ix]) - 1):#check if whole points of current romm collides with other rooms in the floor
                j = 0
                for j in range(len(wh_points) - 1 ):
                    if wh_points[ix][i] in wh_points[j] :
                        if (wh_points[ix][i] not in collision_points.get('collision')) and (wh_points[j] not in collision_points.get('whole_collision')):
                            collision_points.get('collision').append(wh_points[ix][i])
                            collision_points.get('whole_collision').append(wh_points[j])
            #print(f"checking whole points collision of {room} : {collision_points}\n")
            #print(f"whole collision poins : {collision_points.get('whole_collision')}\n")
            #print(f"wall collision points : {collision_points.get('wall_collision')}\n")
            i = 0
            if collision_points.get('whole_collision') != [] and collision_points.get('wall_collision') != []:# if all the collision points are walls it`s ok otherwise it`s a collision
                for i in range(len(collision_points.get('whole_collision'))):
                    j = 0
                    for j in range(len(collision_points.get('wall_collision'))):
                        if collision_points.get('whole_collision')[i] in collision_points.get('wall_collision')[j]:
                            chk.append(False)
                        else:
                            chk.append(True)

            if True in chk :
                print(f"room {room} collides with others")
                print(f"collision details are: \n points {collision_points.get('collision')}\n collides with \n{collision_points.get('whole_collision')} \n")
                rollback_room_corners_insidepoints(room)
                return True
            else :
                return False


        def rollback_room_corners_insidepoints(room):
        # when a recently created room collides with other ones we should delet
        # this room and its corner as well as whole point of this room
            nonlocal room_whole_inside_points, corners

            r_ix = Floor.get_room_position(room_position, 'room').index(room)
            i = 0
            for i in range(4):# removing corners of room from corner list
                if Floor.get_room_position(room_position, 'positions')[r_ix][i] in corners:
                    corners.remove(Floor.get_room_position(room_position, 'positions')[r_ix][i])
            Floor.get_room_position(room_position, 'positions').pop(r_ix)# removing corners from room position dict
            Floor.get_room_position(room_position, 'room').remove(room)# removing collided room from room position dict
            Floor.get_room_position(room_position, 'floor').pop(r_ix)
            in_ix = room_whole_inside_points.get('room').index(room)
            room_whole_inside_points.get('whole_points').pop(in_ix)# removing whole points from room_whole_inside_points dict
            room_whole_inside_points.get('inside_points').pop(in_ix) # removing inside points from room_whole_inside_points dict
            room_whole_inside_points.get('walls').pop(in_ix) # removing walls from room_whole_inside_points dict
            room_whole_inside_points.get('room').remove(room)# removing collided room from room_whole_inside_points dict


        def create_rooms(floor_name, rooms, corners, corner_no, next_corner = None) :
        # placing rooms(order from big to small) based on the floor name

            left_middle = [5,0]
            right_middle = [5,10]
            nonlocal room_whole_inside_points

            if next_corner != None and next_corner + 1 in range(len(corners)):
                i = corner_no
                j = next_corner + 1
                print(f"j is provided so i is now:{i} and j is now:{j} \n")
            else:
                i = corner_no
                j = corner_no
                print(f"i is euql to j and is {i} \n")

            if (corners[j][0] - left_middle[0] > 0) or (corners[j][1] - left_middle[1] > 0):

                Floor.set_room_position(room_position, 'floor', floor_name)
                Floor.set_room_position(room_position, 'room', rooms[i])
                Floor.set_room_position(room_position, 'positions', [corners[j], [abs(corners[j][0] - rooms_parts_dim.get(rooms[i])[0]), corners[j][1]],
                [abs(corners[j][0] - rooms_parts_dim.get(rooms[i])[0]), abs(corners[j][1] - rooms_parts_dim.get(rooms[i])[1])],
                [corners[j][0], abs(corners[j][1] - rooms_parts_dim.get(rooms[i])[1])]])

            elif (corners[j][0] - right_middle[0] > 0) or (corners[j][1] - right_middle[1] > 0):

                Floor.set_room_position(room_position, 'floor', floor_name)
                Floor.set_room_position(room_position, 'room', rooms[i])
                Floor.set_room_position(room_position, 'positions', [corners[j], [corners[j][0], abs(corners[j][1] - rooms_parts_dim.get(rooms[i])[1])],
                [abs(corners[j][0] - rooms_parts_dim.get(rooms[i])[0]), abs(corners[j][1] - rooms_parts_dim.get(rooms[i])[1])],
                [corners[j][0], abs(corners[j][1] - rooms_parts_dim.get(rooms[i])[1])]])

            elif (corners[j][0] - left_middle[0] < 0) or (corners[j][1] - left_middle[1] < 0):

                Floor.set_room_position(room_position, 'floor', floor_name)
                Floor.set_room_position(room_position, 'room', rooms[i])
                Floor.set_room_position(room_position, 'positions', [corners[j], [corners[j][0], corners[j][1] + rooms_parts_dim.get(rooms[i])[1]],
                [corners[j][0] + rooms_parts_dim.get(rooms[i])[0], corners[j][1] + rooms_parts_dim.get(rooms[i])[1]] ,
                [corners[j][0] + rooms_parts_dim.get(rooms[i])[0], corners[j][1]]])

            elif (corners[j][0] - right_middle[0] < 0) or (corners[j][1] - right_middle[1] < 0):

                Floor.set_room_position(room_position, 'floor', floor_name)
                Floor.set_room_position(room_position, 'room', rooms[i])
                Floor.set_room_position(room_position, 'positions', [corners[j], [corners[j][0], corners[j][1] + rooms_parts_dim.get(rooms[i])[1]],
                [corners[j][0] + rooms_parts_dim.get(rooms[i])[0], corners[j][1] + rooms_parts_dim.get(rooms[i])[1]] ,
                [corners[j][0] + rooms_parts_dim.get(rooms[i])[0], corners[j][1]]])

            update_corners(rooms[i])# update corners after successfull placement of room
            #print(f"room position before fit and collide check is: {room_position}\n")
            print(f"corners after update are : {corners}\n")
            room_whole_inside_points.get('room').append(rooms[i])# appending current room inside points to room_whole_inside_points dict
            room_whole_inside_points.get('walls').append(room_points(rooms[i])[0])
            room_whole_inside_points.get('inside_points').append(room_points(rooms[i])[1])
            room_whole_inside_points.get('whole_points').append(room_points(rooms[i])[2])


            print(f"room positions after fit and collide check is: {room_position}\n")
            #print(f"returned values from create_room function are: {chk_room_fit , collide_chk, i, j}\n")
            return  i, j

        # start of creation of floor
        #   start of creation of biggest room

        #j = -1
        chk_room_fit = True
        collide_chk = False

        result = (0, None)
        rooms = Floor.floor_room_sorter(floor_name)# sort rooms of a floor based on their size (big to small)
        i = 0
        j = None
        if (floor_name in ['basement', 'ground_floor', 'first_floor']) : #and result[0] :
            #print(f"i is {i} , check_room_fit is {ch}")
            while i in range(len(rooms)) and chk_room_fit == True and collide_chk == False :

                print(f"calling create_room methode with values : {floor_name, rooms, corners, i, j}\n")
                result = create_rooms(floor_name, rooms, corners, i, j)
                print(f"returned result are(collision not happend): {result, chk_room_fit, collide_chk}\n")
                     # else :# collide has happened. system tries to create that room with another corner from corners list
                     #     print(f"returned result from create_room function are(collision happend): {result}\n")
                     #     i = result[0]
                     #     j = result[1]
                     #     print(f"collision index is {j}\n")
                     #     print(f"calling create_room methode with values : {floor_name, rooms, corners, i, j}\n")
                     #     result = create_rooms(floor_name, rooms, corners, i, j)# here we use optional parameter(j). by setting j we try ro create room with an other corner

                if i < len(rooms) :# checks if rooms fits in the remaining space of floor
                    chk_room_fit = check_room_fit(floor_name, rooms[i])
                    if chk_room_fit == False : # checks if room fits in floor
                        print(f"{rooms[i]} does not fit in {floor_name}.\n")
                    elif i > 0 :# checks if dimentions of current room collides with other rooms
                        collide_chk = collide_check(rooms[i], room_whole_inside_points)# here we can get the index of room that collides with others
                        while  collide_chk == True and j in range(len(corners)) :# checks if current room collides with other rooms created before
                            print(f"returned result are(collision happend): {result, chk_room_fit, collide_chk}\n")
                            i = result[0]
                            j = result[1]
                            print(f"collision index is {j}\n")
                            print(f"calling create_room methode with values (collision happend) : {floor_name, rooms, corners, i, j}\n")
                            result = create_rooms(floor_name, rooms, corners, i, j)# here we use optional parameter(j). by setting j we try ro create room with an other corner

                 #else:

                     #result = create_rooms(floor_name, rooms, corners, i, j)
                # update_corners(rooms[i])# update corners after successfull placement of room
                i += 1

            # if chk_room_fit == False : # checks if room fits in floor
            #     print(f"{rooms[i]} does not fit in {floor_name}.\n")
            #     if collide_chk == True :# checks if current room collides with other rooms created before
            #         print(f"returned result are(collision happend): {result, chk_room_fit, collide_chk}\n")
            #         i = result[0]
            #         j = result[1]
            #         print(f"collision index is {j}\n")
            #         print(f"calling create_room methode with values : {floor_name, rooms, corners, i, j}\n")
            #         result = create_rooms(floor_name, rooms, corners, i, j)# here we use optional parameter(j). by setting j we try ro create room with an other corner
        else :
            print(f"Invalide floor name {floor_name}.")
            return
        # end of making floor

        Floor.set_status()# save the current floors and room status to statusfile


    def set_status():# save the current floors and room status to statusfile
        status_file = open("/home/mohammad/projects/skeleton/puzzle_room"+
                            "/statusfile.txt", "w")
        status_file.write("positions of the rooms in floors of the building: \n")
        i = 0
        f = Floor.get_room_position(room_position, 'floor')
        r = Floor.get_room_position(room_position, 'room')
        p = Floor.get_room_position(room_position, 'positions')
        while i in range(len(f)):
            status_file.write(str(f[i]) + ', ' + str(r[i]) + ', ' + str(p[i])+'\n')
            i+=1
        status_file.close()


    def get_status():# recover room_position dictionary to the status before leaving game
        status_file = open("/home/mohammad/projects/skeleton/puzzle_room/"+
                            "statusfile.txt", "r")
        text = status_file.readlines()
        i = 0
        while i in range(1,len(text)):
            rp_part = text[i].splite(", ")
            Floor.set_room_position(room_position, 'floor', rp_part[0])
            Floor.set_room_position(room_position, 'room', rp_part[1])
            Floor.set_room_position(room_position, 'positions', rp_part[2])
            i+=1
        status_file.close()

    # try to place rooms in floor regarding rooms  wall collision
    # to avoid this matter first we sort the rooms based on its area(from big to small)
    # then place bigest room in floor then update the corners to update remaining
    # space then try to place next room with given dimention if it`s not possible
    # swap the length and width of the room and try agian finally if none of these
    # solutions are possible, raise an error
    def floor_room_sorter(floor_name):
        # calculating the area of each room
        room_area = []
        i = 0
        if floor_name in globals():
            for i in range(len(globals()[floor_name])):
                room_area.append({'room': globals()[floor_name][i], 'area':
                                   rooms_parts_dim.get(globals()[floor_name][i])[0]
                                   * rooms_parts_dim.get(globals()[floor_name][i])[1]})
        else:
            print(f"we have no floor with name {floor_name}")

        # sort room_area listofdictionary from biggest area to smallest one
        def getval(sub):
            return sub['area']

        room_area.sort(key = getval, reverse = True)
        # return sorted list of given floor basedon room area
        i = 0
        sorted_floor = []
        for i in range(len(room_area)):
            sorted_floor.append(room_area[i]['room'])
        return sorted_floor


    def floor_furniture(self):
        pass


Floor.create_floor('basement')
Floor.create_floor('ground_floor')
Floor.create_floor('first_floor')
#Floor.floor_room_sorter('ground_floor')
# Floor.get_status()
