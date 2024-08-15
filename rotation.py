import math
import numpy as np
import cv2

def R(theta, counterclockwise=True):
    if counterclockwise:
        theta = -theta
    theta = (theta*math.pi)/180
    return np.array([[math.cos(theta), math.sin(theta)],[ -math.sin(theta), math.cos(theta)]])

def product(point, theta, counterclockwise=True): # Theta is in degrees
    return np.dot(R(theta, counterclockwise), point)


angle = int(input("Enter the angle you want this image to rotate with: "))
p = input("1. Clockwise \n2.Counterclockwise\n")
counterclockwise = bool(int(p)-1)

image = cv2.imread("free-nature-images.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
new_image = np.zeros_like(image*2)
origin = np.array([[image.shape[0] // 2], [image.shape[1] // 2]])

p = input("Wanna rotate the image around an arbitrary origin (y/n)? ")
if p=='y':
    origin_input = input("Enter the coordinates you want the image to rotate around (x,y): ").split()
    origin = np.array([[int(origin_input[0])], [int(origin_input[1])]])
elif p=='n':
    origin = np.array([[image.shape[0] // 2], [image.shape[1] // 2]])

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        translated_point = np.array([[i], [j]]) - origin
        x, y = product(translated_point, angle, counterclockwise)
        x, y = x + origin[0], y + origin[1]
        if 0 <= x < image.shape[0] and 0 <= y < image.shape[1]:
            new_image[int(x), int(y)] = image[i, j]
