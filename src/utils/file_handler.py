def read_chat_log(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_summary(output_path, summary_data):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write("AI Chat Log Summary\n")
        file.write("=" * 50 + "\n\n")
        
        # Write message statistics
        summary = summary_data['summary']
        file.write(f"Total messages: {summary['total_messages']}\n")
        file.write(f"User messages: {summary['user_messages']}\n")
        file.write(f"AI messages: {summary['ai_messages']}\n\n")
        
        # Write top 5 keywords
        keywords = summary_data['keywords']
        file.write("Top 5 most frequently used words:\n")
        for word, count in keywords:
            file.write(f"  - {word}: {count} times\n")
        
        print(f"Summary written to: {output_path}")