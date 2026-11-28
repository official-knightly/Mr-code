"""Lightweight Vercel gateway for the Mr Aegis OpenAI-compatible backend.

Set AEGIS_BACKEND_URL to the backend's OpenAI-compatible base URL, including /v1.
This gateway uses the official OpenAI Python SDK to communicate with that backend.
It does not call OpenAI-hosted models or load model weights inside Vercel.
"""
import os
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from openai import OpenAI

app = FastAPI(title="Mr Aegis API", version="1.0.0")


def get_backend_client() -> OpenAI:
    base_url = os.getenv("AEGIS_BACKEND_URL")
    if not base_url:
        raise HTTPException(
            status_code=503,
            detail="Mr Aegis model backend is not configured. Set AEGIS_BACKEND_URL to your OpenAI-compatible backend URL ending in /v1.",
        )
    return OpenAI(
        base_url=base_url.rstrip("/") + ("" if base_url.rstrip("/").endswith("/v1") else "/v1"),
        api_key=os.getenv("AEGIS_BACKEND_API_KEY", "aegis-local"),
        timeout=120.0,
    )


@app.get("/")
async def root():
    return {
        "name": "Mr Aegis",
        "status": "gateway_online",
        "backend_configured": bool(os.getenv("AEGIS_BACKEND_URL")),
        "sdk": "openai-python",
    }


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "backend_configured": bool(os.getenv("AEGIS_BACKEND_URL")),
    }


@app.get("/v1/models")
async def list_models():
    client = get_backend_client()
    try:
        result = client.models.list()
        return result.model_dump()
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Backend model listing failed: {exc}") from exc


@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    payload: dict[str, Any] = await request.json()
    client = get_backend_client()
    try:
        if payload.get("stream"):
            stream = client.chat.completions.create(**payload)

            def events():
                try:
                    for chunk in stream:
                        yield "data: " + chunk.model_dump_json(exclude_none=True) + "\n\n"
                    yield "data: [DONE]\n\n"
                except Exception as exc:
                    yield "data: " + __import__("json").dumps({"error": {"message": str(exc)}}) + "\n\n"

            return StreamingResponse(events(), media_type="text/event-stream")

        result = client.chat.completions.create(**payload)
        return result.model_dump()
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Mr Aegis backend request failed: {exc}") from exc
