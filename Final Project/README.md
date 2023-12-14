# **CS50P Final project**
---

### _This is my final project for the [CS50P course](https://cs50.harvard.edu/python/2022/) at Harvard Online_

### _You can find the final project instructions [here](https://cs50.harvard.edu/python/2022/project/)_

![CS50 Duck Debugger](https://cs50.gallerycdn.vsassets.io/extensions/cs50/ddb50/1.1.2/1691002683906/Microsoft.VisualStudio.Services.Icons.Default)

---

## Changelog:

> ### Last Version : 0.1.2.1
>
> ### Last Update : 15-12-2023
>
> _Date format DD-MM-YYYY_

### **[v0.1.2.1] - 15-12-2023 (latest commit)**
--- 
#### 🔥 Enhancements
- All start screen rendering functionality moved to start_screen.py.   
render_start_screen() is called from the main(), and the rest is done inside the file itself.
- main() made more readable thanks to the enhancement described above.

#### 🛠️ Fixed
- Objects on the screen scale according to the device screen size and not a fixed number.


### **[v0.1.2] - 13-12-2023** (commit a08d2e3)
---
#### 🚀 Added
- Button class created  
    - Depending on the current page, the button may be clickable or uncliackable using is_clickable() boolean.
    - All the buttons have to be images
    - You get and set the following properties of the button:  
        - top  
        - left  
        - bottom  
        - right  
        - collidepoint  
        - position  
        - x  
        - y  
        - width  
        - hight  

- all_button_instances\[ \] list added in project.py
    - When a button is created it is appended to the list.  
  it is done so you can access all the buttons in one place.
- The game exits when pressing Alt+F4 or by pressing the in-game X button or the ESC button on the keyboard.
#### 🎨 Changed
- Button creating process changed to take advantage of the Button class  
    - All the buttons are images saved in the /images/ folder.
    - Initially, you load the image and then give it as input to the Button class to create a button instance of that image.
    - Button class also takes the dimensions of the button.
    - After the button instance is created it needs to be drawn using .draw
- mouse_when_over_button() in game_loop.py refactored to take advantage of the new Button class.  
  It made the code more readable and less prone to bugs when adding new buttons.  
  All you need to do is to ensure all the buttons are in the all_button_instances\[ \] list.
- Method comments changed to a new format

### **[v0.1.1] - 10-12-2023** (commit 449a3ad)
---
#### 🔥 Enhancements
- Type annotations added to project.py, game_loop.py, start_screen.py


### **[v0.1.0] - 06-12-2023** (commit 556477f)
---

#### 🚀 Added

- Title added
- X exit button added
- X button functionality implemented
- Background image added
- Screen set to fullscreen
- Level buttons added (not clickable yet)
- When mouse over a button, a hand courser appears
