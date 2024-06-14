import openai
import subprocess
from utils import *
import pandas as pd
import sys
import os
from rdflib import Graph

inpts = sys.argv
poem_id = int(inpts[1])
r_question = int(inpts[2])

# Set your API key
openai.api_key = secret_key

file_csv = "Poem/Poem_{}.csv".format(poem_id)
poem_df = pd.read_csv(file_csv)

file_txt = "Poem/Poem_{}.txt".format(poem_id)
poem_txt = read_txt_file(file_txt)

if(r_question == 1):
    print(f"Research question {r_question}\n")
    role = "You are a linguist. You are given verses from a poem and your task is to\
            identify conversational implicatures present in those verses and see if they\
            are violating any of Grice's four conversational maxims."
    prompt = f"Poem verses: {poem_txt}\nMake a list of all the implicatures present in the\
            peom and also give a motivational reasoning behind your evaluation for\
            each occurance"
elif(r_question == 2):
    print(f"Research question {r_question}\n")
    file_path = f"implicatures_{poem_id}.txt"
    implicatures = read_txt_file(file_path)
    role = "You are knowledge engineer. You will be provided with a list containing conversational\
            implicatures that violate Grice's conversational maxims from a poem and the motivation behind\
            those violations. You are also provided a KG which already has\
            formally structured knowledge from the poem's text that can be interpreted by machines\
            according to a shared semantics. You have to populate the knowledge graph containing the\
            formal structure with all the implicatures that violate the maxims and the motivations behind them"
    
    # Define the arguments you want to pass to the script
    arguments = ['-m','amr2fred','-d',';','-n','https://w3id.org/stlab/mr_data/','-o','out.ttl',os.path.join("..",file_csv)]
    
    os.chdir('./machine-reading')
    # Verify the current working directory
    print("Current working directory:", os.getcwd())
    
    # Run the script with the arguments
    result = subprocess.run(['python', 'mr.py'] + arguments, capture_output=True, text=True)
    # Print the output of the script
    print("Output of AMR2FRED:\n")
    print(result.stdout)
    print(result.stderr)
    
    # Create a graph
    kg = Graph()# Parse the TTL file
    kg.parse("out.ttl", format="turtle")
    print("KG saved as out.ttl")

    prompt = f"Implicatures: \n"+ implicatures + f"\nKnowledge graph: {kg}"+"\n.Populate th\
            provided knowledge graph in the context with the contents of the implicatures and output the populated KG as .ttl file."
    os.chdir('../')# Verify the current working directory
    print("Current working directory:", os.getcwd())
elif(r_question == 3):
    print(f"Research question {r_question}\n")

    ttl_file_path = 'machine-reading/out.ttl'
    # Read and print the contents of the TTL file as text
    graph = read_txt_file(ttl_file_path)
    role = "You are a knowledge engineer and you are a poet. You are\
            provided with a knowledge graph which contains the formal respresentation of a poem and\
            the conversational maxims that the poem verses violate. You have to extract meaning from the\
            knowledge graph and generate poems of your own based on the extracted meaning"
    prompt = f"knowledge graph: \n"+ graph + "\n. Generate a new poem from the provided knowledge graph."
# Define the conversation
messages = [
    {"role": "system", "content": role},
    {"role": "user", "content": prompt}
]
# Make the API request
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages
)
# Print the response
print(response['choices'][0]['message']['content'])
if(r_question == 1):
    save_path = f"implicatures_{poem_id}.txt"
    save_txt_file(response['choices'][0]['message']['content'],save_path)
elif(r_question == 2):
    save_path = f"KG_{poem_id}.txt"
    save_txt_file(response['choices'][0]['message']['content'],save_path)