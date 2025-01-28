from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the conversation template
template = """
You are a helpful and knowledgeable assistant. Answer the question clearly and concisely.
Here is the Conversation History:
{context}

Question: {question}
Answer:
"""

# Initialize the model and prompt
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Context storage
conversation_context = {}

def summarize_context(context):
    if len(context.split()) > 500:  # Example threshold
        return summarize_text(context)  # Define this summarize_text function as needed
    return context

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler."""
    user_id = update.effective_user.id
    conversation_context[user_id] = ""  # Initialize context for the user
    await update.message.reply_text("Welcome to nanoVoltz's ChatBot! Ask me anything.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user messages."""
    user_id = update.effective_user.id
    user_input = update.message.text.strip()
    
    if user_id not in conversation_context:
        conversation_context[user_id] = ""
    
    try:
        # Generate a response using the model
        current_context = conversation_context[user_id]
        result = chain.invoke({"context": current_context, "question": user_input})
        await update.message.reply_text(result)
        
        # Update and summarize context
        conversation_context[user_id] += f"\nUser: {user_input}\nAI: {result}"
        conversation_context[user_id] = summarize_context(conversation_context[user_id])
    except Exception as e:
        await update.message.reply_text(f"Sorry, an error occurred: {e}")

def main():
    """Main function to start the bot."""
    token = "BOT_TOKEN"  # Replace with your bot's token
    app = Application.builder().token(token).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    app.run_polling()

if __name__ == "__main__":
    main()
