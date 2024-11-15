import openai

try:
    models = openai.Model.list()
    print("Modele:")
    for model in models['data']:
        print(model['id'])
except Exception as e:
    print(f"error: {e}")
