import requests, json, os, sys

def analyze_risk(document_text):
    api_key = os.environ.get("FEATHERLESS_KEY")
    url = "https://api.featherless.ai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    system_prompt = (
        "Eres el Agente Alfa del NONACORTEX. Analiza riesgos en flujos de alta responsabilidad. "
        "Responde estrictamente en JSON: {'risk_flag': 'descripción'}"
    )
    
    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.3",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": document_text}
        ],
        "temperature": 0.2,
        "response_format": {"type": "json_object"}
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    input_text = sys.argv[1] if len(sys.argv) > 1 else ""
    print(analyze_risk(input_text))