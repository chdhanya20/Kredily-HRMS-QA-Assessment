# Kredily HRMS — QA Engineer Intern Assessment

## Project Overview
This project documents functional testing, observed issues, mobile automation attempts, API testing limitations, and AI-assisted QA for the Kredily HRMS Android application.

## Application Under Test
- **Application:** Kredily HRMS
- **Platform:** Android
- **Framework:** Python, Appium
- **API tool:** Postman (API endpoints were not provided)

## Project Structure
- `Manual_Testing/` — Functional test cases and execution results
- `Bug_Reports/` — Observed issues and investigation notes
- `Automation_Evidence/` — Automation screenshots and XML evidence
- `Execution_Reports/` — Automation execution reports
- `API_Testing/` — API test cases and endpoint-access limitation
- `AI_Assisted_QA/` — AI prompt, output, and validation report
- `test_login.py` — Login automation
- `test_invalid_login.py` — Invalid-login automation
- `test_dashboard.py` — Dashboard validation attempt
- `test_attendance.py` — Attendance-screen validation
- `test_journey5.py` — Back-navigation test

## Setup
1. Install Python and Node.js.
2. Install Appium and the UiAutomator2 driver.
3. Install the Python Appium client:
   `pip install Appium-Python-Client`
4. Enable USB debugging on an Android device and connect it to the computer.
5. Start the Appium server.
6. Update device capabilities in the scripts if required.

## Running Tests
Run individual scripts from the project directory, for example:

`python test_login.py`

`python test_invalid_login.py`

`python test_dashboard.py`

`python test_attendance.py`

`python test_journey5.py`

**Note:** Some scripts require the app to be in a particular starting state or require manual interaction. Review each script before execution.

## API Testing Limitation
The assignment supplied the APK but no API base URL, API documentation, Swagger specification, or Postman collection. Attempts to inspect the production app did not reveal identifiable Kredily endpoints. API scenarios are documented as blocked rather than reported as executed.

## AI-Assisted QA
The `AI_Assisted_QA/` folder documents the prompt used, AI-generated test-design assistance, and the application behaviors validated.

## Evidence and Reporting
Screenshots, XML hierarchy files, manual test results, and issue observations are included where available. Observed issues are distinguished from confirmed defects when their root cause has not been established.

## Final Status
The project records the testing completed and identifies the remaining limitations honestly. See the individual reports for execution status and supporting evidence.