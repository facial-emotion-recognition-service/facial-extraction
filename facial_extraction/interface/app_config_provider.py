import os

class AppConfigProvider:
    def __init__(self):
        self._image_input_dir = os.environ.get("IMAGE_INPUT_DIR")

    @property
    def app_config(self):
        result = {
            "image_input_dir": self._image_input_dir,
        }

        return result
