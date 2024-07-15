# Open the file and read through it line by line
with open("books_and_chapters.txt", "r") as file:
    max_chapters = 0
    book_with_max_chapters = ""
    
    for line in file:
        # Split the line into key-value pairs
        book, chapters, scripture_type = line.split(":")
        
        # Extract information
        book = book.strip()
        chapters = int(chapters)
        scripture_type = scripture_type.strip()
        
        # Format and print the desired output
        output_line = f"Scripture: {scripture_type}, Book: {book}, Chapters: {chapters}"
        print(output_line)
        
        # Check for the largest number of chapters and the corresponding book
        if chapters > max_chapters:
            max_chapters = chapters
            book_with_max_chapters = book

# Print the results after reading through the entire file
print("\nResults:")
print(f"Largest number of chapters in the scriptures: {max_chapters}")
print(f"Book with the largest number of chapters: {book_with_max_chapters}")
