Before looking on OWASP Top 10 i would first check the connections between different modules of the whole system. I would check the following.

-Connection between FastAPI back and database
-Connection between Web Front and Mobile App with API

I would make sure that:

-Access to database is protected using authentication and that ONLY the database administrator (one of the sw engineers) can directly access it and make modifications to it.
-Access to the API is protected by an authentication mechanism, for example, JSON web tokens. And that the corresponding users (clients, sw engineers, support employess and sales employeess) have the permissions they should have.
- That the input received from the front and sent to back is processed to prevent any form of code injection, specially SQL injection.

After that i would look into OWASP Top 10 for year 2021 (as stated in the question). The list is the following:

1. Broken Access Control
2. Cryptographic failures
3. Injection
4. Insecure Design
5. Security Miconfiguration
6. Vulnerable and Outdated components
7. Identification and Authentication failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery
