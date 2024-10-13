from code_summarizer import CodeSummarizer

if __name__ == "__main__":
    codeSummarizer = CodeSummarizer()
    code_summary = codeSummarizer.get_part_wise_summary(source_path="path_to_text_file")