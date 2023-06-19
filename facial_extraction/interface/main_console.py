from app_config_provider import AppConfigProvider
from args_provider import ArgsProvider
from app_logic import AppLogic

if __name__ == "__main__":
    appConfigProvider = AppConfigProvider()
    app_config = appConfigProvider.app_config
    argsProvider = ArgsProvider()

    config_path = app_config["config_path"]
    image_input_dir = app_config["image_input_dir"]
    json_output_dir = app_config["json_output_dir"]

    print(config_path)
    args = argsProvider.getArgs()

    app = AppLogic(image_input_dir, json_output_dir, config_path)
    app.get_face_emotions_from_file(args.face_image_file, args.top_n, args.ret)
