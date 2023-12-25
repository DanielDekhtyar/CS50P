# **CS50P Final project 💪**
![CS50 Duck Debugger](https://cs50.gallerycdn.vsassets.io/extensions/cs50/ddb50/1.1.2/1691002683906/Microsoft.VisualStudio.Services.Icons.Default)

---

### _This is my final project for the [CS50P course](https://cs50.harvard.edu/python/2022/) at Harvard Online_

### _You can find the final project instructions [here](https://cs50.harvard.edu/python/2022/project/)_

---

## 📝 Changelog:

> ### Last Version : 0.2.5
>
> ### Last Update : 24-12-2023
>
> _Date format DD-MM-YYYY_

### 🗓️ *Version 0.2.5 - 25-12-2023  (latest commit)*
---
#### 🚀 Added
- The game loop of the game screen is now working as it should.
- The loop is located in `hangman_game.py` in the `game_logic` function.
- The main game loop inside `main` in `project.py` changed to work with the new game screen game loop.
- `render_game_screen` in `game_screen.py` now also returns the exit button (`Button` class) to be later used int the `game_logic` inside `hangman_game.py`.

#### 🔥 Enhancements
- `button_clicked` function in `project.py` was refactored to be more efficient
  - Filter out non-clickable buttons before the loop.  
  Iterates just over the clickable buttons using `clickable_buttons[]` list
  - Type annotation changed to -> str.  
  It was mistakenly set to -> int.
  - `mouse_click = pygame.mouse.get_pressed()` is out of the for loop, otherwise it would be called every time the loop iterates.


### 🗓️ *Version 0.2.0 - 24-12-2023  (ee4ce10)*
---
#### 🚀 Added
- Game screen added in `game_screen.py`
  - The background and the exit button code imported from `start_screen.py`
  - The topic of the guessed word is displayed at the top of the screen
  - The masked word is displayed at the center of the screen.  
  i.e ( _ _ _ _ _ )
  - All the letters of the alphabet are displayed as buttons (`Button` class instances) in 2 rows, A-M and N-Z at the bottom of the screen (**Not yet clickable**)
- `Word` class created
  - The class contains for following attributes:
    - `word` (str) - The guessed word
    - `topic` (str) -  The topic of the word
    - `guessed_letters_index` (bool) - If a letter was guessed then its index will be True, otherwise it will be False
    - `masked_word` (str) - The masked word i.e ( _ _ _ _ _ )
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
- `is_clickable` property deleted as it is no longer needed thanks to the new `clickable` attribute.

### 🗓️ *Version 0.1.2.1 - 15-12-2023 (99ad8ab)*
--- 
#### 🔥 Enhancements
- All start screen rendering functionality moved to `start_screen.py`.   
`render_start_screen()` is called from the `main()`, and the rest is done inside the file itself.
- `main()` made more readable thanks to the enhancement described above.

#### 🛠️ Fixed
- Objects on the screen scale according to the device screen size and not a fixed number.


### 🗓️ *Version 0.1.2 - 13-12-2023 (commit a08d2e3)*
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

### 🗓️ *Version 0.1.1 - 10-12-2023 (commit 449a3ad)*
---
#### 🔥 Enhancements
- Type annotations added to `project.py`, `game_loop.py`, `start_screen.py`


### 🗓️ *Version 0.1.0 - 06-12-2023 (commit 556477f)*
---

#### 🚀 Added

- Title added
- X exit button added
- X button functionality implemented
- Background image added
- The screen is set to fullscreen
- Level buttons added (**not clickable yet**)
- When mouse over a button, a hand courser appears
