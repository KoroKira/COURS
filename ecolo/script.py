import re

# Step 1: Read the content of the markdown file
input_file = "/Users/guilhem/Documents/GitHub/COURS/ecolo/sources.md"
output_file = "extracted_links.txt"

with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# Step 2: Extract all URLs using a regular expression
# Matches URLs starting with http or https
urls = re.findall(r"https?://[^\s\)]+", content)

# Step 3: Write the extracted URLs to a .txt file
with open(output_file, "w", encoding="utf-8") as file:
    for url in urls:
        file.write(url + "\n")

print(f"Extracted {len(urls)} URLs and saved to {output_file}")