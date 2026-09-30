# High CPU Runbook

## Symptoms

- CPU usage remains consistently high.
- Application response time may increase.
- Requests may start timing out.
- Nginx may return 502 or 504 errors if the backend becomes overloaded.

## Investigation

1. Check CPU usage in Prometheus.
2. Check whether request traffic increased.
3. Check recent Nginx logs in Loki.
4. Check which process is consuming CPU.
5. Check application response time and error rate.

## Possible Causes

- Sudden increase in incoming traffic.
- CPU-intensive application workload.
- Runaway process.
- Inefficient application operation.

## Remediation

- Identify the process responsible for high CPU usage.
- Check whether the increase is caused by legitimate traffic.
- Investigate application errors or slow operations.
- Reduce unnecessary workload or scale the service when appropriate.
