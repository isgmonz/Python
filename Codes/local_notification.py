import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="alert",
        message="Please",
        timeout=10
    )
    time.sleep(.5)
