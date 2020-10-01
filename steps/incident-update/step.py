#!/usr/bin/env python
# posts an event to VictorOps from Relay

import requests, os
from relay_sdk import Interface, Dynamic as D

relay = Interface()

url_base = relay.get(D.endpoint_url),
routing_key = relay.get(D.routing_key)

url = url_base + '/' + routing_key

event_payload = {
  'message_type': 'INFO',
  'entity_id': relay.get(D.entity_id),
  'entity_display_name': relay.get(D.entity_display_name),
  'state_message': relay.get(D.state_message),
}

r = requests.post(url, json=event_payload)

print('Emitted event to VictorOps REST API, got response: ', r.text)

r.raise_for_status()
