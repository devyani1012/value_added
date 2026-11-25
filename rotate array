def rotateArray(arr: List[int], r: int) -> List[int]:
    n = len(arr)

    if n == 0:
        return arr

    r = r % n

    return arr[-r:] + arr[:-r] if r != 0 else arr