import chainlit as cl
import dotenv

dotenv.load_dotenv()

# cl acts as a temporary storage location for the current active conversation, 
# but it's more accurate to say that Chainlit manages the current session's messages rather 
# than calling cl itself a storage location.

# The @cl.on_message decorator registers the function below it to run whenever a user sends 
# a message in the Chainlit chat interface.

@cl.on_message
async def on_message(message: cl.Message):
    await cl.Message(content=f"Received: {message.content}").send()

# The .send() method transmits the message to the user's browser/chat interface so they 
# can actually see it.

# Basically what the function does is that when a user sends a message, 
# a received message ("Received: " + the user's message) is displayed on the 
# chat interface/ui.
