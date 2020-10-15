from relay_sdk import Interface, WebhookServer
from quart import Quart, request, render_template_string

import logging, sys

relay = Interface()
app = Quart('incident-triggered')

logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['POST'])
async def handler():
    data = await request.form

    event = { 'incident': 0 }

    # the payload comes in with urlencoded double-quotes around the keys ...
    for field, value in data.items():
        event[field] = value.strip('"')

    relay.events.emit(event,key=event['entity_id'])

    return await render_template_string("Relay received payload about {{incident}}", incident=event['incident'])

if __name__ == '__main__':
    WebhookServer(app).serve_forever()
