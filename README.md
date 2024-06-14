# FLIP-KG: ISWS-24
Facilitating Lyrical Implicatures within Poems using Knowledge Graphs. Public repository of the task force "Vulcan" from ISWS 2024 led by Aldo Gangemi and Andrea Poltronieri

Knowledge graphs (KGs) are useful tools to uniformly represent and integrate heterogeneous information about a domain of interest. However, the construction and population of KGs related to specific domains by extracting knowledge from unstructured texts is a challenging research activity. In this paper, we present the first steps toward the construction and evaluation of FLIP-KG. FLIP-KG is a knowledge extraction tool that produces KGs starting from a dataset of poems by combining semantic tools and LLMs. FLIP-KG extracts literal meaning from poetic lines, infers implicit knowledge, and leverages the resultant KG to generate new poems. Preliminary experiments demonstrate FLIP-KG's high accuracy in extracting poetry-related KGs and generating new poems by guiding the LLM with the underlying KG. FLIP-KG offers a promising approach to knowledge extraction and knowledge-grounded text generation for the poetic domain.

FLIP-KG utilizes the machine reading tool "AMR2FRED" which reads text and performs Abstract Meaning Representation (AMR) to RDF using the knowledge patterns applied by the FRED machine reading method. Further details can be found at the link : https://github.com/polifonia-project/machine-reading/tree/main

# Setup
- Clone the FLIP-KG repo: git clone https://github.com/junahmkh/FLIP-KG-ISWS-24.git
- Clone the repository: git clone --filter=blob:none --quiet https://github.com/anuzzolese/machine-reading
- Move inside the folder machine-reading by command line and run the installation: pip install .

# How to use
The repo contains two python scripts (run.py and utils.py). Add your secret key for Chat-gpt API in the utils.py file. The subfolder "Poem" contains the five poems used for evaluation of the proposed framework. 

- Open a terminal in the repository
- write: python run.py {poem_id} {research_question_id}; where: poem_id = {1,2,3,4,5} and research_question_id = {1,2,3}.
- Research Questions:
    - RQ1: Are existing LLMs good at interpreting implicatures in poetry?
    - RQ2: Can LLMs generate implicature knowledge graphs from a poem?
    - RQ3: Can we use LLMs to generate an interesting poem, when giving an implicature-intensive story to them?
    - RQ4: How to plan an evaluation study about the results from the previous questions? [Results at the end]

# Workflow
![FLIP-KG: Workflow](https://github.com/junahmkh/FLIP-KG-ISWS-24/assets/103508915/7245ff31-5f43-42f3-8a76-045d7ba32b43)

For the research question 3 for generating new poem from the generated KG, the workflow is defined in the following image:


![FLIP-KG: Generating Poem](https://github.com/junahmkh/FLIP-KG-ISWS-24/assets/103508915/8f701d45-8381-4213-8ce9-379112811a31)

# Evaluation

