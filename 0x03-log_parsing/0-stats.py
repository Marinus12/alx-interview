#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
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


def print_statistics():
    """Print the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handle the keyboard interruption signal (CTRL + C)."""
    print_statistics()
    sys.exit(0)


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()

        # Validate the line format
        if len(parts) < 9:
            continue

        try:
            # Parse the relevant parts of the line
            ip_address = parts[0]
            date = parts[3] + " " + parts[4]
            request = parts[5] + " " + parts[6] + " " + parts[7]
            status_code = parts[8]
            file_size = parts[9]

            # Validate request format
            if not (request.startswith("\"GET") and
                    request.endswith("HTTP/1.1\"")):
                continue

            # Validate status code and file size
            try:
                status_code = int(status_code)
                file_size = int(file_size)
            except ValueError:
                continue

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            total_file_size += file_size
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()

        except IndexError:
            continue

except Exception as e:
    print(f"An error occurred: {e}")


# Print the final statistics if the loop ends
print_statistics()
