# ResearchMind

> A multi-agent AI research assistant that searches the web, extracts source content, writes a structured report, and evaluates the final result.

ResearchMind is a Streamlit application built with LangChain and Mistral AI. It coordinates specialized agents and chains to turn a research topic into a polished, reviewable report.

## Project Highlights

- Multi-agent research workflow with separate search and reading agents
- Mistral AI integration through LangChain
- Tavily-powered web search for current information
- URL scraping and content extraction with Requests and BeautifulSoup
- Dedicated writer chain for structured report generation
- Critic chain that scores the report and identifies improvements
- Streamlit interface with progress states, expandable raw results, report rendering, and Markdown download
- Local `.env` support and Streamlit Cloud secrets support

## Architecture

```mermaid
flowchart LR
    A[Research topic] --> B[Search Agent]
    B -->|Tavily results| C[Reader Agent]
    C -->|Scraped source content| D[Writer Chain]
    D -->|Draft report| E[Critic Chain]
    E --> F[Report and feedback]
```

### Workflow

1. The Search Agent uses Tavily to find recent and relevant sources.
2. The Reader Agent selects a useful URL and extracts its content.
3. The Writer Chain combines the search results and scraped content into a structured report.
4. The Critic Chain reviews the report, assigns a score, and provides actionable feedback.

## Technology Stack

- **Frontend:** Streamlit
- **LLM orchestration:** LangChain and LangGraph agent runtime
- **Language model:** Mistral AI via `ChatMistralAI`
- **Web search:** Tavily API
- **Web extraction:** Requests, BeautifulSoup, and lxml
- **Configuration:** Python dotenv and Streamlit secrets
- **Language:** Python

## Project Structure

```text
.
├── app.py            # Streamlit user interface and pipeline execution
├── agents.py         # Mistral model, agents, writer chain, and critic chain
├── config.py         # Shared local and Streamlit Cloud secret loading
├── pipeline.py       # Command-line pipeline runner
├── tools.py          # Tavily search and URL scraping tools
├── requirements.txt  # Python dependencies
├── .gitignore        # Excludes local secrets and environment files
└── .env              # Local-only API keys; never commit this file
```

## Security

- Never commit `.env` or API keys to Git.
- Rotate any API key that has been exposed publicly.
- Use Streamlit Cloud Secrets for deployed credentials.
- Keep `.venv`, caches, and generated files out of version control.


## Future Improvements

- Add source citation validation and duplicate-source filtering
- Add retry handling and user-facing error messages for API failures
- Persist research history and export reports as PDF
- Add automated tests for tools, chains, and pipeline state transitions
- Support configurable models and search depth from the UI

## License

This project is intended as a portfolio and learning project. Add a license before distributing it publicly.
