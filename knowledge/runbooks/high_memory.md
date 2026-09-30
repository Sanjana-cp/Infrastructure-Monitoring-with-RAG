# High Memory Runbook

## Symptoms

- Available memory is consistently low.
- Applications may become slow or unstable.
- The system may start using swap heavily.
- Processes may be killed by the OOM killer.

## Investigation

1. Check memory usage in Prometheus.
2. Check available memory and swap usage.
3. Identify processes consuming the most memory.
4. Check recent application and Nginx logs in Loki.
5. Check whether memory usage is continuously increasing.

## Possible Causes

- Memory leak.
- Sudden increase in application workload.
- Too many concurrent processes.
- Large or unexpected requests.
- Insufficient memory for the workload.

## Remediation

- Identify the process consuming excessive memory.
- Investigate possible memory leaks.
- Reduce unnecessary workload.
- Restart the affected service when appropriate.
- Increase available resources or scale the service when necessary.
