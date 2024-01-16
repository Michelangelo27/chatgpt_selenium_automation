from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from handler.chatgpt_selenium_automation import ChatGPTAutomation
import time

options = Options()
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#                          options=options)
chrome_driver_path = r"/Users/allisoncasasola/medical-ai/chromedriver-mac-arm64/chromedriver"
chrome_path = r'"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"'
chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)

questions = ["What are the benefits of exercise?", "What happens to someone who lays in bed 24/7?", "What are the benefits of eating well?"]

# for question in questions:
#     prompt = question
#     chatgpt.send_prompt_to_chatgpt(prompt)
#     response = chatgpt.return_last_response()
#     print(response)

# Define a prompt and send it to chatGPT
prompt = "What are the benefits of exercise?"
chatgpt.send_prompt_to_chatgpt(prompt)

user_input = input(
    "Enter 'y' to retrieve response: ").lower()

# Retrieve the last response from chatGPT
response = chatgpt.return_last_response()
print(response)