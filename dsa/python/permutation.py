def permute(nums):
    result = []

    def backtrack(path):
        if ________:
            result.append(list(path))
            return

        for num in nums:
            if num in path:
                continue
            path.append(num)
            backtrack(path)
            path.pop()

    backtrack([])
    return result

nums = [1, 2, 3]
listOFResult = permute(nums)
