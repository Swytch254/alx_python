def fibonacci_sequence(n):
    sequence = []
    if n <= 0:
       return sequence
    elif n == 1:
        sequence.append(0)
    elif n == 2:
        sequence.extend([0,1])
    else:
        sequence.extend([0,1])
        for char in range(2,n):
            next_number = sequence[char-1] + sequence[char-2]
            sequence.append(next_number)
    return sequence
