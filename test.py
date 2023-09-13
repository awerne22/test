import os
import cv2
from fastapi import FastAPI,File,UploadFile
from concurrent.futures import ProcessPoolExecutor
import uvicorn
class ImageProcessor:
    """
    Class to perform image processing using cv2
    """
    @staticmethod
    def process_image(img_path):
        """
        Static function that takes image and return processed image
        Prameters
        --------
        img_path : str
            path to the image 
        """
        #Create a unique identifier for the image
        image_id = os.urandom(16).hex()
        #define oputput_path
        output_path = f"output/{image_id}.jpg"

        # Load the image using cv2 
        img = cv2.imread(img_path)
        # Apply a simple filter for demonstration purposes
        img_processed = cv2.GaussianBlur(img, (5, 5), 0)
        # Save the processed image
        cv2.imwrite(output_path, img_processed)
        return output_path
        
#Read images from file
img_path=[]
for img_name in os.listdir("images/"):
    img_path.append("images/"+img_name)

app=FastAPI()

@app.get("/upload/")
async def upload_image():
    """
    Endpoint that accepts an image
    and returns processed image with
    a unique identifier for that image
    """
    #multiprocessing
    with ProcessPoolExecutor() as executor:
        results = executor.map(ImageProcessor.process_image,img_path)

    return [{result:"was proccessed"} for result in results]

if __name__ == '__main__':
    uvicorn.run(
            "test:app",
            reload=True
            )

    ##Multiprocessing
    #with ProcessPoolExecutor() as executor:
    #    executor.map(ImageProcessor.process_image,img_name)

