with open("books_and_chapters.txt", "r") as file:
    max_chapters = 0
    book_with_max_chapters = ""
    
    for line in file:
        book, chapters, scripture_type = line.split(":")
        
        book = book.strip()
        chapters = int(chapters)
        scripture_type = scripture_type.strip()
        
        output_line = f"Scripture: {scripture_type}, Book: {book}, Chapters: {chapters}"
        print(output_line)
        
        if chapters > max_chapters:
            max_chapters = chapters
            book_with_max_chapters = book

print("\nResults:")
print(f"Largest number of chapters in the scriptures: {max_chapters}")
print(f"Book with the largest number of chapters: {book_with_max_chapters}")

        