import config
import discord
import sql
import logging

class SpellBot2:

    def __init__(self, conf_file='config.cfg'):
        self.conf_manager = config.ConfigManager(config_path=conf_file)
        self.db = sql.SQLManager(connect=True)