class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self, dx, dy):
        position = [0, 0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return "reproduction ",self.way_of_reproduction,position
summer = Bird()
print "after move:",summer.move(5,8)

class Chicken(Bird):
    way_of_move = "walk"
    possible_in_KFC = True

class Oriole(Bird):
    def __init__(self,name):
        self.name = name
        print "I am a oriole, name is ",name,self.way_of_move
    way_of_move = "fly"
    possible_in_KFC = False

birdObj1 = Chicken()
birdObj2 = Oriole("Smile")
birdObj3 = Oriole("Enjoy")
print birdObj2.name,birdObj3.name
birdObj2.way_of_reproduction = "None"
print "birdObj1 : ",birdObj1.have_feather,birdObj1.possible_in_KFC
print "birdObj2 : ",birdObj1.way_of_reproduction,birdObj2.possible_in_KFC,birdObj2.move(3,4)
print birdObj1.way_of_reproduction
print birdObj2.way_of_reproduction
print birdObj3.way_of_reproduction

print dir(Oriole)
print dir(birdObj2)
print help(list)
print help(Oriole)