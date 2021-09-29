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
