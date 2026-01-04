# AI-Assistant-Real-Time-Web-Aware-Chatbot
Real-time AI Chatbot with Web-Context Integration (RAG) | Built with Python, Flask, and Cerebras Llama 3.1 for high-speed streaming inference.


🤖 AI Premium Assistant (Web-Aware Chatbot)
An intelligent, real-time chatbot system that leverages Large Language Models (LLMs) and Web Scraping to provide domain-specific answers. The system "reads" a target website to gain context before answering user queries, implementing a lightweight version of Retrieval-Augmented Generation (RAG).

🚀 Key Features
High-Speed Inference: Utilizes the Cerebras SDK for ultra-low latency streaming responses using Llama 3.1.

Live Web Context: Automatically scrapes and parses website data using BeautifulSoup4 to provide up-to-date, accurate information.

Real-Time Streaming: Implements Server-Sent Events (SSE) via Flask to stream text to the UI as it's being generated.

Premium Glassmorphism UI: A sleek, animated chat interface built with Tailwind CSS and Marked.js for markdown rendering.

Multi-Modal Interaction: Supports Voice-to-Text input via the Web Speech API and handles file attachment metadata.

Intelligent Formatting: Supports nested bullet points, bold headers, and structured data display.

🛠️ Tech Stack
Backend: Python, Flask, Cerebras AI SDK, BeautifulSoup4, Requests

Frontend: JavaScript (ES6+), Tailwind CSS, Marked.js (Markdown), HTML5

DevOps/Tools: Dotenv (Environment Management), CORS, Git

📂 File Structure
app.py: The core Flask server managing API routes and LLM logic.

web_parser.py: The scraping module that extracts and cleans text from URLs.

config.py: Configuration file for target URLs and global settings.

index.html: The frontend interface with popup animations and UI logic.

⚙️ Quick Setup
Clone the repository:

Bash

git clone https://github.com/yourusername/ai-chatbot-system.git
Install dependencies:

Bash

pip install flask flask-cors cerebras_cloud_sdk requests beautifulsoup4 python-dotenv
Configure Environment: Create a .env file and add your Cerebras API key:

Code snippet

CEREBRAS_API_KEY=your_api_key_here
Run the application:

Bash

python app.py
