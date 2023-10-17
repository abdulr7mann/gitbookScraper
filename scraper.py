from langchain.document_loaders import GitbookLoader

"""
This script is used to scrape content from a specific GitBook page, extract the markdown content,
and save it to a markdown file with UTF-8 encoding.

The script uses the langchain.document_loaders.GitbookLoader class to load the GitBook page content,
extracts the markdown content, and saves it to a markdown file in the 'hacktricks' directory.
"""

# Create an instance of GitbookLoader with the URL of the GitBook page to be scraped.
# The load_all_paths parameter is set to True to load all related paths on the GitBook page.
loader = GitbookLoader("https://book.hacktricks.xyz", load_all_paths=True)

# Call the load method to scrape the content of the GitBook page.
# all_pages_data is expected to be a list of objects, each containing the content of a part of the GitBook page.
all_pages_data = loader.load()

# Print the base URL of the loaded GitBook page to the console.
print(f"Fetched {loader.base_url}")

# Extract the markdown content from the first object in all_pages_data.
# This line may need to be modified depending on the actual structure of all_pages_data.
page_content = all_pages_data[0].page_content if all_pages_data else ""

# Extract the last part of the base URL to use as the name of the markdown file.
page_name = loader.base_url.rsplit('/', 1)[-1]

# filename to create the complete path to the markdown file.
filename = f"{page_name}.md"

# Open the markdown file with write permission and UTF-8 encoding.
with open(filename, 'w', encoding='utf-8') as file:
    # Write the extracted markdown content to the file.
    file.write(page_content)

# Print the path to the saved markdown file to the console.
print(f"Page content saved to {filename}")
