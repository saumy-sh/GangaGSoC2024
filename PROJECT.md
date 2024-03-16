# Challenge completion for Ganga project for GSoC 2024

## Running python files through Ganga

For running python files in ganga terminal, i used bash script. I have saved it as "run_python.sh" file. The code to create executable job is
```bash
#!bin/bash
python3 "ABSOLUTE PATH TO THE PYTHON FILE YOU WANT TO RUN" $1
```
here `$1` is to take input file from user

So whichever python file you want to run in GangaGSoC2024 folder just mention it's path here and then this bash script can be given as exe argument to job application parameter. Like this:
```
j = Job()
j.application = Executable()
j.application.exe = File("run_python.sh")
j.submit()
```
Then you see output of python program using following command
```
j.peek("stdout")
```

Remember to change directory to GangaGSoC2024 before executing these commands


## Initial Tasks

### 1 Create "Hello World" Ganga job

I have created hello.py file in GangaGSoc2024 folder which does the job.
This can be executed by bash script which can be run in Ganga terminal.

### 2 Create a job in Ganga that demonstrates splitting a job into multiple pieces and then collates the results at the end.
 - To split the LHC.pdf into different page pdfs, run pdf.py file using bash. Make sure to give absolute path to folder in which you want to get output in pdf.py file. The output will be stored in pdf_pages folder by default. To do this in ganga after creating job as mentioned above, before submitting the job, type `j.application.args = ['ABSOLUTE PATH OF LHC.pdf']` , then submit job. Make sure to give absolute path of files as argument to avoid errors.
 - To count number of repetition of word "it" in each page, run it_counter.py file. Here we will use `ArgSplitter()` function of Ganga splitter to repeatedly do this task on all pdfs created in previous task. So before creating job, you need to store all pdf files in list in order to give it to `ArgSplitter()` files argument. Do following steps in command line
```
import os
files = os.listdir(OUTPUT FOLDER MENTIONED IN pdf.py PROGRAM,BY DEFAULT pdf_pages)
pdf_files = []
for file in files:
	pdf_files.append(File[os.path.join(os.path.abspath(PATH TO OUTPUT FOLDER),file)])
```
 - Then give this as argument to files option of `ArgSplitter()` as `j.splitter = ArgSplitter(files = pdf_files)`. 
 - Then to merge all output files of subjobs created, use `TextMerger` as `j.postprocessors.append(TextMerger(files = ['stdout']))`. Then submit the job. You should see th merged file in output folder of main job.
 - Now to read the content of merged folder and get total count of word "it" in pdf, we will run merger.py file. So change the path to merger.py in run_python.sh file. Then use `j.application.args = [ABSOLUTE PATH TO MERGED FILE OF PREVIOUS JOB]`. Then submit the job. In the output folder you will find total word count.
 
 
## Communicating with llm using python
Here I have used llama2 of meta for llm and the script for this is llm.py. Here you can give various input in prompt_input section and change various parameters of output to get desird result. I gave following questions prompt to llm.
 - Let's start by importing necessary modules to do the simulation and create subjobs using ganga.
 - Create python script to do accept reject simulation method to find value of pi by taking millions of random points as input.
 - Now write code in ganga command line to create subjobs using the python script to run on thousand points. To create subjobs use ArgSplitter function of Ganga.
 - Finally, we'll submit the job to Ganga. Please write the code to submit the job, ensuring that it consists of one million simulations split into subjobs.

Following was the output produced by llm:
```
Sure, I'd be happy to help you with that! Here's the code for each step:
Step 1: Importing necessary modules
import numpy as np
import ganga

Step 2: Creating the Python script for the accept-reject simulation
def accept_reject_simulation(num_points):
# Generate random points inside a square
points = np.random.uniform(0, 1, size=(num_points, 2))

# Acceptance/rejection algorithm to estimate pi
accepted = 0
for i in range(num_points):
    if points[i][0] * points[i][1] < 1:
        accepted += 1

# Calculate the estimate of pi
estimate = 4 * accepted / num_points

return estimate

Step 3: Creating subjobs using Ganga's ArgSplitter

# Split the simulation into subjobs
subjobs = ganga.ArgSplitter(njobs=1000, job_fn=accept_reject_simulation, args=(1000,))

Step 4: Submitting the job to Ganga

# Submit the job to Ganga
ganga.submit(subjobs)

This code will submit a job to Ganga that consists of one million simulations, split into subjobs of 1000 simulations each. Each subjob will run the accept-reject simulation method on 1000 random points, and the results will be combined to estimate the value of pi. Let me know if you have any questions or need further assistance!
```

We can see there is refinement needed as the code generated isn't running in Ganga. But with more time in hand, this can be rectified.

