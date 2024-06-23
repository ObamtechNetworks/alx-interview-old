#!/usr/bin/python3
"""LOG PARSING"""
import sys
import signal

# Initialize the metrics
total_file_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}


def print_metrics():
    """Print the metrics to stdout"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """Handle the SIGINT signal (Ctrl+C)"""
    print_metrics()
    sys.exit(0)


# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

        parts = line.split()
        if len(parts) < 7:
            continue

        # Extract file size
        try:
            file_size = int(parts[-1])
            total_file_size += file_size
        except ValueError:
            continue

        # Extract status code
        try:
            status_code = int(parts[-2])
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1
        except ValueError:
            continue

        # Print metrics after every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
    raise

# Print metrics for the remaining lines if any
print_metrics()
