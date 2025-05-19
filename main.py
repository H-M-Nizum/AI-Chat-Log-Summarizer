import os
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Separate and Store messages in appropriate structures for further analysis.
def parse_chat_log(chat_text):
    user_messages = []
    ai_messages = []
    
    lines = chat_text.splitlines()
    for line in lines:
        line = line.strip() 
        if line.startswith("User:"):
            message = line[len("User:"):].strip()
            user_messages.append(message)
        elif line.startswith("AI:"):
            message = line[len("AI:"):].strip()
            ai_messages.append(message)

    return {
        'user_messages' : user_messages, 
        'ai_messages' : ai_messages
    }

# Count total messages and messages from User vs. AI.
def message_statistics(val):
    total_user_message = len(val['user_messages'])
    total_ai_message = len(val['ai_messages'])
    total_message = total_user_message + total_ai_message
    
    return {
        'total_user_message' : total_user_message, 
        'total_ai_message' : total_ai_message, 
        'total_message' : total_message
    }

# Exclude common stop words
def clean_and_tokenize(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    
    filtered_tokens = [
        word for word in tokens
        if word.lower() not in stop_words and word.isalpha()
    ]
    return filtered_tokens

# Extract the top 5 most frequently used words.
def get_top_keywords(tokens, top_n=5):
    frequently_word = Counter(tokens)
    top_most_word = frequently_word.most_common(top_n)
    top_most_keywords = [word for word, _ in top_most_word]
    
    return top_most_keywords

# Process Chat File Data
def process_chat_file(file_path):
    print(f"\n Processing file: {os.path.basename(file_path)}")
    with open(file_path, 'r', encoding='utf-8') as f:
        chat_content = f.read()

    message_data = parse_chat_log(chat_content)
    statistics_data = message_statistics(message_data)

    combined_text = " ".join(message_data['user_messages'] + message_data['ai_messages'])
    tokens = clean_and_tokenize(combined_text)
    top_keywords = get_top_keywords(tokens)

    print("Summary:")
    print(f"- The conversation had {statistics_data['total_message']} exchanges.")
    if len(top_keywords) >= 2:
        print(f"- The user asked mainly about {top_keywords[0]} and {top_keywords[1]}.")
    elif len(top_keywords) == 1:
        print(f"- The user asked mainly about {top_keywords[0]}.")
    else:
        print("- No clear topic keywords found.")
    print(f"- Most common keywords: {', '.join(top_keywords)}")

# ==== MAIN  ====
if __name__ == "__main__":
    # Take input and read .txt file
    input_path = input("Enter the name of a chat file or folder: ").strip()

    if os.path.isdir(input_path):
        for file_name in os.listdir(input_path):
            if file_name.lower().endswith(".txt"):
                file_path = os.path.join(input_path, file_name)
                process_chat_file(file_path)

    elif os.path.isfile(input_path) and input_path.lower().endswith('.txt'):
        process_chat_file(input_path)
        
    else:
        print("The path not found or it is neither a folder nor a .txt file. Exiting.")
        
