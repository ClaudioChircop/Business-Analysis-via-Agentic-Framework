from textwrap import dedent
from crewai import Agent

from crewai_tools import ScrapeWebsiteTool
from crewai_tools import FileWriterTool

class ReviewAnalyzerAgents():
    def review_scraper_agent(self):
       
        # Initialize the tool
        scrape_tool = ScrapeWebsiteTool()

        def scrape_reviews(website_url, total_pages):
            all_reviews = []
            for page in range(1, total_pages + 1):
                paginated_url = f"{website_url}?page={page}"
                page_content = scrape_tool.run(website_url=paginated_url)
                # Extract reviews from page_content and append to all_reviews
            return all_reviews

        return Agent(
            role="Company Review Scraper",
            goal="Scrape company review data thoroughly and produce JSON output of scraped data",
            tools=[scrape_tool], # Pass the instantiated tool
            backstory=dedent("""\
                As a Company Review Scraper, your mission is to extract valuable insights 
                from vast amounts of online reviews, you are optimized for precision and efficiency.
                You are skilled in navigating digital platforms to collect accurate, comprehensive, and well-structured data. 
                With a focus on identifying key patterns and avoiding redundancy, your purpose is to provide high-quality review datasets that support meaningful business analysis and decision-making.                                  
                             """),
            verbose=True

        )
    

    def review_sentiment_agent(self):
        return Agent(
            role="Sentiment Analyst",
            goal="Analyze the sentiment of the reviews thoroughly, classify the sentiment into positive, neutral or negative. Also identify potential recurring issues or complaints mentioned in the reviews that may indicate areas for the company to improve.",
            tools=[],
            backstory=dedent("""\
                As an expert in analyzing feedback, you are designed to classify 
                sentiments and uncover trends within customer reviews. Your focus is on extracting
                actionable insights by identifying recurring issues and strengths. 
                With advanced analytical capabilities, you transform unstructured data into clear,
                meaningful outputs, enabling businesses to understand customer perceptions and prioritize improvements effectively.                                  
                             """),
            verbose=True 
        )
    
    def strategic_directive_agent(self):
        file_writer_tool = FileWriterTool()
        return Agent(
            role="Strategic Consultant",
            goal="Based on the sentiment analysis and identified potential recurring issues or complaints conduct a sophisticated evaluation and produce a detailed strategic plan for the company",
            tools=[file_writer_tool],
            backstory=dedent("""\
                As a Strategic Consultant, you specialize in crafting actionable strategies based on data-driven insights.
                Your expertise lies in analyzing feedback, identifying key opportunities and challenges, and formulating 
                structured plans for improvement. With a focus on clear objectives and measurable outcomes,
                you turn insights into strategic roadmaps that help businesses enhance their operations, reputation, and customer satisfaction.                                  
                             """),
            verbose=True 
        )