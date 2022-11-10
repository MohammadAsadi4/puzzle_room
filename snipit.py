#my_dict = dict(floor = '1st floor', position = [[1,1], [1,2], [3,4], [4,5]])
#print (my_dict)
#print (my_dict.items())
#print(type(my_dict))

#pos = [1,2]
#first_dict = {1:[0,1], 2:[3,2], 3:[4,5]}
#pos2 = [3,5]
#pos3 = [pos[0]-pos2[0], pos[1]-pos2[1]]

#list = list()
#list.append(1)
#list.append(2)
#print(list)
#shimpool = []
#print(shimpool)
#dict2 = dict(name = [], age = [])
#dict2.get('name').append("q")
#dict2.get('name').append("r")
#dict2.get('name').append("s")
#dict2["name"][2] = "c"
#print(dict2)
#print(text.index("f"))
#t1 = text.split("''")
#print(t)
#t2 = text.split(",")
#print(t)
#t3 = text.split("', ")
#print(t)
#t4 = text.partition("['")
#print(t4)
#txt = "this is the way we wash our hands"
#partof = txt.partition("way")
#print(partof)
#print(partof[0]+partof[1]+partof[2])
#room_position = dict(floor = [], room = [], positions = [])
#text = "{'floor': ['ground_floor', 'ground_floor', 'ground_floor', 'first_floor', 'first_floor', 'first_floor', 'basement', 'basement', 'basement'], 'room': ['hall', 'kitchen', 'bathroom', 'bedroom', 'studyroom', 'balcony', 'warehouse', 'facility', 'stairway'], 'positions': [[[0, 10], [5, 10], [5, 0], [0, 0]], [[0, 10], [6, 10], [6, 6], [0, 6]], [[10, 10], [7, 10], [7, 7], [10, 7]], [[10, 10], [5, 10], [5, 5], [10, 5]], [[10, 10], [3, 10], [3, 3], [10, 3]], [[0, 0], [0, 3], [3, 3], [3, 0]],"+ "[[10, 0], [4, 0], [4, 5], [10, 5]], [[0, 0], [0, 4], [4, 4], [4, 0]], [[10, 10], [8, 10], [8, 0], [10, 0]]]}"
#print(room_position)
#part = tuple()
#part1 = tuple()
#part = text.partition("floor': [")
#part1 = part[2].partition("],")
#print("part1[0] :" + part1[0])
#print("************************")
#room_position.get('floor').append(part1[0])
#part = tuple()
#part1 = tuple()
#part = text.partition("'room': [")
#part1 = part[2].partition("],")
#print("part1[0] :" + part1[0])
#print("************************")
#room_position.get('room').append(part1[0])
#part = tuple()
#part1 = tuple()
#part2 = tuple()
#part = text.partition("'positions': [")
#part1 = part[2].partition("]]]")
#print("part1[0] :" + part1[0])
#print("########################")
#print(part1)
#part2 = part1[1].partition("]")
#print("part2[2] :" + part2[2])
#print("************************")
#print(str(type(part1))+'---'+str(type(tuple(part2[2]))))
#room_position.get('positions').append(part1[0])
#room_position.get('positions').append(part2[2])
#print(len(room_position.get('floor')))
#print(len(room_position.get('room')))
#print(len(room_position.get('positions')))
#print(room_position)
#list = ['ali', 'zahra', 'mohammad', 'peyman', 'xaniar']
#list2 = [1, 4, 0, -2, 10]
#print(list)
#print(sorted(list, reverse = True))
#print(list2)
#print(sorted(list2, reverse = True))
#room_area = [{'hall': 30}, {'kitchen': 14}, {'bedromm': 12},
#             {'bathroom': 6}, {'balcony': 9}]
#room_area = []
#room_area.append(dict(room = 'hall', area = 30))
#room_area.append(dict(room = 'kitchen', area = 14))
#room_area.append(dict(room = 'bedroom', area = 12))
#room_area.append(dict(room = 'bathroom', area = 6))
#room_area.append(dict(room = 'balcony', area = 9))
#def getval(listofdic, key):
#    for subval in listofdic:
#        if key in subval:
#            return subval[key]
#print(room_area)
#print (getval(room_area, 'kitchen'))
#room_area =[]
#for i in range(len(floor_name)):
#    room_area.append({floor_name[i]: rooms_parts_dim.get(floor_name[i])[0]
#                                 * rooms_parts_dim.get(floor_name[i])[1]})
#print (room_area)
#print(sorted(room_area, key = room_area['area']))

#class rp_setter_getter:# set & get room_position dictionary

#   room_position = {'floor' : [], 'room' : [], 'positions' : []}

#    def set_room_position(key, value):
#        room_position.get(key).append(value)

#    def get_room_position():
#        return room_position



#class floor():
#    rp_setter_getter.set_room_position('floor', 'ground_floor')
#    print(rp_setter_getter.get_room_position())
#list1 = [[0,0], [0,10], [10,0], [10,10]]
#list2 = [[0,0], [10,10], [5,0], [5,10]]
#i = 0
#for i in range(len(list1)):
#    print(list1[i])
#    if list1[i] not in list2:
#        list2.append(list1[i])
#    else:
#        list2.remove(list1[i])
#print(list2)

#l1 = ['a','b','c','d','e'] # create our list of letters
#iter_list = iter(l1)
#print(type(iter_list))

#if (0-0 > 0) or (0-5 > 0):
#    print('true')
#if 2 in range(3):
#    print("ok")
#i = 5
#for i in range(5, 10):
#    print(i)
#ch = []
#ch.append(True)
#print(ch)
#if True in ch:
    #print("True is in list")
#if 5 in range (10,5):
#    print(ok)
#print(ch.index(False))
# def check(a):
#     if a in ['a', 'b', 'c']:
#         print(f"{a} is in the list")
#     else:
#         print(f"value {a} is not in the list")
# a = 'a'
# d = 'd'
# check(a)
# check(d)
# a = [1, 2, 3, 4, 2]
# print(a.index(2))
# i = 1
# j = 2
# expresion = 'i-j < 0'
# print(eval(expresion))
# a = [10,5]
# b = a[0]
# print(b)
# a = [[1, 1], [2, 3], [5,4]]
# b = [2, 3]
# if b in a :
#     print('yes')
# else:
#     print('no')
# def math(a,b):
#     sum = a + b
#     mul = a * b
#     return sum , mul
# res = math(12,9)
# print(type(res))
# text = 'qwertyuiop'
# i = 0
# for i in range(len(text)):
#     print(i)
# print(eval('2<1'))
# list = [1,3,4,5]
# print(max(list))
# a = [[[1],[2]],[[3],[4]]]
# b = [[1],[5],[6]]
# i = 0

# for i in range(len(b)):
#     j = 0
#     for j in range(len(a)):
#         if b[i] in a[j]:
#             print(f"found {b[i]}")
#         else:
#             print("not found")
i = 2
if i > 0 and i <3:
    print('aa')
elif i>1 and i<4 :
    print('bb')    
