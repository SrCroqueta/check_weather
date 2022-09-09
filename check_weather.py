from bs4 import BeautifulSoup
import requests, colorama, os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/357.36 (KHTML, like Gecko) \
           Chrome/58.0.3029.110 Safari/537.3'}

os.system('cls||clear')

def weather(city):
    city = city.replace(" " , "+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=\
                        chrome&ie=UTF-8', headers = headers)
    
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()

    print(f'{colorama.Fore.LIGHTCYAN_EX}Ciudad: {colorama.Fore.RESET}' + location)
    print(f'{colorama.Fore.LIGHTCYAN_EX}Día de la semana y hora: {colorama.Fore.RESET}' + time)
    print(f'{colorama.Fore.LIGHTCYAN_EX}Estado del tiempo: {colorama.Fore.RESET}' + info)
    print(f'{colorama.Fore.LIGHTCYAN_EX}Temperatura: {colorama.Fore.RESET}' + weather + ' C') 

while True:
    try:
        print(f'{colorama.Fore.LIGHTMAGENTA_EX}=================================================={colorama.Fore.RESET}')
        city = input(f'{colorama.Fore.LIGHTBLUE_EX}Introduce el nombre de la ciudad: {colorama.Fore.RESET}')
        print(f'{colorama.Fore.LIGHTMAGENTA_EX}=================================================={colorama.Fore.RESET}')
        print(f"{colorama.Fore.LIGHTYELLOW_EX}Buscando . . .{colorama.Fore.RESET}\n{colorama.Fore.LIGHTMAGENTA_EX}..................................................{colorama.Fore.RESET}")
        city = city + ' weather'

        weather(city)
    except KeyboardInterrupt:
        os.system('cls||clear')
        break
