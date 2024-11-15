import openai


openai.api_key = API_KEY

def read_file(artykul):
    try:
        with open(artykul, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Plik {artykul} nie został znaleziony.")
        return None

def generate_html(artykul):
    prompt = (
        "Przekształć poniższy artykuł na strukturalny kod HTML. "
        "Dodaj odpowiednie tagi HTML do nagłówków, paragrafów, list itp. "
        "Użyj tagów <img> z src='image_placeholder.jpg' oraz alt z dokładnym opisem "
        "tam, gdzie można dodać grafikę. Dodaj podpisy pod grafikami. "
        "Nie używaj CSS ani JavaScript. Zwróć tylko kod HTML do wstawienia między <body> i </body>.\n\n"
        f"Artykuł:\n{artykul}"
    )

    try:
        answer = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500,
            temperature=0.7,
        )
        return answer.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Błąd podczas komunikacji z OpenAI: {e}")
        return None

def save_html(plik, kod_html):
    with open(plik, 'w', encoding='utf-8') as f:
        f.write(kod_html)

def main():
    tekst = 'artykul.txt'
    html = 'artykul.html'

    # Odczytanie pliku tekstowego
    read_artykulu = read_file(tekst)
    if not read_artykulu:
        print("Nie ma nic do przetworzenia")
        return

    kod_html = generate_html(read_artykulu)
    if kod_html:
        save_html(html, kod_html)
        print(f"Wygenerowano kod HTML i zapisano w {html}")
    else:
        print("Nie udało się wygenerować kodu HTML")

if __name__ == '__main__':
    main()
