import os
import json
from flask import Flask, request, Response, stream_with_context
from flask_cors import CORS
from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv
from web_parser import get_website_content
from config import WEBSITE_URL

# Load environment variables
load_dotenv()

# Initialize Cerebras client [cite: 1]
client = Cerebras(api_key=os.getenv("CEREBRAS_API_KEY"))

# Flask app setup
app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(force=True)

    user_input = data.get("message", "")
    file_name = data.get("file", "")

    website_context = get_website_content(WEBSITE_URL)

    # Build final prompt
    final_prompt = user_input
    if file_name:
        final_prompt = f"User uploaded file: {file_name}\nQuestion: {user_input}"

    def generate():
        try:
            stream = client.chat.completions.create(
                model="llama3.1-8b",
                stream=True,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful AI assistant. "
                            "Be direct and concise. Provide the required answer clearly without unnecessary length. "
                            "Only provide a descriptive or long-form answer if the user's question explicitly asks for it "
                            "or if the topic is complex enough to require explanation for clarity. "
                            f"Website Context:\n{website_context}"
                        )
                    },
                    {
                        "role": "user",
                        "content": final_prompt
                    }
                ]
            )

            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta:
                    content = chunk.choices[0].delta.content
                    if content:
                        yield f"data: {json.dumps({'content': content})}\n\n"

        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)