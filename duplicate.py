def duplicateZeros(arr: List[int]) -> List[int]:
    result = []

    for num in arr:
        result.append(num)

        if num == 0:
            result.append(0)

    return result[:len(arr)]