"""Provides an API for extracting faces from an image file."""

import os
from PIL import Image, ImageDraw
import face_recognition

## TO DO: Store in config file
IMAGES = [".png", ".jpg"]
VIDEOS = [".mp4"]

DIR = "facial-extraction/raw_data/"
IM_FILE = "image1.jpg"
img_path = os.path.join(DIR, IM_FILE)


class Extractor:
    def __init__(self, config_data):
        pass

    def extract_faces(self, img_path, display=False, save=False, size=100):
        """Returns the locations of faces from a single image.

        Returns the locations of faces from a single image with the option
        to display the images or save individual faces.

        Args:
            img_path: Path to the image file.
            display: Boolean to display the image with faces outlined.
            save: False or a path to save each face too.
            size: If a path is provided for save, save the file at this size (square)

        Returns:
            A list of tuples of found face locations in css (top, right, bottom, left) order
        """
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
