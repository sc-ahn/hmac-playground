import hmac
from time import time
from common.settings import env

class HMACHelper:
    key: str
    digestmod: str

    def __init__(self, key: str, digestmod: str = "sha256"):
        self.key = key
        self.digestmod = digestmod

    def _extract_timestamp(self, message, separator="-") -> tuple[int, str]:
        """
        return timestamp and message
        """

        timestamp, message = message.split(separator, 1)
        return int(timestamp), message

    def _check_expired(self, timestamp, expire_seconds: int) -> bool:
        """
        return True if message is expired
        """
        return time() - int(timestamp) > expire_seconds

    def generate(self, message: str) -> str:
        hmac_msg = hmac.new(self.key.encode(), message.encode(), self.digestmod)
        return hmac_msg.hexdigest()

    def verify(self, message: str, digest: str) -> bool:
        timestamp, _ = self._extract_timestamp(message)
        if self._check_expired(timestamp, env.expire_seconds):
            return False
        return hmac.compare_digest(digest, self.generate(message))
