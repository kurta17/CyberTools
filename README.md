# CyberTools - A Cybersecurity Portfolio and Toolkit

**CyberTools** is a web platform built using Django, PostgreSQL, and Tailwind CSS, designed to showcase practical cybersecurity skills through interactive tools. This project serves as a portfolio for aspiring cybersecurity professionals, demonstrating a wide range of security techniques and solutions.

## Features:
- **Password Strength Checker**: Evaluate the strength of user passwords and provide feedback to improve security.
- **Network Scanner**: Identify active devices on a given network range through automated ping scans.
- **Encryption/Decryption Tool**: Encrypt and decrypt messages using symmetric encryption algorithms (AES).
- **Cybersecurity Blog**: Share insights, best practices, and write-ups on security tools and projects.

This project highlights key areas of cybersecurity such as password security, network scanning, and data encryption. It is designed to demonstrate practical experience and provide potential employers with an overview of technical skills.

## Technologies Used:
- **Backend**: Django
- **Frontend**: HTML, Tailwind CSS
- **Database**: PostgreSQL
- **Encryption Library**: Cryptography (Fernet AES)

## How to Run Locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cybertools.git
2. Install dependencies:
   pip install -r requirements.txt

3. Set up the PostgreSQL database:

    Update your database settings in settings.py.
    Run migrations:
        python manage.py migrate

4. Run the development server:
    python manage.py runserver

5. Access the site at http://127.0.0.1:8000.