def reverseString1(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def main():
    s = ["h", "e", "l", "l", "o"]
    print(s)
    reverseString1(s)
    print(s)
    return 0

if __name__ == "__main__":
    main()
