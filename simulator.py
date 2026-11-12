
def fcfs(processes):
    jobs = sorted(processes, key=lambda p: (p["at"], p["pid"]))
    time = 0
    result = []

    for p in jobs:
        start = max(time, p["at"])
        ct = start + p["bt"]
        tat = ct - p["at"]
        wt = tat - p["bt"]

        result.append({
            "pid": p["pid"],
            "ct": ct,
            "tat": tat,
            "wt": wt
        })
        time = ct

    return result


def sjf(processes):
    remaining = processes.copy()
    result = []
    time = 0

    while remaining:
        available = [p for p in remaining if p["at"] <= time]

        if not available:
            time = min(p["at"] for p in remaining)
            continue

        p = min(available, key=lambda x: (x["bt"], x["at"], x["pid"]))

        ct = time + p["bt"]
        tat = ct - p["at"]
        wt = tat - p["bt"]

        result.append({
            "pid": p["pid"],
            "ct": ct,
            "tat": tat,
            "wt": wt
        })

        time = ct
        remaining.remove(p)

    return result


def srtf(processes):
    remaining = {p["pid"]: p["bt"] for p in processes}
    result = {}
    time = 0
    completed = 0
    n = len(processes)

    while completed < n:
        available = [
            p for p in processes
            if p["at"] <= time and remaining[p["pid"]] > 0
        ]

        if not available:
            time += 1
            continue

        p = min(
            available,
            key=lambda x: (
                remaining[x["pid"]],
                x["at"],
                x["pid"]
            )
        )

        remaining[p["pid"]] -= 1
        time += 1

        if remaining[p["pid"]] == 0:
            ct = time
            tat = ct - p["at"]
            wt = tat - p["bt"]

            result[p["pid"]] = {
                "pid": p["pid"],
                "ct": ct,
                "tat": tat,
                "wt": wt
            }
            completed += 1

    return list(result.values())


def display(name, results):
    print(f"\n--- {name} ---")
    print("PID\tCT\tTAT\tWT")

    for p in sorted(results, key=lambda x: x["pid"]):
        print(
            f'{p["pid"]}\t{p["ct"]}\t'
            f'{p["tat"]}\t{p["wt"]}'
        )

    avg_wt = sum(p["wt"] for p in results) / len(results)
    avg_tat = sum(p["tat"] for p in results) / len(results)

    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


# Main program
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    print(f"\nProcess P{i + 1}")
    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))

    if at < 0 or bt <= 0:
        raise ValueError("Arrival time must be >= 0 and burst time > 0")

    processes.append({
        "pid": f"P{i + 1}",
        "at": at,
        "bt": bt
    })

display("FCFS", fcfs(processes))
display("SJF", sjf(processes))
display("SRTF", srtf(processes))
