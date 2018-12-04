import re
from datetime import datetime

def parse_record(record_str):
  record_fmt = r'^\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]( Guard #(?P<guard_id>\d+))? (?P<action>.+)'
  match = re.match(record_fmt, record_str)
  timestamp = datetime.strptime(match.group('timestamp'), '%Y-%m-%d %H:%M')
  return (timestamp, match.group('action'), match.group('guard_id'))

def process_records(records):
  records = records.split('\n') if type(records) == str else records
  parsed_records = [parse_record(r) for r in filter(None, records)]
  return sorted(parsed_records, key=lambda x: x[0])

def sneaky_code(records):
  guard_sleeping_times = {}
  current_guard_id = None
  guard_ids = set()
  for timestamp, action, guard_id in process_records(records):
    if guard_id:
      current_guard_id = guard_id
      guard_ids.add(guard_id)
    if action == 'falls asleep':
      if current_guard_id not in guard_sleeping_times:
        guard_sleeping_times[current_guard_id] = []
      guard_sleeping_times[current_guard_id].append([timestamp])
    elif action == 'wakes up':
      guard_sleeping_times[current_guard_id][-1].append(timestamp)

  guards_asleep_at_minute = {}
  for guard_id, sleeping_times in guard_sleeping_times.items():
    for timestamps in sleeping_times:
      for i in range(timestamps[0].minute, timestamps[1].minute):
        if i not in guards_asleep_at_minute:
          guards_asleep_at_minute[i] = []
        guards_asleep_at_minute[i].append(guard_id)

  # sleeping_counts = sum(guards_asleep_at_minute.values(), [])
  # most_sleeping_guard = sorted(list(guard_ids), key=lambda guard_id: sleeping_counts.count(guard_id), reverse=True)[0]
  # most_sleeping_minute = sorted([(m, c.count(most_sleeping_guard)) for m, c in guards_asleep_at_minute.items()], key=lambda x:x[1], reverse=True)[0][0]
  # return int(most_sleeping_minute) * int(most_sleeping_guard)
  highest_count = 0
  winner = None
  for guard_id in guard_ids:
    sleep_counts_per_minute = [(m, c.count(guard_id)) for m, c in guards_asleep_at_minute.items()]
    most_sleeping_minute, most_sleeping_count = sorted(sleep_counts_per_minute, key=lambda x:x[1], reverse=True)[0]
    if most_sleeping_count > highest_count:
      highest_count = most_sleeping_count
      winner = int(guard_id) * int(most_sleeping_minute)
  return winner


def test_example():
  records = [
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-05 00:55] wakes up',
  ]
  assert sneaky_code(records) == 4455

if __name__ == '__main__':
  data = open('input-4.txt').read().split('\n')
  print(sneaky_code(data))
