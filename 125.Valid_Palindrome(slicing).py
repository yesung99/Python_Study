import re

def isPalindrome(s:str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]

def main():
    if (isPalindrome("A man, a plan, a canal: Panama") == True):
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()