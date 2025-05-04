from datetime import datetime

from dateutil.relativedelta import relativedelta
from sanic import json, text

from backend.app.user.UserEntity import UserEntity
from backend.database import SessionLocal


class UserService:

