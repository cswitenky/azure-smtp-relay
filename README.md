# Azure SMTP Relay

This is a simple SMTP relay server written in Python 3 that can be used to relay emails to Azure Communication Services. It is based on the [aiosmtpd](https://pypi.org/project/aiosmtpd/).

## Purpose

The purpose of this SMTP relay server is to allow you to send emails from your application to Azure Communication Services via SMTP protocol. This is useful if you want to send emails from your self-hosted applications or if you want to send emails from your local development environment.

This is **NOT** intended to be exposed to the public internet. There is no authentication or authorization implemented in this SMTP relay server. It is intended to be used in a local development environment or in a private network.

## Prerequisites

Before using this SMTP relay server, you need to have an Azure Communication Services resource for email. You can create one by following the [documentation](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/create-email-communication-resource).

## Installation

### Python 3.8+

First, add your connection string to `config.json`.

```json
{
  "connection_string": "your-connection-string-here"
}
```

Then run the server with `python3 src/smtp_server.py`.

### Docker

Run this command: `docker run -p 1025:1025 -e CONNECTION_STRING="your-connection-string-here" ghcr.io/cswitenky/azure-smtp-relay:latest`.

### docker-compose

Create a `docker-compose.yml` and copy and paste the following:

```yaml
version: "3"

services:
  azure-smtp-relay:
    container_name: azure-smtp-relay
    image: ghcr.io/cswitenky/azure-smtp-relay:latest
    ports:
      - 1025:1025/tcp
    environment:
      - CONNECTION_STRING="your-connection-string-here"
```

Then run `docker-compose up -d`.

## Usage

To use `azure-smtp-relay`, you need to configure your application to use your new SMTP relay server.

Generally, you will need to set the IP address to the computer running `azure-smtp-relay` serrver and the port to 1025. No authentication is required to interact with the SMTP relay server so you can turn off corresponding security/authentication settings in your application. Then set your from address to the email address you want to send the email from. Usually, that is your donotreply@domain.com address you set up in your Azure Communication Services resource.
