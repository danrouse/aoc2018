from functools import reduce

def frequency_calibrator(inputs):
  frequency_shifts = [int(f) for f in inputs.split(', ') if f]
  known_frequencies = [0]
  i = 0
  while i < len(frequency_shifts):
    next_sum = known_frequencies[-1] + frequency_shifts[i]
    if next_sum in known_frequencies:
      return next_sum
    known_frequencies.append(next_sum)
    i = 0 if i == len(frequency_shifts) - 1 else i + 1
  return None

def test_examples():
  assert frequency_calibrator('+1, -2, +3, +1') == 2
  assert frequency_calibrator('+1, -1') == 0
  assert frequency_calibrator('+3, +3, +4, -2, -4') == 10
  assert frequency_calibrator('-6, +3, +8, +5, -6') == 5
  assert frequency_calibrator('+7, +7, -2, -7, -4') == 14

if __name__ == '__main__':
  data = open('input-1.txt').read().replace('\n', ', ')
  print(frequency_calibrator(data))
