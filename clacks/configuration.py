import os
import json
import atexit

class Config(object):

    _CONFIG_FILE = '~/.config/clacks/settings'

    def __init__(self, custom_path=_CONFIG_FILE, auto_load=False):
        self.loaded = False
        self.file_path = os.path.expanduser(custom_path)
        if auto_load:
            self.load()

    def save(self):
        if not self.loaded:
            raise RuntimeError("Config has not been loaded yet!")

        content = json.dumps(self._config)

        # make sure correct directories exist
        directory = os.path.dirname(self.file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # save to file
        with open(self.file_path, "w") as text_file:
            text_file.write(content)

    def load(self):
        if self.loaded:
            raise RuntimeError ("Config has already been loaded!")
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as text_file:
                self._config = json.loads(text_file.read())
        else:
            self._config = {}
        self.loaded = True

    def set(self, k, v):
        self._config[k] = v

    def get(self, k):
        return self._config[k]

    def iteritems(self):
        return self._config.iteritems()

    def keys(self):
        return self._config.keys()

config = Config()

