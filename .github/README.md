# Email Header Processor

A Python script to process email headers by:
1. Removing sensitive/redundant headers (Received, Return-Path, DKIM, etc.)
2. Changing domain `.fin` to `.[RDNS]` in From field
3. Adding `[EID]` to Message-ID field

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/email-header-processor.git
cd email-header-processor

# Install dependencies
pip install -r requirements.txt
