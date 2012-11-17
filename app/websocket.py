# coding: utf-8
import anyjson as json
from tornado.websocket import WebSocketHandler


class WSHandler(WebSocketHandler):
    def open(self):
        print 'new connection'
        self.write_message(json.dumps(dict(output="Hello World")))

    def on_message(self, incoming):
        print 'message received %s' % incoming

        text = json.loads(incoming).get('text', None)
        msg = text if text else 'Sorry could you repeat?'

        response = json.dumps(dict(output='Parrot: {0}'.format(msg)))
        self.write_message(response)

    def on_close(self):
        print 'connection closed'
