*** Settings ***
Documentation     Suite 3: ISO 20022 Bank Statement (camt.053) Processing Suite
Library           ../libraries/EnvInitializer.py
Library           ../libraries/DataSerializer.py

Suite Setup       Initialize Suite Environment    ${ENV_NAME}    ${CAMT053_URL}    ${SCRIPT_TIMEOUT}    ISO

*** Variables ***
${TEMPLATE_PATH}    ${CURDIR}/../templates/camt.053.001.08.xml
${XSD_PATH}         ${CURDIR}/../schemas/camt.053.001.08.xsd
${EXCEL_PATH}       ${CURDIR}/../testdata/iso_camt053_data.xlsx

*** Test Cases ***
TC_CAMT053_01: Validate Statement Balances and Booked Entries
    [Documentation]    Fetches camt.053 statement details using active target environment variables.
    ${response_xml}=    Fetch CAMT053 Statement Keyword "TC_CAMT053_01"
    Should Contain      ${response_xml}    <Amt Ccy="EUR">100000.00</Amt>
    Should Contain      ${response_xml}    <Amt Ccy="EUR">125000.00</Amt>

*** Keywords ***
Fetch CAMT053 Statement Keyword "${test_id}"
    ${excel_data}=      Read Excel Test Data           ${EXCEL_PATH}       ${test_id}
    ${full_payload}=    Combine Headers And Data       ${ISO_HEADER_DEFAULTS}    ${excel_data}
    ${request_xml}=     Process And Serialize Xml      ${TEMPLATE_PATH}    ${full_payload}

    Validate Xml Against Xsd    ${request_xml}    ${XSD_PATH}

    ${response}=        Send Swift Api Request         ${CAMT053_URL}      ${request_xml}    ${AUTH_USER}    ${AUTH_PASS}    ${SCRIPT_TIMEOUT}
    RETURN              ${response}