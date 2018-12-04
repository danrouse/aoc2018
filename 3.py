import re
def parse_row(row_str):
  return map(int, filter(None, re.split(r'\D+', row_str)))

# def overlapping_area(claims):
#   occupied_area = {}
#   overlap_count = 0
#   for claim in claims:
#     if claim == '':
#       continue
#     claim_id, x, y, w, h = parse_row(claim)
#     for tx in range(x, x+w):
#       if tx not in occupied_area:
#         occupied_area[tx] = {}
#       for ty in range(y, y+h):
#         occupied_area[tx][ty] = occupied_area[tx].get(ty, 0) + 1
#         if occupied_area[tx][ty] == 2:
#           overlap_count += 1
#   return overlap_count

def non_overlapping_id(claims):
  occupied_area = {}
  no_overlaps_yet = []
  for claim in filter(None, claims):
    claim_id, x, y, w, h = parse_row(claim)
    claim_overlaps = False
    for tx in range(x, x+w):
      for ty in range(y, y+h):
        if (tx, ty) not in occupied_area:
          occupied_area[(tx, ty)] = []
        else:
          for claim_id in occupied_area[(tx, ty)]:
            if claim_id in no_overlaps_yet:
              no_overlaps_yet.remove(claim_id)
          claim_overlaps = True
        occupied_area[(tx, ty)].append(claim_id)
    if claim_overlaps == False:
      no_overlaps_yet.append(claim_id)
  return no_overlaps_yet[0]

def test_example():
  input = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
  ]
  assert non_overlapping_id(input) == 3

if __name__ == '__main__':
  data = open('input-3.txt').read().split('\n')
  print(non_overlapping_id(data))
