# main.py

import os
import sys
import glob
from chat_parser import ChatParser
from summarizer import Summarizer
from keyword_analyzer import KeywordAnalyzer
from utils.file_handler import read_chat_log, write_summary, write_batch_summary

def process_single_file(file_path):
    """Process a single chat log file and return the summary data."""
    print(f"Processing: {file_path}")
    
    chat_log = read_chat_log(file_path)
    
    parser = ChatParser()
    parsed_chat = parser.parse(chat_log)
    
    summarizer = Summarizer()
    summary = summarizer.generate_summary(parsed_chat)
    
    keyword_analyzer = KeywordAnalyzer()
    keywords = keyword_analyzer.extract_keywords(parsed_chat)
    
    return {
        'file_name': os.path.basename(file_path),
        'file_path': file_path,
        'summary': summary,
        'keywords': keywords
    }

def get_chat_files(path):
    """Get all chat log files from the given path."""
    if os.path.isfile(path):
        return [path]
    elif os.path.isdir(path):
        # Look for common chat log file extensions, excluding summary files
        patterns = ['*.txt', '*.log', '*.chat']
        files = []
        for pattern in patterns:
            found_files = glob.glob(os.path.join(path, pattern))
            files.extend(found_files)
        return files
    else:
        return []

def main():
    # Check if a command-line argument for chat log path is provided
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
        print(f"Using provided path: {input_path}")
    else:
        input_path = os.path.join('..', 'input')
        print(f"Using default input folder: {input_path}")
    
    # Check if the path exists
    if not os.path.exists(input_path):
        print(f"Error: Path not found at '{input_path}'")
        sys.exit(1)
    
    # Get all chat files
    chat_files = get_chat_files(input_path)
    
    if not chat_files:
        print(f"Error: No chat log files found in '{input_path}'")
        print("Supported file extensions: .txt, .log, .chat")
        sys.exit(1)
    
    print(f"Found {len(chat_files)} chat log file(s)")
    
    # Process all files
    all_summaries = []
    for file_path in chat_files:
        try:
            summary_data = process_single_file(file_path)
            all_summaries.append(summary_data)
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            continue
    
    if not all_summaries:
        print("Error: No files were successfully processed")
        sys.exit(1)
      # Write output
    if len(all_summaries) == 1:
        # Single file - use original format
        output_path = os.path.join('..', 'output', 'summary_output.txt')
        write_summary(output_path, all_summaries[0])
    else:
        # Multiple files - use batch format
        output_path = os.path.join('..', 'output', 'batch_summary_output.txt')
        write_batch_summary(output_path, all_summaries)
    
    print(f"Processing complete! Processed {len(all_summaries)} file(s).")

if __name__ == "__main__":
    main()