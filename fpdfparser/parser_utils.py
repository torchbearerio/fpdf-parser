from .code_map import code_map
import itertools


def parse_entry(entry):
    pid, values = entry.split("=")
    pid = int(pid, 16)
    split_values = values.split(";")
    if isinstance(code_map[pid], list):
        assert len(code_map[pid]) == len(split_values), "The values received for {} are not of expected length {}"\
            .format(pid, len(code_map[pid]))
        return [(code_map[pid][idx], value) for idx, value in enumerate(split_values)]

    return [(code_map[pid], split_values[0])]


def parse_raw_entries(entries):
    parsed_entries = list(itertools.chain(*[parse_entry(e) for e in entries]))
    timerseries = []

    # Need to compress entries split by timestamp
    current = {}
    for e in parsed_entries:
        # If we hit a new timestamp, wrap up the current entry we're building
        if e[0] == 'timestamp':
            if current.get('timestamp'):
                timerseries.append(current)
            current = {}

        current[e[0]] = e[1]

    # Tack the last entry onto the timeseries
    if current.get('timestamp'):
        timerseries.append(current)

    return timerseries


def parse_updf_file(file):
    raw_entries = file.read().split(",")
    return parse_raw_entries(raw_entries)
