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