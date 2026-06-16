<!-- GENERATED FILE - do not edit. Source: block-knowledge/assign-instance-name.yaml. Regenerate: make refgen -->
# Assign Instance Name

Assign a human-readable name to the running instance for traceability in analytics.

## How it works

Label this run. Instead of an Instance ID GUID, the Instances tab shows your name.

## When to use it

Make instances identifiable in the Instances list (vs raw GUIDs); assign early.

## Configuration

| Field | Description |
| --- | --- |
| Instance Name | Required. Static text, dynamic values, or a composite (e.g. "User: {{name}}"). |

## Behavior

- Sets the instance's name; appears in the Instances list (else the raw GUID shows).

## Things to watch for

- No result alias (produces no referenceable result).
- Assign early so the name is visible throughout the instance lifecycle.

## Related

- instances-concept
- expression-editor
