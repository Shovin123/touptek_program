import tracemalloc

# Start tracing memory allocations
tracemalloc.start()

# Your code here

# Stop tracing and get a snapshot of memory usage
snapshot = tracemalloc.take_snapshot()

# Print the top 10 lines that allocate the most memory
top_stats = snapshot.statistics('lineno')
print("[ Top 10 memory usage by line ]")
for stat in top_stats[:10]:
    print(stat)
