from scheduler import fcfs, sjf, round_robin
from visualizer import draw_gantt

processes = [
    {'pid': 'P1', 'arrival': 0, 'burst': 5},
    {'pid': 'P2', 'arrival': 1, 'burst': 3},
    {'pid': 'P3', 'arrival': 2, 'burst': 8},
]

print("\nChoose Algorithm:")
print("1. FCFS")
print("2. SJF")
print("3. Round Robin")

choice = int(input("Enter choice: "))

if choice == 1:
    schedule, metrics = fcfs(processes)
    title = "FCFS Scheduling"

elif choice == 2:
    schedule, metrics = sjf(processes)
    title = "SJF Scheduling"

elif choice == 3:
    quantum = int(input("Enter Time Quantum: "))
    schedule, metrics = round_robin(processes, quantum)
    title = "Round Robin Scheduling"

else:
    print("Invalid choice!")
    exit()

# Print Results
print("\nGantt Chart Data:", schedule)

details, avg_wt, avg_tat = metrics

print("\nProcess Details:")
for d in details:
    print(d)

print("\nAverage Waiting Time:", avg_wt)
print("Average Turnaround Time:", avg_tat)

# Draw Gantt Chart
draw_gantt(schedule, title)