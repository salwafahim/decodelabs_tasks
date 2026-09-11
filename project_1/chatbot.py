print("🤖 Hello! I am Engineo, your Rule-Based AI Chatbot.")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    # Greetings
    if user_input == "hello" or user_input == "hi" or user_input == "hey":
        print("Bot: Hello! Nice to meet you. 😊")

    elif user_input == "good morning":
        print("Bot: Good morning! 🌞 How can I help you today?")

    elif user_input == "good afternoon":
        print("Bot: Good afternoon! How can I help you?")

    elif user_input == "good evening":
        print("Bot: Good evening! How can I help you?")

    # About the chatbot
    elif user_input == "what is your name":
        print("Bot: My name is Engineo. 🤖")

    elif user_input == "who are you":
        print("Bot: I am a rule-based AI chatbot.")

    elif user_input == "what can you do":
        print("Bot: I can answer predefined questions using rule-based logic.")

    # General conversation
    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking. 😊")

    elif user_input == "thank you" or user_input == "thanks":
        print("Bot: You're welcome! 😊")

    # AI-related questions
    elif user_input == "what is ai":
        print("Bot: AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.")

    elif user_input == "what is machine learning":
        print("Bot: Machine Learning is a branch of AI where computers learn patterns from data.")

    elif user_input == "what is deep learning":
        print("Bot: Deep Learning is a type of machine learning that uses neural networks with multiple layers.")

    # Help
    elif user_input == "help":
        print("Bot: You can ask me about my name, capabilities, AI, Machine Learning, or Deep Learning.")

    # Exit
    elif user_input == "bye" or user_input == "goodbye" or user_input == "exit":
        print("Bot: Goodbye! Have a great day! 👋")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that yet. Please try another question.")