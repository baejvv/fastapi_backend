import subprocess

def chat_with_llama3(prompt: str, model: str = "llama3") -> str:
    try:
        response = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True, text=True
        )
        text = response.stdout.strip()
        return text
    except Exception as e:
        return f"에러 발생: {str(e)}"