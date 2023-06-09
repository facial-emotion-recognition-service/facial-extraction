import os
from PIL import Image, ImageDraw
import face_recognition


## TO DO: Store in config file
IMAGES = [".png", ".jpg"]
VIDEOS = [".mp4"]

DIR = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-extraction/raw_data/"
IM_FILE = "image1.jpg"
img_path = os.path.join(DIR, IM_FILE)


def extract_faces(img_path=img_path, display=False):
    img_arr = face_recognition.load_image_file(img_path)
    face_locations = face_recognition.face_locations(img_arr)
    print(face_locations)

    if display:
        img = Image.fromarray(img_arr)
        img_draw = ImageDraw.Draw(img)
        for top, right, bottom, left in face_locations:
            rect = [(left, top), (right, bottom)]
            img_draw.rectangle(rect, fill=None, outline=(0, 0, 225))
        # Display the resulting image
        img.show()
        # cv.imwrite('/home/nathan/code/nihonlanguageprocessing/human_emotion/raw_data/faces_extraction/extracted1.jpg', img)

    return face_locations, img


if __name__ == "__main__":
    extract_faces(img_path, True)
