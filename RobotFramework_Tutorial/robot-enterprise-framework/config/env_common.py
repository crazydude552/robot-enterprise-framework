# System-wide execution defaults
DEFAULT_TIMEOUT = 30
DEFAULT_RETRY_COUNT = 3

# SWIFT FIN Header Defaults
FIN_HEADER_DEFAULTS = {
    "ApplicationId": "F01",
    "ServiceId": "01",
    "LogicalTerminal": "BANKBE2AAXXX",
    "SessionNumber": "0000",
    "SequenceNumber": "000000",
    "MsgType": "pacs.008.001.08",
    "Priority": "N"
}

# ISO 20022 Common Message Headers
ISO_HEADER_DEFAULTS = {
    "BusinessService": "swift.cbprplus.01",
    "MarketInfrastructure": "TARGET2",
    "XmlNamespace": "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08",
    "Charset": "UTF-8"
}