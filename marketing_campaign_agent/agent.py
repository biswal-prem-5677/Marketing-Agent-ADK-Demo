import os

try:
    from dotenv import load_dotenv
    load_dotenv()

    MODEL_NAME = os.environ.get("GOOGLE_GENAI_MODEL", "gemini-2.5-flash")
except ImportError:
    print("Warning: python-dotenv not installed. Ensure API key is set")
    MODEL_NAME = "gemini-2.5-flash"

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search



from marketing_campaign_agent.instructions import (
    MARKET_RESEARCH_INSTRUCTION,
    CAMPAIGN_ORCHESTRATOR_INSTRUCTION
)

market_research_agent = LlmAgent(
    name="MarketResearcher",
    model=MODEL_NAME,
    instruction=MARKET_RESEARCH_INSTRUCTION,
    tools=[google_search],
    output_key="market_research_summary"
)

campaign_orchestrator = SequentialAgent(
    name="MarketingcCampaignAssistant",
    description=CAMPAIGN_ORCHESTRATOR_INSTRUCTION,
    sub_agents=[
        market_research_agent
    ]
)

root_agent = campaign_orchestrator