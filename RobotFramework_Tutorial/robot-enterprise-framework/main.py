from pathlib import Path
from fastapi import FastAPI, Response, status
import pandas as pd

app = FastAPI(title="ISO 20022 Enterprise Mock Server", version="2.0.0")

TESTDATA_DIR = Path("testdata")


def read_testdata(filename: str, testcase_id: str = "TC_01") -> dict:
  """Reads specific testcase row from Excel file with fallback."""
  filepath = TESTDATA_DIR / filename
  if filepath.exists():
    try:
      df = pd.read_excel(filepath)
      if not df.empty:
        if "TestCaseId" in df.columns:
          match = df[df["TestCaseId"] == testcase_id]
          if not match.empty:
            return match.iloc[0].to_dict()
        return df.iloc[0].to_dict()
    except Exception as e:
      print(f"[WARN] Failed to read {filepath}: {e}")
  return {}


# ------------------------------------------------------------------
# 1. CAMT.053 - Bank Statement Endpoint
# ------------------------------------------------------------------
@app.api_route(
    "/api/v2/iso/camt053", methods=["GET", "POST"], status_code=status.HTTP_200_OK
)
def handle_camt053():
  d = read_testdata("iso_camt053_data.xlsx", "TC_CAMT053_01")

  opening_bal = f"{float(d.get('OpeningBalance', 100000.00)):.2f}"
  closing_bal = f"{float(d.get('ClosingBalance', 125000.00)):.2f}"
  entry_amt = f"{float(d.get('EntryAmount', 25000.00)):.2f}"
  entry_type = str(d.get("EntryType", "CRDT"))
  iban = str(d.get("AccountIBAN", "BE68001234567890"))

  xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.053.001.08">
    <BkToCstmrStmt>
        <GrpHdr>
            <MsgId>{d.get('MsgId', 'MOCK-CAMT053-2026-001')}</MsgId>
            <CreDtTm>2026-08-28T12:00:00Z</CreDtTm>
        </GrpHdr>
        <Stmt>
            <Id>STMT-2026-08-28-001</Id>
            <ElctrncSeqNb>1</ElctrncSeqNb>
            <Acct>
                <Id>
                    <Othr>
                        <Id>{iban}</Id>
                    </Othr>
                </Id>
            </Acct>
            <Bal>
                <Tp><CdOrPrtry><Cd>OPBD</Cd></CdOrPrtry></Tp>
                <Amt Ccy="EUR">{opening_bal}</Amt>
                <CdtDbtInd>CRDT</CdtDbtInd>
                <Dt><Dt>2026-08-28</Dt></Dt>
            </Bal>
            <Bal>
                <Tp><CdOrPrtry><Cd>CLBD</Cd></CdOrPrtry></Tp>
                <Amt Ccy="EUR">{closing_bal}</Amt>
                <CdtDbtInd>CRDT</CdtDbtInd>
                <Dt><Dt>2026-08-28</Dt></Dt>
            </Bal>
            <Ntry>
                <Amt Ccy="EUR">{entry_amt}</Amt>
                <CdtDbtInd>{entry_type}</CdtDbtInd>
                <Sts><Cd>BOOK</Cd></Sts>
                <BookgDt><Dt>2026-08-28</Dt></BookgDt>
            </Ntry>
        </Stmt>
    </BkToCstmrStmt>
</Document>"""
  return Response(content=xml, media_type="application/xml")


# ------------------------------------------------------------------
# 2. PACS.002 - Payment Status Report Endpoint
# ------------------------------------------------------------------
@app.api_route(
    "/api/v2/iso/pacs002", methods=["GET", "POST"], status_code=status.HTTP_200_OK
)
def handle_pacs002():
  d = read_testdata("iso_pacs002_data.xlsx", "TC_PAC002_01")
  # Default fallback set to ACTC
  tx_status = str(d.get("TxSts", "ACTC"))

  xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.002.001.10">
    <FIToFIPmtStsRpt>
        <GrpHdr>
            <MsgId>{d.get('MsgId', 'MOCK-PACS002-2026-001')}</MsgId>
            <CreDtTm>2026-08-28T12:00:00Z</CreDtTm>
        </GrpHdr>
        <TxInfAndSts>
            <OrgnlEndToEndId>{d.get('OrgnlEndToEndId', 'E2E-12345')}</OrgnlEndToEndId>
            <TxSts>{tx_status}</TxSts>
        </TxInfAndSts>
    </FIToFIPmtStsRpt>
</Document>"""
  return Response(content=xml, media_type="application/xml")


# ------------------------------------------------------------------
# 3. PACS.008 - Credit Transfer Endpoint
# ------------------------------------------------------------------
@app.api_route(
    "/api/v2/iso/pacs008", methods=["GET", "POST"], status_code=status.HTTP_200_OK
)
def handle_pacs008():
  d = read_testdata("fin_pacs008_data.xlsx", "TC_PAC008_01")
  amt = f"{float(d.get('Amount', 25000.00)):.2f}"
  tx_status = str(d.get("TxSts", "ACTC"))

  xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08">
    <FIToFICstmrCdtTrf>
        <GrpHdr>
            <MsgId>{d.get('MsgId', 'MOCK-PACS008-2026-001')}</MsgId>
            <NbOfTxs>1</NbOfTxs>
        </GrpHdr>
        <CdtTrfTxInf>
            <PmtId><EndToEndId>{d.get('EndToEndId', 'E2E-12345')}</EndToEndId></PmtId>
            <IntrBkSttlmAmt Ccy="{d.get('Ccy', 'EUR')}">{amt}</IntrBkSttlmAmt>
            <TxSts>{tx_status}</TxSts>
            <Dbtr><Nm>{d.get('DebtorName', 'Debtor Corp')}</Nm></Dbtr>
            <Cdtr><Nm>{d.get('CreditorName', 'Creditor Ltd')}</Nm></Cdtr>
        </CdtTrfTxInf>
    </FIToFICstmrCdtTrf>
</Document>"""
  return Response(content=xml, media_type="application/xml")