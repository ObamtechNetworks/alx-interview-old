#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics:
"""

import sys
import re

# Initialize the number of lines read, a dictionary to count status codes,
# and the total file size
lines_read = 0
status_code_count = {}
total_size = 0

try:
    for line in sys.stdin:
        lines_read += 1

        # Regular expression to match the line format
        line_match = re.search(
            r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s-\s\[[\d -:.]*\]\s'
            r'"GET\s\/projects\/260\sHTTP\/1.1"\s\d{3}\s\d+$',
            line
        )

        if line_match:
            # Extract the status code and file size using regular expressions
            status_match = re.search(r'(?<=HTTP\/1.1" )\d{3}', line)
            file_size_match = re.search(r'\d+$', line)

            if status_match and file_size_match:
                status_code = status_match.group()
                file_size = int(file_size_match.group())

                # Update the count of the status code
                status_code_count[status_code] = (
                    status_code_count.get(status_code, 0) + 1
                )

                # Add the file size to the total size
                total_size += file_size

        # Every 10 lines, print the statistics
        if lines_read % 10 == 0:
            print(f"File size: {total_size}")
            for status in sorted(status_code_count):
                print(f"{status}: {status_code_count[status]}")

except KeyboardInterrupt:
    # Handle keyboard interruption gracefully
    pass

finally:
    # Print the final statistics when the script ends
    print(f"File size: {total_size}")
    for status in sorted(status_code_count):
        print(f"{status}: {status_code_count[status]}")
