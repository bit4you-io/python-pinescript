This project has to be able to run a pinescript code and return the expected result.
The result could be a json object of data that needs to be drawn on the tradingview chart, as well a buy or sell signal, or any other built in functionality.

In order to do so, we can split our project in multiple components like this:

# components:
- pinescript: contains all functions and variables needed to run pinescript code in python
- transform:  transforms pinescript to python code
- server:     evaluate pinscript and retuns result to show in graph

Once the pine code is transfromed to python, the syntax looks nearly the same and can be extended on the fly.

In order to encapsulate a tradingbot and run older versions without being affected by package/server changes, it would be nice to be able to convert everything to WebAssembly at the end.
The whole python package and bot would be converted to a webassembly file that could been runned from everywhere.

# the current example is not working
The provided sample just indicate what we want to works at the end of the ongoing project