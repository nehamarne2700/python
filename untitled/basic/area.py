#area of circle
radius=int(input('enter radius'))
area=3.14*radius**2;
msg=f'area of circle with radius {radius} is {area}'
print(msg)

#area of retangle
length=int(input('enter length'))
width=int(input('enter width'))
area=length*width
msg=f'area of rectangle with length {length} and width {width} is {area}'
print('area of rectangle with length {!s} and width {!s} is {!s}'.format(length,width,area))

#area of triangle
base=int(input('enter base'))
height=int(input('enter height'))
area=base*height//2
msg=f'area of triangle with length {base} and width {height} is {area}'
print(msg)