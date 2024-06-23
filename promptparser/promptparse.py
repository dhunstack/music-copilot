from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
# from langchain.chains.openai_tools import create_extraction_chain_pydantic
from typing import Optional, List
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

class TunesformerPrompt(BaseModel):
    """Tunesformer Prompt with structured output"""

    sections: int = Field(description="Number of sections in the piece.")
    bar_lengths: List[int] = Field(description="List of bar lengths in each section.")
    sections_similarity: Optional[List[List[int]]] = Field(description="List of similarity scores between sections.")
    key_signature: Optional[str] = Field(description="Key signature of the piece.")
    metre: Optional[str] = Field(description="Metre of the piece.")
    starter_string: Optional[str] = Field(description="Starter string for the piece.")

structured_llm = llm.with_structured_output(TunesformerPrompt)

def with_structured_output() -> TunesformerPrompt:
    """LLM to add structured output to a prompt class."""
    res = structured_llm.invoke("Generate a piece of music with 3 sections, each with 4 bars, and a key signature of Amin.")
    print(res)
    return res


def few_shot_structured_output() -> TunesformerPrompt:
    """LLM to add structured output to a prompt class."""
    system = """Extract information from the user's query and return structured output. \

    Here are some examples of queries and responses:

    example_user: Make me a melody with three sections of 4 bars each. Sections should be musically related and coherent. \
    Should be in 4/4time, A minor. Start with the root chord.
    example_assistant: {{"sections": "3", "bar_lengths": "[4, 4, 4]", "sections_similarity": "[[], [5], [5, 5]]", "key_signature": "Amin", "metre": "4/4", "starter_string": "Am"}}

    example_user: Make me a melody with two sections, 4 and 8 bars respectively. Sections don't need to be related to each other. \
    Should be in 3/4 time, C major. Start with the dominant chord.
    example_assistant: {{"sections": "2", "bar_lengths": "[4, 8]", "sections_similarity": "[[], [0]]", "key_signature": "C", "metre": "3/4", "starter_string": "G"}}

    example_user: Make me a melody with three sections of 4, 6, and 8 bars respectively. Section 1 and 2 should be highly related, section 3 should be medium related to 2 and highly related to 1. \
    Should be in 6/8 time, D major. Start with the subdominant chord.
    example_assistant: {{"sections": "3", "bar_lengths": "[4, 6, 8]", "sections_similarity": "[[], [10], [10, 5]]", "key_signature": "D", "metre": "6/8", "starter_string": "G"}}"""

    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", "{input}")])

    few_shot_structured_llm = prompt | structured_llm
    # query = "Give me a song with 5 sections, 4 bars each, in 4/4 time, C major, starting with the tonic chord. Sections should be highly related to each other."
    query = "Give me a song with 3 sections, 4 bars each, in 4/4 time, C major, starting with the tonic chord. Section 1 and 2 should be highly related, section 3 should be completely different."
    res = few_shot_structured_llm.invoke(query)
    print(res)



