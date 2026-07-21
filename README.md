# RemixHub

**RemixHub** is a platform for discovering and creating authentic brand stories through AI‑driven content remixing.

## Overview
- **Backend**: FastAPI (Python 3.11) running in Docker.
- **AI/NLP**: TensorFlow & HuggingFace Transformers (distil‑BERT) for trend classification and content generation.
- **Data pipeline**: Kafka → Spark Structured Streaming → PostgreSQL for time‑series storage.
- **Auth & Ops**: OAuth2 for social logins, AWS Lambda for webhook handling, CloudWatch for monitoring.

## Core APIs
- `POST /trends` – retrieve behavior‑verified trends.
- `POST /generate` – generate brand‑compliant copy, hashtags and visual prompts.
- `POST /dispatch` – queue content for social platforms (Instagram, TikTok, LinkedIn).

## Quick Start
```bash
# Build and start services
docker compose up --build -d

# Test API (example)
curl -X POST http://localhost:8000/trends -H "Content-Type: application/json" -d '{"query": "sustainability"}'
```

Further implementation details (trend engine, NLP core, dispatcher) are TODOs in the code.
