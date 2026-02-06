# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

**Note:** Please update this table based on your actual versioning strategy.

## Reporting a Vulnerability

The Basalt team takes security bugs seriously. We appreciate your efforts to responsibly disclose your findings and will make every effort to acknowledge your contributions.

### Where to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of the following methods:

1. **Email**: Send details to [oberhalsi](oberhalsi.dev@gmail.com) (and/or) [thealxlabs](thealxlabs@icloud.com)
2. **GitHub Security Advisory**: Use the [Security Advisory](https://github.com/oberhalsi/basalt/security/advisories/new) feature on GitHub

### What to Include

To help us better understand the nature and scope of the possible issue, please include as much of the following information as possible:

* **Type of issue** (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
* **Full paths of source file(s)** related to the manifestation of the issue
* **The location of the affected source code** (tag/branch/commit or direct URL)
* **Any special configuration required** to reproduce the issue
* **Step-by-step instructions to reproduce the issue**
* **Proof-of-concept or exploit code** (if possible)
* **Impact of the issue**, including how an attacker might exploit it

This information will help us triage your report more quickly.

### What to Expect

After you submit a report, we will:

1. **Acknowledge receipt** of your vulnerability report within 48 hours
2. **Send you regular updates** about our progress (at least every 5 business days)
3. **Provide an estimated timeline** for a fix and disclosure
4. **Notify you** when the vulnerability is fixed
5. **Publicly acknowledge your responsible disclosure**, if you wish (we will ask for your permission first)

### Response Timeline

* **Initial Response**: Within 48 hours
* **Status Update**: Within 5 business days
* **Fix Timeline**: Depends on severity and complexity
  - **Critical**: 7 days
  - **High**: 30 days
  - **Medium**: 90 days
  - **Low**: 120 days

### Disclosure Policy

* We will coordinate with you on the timing of public disclosure
* We prefer to fully remediate issues before any public disclosure
* We will credit you (with your permission) in our security advisories
* We follow a 90-day disclosure deadline from initial report (unless mutually agreed otherwise)

## Security Update Process

When we receive a security bug report, we will:

1. **Confirm the problem** and determine the affected versions
2. **Audit code** to find any similar problems
3. **Prepare fixes** for all supported releases
4. **Release new versions** as soon as possible
5. **Publish a security advisory** on GitHub

## Security-Related Configuration

### Best Practices for Users

When using Basalt, please follow these security best practices:

1. **Keep Basalt updated** to the latest version
2. **Review permissions** before running scripts
3. **Validate input** from untrusted sources
4. **Use official sources** for downloading Basalt
5. **Check file integrity** using provided checksums (when available)
6. **Run with least privileges** necessary
7. **Review code** from third-party sources before execution

### Secure Usage

* Avoid running Basalt with elevated privileges unless absolutely necessary
* Be cautious when executing scripts from unknown sources
* Review any scripts before execution
* Use version control to track changes to your configurations

## Known Security Limitations

* Basalt executes Bash code, which inherently has access to system resources
* Users are responsible for validating the security of scripts they run
* No sandboxing is provided by default

## Security Hardening

### Recommended Measures

1. **Input Validation**: Always validate and sanitize user inputs
2. **Principle of Least Privilege**: Run with minimal necessary permissions
3. **Code Review**: Review third-party code before execution
4. **Monitoring**: Monitor for unexpected behavior
5. **Updates**: Keep Basalt and all dependencies up to date

### Environment Security

* Use read-only file systems where possible
* Limit network access for scripts when appropriate
* Use separate user accounts for running untrusted scripts
* Enable system auditing and logging


## Preferred Languages

We prefer all communications to be in English.

## Security Hall of Fame

We would like to thank the following researchers for responsibly disclosing security issues:

* (No reports yet)

---

## Additional Resources

* [OWASP Top 10](https://owasp.org/www-project-top-ten/)
* [CWE Top 25](https://cwe.mitre.org/top25/)
* [Bash Security Best Practices](https://mywiki.wooledge.org/BashGuide/Practices)

## Contact

For any security-related questions or concerns, please contact:

* Security Email: [oberhalsi](oberhalsi.dev@gmail.com) (and/or) [thealxlabs](thealxlabs@icloud.com)
* Project Maintainer: [@oberhalsi](https://github.com/oberhalsi) and [@thealxlabs](https://github.com/thealxlabs)

---

**Last Updated**: February 2026

Thank you for helping keep Basalt and our users safe!
