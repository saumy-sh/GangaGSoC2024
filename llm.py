#!usr/bin/python3
import os

#this is the API token to access llama2 llm model
os.environ["REPLICATE_API_TOKEN"] = "r8_DlML8HMdTYVdYuUXVxcAVu2X37l3q6V28QGpu"
import replicate

#prompts
pre_prompt = "Hello Llama 2! I have a programming task that I need assistance with. I want to set up a Ganga job to calculate an approximation to the number pi using an accept-reject simulation method. The job should consist of one million simulations, split into subjobs that each perform a thousand simulations. Can you help me write the code for this? You don't respond as 'User' or pretend to be one. You are 'Assisstant'"

#prompt_input takes prompts form user to give to llama2 model
#change prompt to be given here to get different output
prompt_input = '''1 Let's start by importing necessary modules to do the simulation and create subjobs using ganga.
2 Create python script to do accept reject simulation method to find value of pi by taking millions of random points as input.
3 Now write code in ganga command line to create subjobs using the python script to run on thousand points. To create subjobs use ArgSplitter function of Ganga.
4 Finally, we'll submit the job to Ganga. Please write the code to submit the job, ensuring that it consists of one million simulations split into subjobs.'''

#here you can model parameters like 
#temperature - to chnange creativity level of response. The higher the value of temperature, the more creative outputs you get.
#top_p - top ranking cumulative probability of response to be generated
#max_length - no of words of output we are getting.
output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', # LLM model
                        input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ", # Prompts
                        "temperature":0.1, "top_p":0.9, "max_length":1000, "repetition_penalty":1})  # Model parameters
text = ""
for item in output:
    text += item
print(text)