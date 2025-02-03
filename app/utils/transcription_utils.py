import os
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()


def get_updated_transcription(transcription: str) -> str:
    prompt = ChatPromptTemplate(
        [
            SystemMessage(
                content="""You are an expert scriptwriter specializing in transforming raw transcripts into highly engaging, professional solo scripts. Your goal is to refine, structure, and enhance the provided transcript into a well-paced, compelling monologue that captivates the audience.

                Follow these key principles:
                - **Engagement**: Hook the audience from the start with a strong introduction.
                - **Clarity & Flow**: Organize ideas logically, ensuring smooth transitions between topics.
                - **Conciseness**: Remove unnecessary filler words while maintaining a conversational tone.
                - **Energy & Delivery**: Infuse energy, storytelling, and rhetorical techniques for a dynamic delivery.
                - **Call-to-Action (if needed)**: End with a strong conclusion that leaves an impact.

                Output a formatted script, structured for an effective solo delivery. Keep it natural, energetic, and professional."""
            ),
            HumanMessage(
                content=f"""
                Below is the raw transcription of the video. Please transform it into a **highly engaging, professional solo script** while ensuring clarity, structure, and energy in delivery.

                ---
                **Raw Transcription:**
                {transcription}
                ---

                Kindly refine the script, making it **concise, compelling, and audience-friendly** while maintaining the essence of the original content.
                """
            ),
        ]
    )
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, api_key=os.getenv("OPENAI_API_KEY"))
    response = model.invoke(prompt.format_messages())
    return response.content
