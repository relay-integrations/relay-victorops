# victorops-trigger-incident-triggered

This [VictorOps](https://victorops.com) trigger fires when a new incident is created. 

## Usage and Schema

See the [event.schema.json](event.schema.json) for the formal description of its outputs and the [trigger.yaml](trigger.yaml) for usage examples.

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
