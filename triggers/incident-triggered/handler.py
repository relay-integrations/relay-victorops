from relay_sdk import Interface, WebhookServer
from quart import Quart, request, render_template_string

import logging, sys

relay = Interface()
app = Quart('incident-triggered')

logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['POST'])
async def handler():
    data = await request.form

    event = { 'webhook_payload': {},
              'incident': 0
            }

    # handle incident_id a bit special since it's the main key, the rest of the
    # payload may change so just stuff it in a top-level key unmodified
    for field, value in data.items():
        event['webhook_payload'][field] = value.strip('"')
        if field == 'incident':
            event['incident'] = value

    print("Emitting event about incident " + event['incident'] + ":::",file=sys.stderr)
    print(event,file=sys.stderr)
    relay.events.emit(event,key=event['webhook_payload']['entity_id'])

    return await render_template_string("Relay received payload about {{incident}}", incident=event['incident'])

if __name__ == '__main__':
    WebhookServer(app).serve_forever()
