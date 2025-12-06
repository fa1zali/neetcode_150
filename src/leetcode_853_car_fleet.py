# LeetCode 853: Car Fleet

# There are n cars going to the same destination along a one lane road. The destination is target miles away.
# You are given 2 integer array position and speed both of length n.

# A car can never pass a car ahead of it, but can catch upto it and drive bumper to bumper at same speed.
# The faster car will slow down to match the slower cars speed. The distance between 2 cars is ignored.

# A car fleet is some non empty set of cars driving at same position and same speed. Note that a single car is also a car fleet.

# If a car catches up to a car fleet right at the destination point, it will be considered one car fleet.

# Return number of car fleets that will arrive at destination

# Optimized Approach(Time Complexity: O(nlogn), Space Complexity: O(n))
def car_fleet(position, speed, target):
    
    cars_data = sorted(zip(position,speed), reverse=True)
    
    stack = []

    for pos,spd in cars_data:
        time_to_arrive = (target-pos)/spd

        stack.append(time_to_arrive)
        
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    
    print(stack)

    return len(stack)


position = [10,8,0,5,3]
speed = [2,4,1,1,3]
target = 12
result = car_fleet(position, speed, target)
print(result)