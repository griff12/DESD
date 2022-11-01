# %%
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import requests

# %%
# do, car, story
words = [
            'baby', 'one', 'boat', 
            'was', 'daddy', 'book', 'good', 'doll', 
            'girl', 'apple', 'they', 'some',
            'above', 'what', 'any', 'busy', 'night',
            'done', 'huge', 'ocean', 'station', 'could',
            'because', 'echo', 'couple', 'eager', 'together',
            'bought', 'delicious', 'neighbor', 'achieve', 'region',
            'malicious', 'bureau', 'similar', 'campaign', 'waltz',
            'prairie', 'gadget', 'facsimile', 'emphasize', 'prescription',
            'zealous', 'clique', 'atrocious', 'catastrophe', 'liquidate'
        ]
# %%
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# %%
for word in words:
    driver.get(f"https://www.google.com/search?q=how+to+pronounce+{word}")
    audio = WebDriverWait(driver, timeout=12).until(lambda x: x.find_element(By.TAG_NAME,"AUDIO"))
    src = requests.get(audio.get_attribute('src'))
    with open(f'audio_files/{word}.mp3', 'wb') as f:
        f.write(src.content)
    





# %%
