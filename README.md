# LinkedIn Profile Summarizer

## Project Overview

This project automates the process of summarizing LinkedIn profiles. It uses Selenium to log in to LinkedIn, captures screenshots of the profile pages, extracts text from the screenshots using OCR (Optical Character Recognition) with EasyOCR, and processes the extracted text with OpenAI's language model to generate a refined summary.

---

## Features

- **Automates LinkedIn profile scraping**  
- **Captures profile page screenshots**  
- **Extracts text using OCR**  
- **Generates a concise summary using OpenAI's LLM**  
- **Stores cookies for persistent login to avoid repeated logins and reduce LinkedIn account blocking risk**

---

## Prerequisites

Before running this project, ensure you have the following installed and configured:

- **Python 3.11**
- **Selenium**
- **EasyOCR**
- **Pandas**
- **OpenAI library**
- A valid **LinkedIn account**
- An **OpenAI API Key**

---

## Setup Instructions

### 1. Configure LinkedIn Credentials  
Edit the `linkedin_scraper.py` file and add your LinkedIn email and password to the designated fields:  

```python
email = "your_email"
password = "your_password"
```

### 2. Cookie File for Persistent Login  
- When the script is run for the first time, it logs into LinkedIn using the provided credentials and creates a `cookies.pkl` file.  
- On subsequent runs, the script uses this cookie file for login, eliminating the need to log in repeatedly and reducing the likelihood of your LinkedIn account being blocked.

### 3. Add OpenAI API Key  
In the `llm.py` file, add your OpenAI API key:  

```python
openai.api_key = "your_openai_api_key"
```

### 4. Install Dependencies  
Run the following command to install the required Python libraries:  
```bash
pip install selenium easyocr pandas openai
```

---

## Usage

1. **Run the Script**  
   Start the summarization process by running the following command:  
   ```bash
   python main.py
   ```

2. **Provide LinkedIn Profile URLs**  
   - The script reads profile URLs from a CSV file specified in the `main.py` file.  
   - Each row of the CSV is processed sequentially, and the profiles are opened in the Selenium browser.

3. **Screenshots and Text Extraction**  
   - The script captures screenshots of the LinkedIn profiles.  
   - Text is extracted from these screenshots using EasyOCR.

4. **Generate Summaries**  
   - The extracted text is processed by OpenAI's language model, which generates a refined summary for each profile.  

---

## Important Notes

### LinkedIn Restrictions
- Scraping LinkedIn may lead to your account and/or IP being blocked.  
- To reduce the risk, the script:
  - Stores login cookies to avoid repeated logins.
  - Operates in a controlled manner to minimize suspicious activity.  
  - For added safety, consider using multiple LinkedIn accounts and proxies.  

### Libraries Used
- **Selenium**: Automates browser interactions and handles LinkedIn login.  
- **EasyOCR**: Extracts text from profile screenshots.  
- **OpenAI API**: Processes extracted text and generates summaries.  

---

## Disclaimer

Using this project to scrape LinkedIn profiles may violate LinkedIn's terms of service. Proceed with caution, and ensure compliance with any applicable legal and ethical guidelines.
