#!/usr/bin/python

# Lambda expressions
print("Lambda Expressions")
ans = (lambda x: x + 1)(10)
print("answer = %d" % ans)

ans = (lambda x, y: x + y)(10, 20)
print("answer = %d" % ans)

print("------------------------------")
print("Map Function")

ans = map( lambda x: x+1, [1, 2, 3, 4, 5])
print("answer = %s" % ans)

print("------------------------------")
print("Reduce Function")

ans = reduce( lambda x,y: x+y, [1, 2, 3, 4, 5], 0)
print("answer = %d" % ans)

ans = reduce( lambda x,y: x+y, [1, 2, 3, 4, 5], 100)
print("answer = %d" % ans)

print("------------------------------")
print("Filter Function")

ans = filter( lambda x: x > 3, [1, 2, 3, 4, 5])
print("answer = %s" % ans)



