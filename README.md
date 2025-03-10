# Web-Automation-AI-agent-using-LLMs-browseruse


This repository contains two Python scripts (`gemini.py` and `travel.py`) that demonstrate web automation using large language models (LLMs) and a browser automation framework. These scripts leverage LLMs to perform tasks such as web searches and data extraction by interacting with websites programmatically.

- **`gemini.py`**: Uses Google's Gemini model (via API) to search for products on Flipkart and retrieve pricing information.
- **`travel.py`**: Uses the Qwen2.5 model (via Ollama locally) to break down user-defined tasks into actionable steps for web automation.

Both scripts utilize the `browser_use` library for browser automation and rely on the `langchain` ecosystem for LLM integration.

## Features
- **Gemini Integration**: Perform web tasks using Google's Gemini API (`gemini.py`).
- **Local LLM Support**: Run tasks locally with Ollama and the Qwen2.5 model (`travel.py`).
- **Dynamic Task Breakdown**: Automatically convert user-defined tasks into executable steps (`travel.py`).
- **Browser Automation**: Interact with websites programmatically using the `browser_use` library.

## Prerequisites
- Python 3.8+
- A modern web browser (e.g., Chromium-based browser for `browser_use`)
- Required Python packages (see [Installation](#installation))
- For `gemini.py`: A Google Gemini API key
- For `travel.py`: Ollama installed locally with the Qwen2.5 model

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mrxvision97/Web-Automation-AI-agent-using-LLMs-browseruse.git
   cd Web-Automation-AI-agent-using-LLMs-browseruse
   ```
## Set Up a Virtual Environment
   ```bash
   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
 ```

### Install Dependencies Install the required Python packages
 ```bash
   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
 ```
### Additional Setup
1. **Google Gemini API Key**
   - Obtain a Google Gemini API key from the [Google Cloud Console](https://console.cloud.google.com/).
   - Set the `GOOGLE_GEMINI_API_KEY` environment variable to your API key.
2. **for `travel.py`**
Install Ollama locally
Pull the Qwen2.5 model
 ``` bash
ollama pull qwen2.5:7b
```
3. **Run the Scripts**
   - Run `gemini.py` to search for products on Flipkart and retrieve pricing information.
   - Run `travel.py` to break down user-defined tasks into actionable steps for web automation.

## Acknowledgements
Built with LangChain and Ollama.
Browser automation powered by browser_use.
