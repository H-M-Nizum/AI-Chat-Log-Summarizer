# Chat Log Summarizer

A Python tool to analyze and generate summaries from chat logs. It processes conversation files, extracts key statistics, and highlights the main topics discussed by identifying the most frequent meaningful keywords.

---

## Features

- **Parse chat logs** formatted with user and AI messages.
- **Count total messages** and exchanges between user and AI.
- **Clean and tokenize text**, filtering out common stop words.
- **Extract top keywords** to reflect the main topics discussed.
- **Generate clear summaries** including:
  - Total number of exchanges
  - Nature of the conversation (based on keywords)
  - Most common keywords
- **Support single chat file or multiple chat files** in a folder for batch processing.

---

## Requirements

- Python 3.6+
- [NLTK](https://www.nltk.org/) (Natural Language Toolkit)
  
### Optional
- [1. NLTK Install](https://www.nltk.org/data.html) (Natural Language Toolkit)
- [2. NLTK Install](https://www.pythonanywhere.com/forums/topic/3060/)  (Natural Language Toolkit)

---

## Installation

1. Clone the repository:

   ```
   git clone [https://github.com/your-username/chat-log-summarizer.git](https://github.com/H-M-Nizum/AI-Chat-Log-Summarizer)
   cd chat-log-summarizer
   ```
2. Install required Python packages:
```
  pip install nltk
```
3. Download NLTK resources (run once):
 ```
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')
```

## Usage

Run the script and provide either a single chat .txt file or a folder containing multiple .txt chat log files:
```
python main.py
```

## Contact
For any questions or suggestions, please open an issue or contact:
Gmail - hmnizum1714032@gmail.com
Phone: 8801981251861
