# Kredily HRMS — Mobile Automation Execution Report

## Environment
- Application: Kredily HRMS Android APK
- Automation framework: Appium
- Language: Python
- Device: Android phone connected through USB debugging

## Execution Summary

| Journey | Test | Result |
|---|---|---|
| 1 | Valid login | Passed — Home dashboard reached |
| 2 | Invalid login | Passed — "No account found with this email or mobile number." displayed |
| 3 | Dashboard validation | Inconclusive — screenshot and XML captured; automated assertion did not confirm the dashboard |
| 4 | Attendance screen validation | Partially executed — screenshot/XML captured after manual navigation |
| 5 | Back navigation from Attendance to Home | Passed — Home dashboard observed after Back |

## Evidence Files
- Journey 2: `journey2_invalid_login.png`, `journey2_result.xml`
- Journey 3: `journey3_dashboard.png`, `journey3_dashboard.xml`
- Journey 4: `journey4_attendance.png`, `journey4_attendance.xml`
- Journey 5: `journey5_before.png`, `journey5_after.png`, `journey5_before.xml`, `journey5_after.xml`
- Dashboard verification: `final_dashboard_verification.png`, `final_dashboard_verification.xml`

## Limitations
Journey 3 needs a stronger automated assertion. Journey 4 involved manual navigation and is not fully automated. Therefore, five fully automated journeys have not been confirmed.

## Conclusion
The valid-login and invalid-login automation scripts executed, and Back navigation was verified. Other journey evidence is retained with its execution limitations clearly documented.