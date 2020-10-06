from relay_sdk import Interface, WebhookServer
from quart import Quart, request, render_template_string

import logging

relay = Interface()
app = Quart('incident-triggered')

logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['POST'])
async def handler():
    data = await request.form

    relay.events.emit({
	'incident_id': data['incident'],
	'incident_name': data['entity_display_name'],
	'incident_state': data['entity_state'],
	'incident_routing_key': data['routing_keys'],
	'incident_entity_id': data['entity_id']
    })
    return await render_template_string("Relay received payload about {{incident_id}}", incident_id=data['incident'])

if __name__ == '__main__':
    WebhookServer(app).serve_forever()
