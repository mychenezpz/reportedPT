import importlib.util
import os
import time, random
from logic.config_watcher import cfg

class KMBoxMouse:
    def __init__(self):
        module_path = cfg.kmnet_module_path
        module_name = os.path.splitext(os.path.basename(module_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.kmNet = module
        # Initialize the KMNet connection
        self.kmNet.init(cfg.kmnet_ip, cfg.kmnet_port, cfg.kmnet_uuid)
        # Enable keyboard and mouse monitoring
        self.kmNet.monitor(cfg.kmnet_monitor_rate)

    def random_delay(self, min_delay=0.1, max_delay=0.2):
        time.sleep(random.uniform(min_delay, max_delay))

    def click(self):
        self.kmNet.left(1)
        self.random_delay()
        self.kmNet.left(0)

    def press(self):
        self.kmNet.left(1)

    def release(self):
        self.kmNet.left(0)

    def move(self, x, y):
        self.kmNet.move(x, y)

    def close(self):
        self.kmNet.reboot()

    def __del__(self):
        self.close()