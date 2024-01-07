import re
import os
import requests
import colorama

clear_command = "cls" if os.name == "nt" else "clear"

while True:
    os.system(clear_command)
    print(colorama.Fore.GREEN + "[URL Checker]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter the Discord invite link or code (type 'exit' to quit):")
    try:
        invite_input = input(colorama.Fore.MAGENTA + "root@you:~$ " + colorama.Fore.WHITE)
    except KeyboardInterrupt:
        print("")
        continue

    if invite_input.lower() == 'exit':
        break

    match = re.search(r"(?:discord\.gg/|discordapp\.com/invite/|discord\.com/invite/)?([a-zA-Z0-9]+)", invite_input)
    if not match:
        print(colorama.Fore.GREEN + "[URL Checker]: " + colorama.Fore.RED + "Invalid invite link or code format.")
    else:
        invite_code = match.group(1)
        invite_url = f"https://discord.com/api/v9/invites/{invite_code}"

        try:
            response = requests.get(invite_url)

            if response.status_code == 200:
                data = response.json()
                os.system(clear_command)
                print("")
                print(colorama.Fore.YELLOW + f" Vanity URL   : " + colorama.Fore.LIGHTWHITE_EX + str(data['guild'].get('vanity_url_code', 'None')))
                print(colorama.Fore.YELLOW + f" Boosts Count : " + colorama.Fore.LIGHTWHITE_EX + str(data['guild'].get('premium_subscription_count', 'None')))
                print("")
                print(colorama.Fore.YELLOW + f" Server ID    : " + colorama.Fore.LIGHTWHITE_EX + str(data['guild']['id']))
                print(colorama.Fore.YELLOW + f" Server Name  : " + colorama.Fore.LIGHTWHITE_EX + str(data['guild']['name']))
                print(colorama.Fore.YELLOW + f" Description  : " + colorama.Fore.LIGHTWHITE_EX + str(data['guild'].get('description', 'None')))
                print("")
                banner_extension = "gif" if data['guild'].get('banner', '').startswith("a_") else "png"
                banner_url = f"https://cdn.discordapp.com/banners/{data['guild']['id']}/{data['guild'].get('banner', '')}.{banner_extension}" if data['guild'].get('banner') else "None"
                print(colorama.Fore.YELLOW + f" Banner URL   : " + colorama.Fore.LIGHTWHITE_EX + str(banner_url))
                icon_extension = "gif" if data['guild'].get('icon', '').startswith("a_") else "png"
                icon_url = f"https://cdn.discordapp.com/icons/{data['guild']['id']}/{data['guild'].get('icon', '')}.{icon_extension}" if data['guild'].get('icon') else "None"
                print(colorama.Fore.YELLOW + f" Icon URL     : " + colorama.Fore.LIGHTWHITE_EX + str(icon_url))
                splash_extension = "png"
                splash_url = f"https://cdn.discordapp.com/splashes/{data['guild']['id']}/{data['guild'].get('splash', '')}.{splash_extension}" if data['guild'].get('splash') else "None"
                print(colorama.Fore.YELLOW + f" Splash URL   : " + colorama.Fore.LIGHTWHITE_EX + str(splash_url))

                print("")
                print(colorama.Fore.YELLOW + f" Channel Name : " + colorama.Fore.LIGHTWHITE_EX + f"#{data['channel']['name']}")
                print(colorama.Fore.YELLOW + f" Channel ID   : " + colorama.Fore.LIGHTWHITE_EX + f"{data['channel']['id']}")
                print(colorama.Fore.YELLOW + f" Invite Link  : " + colorama.Fore.LIGHTWHITE_EX + f"https://discord.gg/{data['code']}")
            else:
                os.system(clear_command)
                print(colorama.Fore.GREEN + "[URL Checker]: " + colorama.Fore.RED + "Invite link is invalid!")

        except KeyboardInterrupt:
            print("")
            continue

    print("")
    try:
        input(colorama.Fore.GREEN + "[URL Checker]: " + colorama.Fore.LIGHTYELLOW_EX + "Press Enter to continue...")
    except KeyboardInterrupt:
        continue
