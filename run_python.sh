#!/bin/bash

#this bash file is used to run python files from ganga terminal
#here this bash file is as application.exe file 
#for example, here we are running hello.py file which outputs hello world. So the code would be:
# j = Job(name = "WHATEVER NAME YOU WANT TO GIVE TO YOUR JOB",\
# application = Executable())
# j.application.exe = File("run_python.sh")
# j.submit()
#the relative path of whatever python file you have given here in run_python.sh,
#will be run.  
#here $1 is to take input argument for other files like it_counter.py,pdf.py and is not required for running files that don't require any input like hello.py file
python3 "GangaGSoC2024/hello.py" $1