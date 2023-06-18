"""Provides an API for extracting faces from an image file."""

import os
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

    def extract_faces(self, img_path):
        """Returns the locations of faces from a single image.

        Returns the locations of faces from a single image with the option
        to display the images or save individual faces.

        Args:
            img_path: Path to the image file.

        Returns:
            A list of tuples of found face locations in css (top, right, bottom, left) order
        """
        img_arr = face_recognition.load_image_file(img_path)
        face_locations = face_recognition.face_locations(img_arr)
        return face_locations


