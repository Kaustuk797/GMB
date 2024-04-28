#    Stella (Development)
#    Copyright (C) 2021 - meanii (Anil Chauhan)
#    Copyright (C) 2021 - SpookyGang (Neel Verma, Anil Chauhan)

#   This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import dns.resolver

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pymongo import MongoClient
from pyrogram import Client
from pyromod import listen

from config import config
from Stella.StellaGban import StellaClient

#from stellagban import StellaClient

OWNER_ID = [6170129160, 2104674370]
BOT_ID="5619875667:AAGbvXd38MTEnHMK2IJcaNmar8_UoQLf4vo"
BOT_NAME = "BadmosBot"
BOT_USERNAME = "Mizuu_testBot"
LOG_CHANNEL = -2118207736
SUDO_USERS = [6170129160, 2104674370]
PREFIX = ['!', '/']
BACKUP_CHAT = -2118207736

StellaCli = Client(
    session_name='StellaSession',
    api_id=6133145,
    api_hash="30d4307da4885a00c58089d5f5503b5b",
    bot_token="5619875667:AAGbvXd38MTEnHMK2IJcaNmar8_UoQLf4vo"
)

# MongoDatabase dns configurations
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] 

StellaAPI = StellaClient(api_key=config.api.stella.api_key)

# Async scheduler
scheduler = AsyncIOScheduler()

try:
  StellaMongoClient = MongoClient(config.database.database_url)
  StellaDB = StellaMongoClient.stella_mongo
except:
  sys.exit(f"{BOT_NAME}'s database is not running!")

TELEGRAM_SERVICES_IDs = (
    [
        777000, # Telegram Service Notifications
        1087968824 # GroupAnonymousBot
    ]
)

GROUP_ANONYMOUS_BOT = 1087968824
