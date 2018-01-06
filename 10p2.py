from functools import reduce

inpt = "187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216"
lengths = [ord(s) for s in inpt]
lengths.extend([17, 31, 73, 47, 23])
cp,ss,count = 0,0,0
numbers = [x for x in range(256)]

while count<64:
    for length in lengths:
        helping = []
        end = (cp+length)%len(numbers)
        if end<=cp and length>0:
            helping.extend(numbers[cp:])
            helping.extend(numbers[0:end])
            helping.reverse()
            numbers[cp:] = helping[0:len(numbers[cp:])]
            numbers[0:end] = helping[len(numbers[cp:]):]
        else:
            helping.extend(numbers[cp:end])
            helping.reverse()
            numbers[cp:end] = helping
        cp += length + ss
        cp %= len(numbers)
        ss += 1
    count += 1

numberChunks = [numbers[i:i + 16] for i in range(0, len(numbers), 16)]
denseHashHex = ""
hexNums = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
for chunk in numberChunks:
    xor = reduce((lambda x, y: x ^ y), chunk)
    hexed = ""
    while xor:
        rest = xor % 16
        xor //= 16
        if rest>=10:
            hexed+=hexNums[rest]
        else:
            hexed+=str(rest)
    denseHashHex+=hexed[::-1]
print(denseHashHex)