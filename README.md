GC3 Adapter
===========

A python based script that should allow you to play *TGC 2019* with a *GC3 Launch Monitor* from Foresight Sports. It receives input from the monitor, maps that input to the input TGC 2019 expects, and sends it along. There are 2 additional scripts for testing input and output.

### Input
A JSON arrray as documented at https://gsprogolf.com/GSProConnectV1.html

### Output
A JSON array as documented at https://csc.protee-united.com/hc/en-us/articles/216279108-ProTee-Golf-Interface-SDK

To run
------
1. Make sure you have python installed. Download it at https://www.python.org/downloads/
2. Download a zip of the repo and unzip it.
3. Run the "listener.py". This can be done through Command Line/Terminal (py PATH_TO_FILE) *or* by opening the GC3_Adapter folder, right clicking on "listener.py", selecting *Open*, and then selecting python.
4. Run TGC 2019 before using the GC3 monitor.
5. Golf!
