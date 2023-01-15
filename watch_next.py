# Import libraries
import spacy

# Specifying the model we want to use
nlp = spacy.load("en_core_web_md")

new_description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""


# Create a function that takes in the description as a parameter and returns the title of the most similar movie.
def next_movie(description):

    max_similarity = 0
    list_similarity = []

    # Try - except will display error if text file doesn't exist
    try:
        with open("movies.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                title, desc = line.split(":")
                similarity = nlp(desc).similarity(nlp(description))
                list_similarity.append((title, desc, similarity))

                if similarity > max_similarity:
                    max_similarity = similarity

        for i in list_similarity:
            if i[2] == max_similarity:
                print(f"Next movie to watch: {i[0]}")

    except FileExistsError as error:
        print("File doesn't exist")
        print(error)


# Display result
next_movie(new_description)

