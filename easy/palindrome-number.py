# https://leetcode.com/problems/palindrome-number/


def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


def main():
    print(is_palindrome(121))


if __name__ == '__main__':
    main()
