import os

from dotenv import load_dotenv
from cohere import Client

# Load the .env file
load_dotenv()

class CohereAPI:
    api_key=os.getenv("COHERE_API_KEY")
    client = Client(api_key)
    models = ['command-light']

    @classmethod
    def invoke(cls, prompt: str, model='command-light', temp: float=0.7) -> str:
        # Set the parameters for text completion
        # parameters = {
        #     'temperature': temp  # Controls randomness in generation
        #     }
        # Generate the completed text
        response = cls.client.generate(
            model='command-light',  # Specify the model to use
            prompt=prompt,
        )
        
        # Return completed text
        return response.generations[0].text

