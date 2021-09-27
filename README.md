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
