class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid  # Process ID
        self.at = at    # Arrival Time
        self.bt = bt    # Burst Time
        self.ct = 0     # Completion Time
        self.tat = 0    # Turnaround Time
        self.wt = 0     # Waiting Time

def main():
    # --- Task 1: Input Handling ---
    n = int(input("Enter number of processes (e.g., 4): "))
    processes = []

    for i in range(n):
        print(f"\nEntering data for Process {i+1}:")
        pid = input("Enter Process ID: ")
        at = int(input("Enter Arrival Time: "))
        bt = int(input("Enter Burst Time: "))
        processes.append(Process(pid, at, bt))

    # Display Input Table
    print("\n--- Input Data ---")
    print("PID\tArrival\tBurst")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}")

    # --- Task 2: FCFS Implementation ---
    # Sorting by Arrival Time (First Come First Serve)
    processes.sort(key=lambda x: x.at)
    
    current_time = 0
    for p in processes:
        if current_time < p.at:
            current_time = p.at  # Handling CPU Idle time
        
        current_time += p.bt
        p.ct = current_time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

    print("\n--- FCFS Results ---")
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

    # --- Task 3: SJF (Non-Preemptive) Implementation ---
    # Using a copy for SJF calculation
    sjf_procs = []
    # Sort remaining processes by Arrival Time initially
    remaining = sorted(processes, key=lambda x: x.at)
    time = 0
    
    while remaining:
        # Check which processes have arrived by 'time'
        available = [p for p in remaining if p.at <= time]
        
        if not available:
            time = remaining[0].at
            continue
            
        # Pick the process with the Shortest Burst Time (SJF)
        next_p = min(available, key=lambda x: x.bt)
        
        # Calculate times
        time += next_p.bt
        # Creating a result object for SJF
        res = Process(next_p.pid, next_p.at, next_p.bt)
        res.ct = time
        res.tat = res.ct - res.at
        res.wt = res.tat - res.bt
        
        sjf_procs.append(res)
        # Remove from remaining list
        for r in remaining:
            if r.pid == next_p.pid:
                remaining.remove(r)
                break

    print("\n--- SJF Results ---")
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in sjf_procs:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

    # --- Task 5: Performance Analysis ---
    avg_wt_fcfs = sum(p.wt for p in processes) / n
    avg_wt_sjf = sum(p.wt for p in sjf_procs) / n
    
    print(f"\nAverage Waiting Time (FCFS): {avg_wt_fcfs:.2f}")
    print(f"Average Waiting Time (SJF): {avg_wt_sjf:.2f}")

if __name__ == "__main__":
    main() 