
https://github.com/user-attachments/assets/73dc3c8f-2bcf-42d2-b61f-091249f5bfbc
# Firecrawl Web Content Summarizer

This project is a web content summarization tool that utilizes the Firecrawl SDK for scraping web content and OpenAI's GPT model to generate summaries. It allows you to input a URL, scrape its content, and then generate a concise summary using AI.

## Features

- **Web Scraping**: Extracts content from web pages using the Firecrawl SDK.
- **AI Summarization**: Uses OpenAI's GPT model to generate summaries of the scraped content.
- **Simple Interface**: Input a URL and get a summary in just a few seconds.

## Getting Started

video example: I have exhausted all my daily quota but if you have the right plan then it will work

https://github.com/user-attachments/assets/e2a3565f-8403-4790-a7f7-11904dfb6f89


### Prerequisites

- **Python 3.7+**
- **Firecrawl SDK**
- **OpenAI Python Client Library**

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/govindup63/firecrawl-web-content-summarizer.git
   cd firecrawl-web-content-summarizer
   ```

   ```

2. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:

   Create a `.env` file in the project root directory and add your API keys:

   ```env
   FIRECRAWL_API_KEY=your_firecrawl_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

### Usage

1. **Run the summarization script**:

   ```bash
   python summarizer.py
   ```

2. **Input the URL** you want to summarize:

   The script will scrape the content from the provided URL and generate a summary using OpenAI's GPT model.

3. **View the summary**:

   The generated summary will be displayed in the terminal.

### Example

```bash
python summarizer.py
```

```plaintext
Scraping the content from: https://firecrawl.dev
Content scraped successfully.
Starting content summarization...
Starting text summarization using OpenAI...
Summarization complete using OpenAI.
Summary of the webpage:
[Generated summary]
```

