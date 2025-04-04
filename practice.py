# import packages - let's you do things native python can't do 
import fitz # analyzes whats in the pdf
import requests #takes our requests and spits into HuggingFace API // anything to do with HuggingFace done here
#Hugginf face provides you with models that companies have already made - it's a website 

def inputBox():
    val = input("Input here: ")
    return val

def extractNotes(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

#API - application programming interface 
# using preexisitng code

def generateLyrics(notes):
    # API's: 2 parts: 1. key 2. url - endpoint

    #imports the API 
    HUGGINGFACE_API_KEY = ......
    API_URL = ............ # got from the many models in HuggingFace
    
    #gpt2 - crappy but lightweight - need to change it 
    #api url is the specific endpoint of the model we are using 
    # we are the starting point, the key is the journey, and the url is the endpoint

#telling you you can use API 
# useful when requesting - 99% of the time you need to do that
    headers = ......
    data = {"inputs:" notes}

    response = requests.post(API_URL, headers=headers,json=data)
    # what is a post request - LEARN - it's important for API 
    #json - format for storing / exchanging data in human text 

    if response.status_code = 200: #if it's good
        return response.json()[0]["generated_text"] #returns the generated lyrics back 
    else: 
        return f"Error: {response.status_code}, {response.text}"
    
    def main():
        pdf_path = inpubox()

        notes_text = extractnotes(pdf_path)
        print("\nExtracted text from PDF: ")
        print(notes_text(:500))

        songlyrics = generateLyrics(notes_text)
        print("\nGenerated song lyrics: ")
        print(songlyrics)

    if __name__ == "__main__";
        main()






