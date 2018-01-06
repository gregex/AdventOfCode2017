lengths = [187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216]
cp,ss = 0,0
numbers = [x for x in range(256)]
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
print(numbers[0]*numbers[1])