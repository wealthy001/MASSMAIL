import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QFileDialog, \
    QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QInputDialog


class EmailSenderGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.import_contacts_button = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mass Email Sender")

        # Main layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Top section - Contact Management
        self.contact_management_layout = QHBoxLayout()
        self.main_layout.addLayout(self.contact_management_layout)

        # Email list
        self.email_list = QTableWidget()
        self.email_list.setColumnCount(1)
        self.email_list.setHorizontalHeaderLabels(["Email Address"])
        self.contact_management_layout.addWidget(self.email_list)

        # Button for adding contacts
        self.add_contact_button = QPushButton("Add Contact")
        self.add_contact_button.clicked.connect(self.add_contact)
        self.contact_management_layout.addWidget(self.add_contact_button)

        # Button for importing contacts
        self.import_contacts_button = QPushButton("Import Contacts")
        self.import_contacts_button.clicked.connect(self.import_contacts)
        self.contact_management_layout.addWidget(self.import_contacts_button)

        # Middle section - Email Composition
        self.email_composition_layout = QVBoxLayout()
        self.main_layout.addLayout(self.email_composition_layout)

        # Email subject
        self.subject_label = QLabel("Subject:")
        self.subject_edit = QLineEdit()
        self.email_composition_layout.addWidget(self.subject_label)
        self.email_composition_layout.addWidget(self.subject_edit)

        # Email body
        self.body_label = QLabel("Body:")
        self.body_edit = QTextEdit()
        self.email_composition_layout.addWidget(self.body_label)
        self.email_composition_layout.addWidget(self.body_edit)

        # Bottom section - Send Email
        self.send_email_layout = QHBoxLayout()
        self.main_layout.addLayout(self.send_email_layout)

        # Send button
        self.send_button = QPushButton("Send Email")
        self.send_button.clicked.connect(self.send_email)  # Placeholder function for now
        self.send_email_layout.addWidget(self.send_button)

        self.show()

    def add_contact(self):
        # Placeholder function to add a contact to the list
        # You can implement a dialog to get email address
        email, _ = QInputDialog.getText(self, "Add Contact", "Enter Email Address:")
        if email:
            self.email_list.insertRow(self.email_list.rowCount())
            new_item = QTableWidgetItem(email)
            self.email_list.setItem(self.email_list.rowCount() - 1, 0, new_item)

    def import_contacts(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Import Contacts", "", "Text files (*.txt);;CSV files (*.csv)")
        if filename:
            try:
                with open(filename, 'r') as file:
                    for line in file:
                        emails = line.strip().split(',')  # Split line by commas and remove whitespace
                        for email in emails:
                            email = email.strip()  # Remove extra whitespace from each email
                            self.email_list.insertRow(self.email_list.rowCount())
                            new_item = QTableWidgetItem(email)
                            self.email_list.setItem(self.email_list.rowCount() - 1, 0, new_item)
            except FileNotFoundError:
                print("Error: File not found!")
            except Exception as e:
                print(f"Error importing contacts: {e}")

            # Implement logic to read emails from the file and add them to the list

    def send_email(self):
        # Placeholder function to send the email
        # You'll need to implement email sending logic here (SMTP or API)
        # This function should iterate through email list and send the email
        # using the subject and body from the UI
        print("Sending email...")

if __name__ == "__main__":
    app = QApplication([])
    window = EmailSenderGUI()
    sys.exit(app.exec_())

