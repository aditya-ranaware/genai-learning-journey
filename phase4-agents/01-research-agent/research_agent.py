from ddgs import DDGS
import ollama

def search_web(query, max_results=3):
    """This is our TOOL — the agent will call this to get real, current info."""
    print(f"🔍 Searching web for: {query}")
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append(f"Title: {r['title']}\nSnippet: {r['body']}\nURL: {r['href']}")
    return "\n\n".join(results)

def research_agent(topic):
    print(f"\n🤖 Starting research on: {topic}\n")
    
    # ACT: Call the search tool
    search_results = search_web(topic, max_results=4)
    
    print("📄 Retrieved search results, now generating report...\n")
    
    # THINK + generate final answer: LLM reads results, writes a report
    system_prompt = """You are a research assistant. You will be given web search results on a topic.
Your job: read them and write a clear, well-organized summary report.
Rules:
- Only use information from the search results given to you
- Structure your report as: Title, then 3-4 key findings as bullet points, then a short conclusion
- Mention it's based on recent web search results, not your own training knowledge
"""

    response = ollama.generate(
        model='llama3.2',
        system=system_prompt,
        prompt=f"Topic: {topic}\n\nSearch Results:\n{search_results}\n\nWrite the report now."
    )
    
    return response['response']

if __name__ == "__main__":
    topic = "latest AI trends 2026"
    report = research_agent(topic)
    print("\n" + "="*60)
    print(f"  📊 RESEARCH REPORT: {topic.upper()}")
    print("="*60 + "\n")
    print(report)
    print("\n" + "="*60)