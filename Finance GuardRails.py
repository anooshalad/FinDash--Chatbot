# test3.py
from guardrails import Guard, OnFailAction
from guardrails.hub import RestrictToTopic, ToxicLanguage, ProfanityFree
from constants import FINANCE_TOPICS, GREETINGS
# In-memory storage for queries
#stored_queries = []

# Safety guard (ALWAYS enforced)
safety_guard = Guard().use_many(
    ToxicLanguage(threshold=0.1, on_fail=OnFailAction.EXCEPTION)
)

# Finance-only guard
finance_guard = Guard().use_many(
    RestrictToTopic(valid_topics=FINANCE_TOPICS, on_fail=OnFailAction.EXCEPTION)
)

def check_query(query: str):
    """Validate query using multiple guardrails."""

    # Block toxic language first
    try:
        safety_guard.validate(query)
    except Exception:
        return "Query is invalid"

    # Allow greetings
    if query.strip().lower() in GREETINGS:
        return "Query is valid"

    # Allow finance queries
    try:
        finance_guard.validate(query)
        return "Query is valid"
    except Exception:
        return "Query is invalid"

def process_query(query: str):
    """Validate and store the query, return a placeholder answer."""
    answer = check_query(query)
#stored_queries.append(query)
    return answer
