from app_config_provider import AppConfigProvider
from args_provider import ArgsProvider
from app_logic import AppLogic

if __name__ == "__main__":
    appConfigProvider = AppConfigProvider()
    app_config = appConfigProvider.app_config
    argsProvider = ArgsProvider()

    image_input_dir = app_config["image_input_dir"]

    args = argsProvider.getArgs()

    app = AppLogic(image_input_dir)
    result = app.extract_faces_coords_from_file(args.image_file)
    print(result)
