# Import NLTK library
import nltk
# Download the required packages
nltk.download('punkt')
nltk.download('wordnet')
# Import the word tokenizer and lemmatizer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# Create an instance of the lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a dictionary of responses
responses = {
    "hello": "Hello, I am a chatbot.",
    "how are you": "I am fine, thank you.",
    "what is your name": "My name is Chatbot.",
    "what can you do": "I can chat with you.",
    "bye": "Goodbye, have a nice day."
}

# Define a function to process the user input
def process_input(input):
    # Convert the input to lowercase
    input = input.lower()
    # Tokenize the input into words
    words = word_tokenize(input)
    # Lemmatize the words
    words = [lemmatizer.lemmatize(word) for word in words]
    # Join the words back into a sentence
    sentence = ' '.join(words)
    # Return the processed input
    return sentence

# Define a function to generate a response
def generate_response(input):
    # Process the input
    input = process_input(input)
    # Check if the input is in the responses dictionary
    if input in responses:
        # Return the matching response
        return responses[input]
    else:
        # Return a default response
        return "I'm sorry, I don't understand."

# Start a conversation with the user
print("Welcome to Chatbot. Type something to start a conversation.")
# Loop until the user types bye
while True:
    # Get the user input
    user_input = input("You: ")
    # Generate a response
    response = generate_response(user_input)
    # Print the response
    print("Chatbot: " + response)
    # Break the loop if the user types bye
    if user_input.lower() == "bye":
        break
