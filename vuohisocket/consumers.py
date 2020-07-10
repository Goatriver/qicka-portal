# vuohisocket/consumers.py
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from vuohisocket.led_driver.led import LedStripSerial, LedStripSerialException
import json
import logging

logger = logging.getLogger("django." + __name__)


class LedConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        # Called on connection.
        # To accept the connection call:
        await self.accept()

    async def receive_json(self, content, **kwargs):
        if 'error' in content.keys():
            await self.send_json(content)
            return
        try:
            with LedStripSerial('/dev/ttyACM0') as led_strip:
                led_strip.write_to_ser(content['r'], content['g'], content['b'])

            await self.send_json({'status': 'ok'})

        except LedStripSerialException as e:
            await self.send_json({'status': 'error', 'error': str(e)})

    async def decode_json(self, text_data):
        try:
            return await super().decode_json(text_data)
        except json.JSONDecodeError as er:
            return {'status': 'error', 'error': 'Malformed JSON: {} - \"{}\" was given'.format(str(er), text_data)}




