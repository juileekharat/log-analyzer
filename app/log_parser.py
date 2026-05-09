import re
from collections import Counter
from datetime import datetime

def analyse_logs(file_path):

    # Initialize counts for each log level
    counts = {
        'INFO': 0,
        'WARNING': 0,
        'ERROR': 0
    }

    # Define a regex pattern to match log lines in the format: "timestamp log_level message"
    pattern = r"^(.*?)\s(INFO|WARNING|ERROR)\s(.*)$"

    total_lines = 0
    parsed_log = []
    error_messages = []
    error_per_hour = Counter()
    
    # Read the log file and count occurrences of each log level
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                timestamp, level, message = match.groups()
                parsed_log.append({
                    'timestamp': timestamp,
                    'level': level,
                    'message': message
                })
                
                dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                hour = dt.strftime("%H")

                total_lines += 1

                if level in counts:
                    counts[level] += 1

                if level == "ERROR":
                    error_messages.append(message)
                    error_per_hour[hour] += 1

    return {
        "total_lines": total_lines,
        **counts,
        "top_errors": dict(Counter(error_messages)),
        "error_per_hour": dict(error_per_hour),
        "error_hours": list(error_per_hour.keys()),
        "error_counts": list(error_per_hour.values()),
        "parsed_log": parsed_log
    }
