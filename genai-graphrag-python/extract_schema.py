import os
from dotenv import load_dotenv
load_dotenv()

from neo4j_graphrag.experimental.components.schema import SchemaFromTextExtractor
from neo4j_graphrag.llm import OpenAILLM
import asyncio

schema_extractor = SchemaFromTextExtractor(
    llm=OpenAILLM(
        model_name="gpt-4",
        model_params={"temperature": 0}
    )
)

text = """
The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France.
"""

# Extract the schema from the text  
extracted_schema = asyncio.run(schema_extractor.run(text=text))

print(extracted_schema)
