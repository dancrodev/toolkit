import os
import shutil
import re
from ebooklib import epub

# Sanitizes a folder name by removing invalid characters.
def sanitize_folder_name(name):
    return re.sub(r'[\\/*?:"<>|]', '', name).strip()

# Extracts the title from an EPUB file's metadata.
def get_epub_title(epub_path):

    try: 

        # Load the EPUB file
        book = epub.read_epub(epub_path)

        # Get the title from the 'DC' metadata field
        title = book.get_metadata('DC', 'title')

        # If title exists and is not empty, return the first title string
        if title and len(title) > 0:
            return title[0][0]
        
    except Exception as e:

        # Handle any exception that occurs while reading the EPUB
        print(f"[ERROR] Failed to extract title from '{epub_path}': {e}")

    # Return None if title couldn't be extracted
    return None

# Main function to process all EPUB files in the current directory.
def main():
    # Get the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Loop through every file in the current directory
    for file in os.listdir(current_dir):

        # Only process files that end with .epub (case-insensitive)
        if file.lower().endswith('.epub'):

            # Create the full path to the EPUB file
            epub_path = os.path.join(current_dir, file)

            # Extract the title from the EPUB file
            title = get_epub_title(epub_path)

            # Only proceed if a valid title was extracted
            if title:

                # Clean the title to make it a safe folder name
                folder_name = sanitize_folder_name(title)

                # Create the full path for the new folder
                folder_path = os.path.join(current_dir, folder_name)

                # Create the folder (do nothing if it already exists)
                os.makedirs(folder_path, exist_ok = True)

                # Define the new location for the EPUB file inside the folder
                new_path = os.path.join(folder_path, file)

                # Print an info message
                print(f"[INFO] Moving '{file}' → '{folder_name}/'")

                # Move the EPUB file to its new folder
                shutil.move(epub_path, new_path)

            else:

                # Warn the user if the title could not be extracted
                print(f"[WARN] Skipping '{file}' (no title found)")

# Run the script only if it's being executed directly (not imported)
if __name__ == '__main__':
    main()
