import json
import subprocess

LLM_MODEL = "qwen2.5:14b"

# تحميل قاعدة البيانات
with open("resources.json", "r", encoding="utf-8") as f:
    RESOURCES = json.load(f)

def detect_query_language(query: str) -> str:
    if any("\u0600" <= ch <= "\u06FF" for ch in query):
        return "ar"
    return "en"

def ask_llm_intent(query: str):
    """استدعاء نموذج Ollama لتصنيف الاستعلام"""
    result = subprocess.run(
        ["ollama", "run", LLM_MODEL, query],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def extract_resource_key(llm_response: str):
    """يبسط استخراج المفتاح من رد النموذج"""
    for res in RESOURCES:
        if res["title_en"].lower() in llm_response.lower() or res["title_ar"] in llm_response:
            return res
    return None

def build_response(resource, lang="en"):
    if not resource:
        return "❌ Resource not found. حاول صياغة السؤال بشكل أوضح." if lang == "ar" else "❌ Resource not found. Please rephrase your query."

    if lang == "ar":
        return f"""
### {resource['title_ar']}
{resource['description_ar']}

**الخطوات:**
{resource['steps_ar']}

**المتطلبات:**
{resource['requirements_ar']}

[رابط رسمي]({resource['official_link']})
"""
    else:
        return f"""
### {resource['title_en']}
{resource['description_en']}

**Steps:**
{resource['steps_en']}

**Requirements:**
{resource['requirements_en']}

[Official Link]({resource['official_link']})
"""

def process_query(query: str, lang: str):
    llm_response = ask_llm_intent(query)
    resource = extract_resource_key(llm_response)
    return build_response(resource, "ar" if lang == "العربية" else "en")
