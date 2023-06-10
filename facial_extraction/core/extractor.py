import os
from PIL import Image, ImageDraw
import face_recognition

## TO DO: Store in config file
IMAGES = [".png", ".jpg"]
VIDEOS = [".mp4"]

DIR = "facial_extraction/raw_data/"
IM_FILE = "image1.jpg"
img_path = os.path.join(DIR, IM_FILE)


class Extractor:
    def __init__(self, config_data):
        pass

    def extract_faces(self, img_path, display=False):
        img_arr = face_recognition.load_image_file(img_path)
        face_locations = face_recognition.face_locations(img_arr)

        if display:
            self.display_faces(img_arr, face_locations)
        return face_locations

    def display_faces(self, img_arr, face_locations):
        img = Image.fromarray(img_arr)
        img_draw = ImageDraw.Draw(img)
        for top, right, bottom, left in face_locations:
            rect = [(left, top), (right, bottom)]
            img_draw.rectangle(rect, fill=None, outline=(0, 0, 225))
        # Display the resulting image
        img.show()

    def save_faces(self, face_locations, size):
        pass


if __name__ == "__main__":
    extractor = Extractor(0)
    print(extractor.extract_faces(img_path, True))
