import json
from numpy_array_encoder import NumpyArrayEncoder


class JsonMatrixParser:
    def __init__(self):
        pass

    def mapMatrixIntoJson(self, matrix_input):
        json_result = json.dumps(matrix_input, cls=NumpyArrayEncoder)
        return json_result
