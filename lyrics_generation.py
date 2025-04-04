import pronouncing

def generate_lyrics(summary):
    words = summary.split()
    lyrics = []
    for i, word in enumerate(words):
        lyrics.append(word)
        if i % 5 == 0:  # Add a line break every 5 words
            lyrics.append("\n")
        # Add a rhyme every 10 words
        if i % 10 == 0 and i > 0:
            rhymes = pronouncing.rhymes(word)
            if rhymes:
                lyrics.append(rhymes[0] + "\n")
    return " ".join(lyrics)