import fitz
import requests

def inputbox():
    val = input("Input here: ")
#    print (val)
    return val

def extractnotes(pdf_path):
        doc = fitz.open(pdf_path)
        text = "" #once all the text is processed it comes up to this final combined text
        for page in doc: 
            text += page.get_text("text") + "\n"  #Takes the text from every page of the PDF
        return text[:1000]

def generatelyrics(notes):
    HUGGINGFACE_API_KEY = "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"
    API_URL = "https://api-inference.huggingface.co/models/t5-base"

    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    data = {
    "inputs": f"Summarize the following notes and turn them into song lyrics:\n\n{notes}",
    }
 #   data = {"inputs": notes}

     #sends request to hugging face
    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
         return response.json()[0]["generated_text"] #this gives back the lyrics the AI generated
    else: 
         return f"Error: {response.status_code}, {response.text}" #js gives the error if the other stuff didnt work
    
def main(): 
    pdf_path = inputbox()

    notes_text = extractnotes(pdf_path) #takes text from PDF
    print("\nExtracted Text from PDF:")
    print(notes_text[:500])

    songlyrics = generatelyrics(notes_text)
    print("\nGenerated Song Lyrics")
    print(songlyrics) #print the generated song lyrics

if __name__ == "__main__":
    main()



  
