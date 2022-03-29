#Algunas funciones para modificar imágenes
import cv2

def get_grayscale(image_path):
    image = cv2.imread(image_path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def invert_image(image_path):
    image = cv2.imread(image_path)
    return cv2.bitwise_not(image)