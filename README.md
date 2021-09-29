# truecolor

A better console color library for python

[GitHub](https://github.com/chanchan69/truecolor/)

[PyPI](https://pypi.org/project/truecolor.py/)

### Print Colored Text
```py
from truecolor import fg, reset
from os import system

system('cls')
print(f"{fg('magenta')}This {fg((255, 0, 0))}is{fg('magenta')} magenta text!{fg('#ff8243')} This is the exact hex color #ff8243 :){reset}")
```

### Output
![alt text](https://media.discordapp.net/attachments/892129513213952010/892608621366632448/unknown.png)


### Another Way
```py
from truecolor import colors
from os import system

system('cls')
print(f"{colors.magenta}This {colors.red)}is{colors.magenta} magenta text!{reset}")
```
