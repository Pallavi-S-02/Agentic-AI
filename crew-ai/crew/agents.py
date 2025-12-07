##Here geeting openai api key error :( , chekc why for gemini working fine 

from crewai import Agent, LLM
from tools import yt_tool
from langchain_groq import ChatGroq

#from dotenv import load_dotenv

import os
#load_dotenv()
#os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
#api_key=os.getenv("GROQ_API_KEY")
#print('aaaaapppii', api_key)
# llm = LLM(
#     model="groq/llama-3.3-70b-versatile",
#     api_key=os.getenv("GROQ_API_KEY"),
#     temperature=0.5,
#     verbose=True,
    
# )

#call gemini model
llm = LLM(
    model="gemini/gemini-1.5-flash", 
    verbose=True,
    temperature=0.5,
    api_key=os.getenv("GOOGLE_API_KEY")
)

# create a senior blog content researcher
blog_researcher=Agent(
    role="Blog researcher from Youtube Videos",
    goal="get the relevant video transcription for the topic {topic} from the provided Yt channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science , Machine Learning And GEN AI and providing suggestion"
    ),
    tools=[yt_tool],
    #llm=ChatGroq(temperature=0.6, groq_api_key=api_key, model_name="llama-3.3-70b-versatile"),
    llm=llm,
    allow_delegation=True #i.e., to pass op of this agent to next agent , its true now coz sending to blog writer (i.e., to communicate with other agent)
)

# create a senior blog write agent with YT tool
blog_writer=Agent(
    role='Blog Writer',
    goal="Narrate compelling tech stories about the video {topic} from YT video",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    #llm=ChatGroq(temperature=0.6, groq_api_key=api_key, model_name="llama-3.3-70b-versatile"),
    llm=llm,
    allow_delegation=False
)