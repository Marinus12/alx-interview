#!/usr/bin/python3
import sys
import signal

# Initialize variables to hold the total file size and count of status codes
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

def print_stats():
    """ Print the accumulated statistics """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """ Handle keyboard interruption (CTRL + C) """
    print_stats()
    sys.exit(0)

# Set the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
try:
    for line in sys.stdin:
        parts = line.split()
        
        # Validate the line format
        if len(parts) != 9:
            continue

        try:
            # Extract relevant parts
            file_size = int(parts[8])
            status_code = int(parts[7])
            
            # Accumulate metrics
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            
            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            continue

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
except BrokenPipeError:
    sys.stderr.close()
    sys.stdout.close()
