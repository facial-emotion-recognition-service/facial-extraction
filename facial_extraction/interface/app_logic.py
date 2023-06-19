import json
from pathlib import Path
from facial_extraction.core.extractor import Extractor


class AppLogic:
    def __init__(self, image_input_dir, json_output_dir):
        self.image_input_dir = Path(image_input_dir)
        self.json_output_dir = Path(json_output_dir)

    def extract_faces_coords_from_file(self, face_image_name):
        img_path = Path(self.image_input_dir, face_image_name)
        extractor = Extractor()

        result = extractor.extract_faces(img_path)

        json_str = json.dumps(result, indent=4)
        json_filename = img_path.stem + ".json"
        json_file_path = Path(self.json_output_dir, json_filename)
        with open(json_file_path, "w") as f:
            f.write(json_str)
