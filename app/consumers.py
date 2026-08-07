"""Kafka consumers for patient-preferences-service.

One handler per subscribed topic. Real handlers write to this service's own
database and/or publish follow-up events; stub handlers just log + audit.
"""
from __future__ import annotations

import logging

from psycopg.types.json import Json

from healthcare_common.audit import emit_audit

log = logging.getLogger("patient-preferences-service.consumers")

TABLE = "patient_preferences"


def register(svc) -> None:
    bus = svc.bus
    db = svc.db
    clients = svc.clients

    @bus.on("patient.created")
    def _on_patient_created(envelope: dict) -> None:
        data = envelope.get("data") or {}
        try:
                    pid = data.get("id")
                    if not pid: return
                    db.execute(f"INSERT INTO {TABLE} (data) VALUES (%s)",
                               (Json({"patient_id": pid, "preferred_channel": "email"}),))
        except Exception as e:
            log.exception("patient-preferences-service/patient.created handler failed: %s", e)
        emit_audit(bus, action="consume.patient.created", actor="system:patient-preferences-service",
                   target=None, details={"envelope_id": envelope.get("id")})

