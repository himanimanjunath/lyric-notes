import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"

def summarize_text(text):
    """Summarizes long text using OpenAI's GPT model."""
    prompt = f"Summarize the following lecture notes concisely:\n\n{text}\n\nSummary:"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert at summarizing lecture notes."},
                  {"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    # Example usage
    text = input("Enter or paste the extracted text: ")
    summary = summarize_text(text)
    print("\nSummary:\n", summary)
