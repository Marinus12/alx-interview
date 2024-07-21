#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.

The input format is expected to be:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Lines that do not match this format are skipped.

After every 10 lines and/or a keyboard interruption (CTRL + C), the script prints these statistics:
- Total file size: the sum of all <file size> values
- Number of lines by status code (only for the specified codes: 200, 301, 400, 401, 403, 404, 405, 500)

Usage:
    ./0-generator.py | ./0-stats.py
"""

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
    """Print the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C) to print statistics and exit."""
    print_stats()
    sys.exit(0)


# Set the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
try:
    for line in sys.stdin:
        parts = line.split()

        # Validate the line format
        if len(parts) != 9 or parts[5] != '"GET' or parts[6] != '/projects/260' or parts[7] != 'HTTP/1.1"':
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
