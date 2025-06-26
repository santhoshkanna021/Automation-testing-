# 🐞 Bug Report Template

## 🆔 Bug ID:
BUG-001

## 📄 Title:
Transfer fails for zero amount

## 📝 Description:
When a user attempts to transfer an amount of 0, the system does not show a validation error and does nothing.

## 🎯 Steps to Reproduce:
1. Login to the application.
2. Navigate to Transfer Funds.
3. Enter 0 as the amount.
4. Click Submit.

## ✅ Expected Result:
A validation message should be displayed saying "Amount must be greater than 0."

## ❌ Actual Result:
No validation message appears, and the form stays on the same page.

## 📌 Severity:
Medium

## 🧪 Environment:
- Browser: Chrome 114
- OS: Windows 10