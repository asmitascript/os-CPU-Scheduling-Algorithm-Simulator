# CPU Scheduling Algorithm Simulator

Project Title: CPU Scheduling Algorithm Simulator for Managing Jobs in a College Computer Laboratory

This is a mini-project that simulates and compares three major CPU scheduling algorithms: FCFS, SJF, and SRTF. It helps understand how an operating system manages multiple processes competing for CPU time.

## 1. Project overview

The simulator models a college computer laboratory where multiple students submit programs for execution. Each program is treated as a process with:

- Process ID
- Arrival Time (AT)
- Burst Time (BT)
- Completion Time (CT)
- Turnaround Time (TAT)
- Waiting Time (WT)

The simulator executes the processes using three scheduling algorithms and compares their performance.

## 2. Algorithms used

| Algorithm | Type | Working principle |
| --- | --- | --- |
| FCFS | Non-preemptive | First process to arrive executes first |
| SJF | Non-preemptive | Process with shortest burst time executes first |
| SRTF | Preemptive | Process with shortest remaining time executes first |

## 3. Performance metrics

- Completion Time (CT): Time when process execution finishes.
- Turnaround Time (TAT): Total time taken from arrival to completion.
- Waiting Time (WT): Total time spent waiting in the ready queue.
- Average Waiting Time: Average waiting time of all processes.
- Average Turnaround Time: Average turnaround time of all processes.

Formulas:

$$
TAT = CT - AT
$$

$$
WT = TAT - BT
$$

$$
Average\ WT = \frac{\sum WT}{n}
$$

## 4. System architecture

User Input

Process ID, Arrival Time, Burst Time

## 5. Technologies required

- Programming language: Python or C
- IDE: VS Code, PyCharm, or Code::Blocks
- Operating system: Windows/Linux
- Concepts: Operating Systems, CPU Scheduling, Process Management

## 6. Expected project outcomes

1. Simulate FCFS, SJF, and SRTF scheduling.
2. Calculate completion, waiting, and turnaround times.
3. Display scheduling results in tabular form.
4. Compare average waiting and turnaround times.
5. Identify which algorithm performs better for a given workload.
6. Understand preemptive and non-preemptive scheduling.

