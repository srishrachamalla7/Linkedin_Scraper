from openai import OpenAI

class LLM:
        
    
    def LLM_ANSWER(self,data,tone='professional'):
        client = OpenAI(api_key = "")#Add your openai key
        System_prompt = f"""
            You are an AI assistant designed to generate optimized LinkedIn profile summaries based on a user's job experience, skills, and accomplishments. Your goal is to create a personalized, well-written summary that captures the user's professional achievements, while considering their selected tone and industry-specific keywords in {tone} nicely.

            Profile Summary Format:

            Start with a brief, attention-grabbing introduction.
            Highlight the user's key skills, experience, and accomplishments.
            Emphasize what makes the user unique in their field.
            Maintain a clear, professional tone unless specified otherwise.
            Tone Options:

            Professional: Use formal, industry-specific language.
            Casual: Use approachable, friendly language.
            Motivational: Use inspiring, energetic language.
            Keyword Optimization:

            Ensure the summary includes relevant keywords for SEO within LinkedIn based on the user's industry and career goals.
            Output Constraints:

            Limit the summary to a maximum of 250 words.
            Ensure readability and coherence.
            Example Input: User-provided data:

            Job Experience: [Details here]
            Skills: [Details here]
            Accomplishments: [Details here]
            Selected Tone: [Professional, Casual, Motivational]
            Industry: [Industry here]
            Example Output: Generate a LinkedIn profile summary tailored to the user's input
        """
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": System_prompt},
                {"role": "user", "content": data},
            ],
            model="gpt-4o-mini",
        )

        # response = response['choices'][0]['message']['content']
        print(response.choices[0].message.content)

        return response.choices[0].message.content

if __name__ == '__main__':
    llm = LLM()
    data = "Job Experience: [Details here]\nSkills: [Details here]\nAccomplishments: [Details here]\nSelected Tone: [Professional, Casual, Motivational]\nIndustry: [Industry here]"
    res = llm.LLM_ANSWER(data)
    print(res)