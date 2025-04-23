from collections import deque

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def round_robin(processes, quantum):
    time = 0
    queue = deque(processes)

    while queue:
        process = queue.popleft()
        if process.remaining_time > quantum:
            time += quantum
            process.remaining_time -= quantum
            queue.append(process)
        else:
            time += process.remaining_time
            process.remaining_time = 0
            process.completion_time = time
            process.turnaround_time = process.completion_time
            process.waiting_time = process.turnaround_time - process.burst_time

    return processes

def print_metrics(processes):
    total_turnaround = 0
    total_waiting = 0
    print("Proceso | Burst | Turnaround | Waiting")
    print("----------------------------------------")
    for p in processes:
        print(f"P{p.pid}\t   {p.burst_time}\t     {p.turnaround_time}\t        {p.waiting_time}")
        total_turnaround += p.turnaround_time
        total_waiting += p.waiting_time
    print("----------------------------------------")
    n = len(processes)
    print(f"Promedio Turnaround: {total_turnaround / n:.2f}")
    print(f"Promedio Waiting: {total_waiting / n:.2f}")

processes = [
    Process(1, 10),
    Process(2, 5),
    Process(3, 8)
]
quantum = 3

completed = round_robin(processes, quantum)
print_metrics(completed)

# Todos los procesos iguales
procesos = [Process(1, 6), Process(2, 6), Process(3, 6)]
quantum = 2
# Quantum mayor que algunos procesos
procesos = [Process(1, 4), Process(2, 9), Process(3, 5)]
quantum = 6
# Quantum muy pequeño
procesos = [Process(1, 10), Process(2, 2), Process(3, 1)]
quantum = 1
