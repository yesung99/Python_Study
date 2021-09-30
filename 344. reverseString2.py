def reverseString2(s: list[str]) -> None:
    s.reverse()

def main():
    s = ["h", "e", "l", "l", "o"]
    print(s)
    reverseString2(s)
    print(s)
    return 0

if __name__ == "__main__":
    main()
