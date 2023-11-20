# Learning Python with CS50
# Just setting up my twttr
# https://cs50.harvard.edu/python/2022/psets/2/twttr/

"""
def main():
  txt = input("Input: ")
  print("Output: " , end="")
  for i in range(len(txt)):
    if txt[i].isalpha():
      if txt[i] not in "aeiouAEIOU":
        print(txt[i] , end="")
    else:
      print(txt[i], end="")
  print("")


main()
"""

# Code for 'Testing my twttr'
# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/


def main():
    word: str = input("Input: ").strip().lower()
    print("Output: ", shorten(word), sep="")


def shorten(word):
    new_str = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in range(len(word)):
        if word[i].isalpha():
            if word[i] not in vowels:
                new_str += word[i]
        else:
            new_str += word[i]
    return new_str


if __name__ == "__main__":
    main()
