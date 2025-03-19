from tbavli.consts.settings import Settings
from tbavli.utils.util import Util


class ServerConstants:
    """Holds server-related constants."""

    settings = Settings()

    GAME_VERSION = 95
    PATCH = "1"
    LOCALE = 8

    SERVER_HOST = Util.get_host(settings.server_address)
    LOGIN_PORT = settings.login_port
    CHANNEL_PORT = settings.channel_port