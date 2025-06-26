def read_chat_log(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_summary(output_path, summary_data):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write("AI Chat Log Summary\n")
        file.write("=" * 50 + "\n\n")          # Write basic summary
        summary = summary_data['summary']
        file.write(f"Total exchanges: {summary['total_exchanges']}\n")
        file.write(f"User messages: {summary['user_messages']}\n")
        file.write(f"AI messages: {summary['ai_messages']}\n")
        file.write(f"Summary: {summary['conversational_summary']}\n\n")
        
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

def write_batch_summary(output_path, all_summaries):
    """Write a summary for multiple chat log files."""
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write("AI Chat Log Batch Summary\n")
        file.write("=" * 60 + "\n\n")
        
        # Overall statistics
        total_files = len(all_summaries)
        total_exchanges = sum(summary['summary']['total_exchanges'] for summary in all_summaries)
        total_user_messages = sum(summary['summary']['user_messages'] for summary in all_summaries)
        total_ai_messages = sum(summary['summary']['ai_messages'] for summary in all_summaries)
        
        file.write("OVERALL STATISTICS\n")
        file.write("-" * 30 + "\n")
        file.write(f"Total files processed: {total_files}\n")
        file.write(f"Total exchanges across all files: {total_exchanges}\n")
        file.write(f"Total user messages: {total_user_messages}\n")
        file.write(f"Total AI messages: {total_ai_messages}\n\n")
        
        # Aggregate keywords across all files
        all_basic_keywords = {}
        all_tfidf_keywords = {}
        
        for summary in all_summaries:
            # Aggregate basic keywords
            for word, count in summary['keywords']['basic_keywords']:
                all_basic_keywords[word] = all_basic_keywords.get(word, 0) + count
            
            # Aggregate TF-IDF keywords (taking average scores)
            for word, score in summary['keywords']['tfidf_keywords']:
                if word in all_tfidf_keywords:
                    all_tfidf_keywords[word] = (all_tfidf_keywords[word] + score) / 2
                else:
                    all_tfidf_keywords[word] = score
        
        # Write aggregated keywords
        file.write("AGGREGATED KEYWORDS ACROSS ALL FILES\n")
        file.write("-" * 40 + "\n")
        
        # Sort and write basic keywords
        sorted_basic = sorted(all_basic_keywords.items(), key=lambda x: x[1], reverse=True)[:10]
        file.write("Most common keywords (basic analysis):\n")
        for word, count in sorted_basic:
            file.write(f"  - {word}: {count} times\n")
        
        # Sort and write TF-IDF keywords
        if all_tfidf_keywords:
            sorted_tfidf = sorted(all_tfidf_keywords.items(), key=lambda x: x[1], reverse=True)[:10]
            file.write("\nKeywords by TF-IDF importance (averaged):\n")
            for word, score in sorted_tfidf:
                file.write(f"  - {word}: {score:.3f}\n")
        
        file.write("\n" + "=" * 60 + "\n\n")
        
        # Individual file summaries
        file.write("INDIVIDUAL FILE SUMMARIES\n")
        file.write("=" * 60 + "\n\n")
        
        for i, summary in enumerate(all_summaries, 1):
            file.write(f"File {i}: {summary['file_name']}\n")
            file.write("-" * (len(f"File {i}: {summary['file_name']}")) + "\n")
            file.write(f"Path: {summary['file_path']}\n")
              # Write individual summary
            summary_data = summary['summary']
            file.write(f"Total exchanges: {summary_data['total_exchanges']}\n")
            file.write(f"User messages: {summary_data['user_messages']}\n")
            file.write(f"AI messages: {summary_data['ai_messages']}\n")
            file.write(f"Summary: {summary_data['conversational_summary']}\n\n")
            
            # Write individual keywords
            keywords = summary['keywords']
            file.write("Most common keywords:\n")
            for word, count in keywords['basic_keywords']:
                file.write(f"  - {word}: {count} times\n")
            
            if keywords['tfidf_keywords']:
                file.write("TF-IDF keywords:\n")
                for word, score in keywords['tfidf_keywords']:
                    file.write(f"  - {word}: {score:.3f}\n")
            
            file.write("\n")
        
        print(f"Batch summary written to: {output_path}")