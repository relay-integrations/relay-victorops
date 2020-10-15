#!/usr/bin/env python
# posts an event to VictorOps from Relay

import requests, os
from relay_sdk import Interface, Dynamic as D

relay = Interface()

URLBase = relay.get(D.endpointURL)
routingKey = relay.get(D.routingKey)

url = f"{URLBase}{routingKey}"

eventPayload = {
  'message_type': 'INFO',
  'entity_id': relay.get(D.entityID),
  'entity_display_name': relay.get(D.entityDisplayName),
  'state_message': relay.get(D.stateMessage),
}

r = requests.post(url, json=eventPayload)

print('Emitted event to VictorOps REST API, got response: ', r.text)

r.raise_for_status()
