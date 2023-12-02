# TODO Fill the comments


class Word:
    def __init__(self, word_str: str) -> None:
        # a list of all the characters in the word. One char per index
        self.word: list[str] = list(word_str)
        self.visibility: list[bool] = [False for _ in self.word]
