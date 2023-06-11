import functions as f

#1 i 2
new_point_1=f.Point()
new_point_2=f.Point()
new_point_1.x=10
new_point_1.y=15
new_point_2.x=10
new_point_2.y=15

new_point=new_point_1.add(new_point_2)

print(new_point)

#3
print(f.Area_Circuit.calculate_circuit(f.Point(-1,0), f.Point(-1,-1), f.Point(1,-1), f.Point(1,0))[0])
print(f.Area_Circuit.calculate_area(f.Point(-1,0), f.Point(-1,-1), f.Point(1,-1), f.Point(1,0)))

print(f.Area_Circuit.calculate_circuit(f.Point(0,0), f.Point(0,1), f.Point(1,0))[0])
print(f.Area_Circuit.calculate_area(f.Point(0,0), f.Point(0,1), f.Point(1,0)))

#4
f.fun()
f.fun1()
f.fun2(5)
f.fun2(3)
f.fun3(1,2,3)
print(f.FunctionCounter.get_count())