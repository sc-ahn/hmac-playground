from time import time
from common.settings import env
from secure.core import HMACHelper

hmac = HMACHelper(env.key, env.digestmod)

def inject_timestamp(message: str, separator="-") -> str:
    """
    return message with timestamp
    """
    return f"{int(time())}{separator}{message}"
