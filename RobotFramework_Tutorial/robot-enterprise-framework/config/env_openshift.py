from pathlib import Path

ENV_NAME = "LOCAL_MOCK"
# 'fastapi-service' will be the internal OpenShift DNS name for your app
BASE_URL = "http://fastapi-service:8000"

# Specific Endpoint Mappings
CAMT053_URL = f"{BASE_URL}/api/v2/iso/camt053"
PACS002_URL = f"{BASE_URL}/api/v2/iso/pacs002"
PACS008_URL = f"{BASE_URL}/api/v2/iso/pacs008"

# Default fallback
API_URL = PACS008_URL

# Auth & Timeouts
AUTH_USER = "mock_user"
AUTH_PASS = "mock_pass"
SCRIPT_TIMEOUT = 30

# Request Headers
ISO_HEADER_DEFAULTS = {
    "Content-Type": "application/xml",
    "Accept": "application/xml",
}
FIN_HEADER_DEFAULTS = {
    "Content-Type": "application/x-swift-fin",
    "Accept": "application/xml",
}