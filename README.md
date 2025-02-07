# Secure Encryption Service

A web application built using Flask that provides secure encryption and decryption services. Users can input a message, choose an encryption algorithm, and perform encryption or decryption operations securely.

## Features
- **Secure Algorithms**: Support for AES and other encryption standards.
- **User-Friendly Interface**: Intuitive web-based UI for easy interaction.
- **Data Security**: No private keys or credentials are stored.

## Technology Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Encryption**: Python cryptography libraries

## Installation

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  
    # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   flask run
   ```

5. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage
1. Enter a message in the "Message" field (up to 500 characters).
2. Select an encryption algorithm (e.g., AES-256).
3. Choose an operation (Encrypt/Decrypt).
4. Click on "Process Request" to see the result.

## Directory Structure
```
project-root/
├── app.py               # Main Flask application
├── templates/           # HTML templates
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Security Notice
- All operations are performed securely.
- Never share private keys or sensitive credentials.

## Dependencies
- Flask
- cryptography 

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

## License
This project is licensed under the MIT License. 

## Contact
For questions or support, contact [zakariatabati55@gmail.com].

