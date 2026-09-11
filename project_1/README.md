# Engineo - Rule-Based AI Chatbot

Engineo is a simple rule-based AI chatbot developed in Python. It uses predefined rules and conditional statements to respond to user inputs.

## Features

- Responds to common greetings
- Provides information about the chatbot
- Answers basic AI-related questions
- Answers questions about Machine Learning and Deep Learning
- Handles basic conversation
- Provides a help option
- Supports exit commands such as `bye`, `goodbye`, and `exit`
- Handles unknown inputs with a default response

## Technologies Used

- Python
- Conditional Statements
- While Loop
- User Input Handling
- String Processing

## How It Works

The chatbot continuously takes input from the user and converts it to lowercase.

It then compares the input with predefined questions using `if`, `elif`, and `else` statements.

If a matching rule is found, Engineo provides the corresponding response. If no rule matches, it displays a default response.

## Example

    🤖 Hello! I am Engineo, your Rule-Based AI Chatbot.
    Type 'bye' to exit.

    You: hello
    Bot: Hello! Nice to meet you. 😊

    You: what is ai
    Bot: AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.

    You: what is machine learning
    Bot: Machine Learning is a branch of AI where computers learn patterns from data.

    You: bye
    Bot: Goodbye! Have a great day! 👋

## How to Run

Make sure Python is installed on your computer.

Run the following command in the terminal:

    python chatbot.py

## Project Type

Beginner-level Python / AI project focused on understanding rule-based chatbot logic and basic conversational AI.
