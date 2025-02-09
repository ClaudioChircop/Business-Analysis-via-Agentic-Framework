from crewai_tools import ScrapeWebsiteTool

# Initialize the tool
scrape_tool = ScrapeWebsiteTool()

def scrape_paginated_website(base_url, total_pages=10):
    """
    Scrape data from a paginated website for a specified number of pages.

    :param base_url: The base URL to scrape (without the page parameter).
    :param total_pages: Total number of pages to scrape.
    :return: Combined scraped data from all pages.
    """
    # Ensure the base URL has a scheme
    if not base_url.startswith("http://") and not base_url.startswith("https://"):
        base_url = f"https://{base_url}"

    # Container for storing data from all pages
    all_data = []

    for page in range(1, total_pages + 1):
        # Construct the paginated URL
        paginated_url = f"{base_url}?page={page}"
        print(f"Scraping Page: {page} - URL: {paginated_url}")

        try:
            # Pass the URL as a keyword argument
            page_data = scrape_tool.run(website_url=paginated_url)
            print(f"Data from Page {page}: {page_data[:2000]}")  # Print first 2000 characters for brevity
            all_data.append(page_data)
        except Exception as e:
            print(f"Error scraping page {page}: {e}")

    # Combine all data into a single output
    return all_data

# Test the function
if __name__ == "__main__":
    test_base_url = "www.trustpilot.com/review/www.zara.com"
    print("Starting pagination test...")
    result = scrape_paginated_website(test_base_url, total_pages=3)  # Testing with 3 pages for now
    print("\nFinal Aggregated Data:")
    print(result[:200])  # Print first 200 characters of the aggregated result for brevity

from crewai_tools import FileWriterTool

# Initialize the tool
file_writer_tool = FileWriterTool()

# Write content to a file in a specified directory
result = file_writer_tool._run('report.txt', '', 'project_final/none')
print(result)
