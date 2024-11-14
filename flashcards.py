# flashcards.py

flashcards = {}

def add_flashcard(word, definition):
    flashcards[word] = definition

def view_flashcard(word):
    return flashcards.get(word, "Word not found")

def delete_flashcard(word):
    flashcards.pop(word, None)

# Sample usage
add_flashcard("Python", "A high-level programming language.")
print("Flashcard for Python:", view_flashcard("Python"))
delete_flashcard("Python")
