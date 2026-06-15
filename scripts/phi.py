import requests, json, os, sys

def verify_compliance(risk_data):
    api_key = os.environ.get("FEATHERLESS_KEY")
    url = "https://api.featherless.ai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    system_prompt = (
        "Eres el Agente Phi del NONACORTEX. Evalúa el cumplimiento normativo del riesgo detectado. "
        "Veredictos: 'cumple', 'no cumple', 'revisión'. Responde en JSON: {'compliance_verdict': '...'}"
    )
    
    payload = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": risk_data}
        ],
        "temperature": 0.1,
        "response_format": {"type": "json_object"}
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    risk_input = sys.argv[1] if len(sys.argv) > 1 else ""
    print(verify_compliance(risk_input))