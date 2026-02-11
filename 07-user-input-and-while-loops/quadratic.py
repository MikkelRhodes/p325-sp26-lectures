from math import sqrt

response1 = input('Enter a numbers for a to plug into the quadratic equation: ')
response2 = input('Enter a numbers for b to plug into the quadratic equation: ')
response3 = input('Enter a numbers for c to plug into the quadratic equation: ')

a_point = float(response1)
b_point = float(response2)
c_point = float(response3)

root1 = (-b_point + sqrt(b_point**2 -4*a_point*c_point))/2/a_point
root2 = (-b_point - sqrt(b_point**2 -4*a_point*c_point))/2/a_point

print(root1, root2)