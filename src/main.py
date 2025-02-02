from settings import get_settings

if __name__ == "__main__": # This only runs when main.py is executed directly
    settings = get_settings()
    print(f"Base Directory: {settings.BASE_DIR}")
    print(f"OpenAI API Key: {settings.openai_api_key}")

# Without the check
# settings = get_settings()  # This would run every time the file is imported
