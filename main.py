import pandas as pd
from LLM import LLM
from linkedin_scraper import LinkedInScraper
from ocr import OCR
import time
import os

# Initialize classes
scraper = LinkedInScraper()
llm = LLM()
ocr = OCR()

def main(urls, tone):
    # Create an empty DataFrame to store OCR text and user info
    # Check if the CSV file exists and load it
    csv_file = 'linkedin_profiles.csv'
    if os.path.exists(csv_file):
        data_df = pd.read_csv(csv_file)
        processed_users = data_df['User'].tolist()  # Get list of already processed users
    else:
        processed_users = []
        # data_df = pd.DataFrame(columns=['User', 'OCR_Text'])
        data_df = pd.DataFrame(columns=['User', 'OCR_Text', 'Summary'])

    try:
        scraper.login_linkedin()
        time.sleep(15)

        for url in urls:
            user = scraper.extract_name(url)

        # Skip already processed users
            if user in processed_users:
                print(f"{user} has already been processed. Skipping...")
                continue

            try:
                # Extract name from the URL
                scraper.driver.get(url)
                time.sleep(6)

                folder1 = scraper.take_screenshot_scroll('linkedin_profile', user)
                scraper.driver.get(url + '/details/skills')
                time.sleep(7)

                folder2 = scraper.take_screenshot_scroll('linkedin_skills', user)

                if folder1 == folder2:
                    print("Screenshot folders are the same")
                else:
                    print("Screenshot folders are different")

                # Extract text from images using OCR
                ocr_text = ocr.folder_reader(folder1)

                # Create a new DataFrame for the new row
                new_row = pd.DataFrame({'User': [user], 'OCR_Text': [ocr_text], 'Summary': [llm.LLM_ANSWER(ocr_text, tone)]})

                # Concatenate the new row to the existing DataFrame
                data_df = pd.concat([data_df, new_row], ignore_index=True)

                # Long interval after processing each user
                time.sleep(5)  # Adjust to your desired interval (30 seconds here)

            except Exception as e:
                print(f"An error occurred for {user}: {e}")

    finally:
        scraper.driver.quit()  # Quit the driver after all users are processed

    # Use LLM to generate summaries for each user
    # data_df['Summary'] = data_df['OCR_Text'].apply(lambda x: llm.LLM_ANSWER(x, tone))

    # Save the complete DataFrame to a CSV file
    save_to_csv(data_df)
    

def save_to_csv(df):
    """Saves the DataFrame to a CSV file."""
    csv_file = 'linkedin_profiles.csv'

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    print(f"Data saved to {csv_file}")

if __name__ == '__main__':
    # df = pd.read_excel("connections.xlsx")
    df = pd.read_csv("connections.csv")
    urls = df['URLS'].to_list()
    # urls = [
    #     'https://www.linkedin.com/in/vsantosh4u/',
    #     'https://www.linkedin.com/in/srishrachamalla/'
    #     # 'https://www.linkedin.com/in/another-user/'
    #     # Add more LinkedIn URLs as needed
    # ]
    tone = 'professional'
    main(urls, tone)