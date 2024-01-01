
import pathlib
import textwrap

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

PROMPTS = {
    'SKILLS': ["Mention 5 skills in related to <input>"]
}

GOOGLE_API_KEY="AIzaSyC6EmL0uJxPBZ1hNo3tvNdzK-2l7be7lSg"

genai.configure(api_key=GOOGLE_API_KEY)

# model = genai.GenerativeModel('gemini-pro')
# response = model.generate_content("what is the meaning of life?")
# to_markdown(response.text)

class GVModel:
    GEMINI_PRO = 'gemini-pro'
    def get_response(self, message, rcs_type):
        model = genai.GenerativeModel(self.GEMINI_PRO)
        prompt = self.prepare_prompt(message, rcs_type)
        messages =[{
            'role': 'user',
            'parts': prompt['parts']
        }]
        result = model.generate_content(prompt, stream=True)
        result.resolve()
        print(result.text)
        messages.append({'role': 'model',
                         'parts': [result.text]})
        response = result.parts[0]
        return response.text

    @staticmethod
    def prepare_prompt(message, rcs_type):
        for pmpt in PROMPTS.SKILLS:
            pmpt.replace("<input>", "message")
        prompts = {
            'role': 'user',
            'parts': PROMPTS.SKILLS,
        }
        return prompts
    @staticmethod
    def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

