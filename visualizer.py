import matplotlib.pyplot as plt

def draw_gantt(schedule, title):
    fig, ax = plt.subplots()

    for task in schedule:
        pid, start, end = task
        ax.barh(pid, end - start, left=start)

    ax.set_xlabel("Time")
    ax.set_ylabel("Processes")
    ax.set_title(title)

    plt.show()