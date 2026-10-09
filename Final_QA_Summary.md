# Kredily HRMS — Final QA Summary

## 1. Project Overview
Functional testing and mobile automation were performed on the Kredily HRMS Android application as part of the QA Engineer Intern assignment.

## 2. Functional Testing
- Test cases were documented for login, dashboard, attendance, approvals, and location-related behavior.
- Positive and negative login scenarios were executed.
- Empty email and empty password validation messages were observed.
- Some test cases remain unexecuted or partially verified; refer to `Manual_Testing/Manual_Test_Cases.md`.

## 3. Bug Reporting
- Observed issues were documented in `Bug_Reports/Bug_Reports.md`.
- Observations include approval-processing failures, unavailable attendance details, and location-related restrictions.
- Potential issues are marked provisional where backend, permissions, or environment limitations may explain the behavior.
- Historical observations require retesting before being treated as confirmed defects.

## 4. Mobile Automation
- Valid login automation reached the Home dashboard.
- Invalid login automation displayed an appropriate account-not-found message.
- Dashboard validation evidence was captured, but its automated assertion was inconclusive.
- Attendance validation involved manual navigation.
- Back navigation from Attendance to Home was verified.
- See `Automation_Execution_Report.md` and the Python scripts for details.

## 5. API Testing
The assignment supplied the Android APK but no API base URL or documentation. Attempts to inspect network activity did not reveal identifiable Kredily API endpoints. Relevant API test cases were documented as blocked; no API execution results are claimed.

## 6. AI-Assisted QA
ChatGPT assisted with test-case design, analysis of observed application behavior, and report preparation. Actual results were checked against application observations, and unverified suggestions were not treated as confirmed defects.

## 7. Overall Conclusion
The project includes functional test documentation, observed issue reports, mobile automation scripts, screenshots, XML evidence, API limitations, AI-assisted QA documentation, and setup instructions.

The work is submitted with execution limitations stated transparently. Additional testing and API access would be needed to complete all scenarios and confirm potential defects.