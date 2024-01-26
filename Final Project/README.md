# **CS50P Final project 💪**

![CS50 Duck Debugger](https://cs50.gallerycdn.vsassets.io/extensions/cs50/ddb50/1.1.2/1691002683906/Microsoft.VisualStudio.Services.Icons.Default)

---
## To play the game, run `Hangman.exe`

### _This is my final project for the [CS50P course](https://cs50.harvard.edu/python/2022/) at Harvard Online_

### _You can find the final project instructions [here](https://cs50.harvard.edu/python/2022/project/)_

### _The original repository is [here](https://github.com/DanielDekhtyar/CS50P/tree/main/Final%20Project)_

---

## 📝 Changelog:

> ### Last Version : 1.0.1
>
> ### Last Update : 26-01-2024
>
> _Date format DD-MM-YYYY_


### 🗓️ _Version 1.0.1 - 26-01-2024 ([commit 5208b7b](https://github.com/DanielDekhtyar/Hangman-with-Pygame/commit/5208b7))_

---
#### 🚀 Added
- `Hangman.exe` has been added so now you can easily run the game on any machine !!!
- `resource_path.py` in `utils` folder is used to load images, fonts, sound and CSV files to allow it to work properly as an exe file.

#### 🔥 Enhancements
- `game_screen.py`, `hangman_game.py`, `start_screen.py`, `play_sound.py` and `get_font.py` changed to take advantage of `resource_path.py`
to make it passable to run as an exe file.



### 🗓️ _Version 1.0.0 - 31-12-2023 ([commit 993f36a](https://github.com/DanielDekhtyar/CS50P/commit/993f36a))_ Happy new 2024 year 🎄🎇✨

---

#### 🚀 Added
- `is_letter_guessed()` added in `project.py`. The function is called by `guess_letter()` in `hangman_game.py`.  
If the letter was guessed correctly, the function will return True, otherwise, the function will return False.
- `make_restart_and_exit_clickable()` added in `pygame.py`. It is called by `game_logic()` in `hangman_game.py`.  
This function ensures that the Exit and Restart buttons are clickable on the game screen. This helps to solve a bug.
- `make_all_main_screen_button_unclickable()` added in `project.py`. The function is called by `guess_letter()` in `hangman_game.py`.  
When the game screen starts, it makes all the buttons on the main screen unclickable. Otherwise, you can click on their rect on another screen.


#### 🔥 Enhancements
- `button_clicked()` and `get_button_instance()` moved to a new file called `util_functions.py` inside the `utils` folder.
- Comments, docstring and type annotations were added all over the code.

#### 🛠️ Fixed
- The dimensions of the buttons in `render_letter_buttons()` in `game_screen.py` are no longer defined by a specific number but a percentage, meaning now  
the size of the buttons will look the same (proportionally) on all screen sizes. `render_v_or_x_image()` changed accordingly.


### 🗓️ _Version 0.9.9 release candidate - 28-12-2023 ([commit a6e5516](https://github.com/DanielDekhtyar/CS50P/commit/a6e5516))_

---

#### 🚀 Added
- In the `project.py` in `if __name__ == "__main__"` a big change was made.
  - All the code that happens only once during the game initialization is now inside the `if __name__ == "__main__"` block.  
  Examples of this are `pygame.init()`, `pygame.display.set_caption`, screen initialization and `pygame.quit()`
  This was done to make level restarts passable.  
  `main()` is called to start a new level but all the things like pygame initialization and screen creation are done only once.
- In `project.py`, `get_button_instance()` returns the Button instance given the name of the button.
- In `project.py`, `exit_or_restart()` determines whether the user wants to exit the game or restart it based on the button clicked.
- In `game_screen.py`, `render_restart_button()` implemented.
- In `hangman_game.py`, different sounds from `play_sounds.py`(in `sounds` folder) are played using `pygame.mixer` at different events along the game.
- In `update_the_hangman()` when the user fails 7 guesses, the game is over and the word is revealed using a for loop and `word.guessed_letters_index[i] = True`.


#### 🔥 Enhancements
- In `Word` class, when setting `word.word`, the word is all uppercase using `.upper()`.
- In `start_screen.py`, when loading the buttons, the name of the buttons changed to work with the new picture files.  
e.g `level 1.png` -> `easy.png` etc.


### 🗓️ _Version 0.9.2 - 26-12-2023 ([commit 3d8ccb6](https://github.com/DanielDekhtyar/CS50P/commit/3d8ccb6))_

---

#### 🚀 Added

- In `game_screen.py`, `render_the_hangman()` implemented.  
It renders the hangman image on the screen.
- `hangman_attempts` variable introduced. It may be found in `hangman_game.py` as well as `game_screen.py`.  
Its purpose is to count how many failed attempts the user had to guess the word.
If more than 7 failed attempts are made, the game will end.
- `guess_letter()` gets `hangman_attempts`, increases the count of failed attempts made, and returns the updated number.
- If a guess was made, be it successful or not, `update_the_hangman()` will update the screen.
- `try_guessing` indicated if a guess attempt happened or not.
- `is_guessed` indicates if the guess attempt was successful or not.
- If more the 7 failed attempts are made, `render_game_over()` will render GAME OVER! on the screen.  
Also, it will make all the buttons, except the exit button, unclickable.


### 🗓️ _Version 0.9.1 - 26-12-2023 ([commit f98a664](https://github.com/DanielDekhtyar/CS50P/commit/f98a664))_

---

#### 🚀 Added

- In `game_screen.py`, `put_v_or_x()` was implemented.  
Every time we rerender the game screen, it puts the green V or red X on the buttons that were previously clicked, depending on whether the letter is in the word or not.
- In `game_screen.py`, `render_v_or_x_image()` was implemented.  
It renders the green V or red X over the letter button after they were clicked, depending on whether the letter is in the word or not.
- In `hangman_game.py`, `get_button_instance()` was implemented.
It returns the instance of a Button class based on the button name(this_button.name).
- In `hangman_game.py`, `guess_letter()` was reimplemented to use `put_v_or_x()`.


#### 🔥 Enhancements

- Button class changed
  - `letter_button_clicked`: bool - If it is not a letter button then it will remain False for the whole duration.
  - `position`: tuple[int, int] - The position of the button on the screen (X, Y)
- In `game_screen.py`, `word_cls` was changed to `word`
- In `game_screen.py`, `render_alphabet_buttons()` and `render_letter_buttons()` merged in to `render_letter_buttons()`. No functionality change.


#### 🛠️ Fixed

- In `game_screen.py`, `render_letter_buttons()` type annotations changed from `-> tuple[Button]` to `-> None`.


### 🗓️ _Version 0.9.0 - 25-12-2023 ([commit 3c5b924](https://github.com/DanielDekhtyar/CS50P/commit/3c5b924))_

---

#### 🚀 Added

- The hangman game functionality.

  - Letter buttons are clickable.
  - When the correct letter is guessed, the mask word will update and reveal the guessed word.
- `guess_letter()` was implemented inside `hangman_game.py`.  
It takes the guessed letter and checks if it is one of the letters of the word.  
If it is, `word.guessed_letters_index` is changed to `True` in the corresponding index.

#### 🔥 Enhancements

- In `start_screen.py`, what previously was `render_screen()` was not changed to `render_bg` to better represent its updated purpose.
- `render_bg()` no longer returns `screen` but instead takes a `screen` parameter.  
This is because `screen` is no longer created inside the function.
- Masked word font size changed from `0.25` to `0.1` percent of the screen.  
It was done to suit better the new font.
- In `hangman_game.py`, `word_cls` changed to `word`
- `render_alphabet_buttons` in `game_screen.py` no longer returns `button[]` as it is no longer needed

#### 🛠️ Fixed

- Screen flickering when re-rendering screen fixed
  - It was caused by `screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)` being placed inside `render_start_screen()` in `start_screen`, so the screen was created each time this function was called.  
  Now `screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)` is called once at the start of `main()`.

### 🗓️ _Version 0.2.5 - 25-12-2023 ([commit 91293f4](https://github.com/DanielDekhtyar/CS50P/commit/91293f4))_

---

#### 🚀 Added

- The game loop of the game screen is now working as it should.
- The loop is located in `hangman_game.py` in the `game_logic` function.
- The main game loop inside `main()` in `project.py` changed to work with the new game screen game loop.
- `render_game_screen()` in `game_screen.py` now also returns the exit button (`Button` class) to be later used int the `game_logic` inside `hangman_game.py`.

#### 🔥 Enhancements

- `button_clicked()` function in `project.py` was refactored to be more efficient
  - Filter out non-clickable buttons before the loop.  
    Iterates just over the clickable buttons using `clickable_buttons[]` list
  - Type annotation changed to -> str.  
    It was mistakenly set to -> int.
  - `mouse_click = pygame.mouse.get_pressed()` is out of the for loop, otherwise it would be called every time the loop iterates.

### 🗓️ _Version 0.2.0 - 24-12-2023 ([commit ee4ce10](https://github.com/DanielDekhtyar/CS50P/commit/ee4ce10))_

---

#### 🚀 Added

- Game screen added in `game_screen.py`
  - The background and the exit button code imported from `start_screen.py`
  - The topic of the guessed word is displayed at the top of the screen
  - The masked word is displayed at the center of the screen.  
    i.e ( \_ \_ \_ \_ \_ )
  - All the letters of the alphabet are displayed as buttons (`Button` class instances) in 2 rows, A-M and N-Z at the bottom of the screen (**Not yet clickable**)
- `Word` class created
  - The class contains for following attributes:
    - `word` (str) - The guessed word
    - `topic` (str) - The topic of the word
    - `guessed_letters_index` (bool) - If a letter was guessed then its index will be True, otherwise it will be False
    - `masked_word` (str) - The masked word i.e ( \_ \_ \_ \_ \_ )
  - Also, there is a property `get_masked_word`.  
    As its name implies, it returns the masked word str based on the values of `guessed_letter_index`.
- `button_clicked()` implemented inside `project.py`.  
  The function returns the `button.name` of the button that was clicked.
- game loop updated to include the game screen
- `hangman_game.py` added to include the game logic

#### 🔥 Enhancements

- `pygame.display.flip()` changed to `pygame.display.update()` as it is more resource efficient
- `mouse_pos = pygame.mouse.get_pos()` moved out of the for event loop for better computational resource efficiency

#### 🛠️ Fixed

- button instance clickability now can be changed using getters and setters `my_button.clickable`.
- `is_clickable()` property deleted as it is no longer needed thanks to the new `clickable` attribute.

### 🗓️ _Version 0.1.2.1 - 15-12-2023 ([commit 99ad8ab](https://github.com/DanielDekhtyar/CS50P/commit/99ad8ab))_

---

#### 🔥 Enhancements

- All start screen rendering functionality moved to `start_screen.py`.  
  `render_start_screen()` is called from the `main()`, and the rest is done inside the file itself.
- `main()` made more readable thanks to the enhancement described above.

#### 🛠️ Fixed

- Objects on the screen scale according to the device screen size and not a fixed number.

### 🗓️ _Version 0.1.2 - 13-12-2023 ([commit a08d2e3](https://github.com/DanielDekhtyar/CS50P/commit/a08d2e3))_

---

#### 🚀 Added

- Button class created

  - Depending on the current page, the button may be clickable or unclickable using `is_clickable()` boolean.
  - All the buttons have to be images
  - You get and set the following attributes of the button:
    - `top`
    - `left`
    - `bottom`
    - `right`
    - `collidepoint`
    - `position`
    - `x`
    - `y`
    - `width`
    - `hight`

- `all_button_instances[]` list added in project.py
  - When a button is created it is appended to the list.  
    it is done so you can access all the buttons in one place.
- The game exits when pressing Alt+F4 or by pressing the in-game X button or the ESC button on the keyboard.

#### 🎨 Changed

- Button creating process changed to take advantage of the `Button` class
  - All the buttons are images saved in the `images` folder.
  - Initially, you load the image and then give it as input to the `Button` class to create a button instance of that image.
  - `Button` class also takes the dimensions of the button.
  - After the button instance is created it needs to be drawn using `.draw` method.
- `mouse_when_over_button()` in `game_loop.py` refactored to take advantage of the new `Button` class.  
  It made the code more readable and less prone to bugs when adding new buttons.  
  All you need to do is to ensure all the buttons are in the `all_button_instances[]` list.
- Method comments changed to a new format

### 🗓️ _Version 0.1.1 - 10-12-2023 ([commit 449a3ad](https://github.com/DanielDekhtyar/CS50P/commit/449a3ad))_

---

#### 🔥 Enhancements

- Type annotations added to `project.py`, `game_loop.py`, `start_screen.py`

### 🗓️ _Version 0.1.0 - 06-12-2023 ([commit 556477f](https://github.com/DanielDekhtyar/CS50P/commit/556477f))_

---

#### 🚀 Added

- Title added
- X exit button added
- X button functionality implemented
- Background image added
- The screen is set to fullscreen
- Level buttons added (**not clickable yet**)
- When mouse over a button, a hand courser appears
