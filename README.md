# Python_Study

### 125. Valid Palindrome
팰린드롬이란 앞뒤가 똑같은 단어나 문장으로 뒤집어도 같은 말이 되는 단어 또는 문장이라고 한다
``` 
# 리스트 변환
def isPalindrome(s: str)->bool:
    strs = []
    for char in s:
        if char.isalnum(): # 문자 char에서 숫자, 알파벳만 찾아낸다
            strs.append(char.lower()) # 문자 char가 숫자나 알파벳일 경우 strs에 소문자로 확장한다

        while len(strs) > 1: 
            if strs.pop(0) != strs.pop(): # strs의 앞 부분과 뒷 부분이 다를 경우
                return False # 이 문자열은 팰린드롬이 아니다
        return True
    

def main():
    if(isPalindrome("A man, a plan, a canal: Panama") == True):
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()
```
### 125. Valid Palindrome(deque)
```
# deque 사용
import collections
from typing import Deque

def isPalindrome(s: str) -> bool:
    strs: Deque = collections.deque() # strs deque 생성

    for char in s:
        if char.isalnum(): # 문자 char에서 숫자, 알파벳만 찾아낸다
            strs.append(char.lower()) # strs 문자가 숫자나 알파벳일 경우 strs deque에 추가된다

    while len(strs) > 1:
        if strs.popleft() != strs.pop(): # strs의 앞 부분과 뒷 부분이 다를 경우, popleft 함수는 O(1)를 가지고 있고 pop 함수는 O(n)을 지니고 있다
            return False # 다르면 이 문자열은 팰린드롬이 아니다
    return True

def main():
    if(isPalindrome("A man, a plan, a canal: Panama") == True):
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()
```

### 125. Valid Palidrome(slicing)
```
# 
import re # 정규 표현식 사용하기 위해서 import 

def isPalindrome(s:str) -> bool:
    s = s.lower() # 문자열 s를 소문자로 변경
    s = re.sub('[^a-z0-9]', '', s) # 문자열 중에서 알파벳 a~z, 숫자 0~9가 아니면(^) 없앤다 
    return s == s[::-1] # 문자열과 뒤집은 문자열[::-1] 을 비교하여 True이면 팰린드롬이다

def main():
    if (isPalindrome("A man, a plan, a canal: Panama") == True):
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()
```    
    
