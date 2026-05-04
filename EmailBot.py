# EmailBot.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
import time
import logging
import os


logging.basicConfig(
    filename='email_log.txt',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_contacts(file):
    with open(file, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        return list(csv_reader)


def attach_file(message, filename):
    try:
        with open(filename, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(filename)}')
        message.attach(part)
    except FileNotFoundError:   
        logging.error(f"ERROR: File '{filename}' not found.")
    except Exception as e:
        logging.error(f"ERROR: Failed to attach file '{filename}' -> {e}")


def send_email(sender_email, sender_password, receiver_email, subject, body, attachment):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    if attachment:
        attach_file(message, attachment)
        
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)      


def send_with_retry(sender_email, sender_password, receiver_email, subject, body, attachment):
    for attempt in range(3):
        try:
            if not sender_email or not sender_password:
                logging.error("Sender email or password not set.")
                return
            
            send_email(sender_email, sender_password, receiver_email, subject, body, attachment)
            logging.info(f"SUCCESS:Email sent to {receiver_email}")
            print(f"SUCCESS:Email sent to {receiver_email}")
            break
        except Exception as e:
            logging.error(f"ERROR ({attempt+1}): {receiver_email} -> {e}")
            print(f"ERROR ({attempt+1}): {receiver_email} -> {e}")

        time.sleep(1)   


def print_contacts(contacts):
    print("\nContacts List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['Name']}, Email: {contact['Email']}")


def get_attachment():
    choice = input("Do you want to attach a file? (y/n): ").strip().lower()

    if choice == 'y':
        filename = input("Enter the filename (with extension): ").strip()
        file_path = os.path.join(os.getcwd(), filename)
        
        if os.path.isfile(file_path):
            return file_path
        else:
            logging.error(f"ERROR: File '{filename}' not found.")
            print(f"ERROR: File '{filename}' not found.")
            print("Continuing without attachment...")
            return None
    
    return None



if __name__ == "__main__":


    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")            # "kyvt rnrk nfde lgpb"
    receiver_email = ""
    
    contacts = load_contacts('contacts.csv')
    
    while True:
        print("\n===== Email Bot Menu =====")
        print("1. Email Everyone")
        print("2. Email One Person")
        print("3. Print Contact List")
        print("4. Exit")

        choice = input("Select an option: ")

        # OPTION 1
        if choice == '1':
            attachment = get_attachment()

            for contact in contacts:
                name = contact['Name']
                receiver_email = contact['Email']
                subject = "Automated Response"
                body = f"Hello {name}\n\nThis is an Automated Email."

                send_with_retry(sender_email, sender_password,receiver_email, subject, body, attachment)

        # OPTION 2
        elif choice == '2':
            print_contacts(contacts)

            try:
                index = int(input("Enter contact index: "))
                contact = contacts[index-1]

                attachment = get_attachment()

                name = contact['Name']
                receiver_email = contact['Email']
                subject = "Automated Response"
                body = f"Hello {name}\n\nThis is an Automated Email."
                
                send_with_retry(sender_email, sender_password, receiver_email,subject, body, attachment)            
            
            except (IndexError, ValueError):
                print("Invalid index!")

        # OPTION 3
        elif choice == '3':
            print_contacts(contacts)

        # OPTION 4
        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid option. Try again.")

