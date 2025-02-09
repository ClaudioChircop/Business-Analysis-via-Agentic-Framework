from textwrap import dedent
from crewai import Task 

class ReviewAnalyzerTasks():
    def scrape_company_review_task(self, agent, website_url, total_pages=10): #url, company name 
        return Task(

            description=dedent(f"""\
                Collect review data from the specified company URL by scraping the amount of pages specified. Use web scraping techniques to extract information 
                such as review content, ratings, reviewer name, and review date from the provided web pages.
                Ensure data integrity and avoid collecting duplicate or incomplete reviews.
            
                Input:
                - Company review page URL to scrape.
                Website URL: {website_url}
                Amount of pages to scrape: {total_pages}
            
                Requirements:
                - Scrape reviews and related metadata (e.g., ratings, and date), from the first {total_pages} pages.
                - Handle pagination to ensure all reviews are collected.
                - Avoid triggering anti-scraping mechanisms or violating website terms of service.
                - You must pass at least 50 reviews to the next agent.
                
                """), 
            
            expected_output=dedent("""\ 
                The ouput must contain all the review data from all the specified number of pages,
                structured in a way that is understandable for future agents. This must include review date, rating and review content of all reviews scraped from the specified number of pages.
                All content must be given to the next agent.
              
                """),
                agent=agent,
                )
    

    def review_sentiment_task(self, agent):
        return Task( 
            
            description=dedent("""\
                analyze_company_reviews_sentiment_task:

                Analyze the sentiment of the enire reviews provided. The analysis should classify reviews 
                into positive, neutral, and negative sentiments. Identify potential recurring issues or complaints 
                mentioned in the reviews that may indicate areas for the company to improve.

                Input: Scraped review data, containing review date, rating and review content.
                
                Requirements:
                - Perform sentiment analysis for each review's content (positive, neutral, or negative).
                - Aggregate sentiment results for each company.
                - Identify patterns or recurring issues mentioned in negative reviews (e.g., "poor customer service," "high prices").
                - Summarize the findings for each company, highlighting key strengths and areas for improvement.
                - You must classify the sentiment of at least 50 reviews, all 50 classified reviews must be passed to the next agent"""),

            expected_output=dedent("""\
                
                Your output must contain a sentiment analysis results for the company. 
                The sentiment analysis of each review shall include a sentiment summary, 
                positive reviews count, neutral reviews count, negative reviews count, common issues. 
                Also include a summary of each review including the sentiment: positive/neutral/negative.
                You must analyze all reviews provided throughout the ten pages.
                
                """),
                agent=agent,
                )           


    def strategic_directive_task(self, agent):
        return Task(

            description=dedent("""\
                
                generate_company_strategic_plan_task:
                Using the sentiment analysis data provided, create a detailed strategic plan for each company. The plan 
                should address key areas of improvement based on identified issues in the reviews and leverage strengths 
                highlighted in positive feedback. The strategic plan should provide a structured approach with clear 
                objectives, action steps, and potential impact analysis.

                Input: Sentiment analysis results for the company reviews.

                Requirements:
                - Analyze the sentiment summary and recurring issues for each company.
                - For recurring issues, propose strategic initiatives with clear objectives and actionable steps to address them.
                - Highlight strengths from positive feedback and suggest strategies to enhance and capitalize on them.
                - Provide a projected impact analysis for each proposed initiative.
                - Structure the strategic plan into sections such as "Key Issues," "Strengths," "Strategic Objectives," "Action Steps," and "Projected Impact."
                """),

            expected_output=dedent("""\
                Produce a detailed strategic plan for the company by following these steps:

                ### Strategic Plan Components:

                1. **Key Issues**  
                - **Definition**: Identify the most pressing challenges or problems the company faces. These could include operational inefficiencies, customer dissatisfaction, or competitive weaknesses.  
                - **Examples**:  
                    - "Delayed customer service"  
                    - "High product pricing"  
                    - "Lack of innovation in product offerings"  
                    - "Low employee engagement and retention"  

                2. **Strengths**  
                - **Definition**: Highlight the company's strengths or positive attributes that can be leveraged to address challenges.  
                - **Examples**:  
                    - "Excellent product quality"  
                    - "High customer loyalty"  
                    - "Strong brand recognition in the market"  
                    - "Robust financial position for investment"  

                ---

                ### Strategic Objectives:

                Break down the plan into clear and actionable objectives that tackle the identified issues or capitalize on the strengths:

                1. **Objective Description**  
                - Clearly outline each goal, e.g., "Improve customer support response times" or "Expand market share in key regions."  

                2. **Action Steps**  
                - Provide a step-by-step plan to achieve each objective.  
                - Examples:  
                    - "Hire additional support staff."  
                    - "Implement a ticketing system for streamlined issue tracking."  
                    - "Launch a marketing campaign to improve brand awareness."  
                    - "Develop a mentorship program to boost employee engagement."

                3. **Projected Impact**  
                - Estimate the potential benefits or outcomes of these actions.  
                - Examples:  
                    - "Reduce average response time by 50% within six months."  
                    - "Achieve 15% growth in market share within one year."  
                    - "Increase employee retention rate by 20% in the next quarter."  

                ---

                ### Additional Enhancements:

                To create a more robust strategic plan, consider including the following elements:

                1. **Stakeholder Alignment**  
                - Identify key stakeholders (e.g., customers, employees, investors) and ensure their priorities align with the plan.  
                - Action: Host workshops or surveys to gather stakeholder insights.  

                2. **Timeline and Milestones**  
                - Define clear timelines and checkpoints to measure progress.  
                - Examples:  
                    - "Complete hiring process for support staff by Q1."  
                    - "Launch marketing campaign by Q2."

                3. **Resource Allocation**  
                - Detail the budget, personnel, and tools required for each objective.  
                - Examples:  
                    - "Allocate $100,000 for technology upgrades."  
                    - "Dedicate a team of five members to oversee the project."

                4. **Risk Assessment**  
                - Anticipate potential challenges or roadblocks and propose mitigation strategies.  
                - Examples:  
                    - "If additional staff cannot be hired on time, consider outsourcing customer support temporarily."  
                    - "If marketing campaign response is low, pivot to digital-first strategies."

                5. **Metrics and KPIs**  
                - Define measurable indicators to track the success of the plan.  
                - Examples:  
                    - "Customer satisfaction score (CSAT) improvement by 10%."  
                    - "Increase in website traffic by 25%."

                By addressing key issues, leveraging strengths, structuring objectives with actionable steps, incorporating measurable outcomes, and proactively managing resources and risks, this strategic plan ensures comprehensive and meaningful improvements for the company.

                Utilize the file_writer_tool to generate a txt document, containing the entire output of this task.                                     
                """),
                agent=agent,
                )          
                               
                               
                