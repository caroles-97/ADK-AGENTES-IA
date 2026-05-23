# from google.adk.agents.llm_agent import Agent

# root_agent = Agent(
#     model='gemini-2.5-flash',
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
# )

import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

root_agent = Agent(
    model='gemini-2.5-flash',
    name='portfolio_manager',
    description='Um agente especializado em gerenciar meu portfólio no GitHub.',
    instruction='Você é um gerente de portfólio do GitHub. Use o MCP do GitHub para listar repositórios, analisar código e ajudar a organizar e apresentar meu trabalho de forma profissional. Utilize as ferramentas para buscar informações e realizar ações no meu perfil.',
    tools=[
        McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="https://api.githubcopilot.com/mcp/",
                headers={
                    "Authorization": f"Bearer {GITHUB_TOKEN}"
                },
            ),
        )
    ],
)

