#!/usr/bin/python3

import sys

metrics = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) > 7:
            status = parts[-2]
            size = int(parts[-1])
            if status in metrics:
                metrics[status] += 1
            total_size += size
        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code, count in sorted(metrics.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code, count in sorted(metrics.items()):
        if count > 0:
            print(f"{code}: {count}")
