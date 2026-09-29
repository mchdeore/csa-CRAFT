"""
Demo user profiles — role, display name, available tools, system prompts.
Each profile gates which tools and pre-filled prompts a user sees.
"""

# Finance profile — CADRe ingestion + parametric comparison
FINANCE_PROFILE = {
    "role": "finance",
    "display_name": "Fred Money — Cost Analyst",
    "tools": [
        "ingest_document",
        "compare_missions",
        "query_data",
        "bar_chart",
        "scatter_chart",
        "radar_chart",
    ],
    "system_prompt": (
        "You are a cost analyst assistant for the Canadian Space Agency. "
        "You can see extracted CADRe fields from uploaded Part A documents, "
        "current weight configurations, and comparison results including "
        "top-5 rankings with weighted Euclidean distances and per-dimension "
        "z-score deltas. Answer questions using this numerical data. "
        "Never call compare_missions yourself — it is triggered by the UI button."
    ),
    "pre_filled_prompts": {
        "Compare to historical missions": "compare_missions",
        "Show raw comparison table": "Show me a table with raw values for all top-3 matches",
        "Explain the ranking": "Why is the top match closest? Which dimension differs most?",
    },
}

# Engineer profile — compliance checklist + version diff
ENGINEER_PROFILE = {
    "role": "engineer",
    "display_name": "Joe Motochar — Systems Engineer",
    "tools": [
        "ingest_document",
        "run_compliance",
        "version_diff",
        "query_data",
        "bar_chart",
        "parameter_margin",
    ],
    "system_prompt": (
        "You are a systems engineer assistant for the Canadian Space Agency. "
        "You can run compliance checks on uploaded CADRe Part A documents against "
        "5 hardcoded design rules, diff two versions of a document to detect changes, "
        "and visualize parameter margins. Answer questions about compliance results "
        "and version differences."
    ),
    "pre_filled_prompts": {
        "Run compliance check": "run_compliance",
        "Diff versions": "Upload two versions and run version_diff",
        "Show parameter margins": "Show me the parameter margin visualization",
    },
}

# Risk profile — risk register + cross-register comparison
RISK_PROFILE = {
    "role": "risk",
    "display_name": "Murphy Slipz — Risk Analyst",
    "tools": [
        "query_data",
    ],
    "system_prompt": (
        "You are a risk analyst assistant for the Canadian Space Agency. "
        "You can parse Part C risk registers, display top-10 risks with heatmaps "
        "and scatter plots, perform cross-register correlation analysis, "
        "and generate uncertainty tornado charts. Answer questions about risk data."
    ),
    "pre_filled_prompts": {},
}

# Map username to profile
PROFILES = {
    "fredmoney": FINANCE_PROFILE,
    "joemotochar": ENGINEER_PROFILE,
    "murphyslipz": RISK_PROFILE,
}

# Demo users with plain-text passwords (throwaway only)
DEMO_USERS = {
    "fredmoney": {"password": "1", "role": "finance", "division": "OCFO", "region": "HQ"},
    "joemotochar": {"password": "1", "role": "engineer", "division": "Engineering", "region": "HQ"},
    "murphyslipz": {"password": "1", "role": "risk", "division": "Risk", "region": "HQ"},
}