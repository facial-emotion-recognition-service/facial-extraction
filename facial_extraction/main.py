import os, sys

sys.path.append('server')
sys.path.append('core')

from extractor import Extractor
from image_viewer import ImageViewer
import json

if __name__ == "__main__":
    config_path = '../config.json'

    with open(config_path, "r") as json_config_file:
        config_data = json.load(json_config_file)

    img_path = "/home/orbartal/Code/files/multi_faces.jpg"
    extractor = Extractor(config_data)
    imageViewer = ImageViewer()
    face_locations = extractor.extract_faces(img_path)
    print(face_locations)
    imageViewer.display_faces(img_path, face_locations)
