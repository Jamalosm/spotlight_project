from dotenv import load_dotenv
import os
from .base import *

DEBUG = False
load_dotenv()

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")