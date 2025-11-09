import pyautogui
import calendar
import time
import tqdm
company_list = "Apple, nvidia, coreweave, Palantir, rigetti, CokeCola, advanced micro devices, quantum computing, sofi, costco, meta, mcdonalt, amazon, jahnson & jahnson, abbvie, tempus AI, Hims, UNH, taiwan simiconductor"
company_list = company_list.split(", ")
year_list = list(range(2015, 2026))[::-1]
month_list = calendar.month_name
count = 0
def new_window():
    pyautogui.moveTo(5, -920, duration=0.1)
    time.sleep(2)
    pyautogui.click()
    pyautogui.moveTo(10, -920, duration=0.1)
    pyautogui.moveTo(5, -920, duration=0.1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(600, -495, duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(610, -275, duration=0.1)
    pyautogui.moveTo(850, -230, duration=0.1)
    time.sleep(1)
    pyautogui.click()
for company in company_list:
    for year in year_list:
        for m in list(range(1,13)):
            if company in ["Apple"]:
                if year >= 2025:
                    continue
            #     if year == 2025:
            #         if m < 6:
            #             continue
            if year==2025:
                if m>=11:
                    continue
            if company == "coreweave":
                if year < 2025:
                    continue
            if company == "Palantir":
                if year < 2021:
                    continue
            if company == "quantum computing":
                if year < 2022:
                    continue
            if company == "sofi":
                if year < 2022:
                    continue
            if company == "Tempus AI":
                if year < 2025:
                    continue
            if company == "Hims":
                if year < 2022:
                    continue
            prompt = f"{company} {month_list[m]} {year}"
            time.sleep(2)  # time to focus the window
            # pyautogui.moveTo(300, 200)   # absolute screen coords
            if count%30==0:
                new_window()
            else:
                pyautogui.moveTo(800, -110, duration=0.1)
                pyautogui.click()
            pyautogui.write(prompt, interval=0.06)
            pyautogui.press("enter")
            for dd in tqdm.tqdm(range(100)):
                time.sleep(1) 
            pyautogui.click()
            pyautogui.moveTo(700, -374, duration=0.1)  # absolute screen coords
            pyautogui.scroll(-100000) 
            time.sleep(0.4) 
            pyautogui.click()
            pyautogui.moveTo(700, -336, duration=0.1)
            time.sleep(0.4) 
            pyautogui.click()
            pyautogui.moveTo(700, -354, duration=0.1)
            time.sleep(0.4) 
            pyautogui.click()
            pyautogui.moveTo(700, -316, duration=0.1)
            time.sleep(0.4) 
            pyautogui.click()
            count+=1
            # pyautogui.hotkey('command', 'r')
            time.sleep(1) 
            

# take screenshot
# img = pyautogui.screenshot('screenshot.png')
