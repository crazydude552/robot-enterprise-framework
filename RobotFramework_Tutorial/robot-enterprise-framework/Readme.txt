.
├── config/
│   └── env_local.py             # Environment configurations, URLs, default headers & timeouts
├── libraries/
│   ├── DataSerializer.py        # Custom keywords: Excel reading, Jinja XML rendering & XSD validation
│   └── EnvInitializer.py        # Suite environment setup & global Robot variable initialization
├── schemas/                     # ISO 20022 XML Schema Definition (XSD) files
│   ├── camt.053.001.08.xsd      # Bank Statement schema
│   ├── pacs.002.001.10.xsd      # Payment Status Report schema
│   └── pacs.008.001.08.xsd      # Customer Credit Transfer schema
├── suites/                      # Robot Framework test suites
│   ├── suite_iso20022_camt053.robot
│   ├── suite_iso20022_pacs002.robot
│   └── suite_pacs008_fin.robot
├── templates/                   # Base XML templates with Jinja2 placeholders
│   ├── camt.053.001.08.xml
│   ├── pacs.002.001.10.xml
│   └── pacs.008.001.08.xml
├── testdata/                    # Excel spreadsheets containing test scenarios
│   ├── fin_pacs008_data.xlsx
│   ├── iso_camt053_data.xlsx
│   └── iso_pacs002_data.xlsx
├── .gitignore
├── main.py                      # FastAPI mock payment server simulating ISO 20022 endpoints
├── README.md                    # Project documentation & execution guide
└── requirements.txt             # Python dependencies (Robot Framework, FastAPI, lxml, pandas, etc.)


To run the API
uvicorn main:app --reload --port 8000

To Run the tests
robot --pythonpath . --variablefile config/env_local.py --outputdir results .\suites\

Then you can see
(.venv) PS C:\Users\pvmrm\Documents\workspace\RobotFramework_Tutorial\robot-enterprise-framework> robot --pythonpath . --variablefile config/env_local.py --outputdir results .\suites\
==============================================================================
Suites
==============================================================================
Suites.Suite Iso20022 Camt053 :: Suite 3: ISO 20022 Bank Statement (camt.05...
==============================================================================
TC_CAMT053_01: Validate Statement Balances and Booked Entries :: F... | PASS |
------------------------------------------------------------------------------
Suites.Suite Iso20022 Camt053 :: Suite 3: ISO 20022 Bank Statement... | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Suites.Suite Iso20022 Pacs002 :: Suite 2: ISO 20022 Status Report (pacs.002...
==============================================================================
TC_PAC002_01: Process ISO Status Report "TC_PAC002_01" :: Executes... | PASS |
------------------------------------------------------------------------------
Suites.Suite Iso20022 Pacs002 :: Suite 2: ISO 20022 Status Report ... | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Suites.Suite Pacs008 Fin :: Suite 1: SWIFT FIN pacs.008 Processing Suite
==============================================================================
TC_PAC008_01: Execute FIN pacs.008 Transfer for "TC_PAC008_01" :: ... | PASS |
------------------------------------------------------------------------------
Suites.Suite Pacs008 Fin :: Suite 1: SWIFT FIN pacs.008 Processing... | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Suites                                                                | PASS |
3 tests, 3 passed, 0 failed
==============================================================================
