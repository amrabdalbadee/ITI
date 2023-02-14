def find_max_recursively(S, n):
    """Find the maximum element in a sequence S, of n elements."""
    if n == 1:  # reached the left most item
        return S[n-1]
    else:
        previous = find_max_recursively(S, n-1)
        current = S[n-1]
        print(previous,current)
        if previous > current:
            return previous
        else:
            return current


if __name__ == '__main__':
    print(find_max_recursively([5, 10, 20, 11, 3], 5)) 