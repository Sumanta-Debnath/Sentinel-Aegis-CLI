from google import genai

client = genai.Client(
    vertexai=True,
    project="sentinel-aegis-cli",
    location="us-central1",
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Write a short story about a robot learning to dance.",
)
print(response.text)