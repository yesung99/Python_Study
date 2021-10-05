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
# 슬라이싱 사용
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

### 815. Most common Word 
문자열 paragraph가 주어지고 문자열 paragraph에서 단어를 금지 할 수 있는 banned words를 입력할 수 있다, banned words를 제외하고 paragraph에서 가장 빈번한 단어를 찾아야 한다 대소문자는 구분하지 않으며 리턴을 소문자로 해야 한다
``` 
import collections
import re
from typing import List

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = []
    processing = re.sub('[^a-zA-Z]', ' ', paragraph).lower().split() # 알파벳이 아닌 경우 공백으로 대체하고 알파벳일 경우 소문자로 변경한다

    for word in processing:
        if not word in banned: # word 문자 안에 banned가 된 단어가 없을 경우
            words.append(word) # words 리스트에 단어를 추가한다
    return collections.Counter(words).most_common(1)[0][0] # 빈도수가 첫번째로 높은 단어를 출력한다

def main():
    findword = mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    print("가장 큰 빈도수를 가진 단어: " + findword)

if __name__ == "__main__":
    main()
```

### 937. Reorder Data in Log Files
```
from typing import List 

class Solution: # 리트코드 제출용 코드
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        
        for log in logs:
            if log.split()[1].isdigit(): # logs = ["dig1 8 1 5 1"]를 split 하고 [dig1, 8, 1, 5, 1] 중 [1] 인덱스 즉 8이 숫자이면
                digits.append(log) # digits에 append 한다
            else:
                letters.append(log) # 숫자가 아닐 경우 letters에 append 한다
        # 3번 조건인 "식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순으로 한다"를 만족 시키기 위해서
        # lambda 함수를 사용한다 x 즉 log = ["let2 own kit dig"]가 들어오면 split을 하여 첫번째 정렬 기준을 [let2, own, kit, dig]의 인덱스 [1:]을 기준으로 정렬한다
        # 만약 문자가 동일 할 경우에는 식별자 순으로 정렬하라고 하였으므로 두번째 키를 x.split()[0] 즉 let2을 기준으로 하여 다시 한번 정렬을 한다
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) 
        return letters + digits
```
