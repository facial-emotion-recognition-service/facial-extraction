import json
from numpy_array_encoder import NumpyArrayEncoder


class JsonMatrixParser:
    def __init__(self):
        pass

    def mapMatrixIntoJson(self, matrix_input):
        # use dump() to write array into json
        json_result = json.dumps(matrix_input, cls=NumpyArrayEncoder)
        print('start JsonMatrixParser.mapMatrixIntoJson')
        print(json_result)
        print('end JsonMatrixParser.mapMatrixIntoJson')
        return json_result
