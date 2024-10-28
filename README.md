# Azure Board Ticket Notifier with WhatsApp Alerts

This project monitors new tickets on an Azure Board and sends WhatsApp alerts to a specified contact whenever a new ticket is added. It is designed to streamline real-time notification for project management by integrating Selenium with WhatsApp Web.

## Features
- **Automated Ticket Monitoring**: Continuously monitors for new tickets on an Azure board.
- **Real-Time WhatsApp Alerts**: Sends WhatsApp notifications when new tickets are detected.
- **Customizable with Environment Variables**: Securely manage sensitive data using environment variables.

## Requirements
- Python 3.x
- Selenium WebDriver
- Google Chrome (for ChromeDriver compatibility)
- A WhatsApp account logged in on WhatsApp Web
- [dotenv](https://pypi.org/project/python-dotenv/) for handling environment variables

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/azure-whatsapp-notifier.git
   cd azure-whatsapp-notifier
