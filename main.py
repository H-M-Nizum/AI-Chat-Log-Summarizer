import os

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


# ==== MAIN  ====
if __name__ == "__main__":
    # Take input and read .txt file
    base_directory = os.getcwd()
    file_name = input("Enter the chat file name (e.g., chat.txt): ").strip()
    file_path = os.path.join(base_directory, file_name)

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            chat_content = f.read()  
            
        message_data = parse_chat_log(chat_content)
        statistics_data = message_statistics(message_data)
        print(statistics_data)
        
    else:
        print(f"File '{file_name}' not found in folder '{base_directory}'.")