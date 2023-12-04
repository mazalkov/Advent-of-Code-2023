with open("Day 4/input.txt") as f:
    lines = f.read()

lines = lines.split("\n")

left, right = [], []
LENGTH = len(lines)
res = 0

for line in lines:
    if line:
        split_lines = line.split("|")
        l = [int(num) for num in split_lines[0].split(':')[1].split()]
        r = [int(num) for num in split_lines[1].split()]
        left.append(l)
        right.append(r)

for i in range(LENGTH-1):
    common = len(set(left[i]) & set(right[i]))
    if common > 0:
        res += 2**(common-1)

print(res)
