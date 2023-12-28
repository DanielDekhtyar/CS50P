"""
    The Word class represents a word in the game, providing functionality to manage and interact
    with the word's properties such as the actual word, its topic, guessed letters index, and a
    masked version of the word.

    Attributes:
    - _word (str): The actual word. The word is converted to uppercase and stripped of any leading and trailing whitespaces.
    - _topic (str): The topic associated with the word.
    - _guessed_letters_index (list[bool]): A list representing whether each letter of the word has
    been guessed or not.
    - _masked_word (str): The masked version of the word, with underscores for unrevealed letters.

    Methods:
    - get_masked_word() -> str: Generates the masked version of the word based on guessed letters.
    - _initialize_guessed_letters_index() -> list[bool]: Initializes the guessed letters index list.

    Properties (with setters):
    - word (str): Gets or sets the actual word.
    - topic (str): Gets or sets the topic associated with the word.
    - guessed_letters_index (list[bool]): Gets the list representing guessed letters.

    Example:
    ```
    # Create a Word instance
    word_instance = Word("PYTHON", "Programming Language")

    # Access properties
    print(word_instance.word)  # Output: "PYTHON"
    print(word_instance.topic)  # Output: "Programming Language"
    print(word_instance.guessed_letters_index)  # Output: [False, False, False, False, False, False]

    # Modify properties
    word_instance.word = "ROCK 'N' ROLL"
    word_instance.topic = "Music"
    ```
    """


class Word:
    def __init__(self, word, topic):
        self._word = word.strip().upper()
        self._topic = topic.strip()
        self._guessed_letters_index = self._initialize_guessed_letters_index()
        self._masked_word = self.get_masked_word()

    def get_masked_word(self) -> str:
        # Create an empty string to store the masked word
        masked_word = ""
        # Go over each character of the word and check if it has been guessed
        for index, char in enumerate(self._guessed_letters_index):
            # If the letter is already guessed then it's shown
            # Otherwise it's shown as an underscore
            if char == True:
                masked_word += self._word[index]
            else:
                masked_word += "_"

        return masked_word

    @property
    def word(self) -> str:
        return self._word

    @word.setter
    def word(self, value: str) -> None:
        self._word = value.strip()

    @property
    def topic(self) -> str:
        return self._topic

    @topic.setter
    def topic(self, value: str) -> None:
        self._topic = value.strip()

    @property
    def guessed_letters_index(self) -> list[bool]:
        return self._guessed_letters_index

    def _initialize_guessed_letters_index(self) -> list[bool]:
        return [False if str.isalpha(char) else True for char in self._word]
