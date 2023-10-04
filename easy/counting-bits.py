# https://leetcode.com/problems/counting-bits/


def count_bits_1(num: int) -> list[int]:
    array_int = []
    for i in range(num+1):
        array_int.append(int(bin(i)[2:].count("1")))
    return array_int


def count_bits_2(num: int) -> list[int]:
    array_int = []
    for i in range(num+1):
        cur = 0
        while i:
            cur += i & 1
            i >>= 1
        array_int.append(cur)
    return array_int


def main():
    print(count_bits_2(5))


if __name__ == '__main__':
    main()
