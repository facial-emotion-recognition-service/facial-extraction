from pathlib import Path
from facial_extraction.core.extractor import Extractor


class AppLogic:
    def __init__(self, image_input_dir):
        self.image_input_dir = Path(image_input_dir)

    def extract_faces_coords_from_file(self, face_image_name):
        img_path = Path(self.image_input_dir, face_image_name)
        extractor = Extractor()
        result = extractor.extract_faces(img_path)

        return result
