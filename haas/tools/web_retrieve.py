from haas.tools.tool import Tool
import requests
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class WebRetrieve(Tool):
    def gpt4_assistants_tool(self):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": "Retrieve live internet web page content using `lynx --dump`.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "URL of the web page to retrieve. Example: https://www.google.com/search?q=I+can+search+the+web+with+lynx",
                        }
                    },
                    "required": ["url"],
                },
            },
        }

    def gpt4_prompt_instructions(self):
        return """
            ## Web Page Retrieval Tool (web_retrieve):

            This tool is designed to retrieve the full text content of a oive internet web page. It operates using `lynx --dump`, providing a text-based representation of the web page specified by the given URL followed by the url links from the page.

            ### Parameters:

            * url: The full HTTP or HTTPS URL of the web page to retrieve content from.
        """

    def do_it(self, url):
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            raise RuntimeError(f"Web page retrieval error: {response.status_code}")

        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove script tags and style tags
        for script in soup(["script", "style"]):
            script.decompose()

        # Get the text from the soup and remove leading and trailing whitespaces
        text = soup.get_text(strip=True, separator=" ")

        # Return the text content of the response
        return text
