from code_parser import CodeParser
from RAG_Pipeline.prompt import Prompt
from RAG_Pipeline.llm import LLM

class CodeSummarizer:
  def __init__(self) -> None:
    self.codeParser = CodeParser()
    self.promptTemplate = Prompt().get_prompt_template()
    self.LLM = LLM()
  def get_part_wise_summary(self,source_path):
    extracted_elements = self.codeParser.parse(source_path)
    reponse_list = []
    for code_part in extracted_elements:
      response = self.LLM(self.promptTemplate.format(text=code_part))
      reponse_list.append(response)
    return reponse_list