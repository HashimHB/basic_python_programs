s = "|**|*|"
s = s.split('|')
res = []
count = 0
for symbol in s:
    if len(symbol) > 0:
        count += len(symbol)
        res.append(count)
print(res)