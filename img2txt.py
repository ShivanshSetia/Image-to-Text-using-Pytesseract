from PIL import Image
import cv2
from pytesseract import image_to_string

#import image
image = cv2.imread('input.png')

#convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#apply threshold to remove noise
th = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#save threshold image
cv2.imwrite('filter_input.png',th)

#import filtered image
img = Image.open('filter_input.png')

#print the text
print( image_to_string(img) )

#save the text
txt = image_to_string(img)
file = open("output.txt",'w')
file.write(txt)
file.close()
