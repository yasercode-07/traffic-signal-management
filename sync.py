def sync_signals(junction_times):
    
    synced = []
    
    max_cycle = max(junction_times)
    
    for time in junction_times:
        synced.append(max_cycle - time)
    
    return synced
