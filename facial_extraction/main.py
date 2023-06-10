import os
from facial_extraction.core import extraction
import json

if __name__ == "__main__":
    config_path = os.environ.get("CONFIG_PATH", "config.json")

    with open(config_path, "r") as json_config_file:
        config_data = json.load(json_config_file)

    img_path = "../input_images/8_hap.png"
    print(extraction.extract_faces(img_path))
