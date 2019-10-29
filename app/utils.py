from .models import Config
import datetime


def access_to_register(passcode):
    register_deadline = Config.get_value("register_deadline")
    if register_deadline and datetime.date.today() > register_deadline:
        return passcode
    return True
