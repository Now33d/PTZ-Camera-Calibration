import os
import time
from hikvisionapi import Client


class Capture():
    event_id = None
    table = 'capture_logs'

    def __init__(self):
        super().__init__()
        # logging.info('Script Started')
        # self.read_params()
        self.user = os.getlogin()
        self.cam = Client('http://192.168.0.145', 'admin', 'Lums@hik12345')

        self.image_dest = '/home/' + str(self.user) + '/images/'

        if not os.path.exists(self.image_dest):
            os.makedirs(self.image_dest)

    def current_milli_time(self):
        return round(time.time() * 1000)

    def run(self):

        try:

            print("Start Capturing")
            image_response = self.cam.Streaming.channels[101].picture(method='get', type='opaque_data')
            if not os.path.exists(self.image_dest):
                os.makedirs(self.image_dest)

            with open(self.image_dest + '/' + str(self.current_milli_time()) + '.jpg', 'wb') as f:
                for chunk in image_response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print(image_response)
            # response = self.cam.Event.notification.alertStream(method='get', type='Stream')
            # status = (response[0]["EventNotificationAlert"]["eventState"])

        except Exception as e:
            print(e)


if __name__ == "__main__":
    capture = Capture()
    capture.run()
