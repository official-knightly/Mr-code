"""Vercel ASGI entrypoint for the existing Mr Aegis API."""
from fastapi import FastAPI
from openai_api import app as aegis_api

app = FastAPI()
app.mount("/", aegis_api)
