# victorops-step-incident-update

This step updates a VictorOps timeline with information from a Relay workflow.  It will update the account timeline and optionally, if an `entity_id` for an existing incident is supplied to the step, will associate the update with that incident. It posts as `INFO` level messages. It requires that you enable the REST integration on your VictorOps account; doing so will generate a unique URL that you should store as a Secret named `endpointURL` in Relay, associated with this workflow.

## Specification

See the [step.schema.json](https://github.com/relay-integrations/relay-victorops/blob/master/steps/incident-update/spec.schema.json) file for the formal specification of how to use this step.

## Usage

See the [examples section in step.yaml](https://github.com/relay-integrations/relay-victorops/blob/master/steps/incident-update/step.yaml) for examples of how to use this step in a workflow.
