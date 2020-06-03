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

## Example Trigger

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

## Example Raw Data 

```
{
  "INCIDENT.INCIDENT_ID": "14",
  "INCIDENT.INCIDENT_NAME": "#14",
  "INCIDENT.INCIDENT_TIMESTAMP": 1591156454582,
  "INCIDENT.ENTITY_TYPE": "SERVICE",
  "INCIDENT.ENTITY_SLUG": "",
  "INCIDENT.HOST": "",
  "INCIDENT.SERVICE": "test14",
  "INCIDENT.CURRENT_PHASE": "UNACKED",
  "INCIDENT.ANNOTATION_COUNT": 0,
  "INCIDENT.ALERT_COUNT": 1,
  "INCIDENT.ENTITY_STATE": "CRITICAL",
  "INCIDENT.POLICIES_PAGED.0.IS_DISPLAYABLE": false,
  "INCIDENT.POLICIES_PAGED.0.POLICY.NAME": "Generated Direct User Policy for kenazk",
  "INCIDENT.POLICIES_PAGED.0.POLICY.SLUG": "directUserPolicySlug-kenazk",
  "INCIDENT.POLICIES_PAGED.0.TEAM.NAME": "",
  "INCIDENT.POLICIES_PAGED.0.TEAM.SLUG": "",
  "INCIDENT.MONITOR_TYPE": "manual",
  "INCIDENT.MONITOR_NAME": "vouser-kenazk",
  "INCIDENT.FIRST_ALERT_UUID": "a5f26d26-7781-4aad-9abd-ad2159b2c489",
  "INCIDENT.LATEST_ALERT_UUID": "a5f26d26-7781-4aad-9abd-ad2159b2c489",
  "INCIDENT.TAGS.0": "incident14",
  "INCIDENT.TAGS.1": "routingdefault",
  "INCIDENT.TAGS.2": "typesystemmessagenotify",
  "INCIDENT.TAGS.3": "typeincidentnotify",
  "INCIDENT.SEQUENCING.SEQUENCE": 85,
  "INCIDENT.SEQUENCING.SERVICE_TIME": 1591156454000,
  "INCIDENT.ROOM_ID": "*",
  "INCIDENT.IS_MULTI_RESPONDER": false,
  "INCIDENT.IS_MUTED": false,
  "INCIDENT.ENTITY_DISPLAY_NAME": "test14",
  "INCIDENT.ACK_DATA.ACKS_EXPECTED": 0,
  "INCIDENT.ACK_DATA.ACKS_RECEIVED": 0,
  "ALERT.VO_ORGANIZATION_ID": "relay",
  "ALERT.created_by": "kenazk",
  "ALERT.monitoring_tool": "manual",
  "ALERT.VO_UUID": "a5f26d26-7781-4aad-9abd-ad2159b2c489",
  "ALERT.entity_display_name": "test14",
  "ALERT.VO_ALERT_RCV_TIME": "1591156454582",
  "ALERT.message_type": "CRITICAL",
  "ALERT.alert_type": "CRITICAL",
  "ALERT.entity_state": "CRITICAL",
  "ALERT.entity_id": "bb065e38-5291-46f8-a69d-1414ee56636e",
  "ALERT.state_message": "test14",
  "ALERT.monitor_name": "vouser-kenazk",
  "ALERT.VO_MONITOR_TYPE": "28",
  "STATE.ENTITY_ID": "bb065e38-5291-46f8-a69d-1414ee56636e",
  "STATE.ENTITY_SLUG": "vouser-kenazk--test14",
  "STATE.HOST": "",
  "STATE.SERVICE": "test14",
  "STATE.LAST_UUID": "a5f26d26-7781-4aad-9abd-ad2159b2c489",
  "STATE.CURRENT_ALERT_PHASE": "UNACKED",
  "STATE.ACK_MSG": "",
  "STATE.ACK_USER": "SYSTEM",
  "STATE.ACK_TIMESTAMP": 0,
  "STATE.CURRENT_STATE": "CRITICAL",
  "STATE.STATE_START_TIME": 1591156454582,
  "STATE.ALERT_COUNT": 1,
  "STATE.LAST_TIMESTAMP": 1591156454582,
  "STATE.INFO_URL": "",
  "STATE.NOTIFICATIONTYPE": "",
  "STATE.VO_ALERT_TYPE": "SERVICE",
  "STATE.INCIDENT_NAME": "14",
  "STATE.INCIDENT_TIMESTAMP": 1591156454582,
  "STATE.MONITOR_TYPE": "Manual",
  "STATE.USERS_PAGED.0": "kenazk",
  "STATE.ACKED_BY": null,
  "STATE.ACKED_AT": null,
  "STATE.RESOLVED_BY": null,
  "STATE.RESOLVED_AT": null
}
```