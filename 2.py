# def checksum(box_ids):
#   has_two = 0
#   has_three = 0
#   for box_id in box_ids:
#     letter_counts = {}
#     for char in box_id:
#       letter_counts[char] = letter_counts.get(char, 0) + 1
#     if 2 in letter_counts.values():
#       has_two += 1
#     if 3 in letter_counts.values():
#       has_three += 1
#   return has_two * has_three

def matching_boxes(box_ids):
  for box_id in box_ids:
    for i in range(len(box_id)):
      for other_box_id in box_ids:
        if box_id == other_box_id:
          continue
        if box_id[0:i] + box_id[i+1:] == other_box_id[0:i] + other_box_id[i+1:]:
          return box_id[0:i] + box_id[i+1:]
  return None

def test_example():
  box_ids = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
  assert matching_boxes(box_ids) == 'fgij'

if __name__ == '__main__':
  data = open('input-2.txt').read().split('\n')
  print(matching_boxes(data))
