*** Settings ***
Documentation     Suite 2: ISO 20022 Status Report (pacs.002) Processing Suite
Library           ../libraries/EnvInitializer.py
Library           ../libraries/DataSerializer.py

Suite Setup       Initialize Suite Environment    ${ENV_NAME}    ${PACS002_URL}    ${SCRIPT_TIMEOUT}    ISO

*** Variables ***
${TEMPLATE_PATH}    ${CURDIR}/../templates/pacs.002.001.10.xml
${XSD_PATH}         ${CURDIR}/../schemas/pacs.002.001.10.xsd
${EXCEL_PATH}       ${CURDIR}/../testdata/iso_pacs002_data.xlsx

*** Test Cases ***
TC_PAC002_01: Process ISO Status Report "TC_PAC002_01"
    [Documentation]    Executes ISO pacs.002 payment status check using active target environment variables.
    ${response_xml}=    Execute PACS002 Status Keyword "TC_PAC002_01"
    Should Contain      ${response_xml}    <TxSts>ACTC</TxSts>

*** Keywords ***
Execute PACS002 Status Keyword "${test_id}"
    ${excel_data}=      Read Excel Test Data           ${EXCEL_PATH}       ${test_id}
    ${full_payload}=    Combine Headers And Data       ${ISO_HEADER_DEFAULTS}    ${excel_data}
    ${request_xml}=     Process And Serialize Xml      ${TEMPLATE_PATH}    ${full_payload}

    Validate Xml Against Xsd    ${request_xml}    ${XSD_PATH}

    ${response}=        Send Swift Api Request         ${PACS002_URL}      ${request_xml}    ${AUTH_USER}    ${AUTH_PASS}    ${SCRIPT_TIMEOUT}
    RETURN              ${response}