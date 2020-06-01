from nebula_sdk import Interface, WebhookServer
from quart import Quart, request

import logging

relay = Interface()
app = Quart('incident-triggered')

logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['POST'])
async def handler():
    data = await request.get_json()
    relay.events.emit({
        'incident_id': data['INCIDENT.INCIDENT_ID'],
        'incident_name': data['INCIDENT.INCIDENT_NAME'],
        'incident_state': data['INCIDENT.ENTITY_STATE'],
        'service': data['INCIDENT.SERVICE'],
        'incident_timestamp': data['INCIDENT.INCIDENT_TIMESTAMP']
    })
    return {'success': True}

if __name__ == '__main__':
    WebhookServer(app).serve_forever()
