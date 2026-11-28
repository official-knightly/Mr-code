#!/bin/sh
set -eu

CHECKPOINT="${AEGIS_CHECKPOINT_PATH:-Aegis/Aegis-7B-Chat}"
HOST="${AEGIS_SERVER_HOST:-0.0.0.0}"
PORT="${AEGIS_SERVER_PORT:-8000}"

set -- python openai_api.py \
  --checkpoint-path "$CHECKPOINT" \
  --server-name "$HOST" \
  --server-port "$PORT"

if [ "${AEGIS_CPU_ONLY:-1}" = "1" ]; then
  set -- "$@" --cpu-only
fi

if [ -n "${AEGIS_API_AUTH:-}" ]; then
  set -- "$@" --api-auth "$AEGIS_API_AUTH"
fi

exec "$@"
