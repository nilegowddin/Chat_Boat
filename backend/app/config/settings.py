import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_NAME = os.getenv("APP_NAME", "docchat")
    PORT = int(os.getenv("PORT", "8080"))

    FLOWISE_API_KEY = os.getenv("FLOWISE_API_KEY")

    FLOWISE_BASE_URL = os.getenv("FLOWISE_BASE_URL")

    FLOWISE_PREDICTION_URL = os.getenv("FLOWISE_PREDICTION_URL")

    FLOWISE_UPLOAD_URL = os.getenv("FLOWISE_UPLOAD_URL")

    FLOWISE_DOCUMENT_URL = os.getenv("FLOWISE_DOCUMENT_URL")

    FLOWISE_CHATFLOW_ID = os.getenv("FLOWISE_CHATFLOW_ID")

    FLOWISE_DOCUMENT_STORE_ID = os.getenv("FLOWISE_DOCUMENT_STORE_ID")

    FLOWISE_DOC_ID = os.getenv("FLOWISE_DOC_ID")

    DATABASE_URL = os.getenv("DATABASE_URL")


settings = Settings()