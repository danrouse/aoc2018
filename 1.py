from functools import reduce

def frequency_calibrator(inputs):
  frequency_shifts = [int(f) for f in inputs.split(', ') if f]
  return reduce((lambda x, y: x + y), frequency_shifts)

def test_examples():
  assert frequency_calibrator('+1, -2, +3, +1') == 3
  assert frequency_calibrator('+1, +1, +1') == 3
  assert frequency_calibrator('+1, +1, -2') == 0
  assert frequency_calibrator('-1, -2, -3') == -6

if __name__ == '__main__':
  data = open('input-1.txt').read().replace('\n', ', ')
  print(frequency_calibrator(data))
