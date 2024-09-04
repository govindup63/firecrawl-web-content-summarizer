from openai import OpenAI
import re
from firecrawl import FirecrawlApp

# Initialize FirecrawlApp with your API key
firecrawl_app = FirecrawlApp(api_key="fc-6628622cad1d431f8a279c0665ac55d6")

# Set your OpenAI API key
api_key = "YOUR_OPENAI_API_KEY"
client = OpenAI(api_key=api_key)

# Function to generate a summary using OpenAI's GPT
def summarize_text_with_openai(text, max_tokens=100):
    print("Starting text summarization using OpenAI...")  # Console log
    
    try:
        completion = client.completions.create(
            model='gpt-3.5-turbo',  # Updated model
            prompt=f"Please summarize the following text:\n\n{text}",
            max_tokens=max_tokens,
            temperature=0.7
        )
        summary = completion.choices[0].text.strip()
        print("Summarization complete using OpenAI.")  # Console log
        return summary
    except Exception as e:
        print(f"An error occurred while summarizing text: {e}")
        return "Error in summarizing the text."

# Function to scrape and summarize a webpage
def scrape_and_summarize(url):
    print(f"Scraping the content from: {url}")  # Console log
    scrape_status = firecrawl_app.scrape_url(url, params={'formats': ['markdown']})
    
    if 'markdown' in scrape_status:
        print("Content scraped successfully.")  # Console log
        content = scrape_status['markdown']
    else:
        print("Failed to retrieve markdown content.")  # Console log
        return "No content to summarize."
    
    content = re.sub(r'\s+', ' ', content)  # Clean up whitespace
    print("Starting content summarization...")  # Console log
    summary = summarize_text_with_openai(content, max_tokens=100)  # Adjust max_tokens as needed
    print("Content summarization complete.")  # Console log
    return summary

# Example usage
url_to_summarize = 'https://firecrawl.dev'  # Replace with your target URL
summary = scrape_and_summarize(url_to_summarize)
print("Summary of the webpage:")
print(summary)
