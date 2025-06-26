# AI Chat Log Summarizer

## Overview
The AI Chat Log Summarizer is a Python project designed to read, parse, and summarize chat logs. It provides insights into conversations by counting messages and identifying frequently used keywords.

## Features
- Parses chat logs to separate messages by speaker.
- Generates summaries including total exchanges and conversation nature.
- Analyzes keywords to extract the most frequently used words while excluding common stop words.

## Project Structure
```
AI-Chat-Log-Summarizer
├── src
│   ├── main.py               # Entry point of the application
│   ├── chat_parser.py        # Contains ChatParser class for parsing chat logs
│   ├── summarizer.py         # Contains Summarizer class for generating summaries
│   ├── keyword_analyzer.py    # Contains KeywordAnalyzer class for keyword analysis
│   └── utils
│       ├── __init__.py       # Marks the utils directory as a package
│       └── file_handler.py    # Utility functions for file handling
├── input
│   ├── chat.txt              # Sample chat log files for processing
│   ├── chat2.txt             # Additional sample chat log
│   ├── chat3.txt             # Additional sample chat log
│   └── README.md             # Input directory documentation
├── output
│   ├── summary_output.txt    # Generated summary for single file processing
│   ├── batch_summary_output.txt # Generated summary for batch processing
│   └── README.md             # Output directory documentation
├── requirements.txt          # Lists project dependencies
├── .gitignore                # Specifies files to ignore in version control
└── README.md                 # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/ashrafulparan2/AI-Chat-Log-Summarizer.git
   ```
2. Navigate to the project directory:
   ```
   cd AI-Chat-Log-Summarizer
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:

### Process all files in the input directory (default):
```
python src/main.py
```

### Process a specific file or directory:
```
python src/main.py <path_to_chat_log>
```
Replace `<path_to_chat_log>` with the path to your chat log files.

### Input Files
Place your chat log files (`.txt`, `.log`, or `.chat` extensions) in the `input/` directory. The application will automatically process all supported files.

### Output Files
- Single file processing: Results saved to `output/summary_output.txt`
- Multiple files processing: Results saved to `output/batch_summary_output.txt`

## Example
After running the application, you will receive a summary of the chat log, including message counts and frequently used keywords.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.