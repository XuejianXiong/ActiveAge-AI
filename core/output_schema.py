# core/output_schema.py

EXERCISE_OUTPUT_SCHEMA = """
When responding to exercise or mental activity results, ALWAYS format as:

Exercise Name:
- <name>

Why this is good:
- 1 short sentence

Steps:
- numbered, simple instructions (5–8 max steps)

Safety tips:
- 1–2 short bullets

Closing:
- one short encouraging sentence only
"""

WEB_OUTPUT_SCHEMA = """
When responding to web search results:

- Provide recommendations immediately. Do not use bridge phrases like "Based on my database" or "Searching the web now." Just give the advice.
- Keep language simple and easy to follow.
- Avoid using professional terms.
"""