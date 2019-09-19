# our input is a list of point coordinates
coordinates = [(0,0),(1,0),(2,0),(3,0),(4,0),
               (0,1),(1,1),(2,1),(3,1),(4,1),
               (0,2),(1,2),(2,2),(3,2),(4,2),
               (0,3),(1,3),(2,3),(3,3),(4,3),
               (0,4),(1,4),(2,4),(3,4),(4,4)]

# find the average point between those points
sum_x = 0
sum_y = 0

for i in coordinates:
    sum_x = sum_x + i[0]
    sum_y = sum_y + i[1]

avg_x = sum_x / len(coordinates)
avg_y = sum_y / len(coordinates)

average_point = (avg_x,avg_y)

print (average_point)