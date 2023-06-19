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
        args = parser.parse_args()
        return args
