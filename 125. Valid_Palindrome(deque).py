import collections
from typing import Deque


def isPalindrome(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

def main():
    if(isPalindrome("A man, a plan, a canal: Panama") == True):
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()

