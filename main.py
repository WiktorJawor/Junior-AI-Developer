import openai
from pyexpat.errors import messages


openai.api_key = API_KEY

def read_file(artykul):
    with open(artykul, 'r') as f:
        return f.read()

def generate_html(artykul):
    prompt =  (
        "Przekształć poniższy artykuł na strukturalny kod HTML. "
        "Dodaj odpowiednie tagi HTML do nagłówków, paragrafów, list itp. "
        "Użyj tagów <img> z src='image_placeholder.jpg' oraz alt z dokładnym opisem "
        "tam, gdzie można dodać grafikę. Dodaj podpisy pod grafikami. "
        "Nie używaj CSS ani JavaScript. Zwróć tylko kod HTML do wstawienia między <body> i </body>.\n\n"
        f"Artykuł:\n{artykul}"
    )

    try:
        answer = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{ "role": "user", "content"=prompt }],
            max_tokens=1500,
            temperature=0.7,
        )
        return answer.choices[0].message['content'].strip()
    except Exception as e:
        print(" Błąd podczas komunikacji z OpenAI {e}")
        return none