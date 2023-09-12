import os
import cv2
#import concurrent
from concurrent.futures import ProcessPoolExecutor

# Class to perform image processing using cv2
class ImageProcessor:
    #@staticmethod
    def process_image(image_name):
        # Load the image using cv2 
        img = cv2.imread("images/"+image_name)
        # Apply a simple filter for demonstration purposes
        img_processed = cv2.GaussianBlur(img, (5, 5), 0)
        # Save the processed image
        cv2.imwrite("output/"+image_name, img_processed)
        print("procesed"+image_name)
        #return output_path

img_name=[]
for i in os.listdir("images/"):
    img_name.append(i)


if __name__ == '__main__':
    #freeze_support()
    with ProcessPoolExecutor() as executor:
        executor.map(ImageProcessor.process_image,img_name)

