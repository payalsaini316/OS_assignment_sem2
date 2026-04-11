def round_robin():
    n = int(input("Enter number of processes: "))
    
    burst_time = []
    for i in range(n):
        bt = int(input(f"Enter burst time for process P{i+1}: "))
        burst_time.append(bt)
    
    time_quantum = int(input("Enter time quantum: "))
    
    remaining = burst_time.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0

    while True:
        done = True
        
        for i in range(n):
            if remaining[i] > 0:
                done = False
                
                if remaining[i] > time_quantum:
                    time += time_quantum
                    remaining[i] -= time_quantum
                else:
                    time += remaining[i]
                    waiting_time[i] = time - burst_time[i]
                    remaining[i] = 0
        
        if done:
            break

    # Turnaround time calculation
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    # Print output
    print("\nP\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{i+1}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

    # Average
    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    print("\nAverage Waiting Time =", avg_wt)
    print("Average Turnaround Time =", avg_tat)


# Run
round_robin()
