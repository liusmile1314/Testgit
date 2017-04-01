n1 = [1,3,2,5,4,5]
print n1.count(5), n1.index(5)
n1.append(0)
print n1
n1.sort()
print n1
print n1.pop()
print n1
n1.remove(2)
print n1
n1.insert(1,"Null")
print n1
print [1,2,3] + [4,5,6]

class superList(list):
    def __sub__(self, b):
        a = self[:]     # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象。
        b = b[:]        
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

class myList(list):
    def __sub__(self, subObj):
        minuend = self[:]
        subtractor = subObj[:]
        for item in subtractor:
            if item in minuend:
                minuend.remove(item)
        return minuend
print "##########################################"
obj1 = [2,3,1,5,6,4,9,0]
obj2 = [0,1,2,8,7]  
a = superList(obj1)
b = superList(obj2)
#print superList(obj1) - superList(obj2)
print a - b
print a
print b
print "##########################################"
a1 = myList(obj1)
b1 = myList(obj2)
#print myList(obj1) - myList(obj2)
print a1 - b1
print a1
print b1