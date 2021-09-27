import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1918817506:AAGHDwJ40y2mJtqGWzzYCBTUMNihYnILukU")
    APP_ID = int(os.environ.get("APP_ID", 7139560))
    API_HASH = os.environ.get("API_HASH", "805d46ae2d01bf1591bea89f54e76f13")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1269408652 1886319600").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 3600
    DEF_WATER_MARK_FILE = ""
    # watermark file
    DEF_WATER_MARK_FILE = ""
