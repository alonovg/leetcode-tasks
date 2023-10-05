# https://leetcode.com/problems/move-zeroes/


def move_zeroes_1(nums: list[int]) -> list[int]:
    counter = 0
    for num in range(len(nums)):
        if nums[num] == 0:
            counter += 1
    for _ in range(counter):
        nums.remove(0)
    for _ in range(counter):
        nums.append(0)
    return nums


def move_zeroes_2(nums: list[int]) -> list[int]:
    zeros_list = []
    while 0 in nums:
        nums.remove(0)
        zeros_list.append(0)
    nums += zeros_list
    return nums


def move_zeroes_3(nums: list[int]) -> list[int]:
    first_pointer = 0
    for second_pointer in range(len(nums)):
        if nums[second_pointer] != 0:
            nums[second_pointer], nums[first_pointer] = nums[first_pointer], nums[second_pointer]
            first_pointer += 1
    return nums


def main():
    nums = [0, 1, 0, 3, 12]
    print(move_zeroes_3(nums))


if __name__ == '__main__':
    main()
