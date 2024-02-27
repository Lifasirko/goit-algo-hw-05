import re
import sys
from typing import List, Dict


def parse_log_line(line: str) -> Dict[str, str]:
    pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>.*)'
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    return {}


def load_logs(file_path: str) -> List[Dict[str, str]]:
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            log = parse_log_line(line.strip())
            if log:
                logs.append(log)
    return logs


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    counts = {}
    # errors = str
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    # for log in logs:
    #     level = log['level']
    #     if level == "ERROR":
    #         errors += f"{log['date'] }"

    return counts


def display_log_counts(counts: Dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<15} | {count}")


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    return [log for log in logs if log['level'] == level.upper()]


def main():
    if len(sys.argv) < 2:
        file_path = input("Please provide the path to the log file.")
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
    # file_path = sys.argv[1]
    # logs = load_logs(file_path)
    # print(1)

    elif len(sys.argv) == 3:
        level = sys.argv[2]
        file_path = sys.argv[1]
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        # лямбда вираз, який просили. хоча, як на мене, це дуже ускладнює читаємість коду
        filtered_logs = list(filter(lambda log: log['level'] == level.upper(), logs))
        # filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня 'ERROR':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        file_path = sys.argv[1]
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
    return


if __name__ == "__main__":
    main()

# python C:\Users\MikeK\PycharmProjects\in_process\pythonProject\goit-algo-hw-05\third_task.py
# C:\Users\MikeK\PycharmProjects\in_process\pythonProject\goit-algo-hw-05\logfile.log
# error
