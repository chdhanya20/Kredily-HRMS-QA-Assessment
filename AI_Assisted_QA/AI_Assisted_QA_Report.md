# AI-Assisted QA Report — Kredily HRMS

## 1. Objective
To use an AI tool to assist with test-case design, mobile automation validation, and analysis of observed application behavior.

## 2. AI Tool Used
ChatGPT

## 3. Prompt Used
"I am testing the Kredily HRMS Android application as part of a QA Engineer Intern assignment. Help me design positive, negative, and edge test cases for login, dashboard, attendance, and approvals. Help me analyze the observed results and identify potential defects without assuming that unverified behavior is a bug."

## 4. AI-Generated Output
AI assistance was used to:
- Design positive and negative login test scenarios.
- Identify validation points for the dashboard.
- Plan attendance and approval workflow tests.
- Structure bug reports with reproduction steps, expected results, actual results, severity, and evidence.
- Help investigate how to identify API endpoints without inventing undocumented APIs.

## 5. What I Changed or Validated
- Executed login and invalid-login scenarios against the actual application.
- Observed the invalid-login message: "No account found with this email or mobile number."
- Checked the dashboard and attendance workflow using the installed APK.
- Observed an approval processing message: "Attendance log not found."
- Attempted Android Studio Network Inspector inspection, but the production APK was not available as a debuggable process.
- Reviewed captured Android logs; no identifiable Kredily API endpoints were found.

AI suggestions were treated as guidance. Application behavior was checked against actual observations, and unverified suggestions were not reported as confirmed defects.

## 6. Limitations
The API base URL and documentation were not supplied. API test cases are documented separately as blocked; no API execution results are claimed.

## 7. Conclusion
AI assisted test design, evidence analysis, and documentation. Actual application observations were distinguished from planned tests and unverified assumptions.