from itertools import chain
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

def main():
    load_dotenv()
    print("Hello from langchain-course-1!")
    #print(os.environ.get("OPEN_API_KEY"))
    information = """
    Elon Musk


    Musk in 2025
    Born	Elon Reeve Musk
    June 28, 1971 (age 54)
    Pretoria, South Africa
    Citizenship	
    South Africa
    Canada
    United States (since 2002)
    Education	University of Pennsylvania (BA, BS)
    Occupations	
    CEO and product architect of Tesla
    Founder, CEO, and chief engineer of SpaceX
    Founder and CEO of xAI
    Founder of the Boring Company and X Corp.
    Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
    President of the Musk Foundation
    Political party	Independent
    Spouses	
    Justine Wilson
    ​
    ​(m. 2000; div. 2008)​
    Talulah Riley
    ​
    ​(m. 2010; div. 2012)​
    ​
    ​(m. 2013; div. 2016)​
    Children	14,[a] including Vivian Wilson
    Parents	
    Errol Musk (father)
    Maye Musk (mother)
    Relatives	Musk family
    Awards	Full list
    Senior Advisor to the President
    In office
    January 20, 2025 – May 28, 2025
    President	Donald Trump
    Elon Musk's voice
    Duration: 1 minute and 13 seconds.1:13
    Musk on his departure from the Department of Government Efficiency
    Recorded May 30, 2025
    Signature

        
    This article is part of
    a series about
    Elon Musk
    Personal
    Companies
    Politics
    In the arts and media
    vte
    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and entrepreneur known for his leadership of Tesla, SpaceX, X, and xAI. Musk has been the wealthiest person in the world since 2021; as of December 2025, Forbes estimates his net worth to be around US$754 billion.

    Born into a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania in Philadelphia, United States, before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002.
    """


    summary_template = """
        Given the information {information} about a person, create:

        1. A short summary about the person.
        2. Two interesting facts about the person.
        """

    summary_prompt_template = PromptTemplate(
            input_variables=["information"],
            template=summary_template,
        )

    # Allow a dry-run mode for local testing when API access/quota is not available.
    dry_run = os.environ.get("DRY_RUN") == "1"
    if dry_run:
        prompt_text = summary_template.format(information=information)
        print("DRY RUN - prompt to send:\n", prompt_text)
        response = {
            "summary": "(DRY RUN) Short summary would appear here.",
            "facts": ["(DRY RUN) Fact 1", "(DRY RUN) Fact 2"],
        }
        print(response)
        return
    llm = OllamaLLM(
            model=os.environ.get("LLM_MODEL_NAME", "gemma3:270m"),
            temperature=0,
        )
    
    '''     # Alternatively, use OpenAI's Chat model
    llm = ChatOpenAI(
            model_name=os.environ.get("LLM_MODEL_NAME", "gpt-4o-mini"),
            temperature=0,
            api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("OPEN_API_KEY"),
        )
    '''
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response)



if __name__ == "__main__":
    main()
