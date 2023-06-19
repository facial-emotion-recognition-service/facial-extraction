import argparse


class ArgsProvider:
    @staticmethod
    def getArgs():
        parser = argparse.ArgumentParser()
        # Define command-line arguments and options using argparse
        parser.add_argument(
            "--image_file",
            type=str,
            help="full file name of a file containing an image to extract faces from",
        )
        parser.add_argument(
            "--display",
            type=bool,
            help="display the image with rectangles bounding extracted faces",
        )
        parser.add_argument(
            "--save_dir",
            type=str,
            help="directory to save images of isolated faces",
        )
        parser.add_argument(
            "--face_dim",
            type=int,
            help="square size to save isolated faces",
        )
        args = parser.parse_args()
        return args
