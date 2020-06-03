# victorops-trigger-incident-triggered

This [VictorOps](https://victorops.com) trigger fires when a new incident is created. 

## Data Emitted 

| Name | Data type | Description | 
|------|-----------|-------------|
| `incident_id` | string | id of the incident | 
| `incident_name` | string | name of the incident | 
| `incident_state` | string | severity of the incident | 
| `service` | string | impacted service name | 
| `incident_current_phase` | string | current phase of the incident |

## Example

```
parameters:
  id:
    default: ""
  name:
    default: ""
  state:
    default: ""
  service:
    default: ""
  timestamp:
    default: ""

triggers:
- name: victorops-incident
  source:
    type: webhook
    image: relaysh/victorops-trigger-incident-triggered:latest
  binding:
    parameters:
      id: !Data 'incident_id'
      name: !Data 'incident_name'
      state: !Data 'incident_state'
      service: !Data 'service'
      timestamp: !Data 'incident_timestamp'
```