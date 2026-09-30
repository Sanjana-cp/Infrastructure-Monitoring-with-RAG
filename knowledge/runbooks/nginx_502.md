# Nginx 502 Runbook

## Symptoms

- Nginx returns HTTP 502 Bad Gateway.
- Users cannot reach the backend application.
- Nginx logs contain upstream connection or response errors.

## Investigation

1. Check recent Nginx logs in Loki.
2. Check whether the backend service is running.
3. Check the backend listening port.
4. Check CPU and memory usage in Prometheus.
5. Check whether request traffic increased.
6. Check backend response time and errors.

## Possible Causes

- Backend service is down.
- Backend is overloaded.
- Backend is not listening on the expected port.
- Connection to the backend timed out.
- Resource exhaustion.

## Remediation

- Verify that the backend service is running.
- Verify the configured upstream address and port.
- Investigate backend errors.
- Reduce excessive workload or scale the service when appropriate.
- Restart the backend only when appropriate and after identifying the cause.
