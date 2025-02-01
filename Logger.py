import json
import os
import time

import constants as Config


def cleanup_logs(self):
    if not self.log_file_path:
        return

    if os.path.getsize(self.log_file_path) > Config.log_file_max_size:
        self.archive_log()

    log_folder = os.path.dirname(self.log_file_path)
    log_files = [f for f in os.listdir(log_folder) if f.startswith("pcmd_log")]
    log_files.sort(key=lambda x: os.path.getmtime(os.path.join(log_folder, x)))

    while len(log_files) > Config.log_file_max_count:
        os.remove(os.path.join(log_folder, log_files.pop(0)))


def create_config_file():
    user_folder = os.path.expanduser("~")
    config_folder = os.path.join(user_folder, ".pcmd")
    config_file = os.path.join(config_folder, "config.json")

    if not os.path.exists(config_folder):
        os.makedirs(config_folder)

    if not os.path.exists(config_file):
        # 创建一个新的配置对象
        config_data = {"logging_enabled": True,
                       "log_file_max_size": 10240,
                       "log_file_max_age": 30,
                       "log_file_max_count": 10,
                       }
    else:
        # 如果文件存在，读取文件内容
        with open(config_file, "r") as f:
            config_data = json.load(f)

    # 将更新后的配置数据写回文件
    with open(config_file, "w") as f:
        json.dump(config_data, f, indent=4)


def load_logging_settings():
    user_folder = os.path.expanduser("~")
    config_folder = os.path.join(user_folder, ".pcmd")
    config_file = os.path.join(config_folder, "config.json")

    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            config_data = json.load(f)

        Config.logging_enabled = config_data.get("logging_enabled", True)
        Config.log_file_max_size = config_data.get("log_file_max_size", 10240)
        Config.log_file_max_age = config_data.get("log_file_max_age", 30)
        Config.log_file_max_count = config_data.get("log_file_max_count", 10)


def save_logging_settings():
    user_folder = os.path.expanduser("~")
    config_folder = os.path.join(user_folder, ".pcmd")
    config_file = os.path.join(config_folder, "config.json")

    config_data = {
        "logging_enabled": Config.logging_enabled,
        "log_file_max_size": Config.log_file_max_size,
        "log_file_max_age": Config.log_file_max_age,
        "log_file_max_count": Config.log_file_max_count
    }

    with open(config_file, "w") as f:
        json.dump(config_data, f, indent=4)


class LoggerUtils:
    def __init__(self):
        self.log_file_path = None

    def init_logging(self):
        user_folder = os.path.expanduser("~")
        config_folder = os.path.join(user_folder, ".pcmd")
        config_file = os.path.join(config_folder, "config.json")

        if not os.path.exists(config_folder):
            os.makedirs(config_folder)

        if not os.path.exists(config_file):
            # 如果 config.json 不存在，创建一个默认的配置文件
            create_config_file()

        load_logging_settings()

        # 设置日志文件路径为 config.json 所在的文件夹
        timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
        self.log_file_path = os.path.join(config_folder, f"pcmd_log_{timestamp}.txt")

    def save_log(self, message):
        if not Config.logging_enabled:
            return

        if not self.log_file_path:
            self.init_logging()

        with open(self.log_file_path, "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

        # 检查日志文件大小并清理旧日志
        cleanup_logs(self)

    def archive_log(self):
        if not self.log_file_path:
            return

        log_folder = os.path.dirname(self.log_file_path)
        log_file_base = os.path.basename(self.log_file_path)
        log_file_name, log_file_ext = os.path.splitext(log_file_base)
        archive_file_name = f"{log_file_name}_{time.strftime('%Y%m%d%H%M%S')}{log_file_ext}"
        archive_file_path = os.path.join(log_folder, archive_file_name)

        os.rename(self.log_file_path, archive_file_path)
