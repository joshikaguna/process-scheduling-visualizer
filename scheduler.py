from collections import deque

# ---------------- FCFS ----------------
def fcfs(processes):
    processes = sorted(processes, key=lambda x: x['arrival'])
    time = 0
    schedule = []
    completion = {}

    for p in processes:
        if time < p['arrival']:
            time = p['arrival']

        start = time
        time += p['burst']
        end = time

        schedule.append((p['pid'], start, end))
        completion[p['pid']] = end

    return schedule, calculate_metrics(processes, completion)


# ---------------- SJF (Non-Preemptive) ----------------
def sjf(processes):
    processes = sorted(processes, key=lambda x: x['arrival'])
    time = 0
    schedule = []
    completed = []
    completion = {}

    ready_queue = []

    while len(completed) < len(processes):
        # Add arrived processes
        for p in processes:
            if p not in completed and p not in ready_queue and p['arrival'] <= time:
                ready_queue.append(p)

        if not ready_queue:
            time += 1
            continue

        # Pick shortest job
        current = min(ready_queue, key=lambda x: x['burst'])
        ready_queue.remove(current)

        start = time
        time += current['burst']
        end = time

        schedule.append((current['pid'], start, end))
        completion[current['pid']] = end
        completed.append(current)

    return schedule, calculate_metrics(processes, completion)


# ---------------- Round Robin ----------------
def round_robin(processes, quantum):
    processes = sorted(processes, key=lambda x: x['arrival'])
    time = 0
    queue = deque()
    schedule = []
    completion = {}

    remaining = {p['pid']: p['burst'] for p in processes}
    i = 0

    while i < len(processes) or queue:
        # Add processes to queue
        while i < len(processes) and processes[i]['arrival'] <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            time += 1
            continue

        current = queue.popleft()
        pid = current['pid']

        start = time
        exec_time = min(quantum, remaining[pid])
        time += exec_time
        remaining[pid] -= exec_time
        end = time

        schedule.append((pid, start, end))

        # Add new arrivals during execution
        while i < len(processes) and processes[i]['arrival'] <= time:
            queue.append(processes[i])
            i += 1

        if remaining[pid] > 0:
            queue.append(current)
        else:
            completion[pid] = end

    return schedule, calculate_metrics(processes, completion)


# ---------------- METRICS ----------------
def calculate_metrics(processes, completion):
    result = []
    total_wt = 0
    total_tat = 0

    for p in processes:
        pid = p['pid']
        arrival = p['arrival']
        burst = p['burst']

        tat = completion[pid] - arrival
        wt = tat - burst

        total_wt += wt
        total_tat += tat

        result.append({
            'pid': pid,
            'waiting_time': wt,
            'turnaround_time': tat
        })

    avg_wt = total_wt / len(processes)
    avg_tat = total_tat / len(processes)

    return result, avg_wt, avg_tat