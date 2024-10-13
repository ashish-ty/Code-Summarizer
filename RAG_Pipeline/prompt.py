from langchain import PromptTemplate

class Prompt:
    def __init__(self):
        self.template = """
            <s>[INST] <<SYS>>
            Act as a Python developer who is excellant at building highly scable appplications in python and optimizing code.
            Summarize the below code snippet in around 2-3 lines.
            <</SYS>>
            {text} [/INST]
        """
    
    def get_prompt_template(self,template = None):
      if template is not None:
        self.template = template
      return PromptTemplate(
          input_variables=["text"],
          template=self.template,
      )