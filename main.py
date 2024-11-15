import openai

API_KEY = "api key OXIDO"

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
        "Zidentyfikuj miejsca, gdzie można dodać odpowiednie grafiki, i wstaw tam tagi <img> "
        "z atrybutem src='image_placeholder.jpg'. "
        "Dla każdego obrazka dodaj atrybut alt z dokładnym promptem do wygenerowania grafiki. "
        "Umieść podpisy pod grafikami używając tagu <figcaption>. "
        "Nie używaj CSS ani JavaScript. Zwróć tylko kod HTML do wstawienia między <body> i </body>.\n\n"
        f"Artykuł:\n{artykul}"
    )

    try:
        answer = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000,
            temperature=0.7,
        )
        return answer.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Błąd podczas komunikacji z OpenAI: {e}")
        return None

def save_html(plik, kod_html):
    with open(plik, 'w', encoding='utf-8') as f:
        f.write(kod_html)

def generate_template():
    template_html = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Podgląd Artykułu</title>
    <style>

    body {
        font-family: 'Roboto', sans-serif;
        background-color: #f4f7f6; /* Jasne tło */
        color: #333; /* Ciemny tekst dla dobrego kontrastu */
        margin: 0;
        padding: 0;
        line-height: 1.8;
        box-sizing: border-box;
    }


    .container {
        max-width: 1100px;
        margin: 40px auto;
        padding: 20px;
        background-color: #fff; /* Białe tło dla artykułu */
        border-radius: 8px; /* Zaokrąglone rogi */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Lekki cień */
    }


    h1 {
        font-size: 3rem;
        color: #2c3e50; /* Ciemniejszy odcień niebieskiego */
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
    }

    h2 {
        font-size: 2rem;
        color: #34495e;
        margin-top: 30px;
        margin-bottom: 10px;
        border-bottom: 2px solid #3498db; /* Nieco subtelna linia pod tytułem */
        padding-bottom: 5px;
    }

    h3 {
        font-size: 1.6rem;
        color: #16a085;
        margin-top: 20px;
        margin-bottom: 10px;
    }


    p {
        font-size: 1.1rem;
        margin-bottom: 15px;
        color: #555;
        line-height: 1.6;
        text-align: justify;
    }


    section {
        margin-bottom: 40px;
    }


    img {
        max-width: 100%;
        height: auto;
        border-radius: 8px; /* Zaokrąglone rogi dla obrazów */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Cień dla obrazów */
        margin: 20px 0;
        display: block;
    }


    figure {
        text-align: center;
        margin: 30px 0;
        background-color: #ecf0f1; /* Jasne tło dla obrazka */
        padding: 20px;
        border-radius: 8px;
    }

    figcaption {
        font-size: 1rem;
        font-style: italic;
        color: #7f8c8d;
        margin-top: 10px;
    }

    ul {
        padding-left: 20px;
        margin-bottom: 20px;
    }

    li {
        font-size: 1.1rem;
        color: #7f8c8d;
        margin-bottom: 10px;
    }

    a {
        text-decoration: none;
        color: #3498db; /* Kolor dla linków */
        font-weight: 600;
    }

    a:hover {
        color: #2980b9; /* Zmiana koloru po najechaniu */
    }

    footer {
        background-color: #2c3e50;
        color: white;
        text-align: center;
        padding: 20px;
        position: fixed;
        width: 100%;
        bottom: 0;
        font-size: 0.9rem;
    }

    @media (max-width: 768px) {
        .container {
            padding: 10px;
            margin: 10px;
        }

        h1 {
            font-size: 2.5rem;
        }

        h2 {
            font-size: 1.8rem;
        }

        h3 {
            font-size: 1.4rem;
        }

        p {
            font-size: 1rem;
        }
    }
</style>
</head>
<body>
    <!-- Wklej wygenerowany artykuł tutaj -->
</body>
</html>
"""
    save_html("szablon.html", template_html)
    print("Wygenerowano plik szablon.html")

def generate_preview(kod_html):
    preview_html = f"""
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Podgląd Artykułu</title>
    <style>

    body {{
        font-family: 'Roboto', sans-serif;
        background-color: #f4f7f6; /* Jasne tło */
        color: #333; /* Ciemny tekst dla dobrego kontrastu */
        margin: 0;
        padding: 0;
        line-height: 1.8;
        box-sizing: border-box;
    }}

    .container {{
        max-width: 1100px;
        margin: 40px auto;
        padding: 20px;
        background-color: #fff; /* Białe tło dla artykułu */
        border-radius: 8px; /* Zaokrąglone rogi */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Lekki cień */
    }}

    h1 {{
        font-size: 3rem;
        color: #2c3e50; /* Ciemniejszy odcień niebieskiego */
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
    }}

    h2 {{
        font-size: 2rem;
        color: #34495e;
        margin-top: 30px;
        margin-bottom: 10px;
        border-bottom: 2px solid #3498db; /* Nieco subtelna linia pod tytułem */
        padding-bottom: 5px;
    }}

    h3 {{
        font-size: 1.6rem;
        color: #16a085;
        margin-top: 20px;
        margin-bottom: 10px;
    }}

    p {{
        font-size: 1.1rem;
        margin-bottom: 15px;
        color: #555;
        line-height: 1.6;
        text-align: justify;
    }}

    section {{
        margin-bottom: 40px;
    }}

    img {{
        max-width: 100%;
        height: auto;
        border-radius: 8px; /* Zaokrąglone rogi dla obrazów */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Cień dla obrazów */
        margin: 20px 0;
        display: block;
    }}

    figure {{
        text-align: center;
        margin: 30px 0;
        background-color: #ecf0f1; /* Jasne tło dla obrazka */
        padding: 20px;
        border-radius: 8px;
    }}

    figcaption {{
        font-size: 1rem;
        font-style: italic;
        color: #7f8c8d;
        margin-top: 10px;
    }}

    ul {{
        padding-left: 20px;
        margin-bottom: 20px;
    }}

    li {{
        font-size: 1.1rem;
        color: #7f8c8d;
        margin-bottom: 10px;
    }}

    a {{
        text-decoration: none;
        color: #3498db; /* Kolor dla linków */
        font-weight: 600;
    }}

    a:hover {{
        color: #2980b9; /* Zmiana koloru po najechaniu */
    }}

    footer {{
        background-color: #2c3e50;
        color: white;
        text-align: center;
        padding: 20px;
        position: fixed;
        width: 100%;
        bottom: 0;
        font-size: 0.9rem;
    }}

    @media (max-width: 768px) {{
        .container {{
            padding: 10px;
            margin: 10px;
        }}

        h1 {{
            font-size: 2.5rem;
        }}

        h2 {{
            font-size: 1.8rem;
        }}

        h3 {{
            font-size: 1.4rem;
        }}

        p {{
            font-size: 1rem;
        }}
    }}
    </style>
</head>
<body>
{kod_html}
</body>
</html>
"""
    save_html("podglad.html", preview_html)
    print("Wygenerowano plik podglad.html")


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

        generate_template()

        generate_preview(kod_html)
    else:
        print("Nie udało się wygenerować kodu HTML")

if __name__ == '__main__':
    main()
