from openai import OpenAI, AsyncOpenAI
from config import Config
from logs import logger
from site_generation.exceptions import FailedTitleGeneration


def title_prompt(topic: str, style: str, num: int, retry: int = 3) -> str:
    prompt = f"""
    You are an expert in creating SEO-optimized titles that are engaging, unique, and relevant to the given topic and style.
    Your task is to generate NUM_TITLES distinct titles for a website based on the following input:

        Topic: [e.g., "Healthy Recipes"]

        Style: [e.g., "Informative and casual"]

        Number of Titles: [ e.g., "10"]

    Each title should:

    Be SEO-friendly (include relevant keywords naturally).

    Be unique and distinct from each other, ensuring a variety of phrasing, structure, and word choices.

    Be directly related to the given topic while reflecting the tone and style specified.

    Be optimized for user engagement and click-through rate (CTR).

    Avoid any repetition or overlap of ideas between the titles.

    Please output the results in JSON format as a list of strings.

    Each title should be a unique string within the list.

    Example Input:

    Topic: "Travel Tips for Solo Travelers"

    Style: "Inspirational and engaging"

    Number of Titles: 5

    Expected Output:

    [
    "Solo Travel Made Easy: Top Tips Every Adventurer Needs to Know",
    "How to Embrace the Freedom of Solo Travel and Explore the World",
    "Master Solo Travel with These Essential Tips for Beginners",
    "Unlock the Secrets to Safe and Fun Solo Adventures",
    "Solo Traveler’s Guide: Expert Tips to Make Your Journey Unforgettable"
    ]
    
    Generate titles:
        Topic: {topic}
        Style: {style}
        Number of Titles: {num}
    """
    return prompt


# 1. Initialize the OpenAI client
client = AsyncOpenAI(
    base_url=Config.LLM_PROVIDER_URL,
    api_key=Config.LLM_API_KEY,
)


async def generate_titles(topic: str, style: str, num: int, retry: int = 3) -> list[str]:
    """
        Generate titles for given topic
    """
    prompt = title_prompt(topic, style, num)
    for trial in range(retry):
        try:
            # What if LLM generate less sites? 
            # CORNER CASE
            completion = await client.chat.completions.create(
                model=Config.LLM_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                response_format=list[str]
            )
            content = completion.choices[0].message.content.parsed
            logger.debug('Titles are generated successfully')
            return content
        except Exception as e:
            logger.warning('Something went wrong during title generation')
            logger.exception(e)
    # If titles were not generated, raise exception
    raise FailedTitleGeneration()
