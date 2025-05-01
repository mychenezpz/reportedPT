import importlib.util
import os
import time
import random
from logic.config_watcher import cfg

# Load the KMNet extension as a module-level singleton
module_path = cfg.kmnet_module_path
module_name = os.path.splitext(os.path.basename(module_path))[0]
spec = importlib.util.spec_from_file_location(module_name, module_path)
kmNet = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kmNet)

# Initialize KMNet connection
kmNet.init(cfg.kmnet_ip, cfg.kmnet_port, cfg.kmnet_uuid)
kmNet.monitor(cfg.kmnet_monitor_rate)

def kmnet_move(x, y):
    kmNet.move(x, y)

def kmnet_press():
    kmNet.left(1)

def kmnet_release():
    kmNet.left(0)

def kmnet_click():
    kmNet.left(1)
    time.sleep(random.uniform(0.1, 0.2))
    kmNet.left(0)

def kmnet_close():
    kmNet.reboot()