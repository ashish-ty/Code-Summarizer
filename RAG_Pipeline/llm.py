import torch
from langchain import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, pipeline
from RAG_Pipeline.config import MODEL_NAME, HF_TOKEN
import os
os.environ['HF_TOKEN'] = HF_TOKEN

class LLM:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
        self.model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, trust_remote_code=True, device_map="auto")
        self.generation_config = GenerationConfig.from_pretrained(MODEL_NAME)
        self.generation_config.max_new_tokens = 1024
        self.generation_config.temperature = 0.0001
        self.generation_config.top_p = 0.95
        self.generation_config.do_sample = True
        self.generation_config.repetition_penalty = 1.15
        
        self.text_pipeline = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                generation_config=self.generation_config,
        )
        return HuggingFacePipeline(pipeline=self.text_pipeline, model_kwargs={"temperature": 0})