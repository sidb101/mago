from selenium import webdriver
import time  
from selenium.webdriver.common.keys import Keys  
import pandas as pd

print("sample test case started")  
driver = webdriver.Chrome(r'/home/ibllsosiddharth/codebase/quicker/MWL/chromedriver')  
#driver=webdriver.firefox()  
#driver=webdriver.ie()  
#maximize the window size  
driver.maximize_window()  


################# TEST 1
#navigate to the entry url  
# driver.get("https://gre.magoosh.com/flashcards/vocabulary/high-frequency-words/vindicate")  

# track = dict()
# worddict = {'word':[], 'meaning':[], 'example':[]}

# while True:
#     elem = driver.find_element_by_partial_link_text("Click to see meaning")
#     elem.click()

#     driver.implicitly_wait(2)

#     w = driver.find_element_by_class_name("flashcard-word").text
#     m = driver.find_element_by_class_name("flashcard-text").text
#     eg = driver.find_element_by_class_name("flashcard-example").text

#     if track.get(w, 0) > 2 or len(track)>50:
#         break
#     else:
#         track[w] = track.get(w,0) + 1

#     worddict['word'] += [w]
#     worddict['meaning'] += [m]
#     worddict['example'] += [eg]

#     time.sleep(1)  

#     driver.find_element_by_partial_link_text("I knew this word").click()
#     time.sleep(2)

# driver.close()  

# df = pd.DataFrame(worddict)
# df.to_csv('op.csv', index=True)


################# TEST 2 ---- To generate decks and wcounts
# d = []
# driver.get("https://gre.magoosh.com/flashcards/vocabulary/decks")
# elems = driver.find_elements_by_class_name("card.flashcard-card")
# for elem in elems:
#     fname = elem.find_element_by_class_name('card-title').text
#     wcount = elem.find_element_by_class_name('card-text').text[5:7]
#     if not wcount.isnumeric():
#         continue
#     d += [(fname, int(wcount))]
    
# print(d)
# time.sleep(3)

################## COMBINED ----- To utilise info of decks found above, to fetch all decks

decks = [('Common Words I', 51), ('Common Words II', 51), ('Common Words III', 51), ('Common Words IV', 51), ('Common Words V', 51), ('Common Words VI', 51), \
    ('Basic I', 50), ('Basic II', 50), ('Basic III', 50), ('Basic IV', 50), ('Basic V', 50), ('Basic VI', 50), ('Basic VII', 51), ('Advanced I', 50), ('Advanced II', 51), \
    ('Advanced III', 50), ('Advanced IV', 51), ('Advanced V', 50), ('Advanced VI', 50), ('Advanced VII', 50)]

for deck in decks:
    driver.get("https://gre.magoosh.com/flashcards/vocabulary/decks")
    driver.find_element_by_partial_link_text(deck[0]).click()

    time.sleep(2)

    track = dict()
    worddict = {'deck':[], 'word':[], 'meaning':[], 'example':[]}

    try:
        while True:
            elem = driver.find_element_by_partial_link_text("Click to see meaning")

            elem.click()
            driver.implicitly_wait(1)

            w = driver.find_element_by_class_name("flashcard-word").text
            m = driver.find_element_by_class_name("flashcard-text").text
            eg = driver.find_element_by_class_name("flashcard-example").text

            if (track.get(w, 0)>2) or (len(track)>=deck[1]):
                break
            else:
                track[w] = track.get(w,0) + 1

            worddict['deck'] += [deck[0]]
            worddict['word'] += [w]
            worddict['meaning'] += [m]
            worddict['example'] += [eg]

            time.sleep(1)  

            driver.find_element_by_partial_link_text("I knew this word").click()
            time.sleep(2)

    except:
        continue
    else:
        df = pd.DataFrame(worddict)
        df.to_csv(deck[0] + '.csv', index=True)

driver.close()

print("sample test case successfully completed")
