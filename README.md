
# Some self modification by bruce30262
Basically added a `config.yml` which can be used for setting :  
  - FlatLaf version  
  - FlatLaf style  
  - Font size and family for Decompiler and Listing Display  
    
Check [config_example.yml](https://github.com/bruce30262/ghidra-dark/blob/main/config_example.yml) for more details.

**Notice: You might have to install pyyaml first : `python3 -m pip install pyyaml`.**


`install.py` will be able to update the settings specified in `config.yml`. After modifying the config file, just update the settings by using the same command as installing ghidra-dark:

```
# In Windows Powershell
.\install.py -d -p "<GHIDRA INSTALLED PATH>"
```

`uninstall.py` will be able to handling the removing of the downloaded FlatLaf.


**( Below is the README from the original repository )**

---

# ghidra-dark

[![Ghidra 9.0-10.0.2](https://img.shields.io/badge/Ghidra-9.0--10.0.2-red)](https://github.com/NationalSecurityAgency/ghidra/releases)
[![Python >=3.6](https://img.shields.io/badge/python->=3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

ghidra-dark provides a simple to use script to install the FlatLaf dark theme, custom colors for disassembly/decompilation in Ghidra, and some other helpful settings. A script is also provided for uninstallation. The scripts support all public builds through version 10.0.2 on Windows, Linux, and macOS.

## Install

```
$ python3 install.py
```

![](ghidra-dark.png)

## Uninstall

```
$ python3 uninstall.py
```
