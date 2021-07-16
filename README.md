# Description
Python script to execute pastebin and pastebin like code on Piston using 
the new httpx python request library (Just to be different).

NB: use the raw link for python as code or any other code where formatting blocks matters!

If you find this useful, give us a star. Feel free to contribute, I created this to be
a community type project! 

# To get started
```git clone https://github.com/ccall48/piston-pastebin.git```
cd `piston-pastebin`

Create a virtual environment.
```python3 -m venv .```

Activate virtual environment.
```source bin/activate```

Install required ependencies.
```pip install -U -r requirements.txt```

Make file executable.
```chmod +x piston.py```

# Usage.. (Still under development)
run file with no inputs
```./piston.py <language> <script raw url>```

run file with arguments
```./piston.py <language> <script raw url> -argv arg1 arg2 etc..```

run a file with stdin
```./piston.py <language> <script raw url> -stdin stdin1 stdin2 etc...```

*** set a hash bang in script to location of your venv if you are using one. ***

# For details on Piston, visit
https://github.com/engineer-man/piston

Or Join Engineer Man Discord Server!
https://discord.gg/Ram7gHtn
