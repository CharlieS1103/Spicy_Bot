
import openai
from embeds import *
import os

# retrieve the api key
api_key = ""
print(api_key)
# Collect the titles of the common issues from the embeds.py file
common_issues_titles = [
    find_config_embed.title,
    install_embed.title,
    uninstall_embed.title,
    path_embed.title,
    keyword_embed.title
]

# Define a function that uses GPT-3 to compare the user's message to the titles of the common issues
async def check_common_issues(message):
    prompt = (f"Compare the following text to following titles, if you think the text is similar to any of the titles, return the title. Otherwise, simply reply `Exit` with no additional text. Titles: {common_issues_titles}")
    print(prompt)
    completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5, api_key=api_key)
    print(completions)
    message = completions.choices[0].text
    print(message)
    return message
