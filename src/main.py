# main.py

import os
import sys
from chat_parser import ChatParser
from summarizer import Summarizer
from keyword_analyzer import KeywordAnalyzer
from utils.file_handler import read_chat_log, write_summary

def main():
    # Check if a command-line argument for chat log path is provided
    if len(sys.argv) > 1:
        chat_log_path = sys.argv[1]
        print(f"Using provided chat log path: {chat_log_path}")
    else:
        chat_log_path = os.path.join('..', 'data', 'chat.txt')
        print(f"Using default chat log path: {chat_log_path}")
    
    # Check if the file exists
    if not os.path.exists(chat_log_path):
        print(f"Error: Chat log file not found at '{chat_log_path}'")
        sys.exit(1)
    
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