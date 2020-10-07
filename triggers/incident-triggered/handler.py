from relay_sdk import Interface, WebhookServer
from quart import Quart, request, render_template_string

import logging

relay = Interface()
app = Quart('incident-triggered')

logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['POST'])
async def handler():
    data = await request.form

    event = {}

    for field, value in data.items():
        event[field] = value

    relay.events.emit(event)


    return await render_template_string("Relay received payload about {{incident_id}}", incident_id=data['incident'])

if __name__ == '__main__':
    WebhookServer(app).serve_forever()
