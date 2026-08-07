# patient-preferences-service

patient-preferences-service — domain: patients

- **Port:** 8103
- **Language:** Python 3.11 + Flask
- **Database:** `patients` (Postgres, table `patient_preferences`)
- **Event bus:** Kafka

## API

| Method    | Path                       |
|-----------|----------------------------|
| GET       | `/api/patient_preferences/`          |
| POST      | `/api/patient_preferences/`          |
| GET       | `/api/patient_preferences/<id>`      |
| PUT/PATCH | `/api/patient_preferences/<id>`      |
| DELETE    | `/api/patient_preferences/<id>`      |
| GET       | `/health`                  |
| GET       | `/ready`                   |

## Events

**Publishes:** (none)
**Subscribes:** patient.created

## HTTP peer dependencies

- `patients-service`
- `audit-log-service`

## Local dev

```bash
pip install -e ../../libs/py-healthcare-common
pip install -r requirements.txt
cp .env.example .env
(cd ../../infra && docker compose up -d postgres kafka kafka-init)
python -m app.main
```

## Tests

```bash
pytest
```
