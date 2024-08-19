
def addBinary(self, a: str, b: str) -> str:
    # Ensure both strings have the same length by padding the shorter one with leading zeros
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Initialize the result and carry
    result = []
    carry = 0

    # Iterate from the last character to the first
    for i in range(max_len - 1, -1, -1):
        bit1 = int(a[i])
        bit2 = int(b[i])
        total = bit1 + bit2 + carry
        carry = total // 2
        result.append(str(total % 2))

    # If there's a carry left at the end, append it to the result
    if carry:
        result.append('1')

    # The result is currently reversed, so reverse it back
    result.reverse()
    return ''.join(result)
