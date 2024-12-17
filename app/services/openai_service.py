from openai import OpenAI


client = OpenAI()


async def analyze_code(
    repo_contents: str, assignment_description: str, candidate_level: str
) -> dict:
    prompt = f"""
    Analyze the following repository contents for a {candidate_level} level assignment:

    Assignment Description:
    {assignment_description}

    Repository Contents:
    {repo_contents}

    Provide:
    - Found files
    - Downsides/Comments
    - Rating
    - Conclusion
    """

    try:
        completion = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )

        return completion.choices[0].message
    except Exception as e:
        raise RuntimeError(f"OpenAI API error: {e}")
