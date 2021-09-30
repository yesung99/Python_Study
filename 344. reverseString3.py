def reverseString3(s: list[str]) -> None:
    s = s[::-1]
    # s[:] = s[::-1] # 리트코드 제출용 코드

def main():
    s = ["h", "e", "l", "l", "o"]
    print(s)
    reverseString3(s)
    print(s)
    return 0

if __name__ == "__main__":
    main()
