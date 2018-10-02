from DataStructure_implement.MyStack import stack

sta = stack()
sta.pop()
sta.push(1)
print(sta.peek())
sta.push(2)
print(sta.check())
sta.push(3)
sta.pop()
sta.push(4)
print(sta.check())
print(sta.getSize())