def read_chat_log(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_summary(output_path, summary_data):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write("AI Chat Log Summary\n")
        file.write("=" * 50 + "\n\n")
        
        # Write basic summary
        summary = summary_data['summary']
        file.write(f"Total messages: {summary['total_messages']}\n")
        file.write(f"User messages: {summary['user_messages']}\n")
        file.write(f"AI messages: {summary['ai_messages']}\n")
        file.write(f"Conversation topics: {summary['nature']}\n\n")
        
        # Write keywords
        keywords = summary_data['keywords']
        file.write("Most common keywords (basic analysis):\n")
        for word, count in keywords['basic_keywords']:
            file.write(f"  - {word}: {count} times\n")
        
        if keywords['tfidf_keywords']:
            file.write("\nKeywords by TF-IDF importance:\n")
            for word, score in keywords['tfidf_keywords']:
                file.write(f"  - {word}: {score:.3f}\n")
        
        print(f"Summary written to: {output_path}")