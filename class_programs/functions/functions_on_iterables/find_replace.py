def find_and_replace(text, search_term, replacement):
    # Using str.find() to search for the search_term in the text
    index = text.index(search_term)

    if index != -1:
        # Search term found
        print(f"Found '{search_term}' at index {index}.")

        # Replace the first occurrence of the search term
        text = text[:index] + replacement + text[index + len(search_term):]

        # Print the updated text
        print("Updated text:")
        print(text)
    else:
        # Search term not found
        print(f"'{search_term}' not found in the text.")


# Example text
document = "This is a sample document. It contains sample text."

# Search for "sample" and replace it with "example"
find_and_replace(document, "Python", "example")
