# Phishing URL Detection System

## Project Overview
A Python-based application that identifies potentially suspicious and phishing URLs using rule-based detection techniques.

The system analyzes different URL characteristics and calculates a risk score to classify a URL as either Safe or Phishing.

## Features
- HTTPS Security Checking
- URL Length Analysis
- IP Address Detection
- Special Character (`@`) Detection
- Multiple Dot Detection
- Hyphen Detection in Domain
- Suspicious Keyword Detection
- Fake Brand Usage Detection
- Suspicious TLD Detection
- Risk Score-Based Classification

## Technologies Used
- Python
- Regular Expressions (`re`)
- URL Parsing (`urllib.parse`)

## How It Works
1. The user enters a URL.
2. The application analyzes the URL using predefined security rules.
3. Suspicious characteristics increase the risk score.
4. The final score determines whether the URL is classified as Safe or Phishing.

## How to Run

1. Install Python.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run:

```bash
python main.py
```

5. Enter a URL to check its classification.
6. Type `exit` to close the application.

## Output
The application displays one of two results:

- Safe URL
- Phishing URL

## Project Objective
To understand URL-based phishing detection and implement basic security analysis using Python.