# hexgen
A small hex code generator and authenticator.

# Requirements

```
$pip install csv 
```

# Guide

There are 3 main files. You use the first file `hexgen.py` to generate a number of hex tokens with 16 digits. Then associate each codes with any kind of string (i.e. A,B,C). 

The codes will be saved to `hex.csv` in the following format: 

```
A,4973106ac8f04c1a5721906a103026c2

B,d19f73e313157a780b25557cd1ae7ec6

C,7be8c752eda445081e7bec1b7e18ec1d
```

In `hexaut.py` you can check the authenticity of any code, given it is in the `hex.csv` file. 

# FAQ

* What can I do with this? 

Up to you. 
