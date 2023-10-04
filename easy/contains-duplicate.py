# https://leetcode.com/problems/contains-duplicate/


def contains_duplicate(nums: list[int]) -> bool:
    return not len(nums) == len(set(nums))


def main():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(contains_duplicate(nums))


if __name__ == '__main__':
    main()
