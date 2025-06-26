# main.py

import os
from chat_parser import ChatParser
from summarizer import Summarizer
from keyword_analyzer import KeywordAnalyzer
from utils.file_handler import read_chat_log, write_summary

def main():
    chat_log_path = os.path.join('..', 'data', 'chat.txt')
    chat_log = read_chat_log(chat_log_path)

    parser = ChatParser()
    parsed_chat = parser.parse(chat_log)

    summarizer = Summarizer()
    summary = summarizer.generate_summary(parsed_chat)

    keyword_analyzer = KeywordAnalyzer()
    keywords = keyword_analyzer.extract_keywords(parsed_chat)

    summary_output = {
        'summary': summary,
        'keywords': keywords
    }

    output_path = os.path.join('..', 'data', 'summary_output.txt')
    write_summary(output_path, summary_output)

if __name__ == "__main__":
    main()