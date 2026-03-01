# File: core.py
from copy import deepcopy as _deepcopy


class InitializableFromConfig(object):
    @classmethod
    def init_from_config(cls, config):
        return cls(**cls.parse_config(config))

    @classmethod
    def parse_config(cls, config):
        return _deepcopy(config)


class WithTeardown(object):
    def teardown(self):
        """
        Implement to take actions to tear down a class instance
        """
        pass
