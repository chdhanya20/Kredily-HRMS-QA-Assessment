# API Testing — Limitation Report

The assignment provided the Kredily HRMS Android APK but did not provide an API base URL, API documentation, Swagger specification, or Postman collection.

An attempt was made to inspect network activity using Android Studio and Android Debug Bridge logs. Android Studio could not inspect the production app through Network Inspector, and the captured logs did not expose identifiable Kredily API endpoints.

Therefore, API testing could not be executed reliably. The relevant test cases have been documented as blocked pending access to API endpoints or documentation.

**Evidence:** APK inspection attempt and captured Android logs.

**Required to proceed:** API base URL, endpoint documentation, or a company-provided Postman collection.