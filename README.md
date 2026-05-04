# 📧 Email Sender Bot (Python)

A powerful and simple **Email Automation Tool** built with Python that allows you to send personalized emails (with optional attachments) to multiple recipients using a CSV contact list.

---

## 🚀 Features

* 📬 Send emails to **all contacts** or a **single recipient**
* 📄 Read recipient details from a **CSV file**
* 🧾 Personalized email messages (using names)
* 📎 Optional file attachments
* 🔁 **Retry logic** for failed email attempts (3 tries)
* 📊 Logging system to track success and errors
* 🔐 Secure login using **environment variables**
* 🧠 Clean CLI menu for user interaction

---

## 🛠️ Tech Stack

* Python 3
* `smtplib` – Sending emails via SMTP
* `email` – Email formatting & attachments
* `csv` – Reading contact lists
* `logging` – Tracking activity and errors
* `os` – Environment variables & file handling
* `time` – Retry delays

---

## 📂 Project Structure

```
EmailBot/
│── EmailBot.py
│── contacts.csv
│── email_log.txt (auto-generated)
```

---

## 🔐 Setup Environment Variables (IMPORTANT)

Before running the script, set your email credentials:

### Windows (CMD)

```
set EMAIL_USER=your_email@gmail.com
set EMAIL_PASS=your_app_password
```

### Windows (PowerShell)

```
$env:EMAIL_USER="your_email@gmail.com"
$env:EMAIL_PASS="your_app_password"
```

### Linux / Mac

```
export EMAIL_USER=your_email@gmail.com
export EMAIL_PASS=your_app_password
```

⚠️ Use a **Gmail App Password**, NOT your real password.

---

## 📄 CSV Format

Create a `contacts.csv` file like this:

```
Name,Email
John Doe,john@example.com
Jane Doe,jane@example.com
```

---

## ▶️ Usage

Run the program:

```
python EmailBot.py
```

### Menu Options:

```
1. Email Everyone
2. Email One Person
3. Print Contact List
4. Exit
```

---

## 📎 Attachments

* You will be prompted to attach a file
* File must exist in the project directory
* If not found, the program continues without attachment

---

## 📊 Logging

All activity is logged in:

```
email_log.txt
```

Includes:

* ✅ Successful emails
* ❌ Errors and failures
* 🔁 Retry attempts

---

## 🔁 Retry Logic

* Each failed email is retried up to **3 times**
* Helps handle temporary network or SMTP issues

---

## 🔒 Security Notes

* Credentials are stored using **environment variables**
* Prevents exposing sensitive data in code
* Always use **App Passwords** for Gmail

---

## 💡 Use Cases

* Bulk email notifications
* Sending reports automatically
* Alerts and updates

---

## 👨‍💻 Author

**Emmanuel Joshua Deoduth**

---

