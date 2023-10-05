# https://leetcode.com/problems/maximum-average-subarray-i/


def find_max_average(nums: list[int], k: int) -> float:
    cur = sum(nums[:k])
    avg_max = cur
    for i in range(k, len(nums)):
        cur -= nums[i-k]
        cur += nums[i]
        avg_max = max(cur, avg_max)
    return avg_max / k


def main():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(find_max_average(nums, k))


if __name__ == '__main__':
    main()
