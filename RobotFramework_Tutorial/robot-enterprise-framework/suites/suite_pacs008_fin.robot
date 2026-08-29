*** Settings ***
Documentation     Suite 1: SWIFT FIN pacs.008 Processing Suite
Library           ../libraries/EnvInitializer.py
Library           ../libraries/DataSerializer.py

Suite Setup       Initialize Suite Environment    ${ENV_NAME}    ${PACS008_URL}    ${SCRIPT_TIMEOUT}    FIN

*** Variables ***
${TEMPLATE_PATH}    ${CURDIR}/../templates/pacs.008.001.08.xml
${XSD_PATH}         ${CURDIR}/../schemas/pacs.008.001.08.xsd
${EXCEL_PATH}       ${CURDIR}/../testdata/fin_pacs008_data.xlsx

*** Test Cases ***
TC_PAC008_01: Execute FIN pacs.008 Transfer for "TC_PAC008_01"
    [Documentation]    Executes FIN pacs.008 payment using active target environment variables.
    ${response_xml}=    Execute FIN Payment Keyword "TC_PAC008_01"
    Should Contain      ${response_xml}    <TxSts>ACTC</TxSts>

*** Keywords ***
Execute FIN Payment Keyword "${test_id}"
    ${excel_data}=      Read Excel Test Data           ${EXCEL_PATH}       ${test_id}
    ${full_payload}=    Combine Headers And Data       ${FIN_HEADER_DEFAULTS}    ${excel_data}
    ${request_xml}=     Process And Serialize Xml      ${TEMPLATE_PATH}    ${full_payload}

    Validate Xml Against Xsd    ${request_xml}    ${XSD_PATH}

    # FIX: Point explicitly to ${PACS008_URL} instead of generic ${API_URL}
    ${response}=        Send Swift Api Request         ${PACS008_URL}      ${request_xml}    ${AUTH_USER}    ${AUTH_PASS}    ${SCRIPT_TIMEOUT}
    RETURN              ${response}