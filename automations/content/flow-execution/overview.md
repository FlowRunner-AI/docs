When flow is enabled and does not have a timer. It will run any actions that it starts with (if any) until it
reaches the first trigger. Now it waits for the trigger to fire. At this point, there is only one instance of the
flow is running. Additional instances of the flow could be launched with the "Call Flow" request.

In that mode one of the three things could happen:

1. Trigger is fired with specific InstanceID - specific instance of the flow continues to run.
2. Tirgger is fired without specific InstanceID - a random instance of the flow continues to run
3. Trigger is fired to activate all waiting instances.

For additional flexibility, and to avoid cases 2 and 3, the "Call Flow" request may create a "reserved" 
instance by assining InstanceID at the time of the call. This parameter would be optional.

When flow is enabled and has a timer, every run of the timer creates a new instance of the flow. If the flow has a trigger and multiple instances reach the same trigger (even if it is the first block in the flow), a pool is created to support cases 2 and 3 above. 
==================================================

FLOWS WITHOUT TIMERS
---------------------
When a flow is enabled and enters the LIVE state, it does not automatically execute. To execute the flow, the user application must
use the "Call Flow" API. The API returns a special InstanceID which uniquely identify the running instance of the flow. Multiple calls of the "Call Flow" API will create a new instance of the flow if it starts with an action or prepare the Automations infrastructure to allocate a new instance if the flow starts with a trigger.

If the flow enters the waiting state with a trigger, it may be important that the trigger activates the same flow instance. To facilitate that, Backendless provides two options: (1) all triggers include "Condition" that can describe the rules for narrowing down to the specific flow instance and (2) all APIs to activate a trigger include the "executionId" parameter than may be set to the provided InstanceId.

Suppose there are multiple running instances of the flow (each created with the "Call Flow" API) and some (or all) of them enter the waiting state on a trigger. As an alternative to targeting a specific flow instance using it's "InstanceID", the trigger may:
- trigger/activate all waiting instances using the "activateAll=true" parameter
- trigger/activate any of the waiting instances using the "activateAny=true" parameter

FLOWS WITH TIMERS
------------------
A flow with a schedule starts automatic execution with every run of the timer. As a result, a flow with a timer may have multiple instances running (except when the flow uses the "Run Once" time mode). These instances generally do not need to be "activated" with the "Call Flow" API. However, when it comes to triggers, the same rules as described above apply. 