# Telegram ChatBot with Ollama and BotMaster

## Overview
This repository contains the source code for a Telegram chatbot built using:
- [Python Telegram Bot](https://python-telegram-bot.readthedocs.io/)
- [LangChain Ollama](https://python.langchain.com/)
- A custom conversation context summarization.

The bot is designed to provide conversational responses leveraging the Llama 3 model through Ollama.

---

## Features
- **Conversational Context**: Maintains a per-user conversation history for contextual responses.
- **Context Summarization**: Automatically summarizes lengthy conversations to remain within processing limits.
- **Scalable Design**: Can handle multiple users simultaneously.

---

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python** (>= 3.9)
2. **Pip** for managing Python packages.

---

## Installation

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/MuddassirSiddiqi/TGChatBotV1.0.git
   cd TGChatBotV1.0
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Required Dependencies

Here is the list of main Python libraries used in the project:

- `python-telegram-bot`: For interacting with Telegram's API.
- `langchain-ollama`: For integrating with the Ollama model.
- `langchain-core`: Provides utilities for handling prompts.

You can find all dependencies in `requirements.txt`.

---

## Configuration

1. Obtain your Telegram bot token from [BotFather](https://core.telegram.org/bots#botfather):
   - Open Telegram and search for "BotFather."
   - Start a chat with BotFather and use the `/newbot` command to create a new bot.
   - Follow the instructions provided to get your API key (bot token).

2. Replace the placeholder `token` in the `main()` function with your Telegram bot token:
   ```python
   token = "<YOUR_BOT_TOKEN>"
   ```

3. Ensure that your Ollama model (Llama 3) is accessible and properly configured.

---

## How to Run

Start the bot by running the following command:
```bash
python bot.py
```

The bot will begin polling for updates from Telegram.

---

## Code Explanation

### Key Components

1. **Conversation Template**:
   A structured prompt ensures consistent responses.
   ```python
   template = """
   You are a helpful and knowledgeable assistant. Answer the question clearly and concisely.
   Here is the Conversation History:
   {context}

   Question: {question}
   Answer:
   """
   ```

2. **Context Management**:
   Maintains and summarizes per-user conversation history.
   ```python
   conversation_context = {}
   
   def summarize_context(context):
       if len(context.split()) > 500:
           return summarize_text(context)  # Define this function for custom summarization logic
       return context
   ```

3. **Telegram Handlers**:
   - `/start`: Initializes the conversation for a user.
   - Message Handler: Responds to user queries using the Ollama model.

   ```python
   app.add_handler(CommandHandler("start", start))
   app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
   ```

4. **Main Function**:
   Entry point for running the bot.
   ```python
   def main():
       app = Application.builder().token(token).build()
       app.add_handler(CommandHandler("start", start))
       app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
       app.run_polling()
   ```

---

## Customization

1. **Custom Prompt**:
   Update the conversation template in the `template` variable to fit your needs.

2. **Error Handling**:
   Improve error handling in `handle_message` for more robust behavior.

3. **Summarization**:
   Implement the `summarize_text` function to define custom logic for context summarization.

---

## Security Note

- **Token Safety**: Never expose your Telegram bot token in a public repository. Use environment variables or a configuration file.
- **Rate Limits**: Ensure the bot adheres to Telegram’s rate limits to avoid being blocked.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests.

---

## Contact

For any questions, reach out to `your.email@example.com` or open an issue on GitHub.

