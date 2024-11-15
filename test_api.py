import openai


openai.api_key = "API_KEY"

try:
    models = openai.Model.list()
    print("Modele:")
    for model in models['data']:
        print(model['id'])
except Exception as e:
    print(f"error: {e}")
