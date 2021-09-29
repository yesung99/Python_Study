import collections
import re
from typing import List

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = []
    processing = re.sub('[^a-zA-Z]', ' ', paragraph).lower().split()

    for word in processing:
        if not word in banned:
            words.append(word)
    return collections.Counter(words).most_common(1)[0][0]

def main():
    findword = mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    print("가장 큰 빈도수를 가진 단어: " + findword)

if __name__ == "__main__":
    main()