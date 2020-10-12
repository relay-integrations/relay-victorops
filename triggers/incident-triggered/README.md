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
      id: !Data incident_id
      name: !Data incident_name
      state: !Data incident_state
      service: !Data service
      timestamp: !Data incident_timestamp
```

## Example Raw Data 


```
POST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
X-VictorOps-Signature: XXXXXXXXXXXXXXXXXXXXX
Content-Length: 508
Connection: keep-alive
Host: 24.21.234.232:8080
Accept: */*
User-Agent: AHC/1.0

incident=31&created_by=%22ahpook%22&monitoring_tool=%22manual%22&vo_alert_rcv_time=%221602527561967%22&entity_display_name=%22Testing+to+localhost%22&message_type=%22CRITICAL%22&alert_type=%22CRITICAL%22&vo_uuid=%22fb2462d3-562e-45f1-824b-b1e870ec48af%22&entity_state=%22CRITICAL%22&entity_id=%2203890e97-15e8-4b2c-8241-e4f646a95c4b%22&state_message=%22maybe+I+don%27t+need+to+get+paged+after+all%22&monitor_name=%22vouser-ahpook%22&message=&vo_organization_id=%22relaysh%22&vo_monitor_type=%2228%22&summary=
```
