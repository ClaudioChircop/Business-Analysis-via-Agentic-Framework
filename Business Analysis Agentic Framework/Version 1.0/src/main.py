from dotenv import load_dotenv, find_dotenv # added find_dotenv 
from crewai import Crew
from tasks import ReviewAnalyzerTasks
from agents import ReviewAnalyzerAgents
import os # added import 

def main():
    load_dotenv(find_dotenv(), verbose=True) #added find dotenv & verbose
    #print(os.getenv('INSERT KEY HERE')) # comment out, added api key 

    print('## Welcome to the Sentiment Analyzer')
    print('------------------------------------')

    website_url = input("Input URL \n")

    tasks = ReviewAnalyzerTasks()
    agents = ReviewAnalyzerAgents()

    # create agents

    review_scraper_agent = agents.review_scraper_agent()
    review_sentiment_agent = agents.review_sentiment_agent()
    strategic_directive_agent = agents.strategic_directive_agent()

    # create tasks 

    scrape_company_review_task = tasks.scrape_company_review_task(review_scraper_agent, website_url, total_pages=10)
    review_sentiment_task = tasks.review_sentiment_task(review_sentiment_agent)
    strategic_directive_task = tasks.strategic_directive_task(strategic_directive_agent)

    review_sentiment_task.context = [scrape_company_review_task]
    strategic_directive_task.context = [review_sentiment_task]

    crew = Crew(
        agents=[
            review_scraper_agent,
            review_sentiment_agent,
            strategic_directive_agent
        ],
        tasks=[
            scrape_company_review_task,
            review_sentiment_task,
            strategic_directive_task
        ]
    )

    result = crew.kickoff()

    print(result)

if __name__ == "__main__":
    main()