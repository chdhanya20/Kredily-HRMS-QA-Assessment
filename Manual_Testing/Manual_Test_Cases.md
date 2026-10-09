# Kredily HRMS — Manual & Functional Test Cases

**Application:** Kredily HRMS Android APK  
**Test type:** Functional, negative, and edge-case testing

| ID | Test Scenario | Expected Result | Actual Result / Status |
|---|---|---|---|
| TC01 | Login with valid credentials | User reaches Home dashboard | Passed — dashboard reached |
| TC02 | Login with an unregistered email | Error message is displayed | Passed — "No account found with this email or mobile number." |
| TC03 | Verify Home dashboard | Dashboard content is displayed | Observed — dashboard opened; complete automated assertion inconclusive |
| TC04 | Open Attendance | Attendance information is displayed | Executed — attendance screen inspected |
| TC05 | Check Clock Out before a location fix | Clear location guidance is displayed | Observed — "Waiting for a location fix" message |
| TC06 | Check Clock Out after a successful clock-out | Attendance status updates | Passed — Clocked out status observed |
| TC07 | Open an attendance day detail | Day details are displayed when accessible | Observed — "Day detail unavailable" message |
| TC08 | Approve an attendance-related request | Request is processed successfully | Failed — "Attendance log not found" message |
| TC09 | Reject an attendance-related request | Request is rejected with the supplied reason | Failed — "Attendance log not found" message |
| TC10 | Verify approval processing feedback | Success or failure is clearly communicated | Observed — processing error displayed |
| TC11 | Verify login with an empty email | App should prevent proceeding and display validation | Passed — "Enter your email or mobile number" displayed |
| TC12 | Verify login with an empty password | App should prevent login and display password validation | Passed — "Enter your password" displayed |
| TC13 | Verify login with an incorrect password | App should reject login and display an appropriate error | Passed — "Incorrect password. 4 attempts remaining" displayed |
| TC14 | Verify repeated invalid login attempts | App should handle repeated failures safely and communicate any attempt limit | Not executed — One incorrect-password attempt was tested; repeated attempts were not tested to avoid risking account lockout |
| TC15 | Verify dashboard after navigation back | Previous screen is displayed correctly | Passed — Home dashboard observed after Back |
| TC16 | Verify attendance screen navigation | Attendance screen opens correctly | Executed — screenshot and XML captured |
| TC17 | Verify attendance records in organization view | Relevant attendance record is displayed | Observed — QA Assessment attendance record displayed |
| TC18 | Verify approval request details | Selected request should display employee, request type, date, and comment | Passed — Request details and action buttons are visible in the Approvals list |
| TC19 | Verify behavior when location is unavailable | Clock action should be prevented safely and clear guidance should be displayed | Observed — Waiting for a location fix — move closer to your workplace and try again  appeared Controlled location-unavailable test not completed. |
| TC20 | Verify recovery after a workflow error | User can navigate back and continue | Partially verified — Back returned to Home |

## Notes
- "Passed" is used only for observed successful behavior.
- "Failed" indicates the observed workflow did not achieve its expected result; root cause is not confirmed.
- "Observed" records behavior without claiming the behavior is necessarily a product defect.
- "Not executed" means the scenario still needs to be tested.
- Screenshots and XML files should be attached as evidence where available.