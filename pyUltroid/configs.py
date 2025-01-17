# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default=6, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", "AQAylOHbkITMqddhtTcN47J8e75ONW8YUPFulK1f7k19VGI1mk_B1u_6G_1PY1GippDRlQzQ4w-jQlZcFbvk4OAIdGOcuY9FTeHGyvgBILAH9j9IcdsgLrrYZFSTcQEX1tkEozrFnx9s2ysZT8MmHAtqS88DVyc0MvywMOoSh5ba8rqHmVP4RAT5a1auP1GaZiSqfwUBZj9XpUeOH_-YmqWE1xE6GHrCpvlGVyRg24L84ODEDTgJLxrYvjyZuMrYbMZUWwuHTkOCja-77Jt3O3e28JMikHzGiPywRPvUP2FLo1kkQtCMeaXbxJCyHQuxzyO4l0bshdDhxp8p8sqOpU5-AAAAAVIO0vgA")
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL", default=None))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default=None)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", "6044780741:AAGamK1in1_DbjJ57wfF-ikcE7X3RysHttM")
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", "mongodb+srv://gand012:gand01@cluster0.8h2015g.mongodb.net/?retryWrites=true&w=majority")
