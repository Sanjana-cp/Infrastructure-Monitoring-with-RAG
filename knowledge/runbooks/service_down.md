# Service Down Runbook

## Symptoms

- A service is unreachable.
- Requests fail or time out.
- Monitoring reports that a target is down.

## Investigation

1. Check the service status.
2. Check whether the expected port is listening.
3. Check Prometheus target health.
4. Check recent service logs.
5. Check system CPU and memory usage.
6. Check whether another process is using the expected port.

## Possible Causes

- Service crashed.
- Service was stopped.
- Configuration error.
- Port conflict.
- Resource exhaustion.
- Dependency failure.

## Remediation

- Check the service logs for the failure reason.
- Correct configuration errors.
- Resolve port conflicts.
- Restart the service when appropriate.
- Verify that monitoring reports the service as healthy again.
