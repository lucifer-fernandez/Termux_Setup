import os
import time

os.system("clear")
time.sleep(1)

print("""\033[1;31m
        
        

  _______                                _____      _               
 |__   __|                              / ____|    | |              
    | | ___ _ __ _ __ ___  _   ___  __ | (___   ___| |_ _   _ _ __  
    | |/ _ | '__| '_ ` _ \| | | \ \/ /  \___ \ / _ | __| | | | '_ \ 
    | |  __| |  | | | | | | |_| |>  <   ____) |  __| |_| |_| | |_) |
    |_|\___|_|  |_| |_| |_|\__,_/_/\_\ |_____/ \___|\__|\__,_| .__/ 
                                                             | |    
                                                             |_|                                                                                             
    \033[1;34m==================================================================
    \033[1;33mTools Author:\033[1;36m Lucifer
    \033[1;33mTool Name: \033[1;36mTermux Setup
    \033[1;33mGithub: \033[1;36mhttps://github.com/lucifer-fernandez/Termux_Setup.git
    \033[1;34m==================================================================
        
\033[0m        
        """)
time.sleep(2)









print("\033[1;32mUpdating & Upgrading your packages...\n\033[0m")
time.sleep(5)
os.system("pkg update -y && pkg upgrade -y")

packages = [
    "python", "python2", "python3", "git", "curl", "wget", "vim", "nano", "htop",
    "figlet", "toilet", "ruby", "perl", "php", "nmap", "openssh", "zip", "unzip",
    "tar", "clang", "cmatrix", "screenfetch", "sl", "tmux", "tree", "jq", "dnsutils",
    "nodejs", "golang", "openjdk-17", "binutils", "proot", "libxml2", "libcurl", "net-tools",
    "whois", "tsu", "sqlite", "neofetch", "ffmpeg", "ranger", "zsh",
    "fish", "irssi", "mc", "hydra", "tor", "proxychains-ng", "ncurses-utils",
    "imagemagick", "weechat", "elinks", "openssl-tool"
]

print("\n\033[1;33mInstalling essential Termux packages...\033[0m\n")
time.sleep(3)
for pkg in packages:
    print(f"\033[1;32mInstalling {pkg}...\033[0m")
    os.system(f"pkg install {pkg} -y")

print("\n\033[1;32mInstalling lolcat via gem...\033[0m")
os.system("gem install lolcat")

print("\n\033[1;36m✅ All 50+ packages have been installed successfully!\033[0m\n\n\n")
time.sleep(2)

print("\033[1;31m—\033[0m"*60)
time.sleep(2)


print("\n\033[1;32mUpgrading pip...\033[0m")
os.system("pip install --upgrade pip")

python_modules = [
    "requests", "beautifulsoup4", "flask", "django", "pillow", "lxml", "pyfiglet",
    "rich", "colorama", "httpx", "selenium",
      "tqdm", "yaspin", "pycryptodome", "telethon", "pyTelegramBotAPI",
    "certifi", "chardet", "idna", "urllib3"

]

print("\n\033[1;33mInstalling Python modules via pip...\n\033[0m")
time.sleep(3)
for module in python_modules:
    print(f"\033[1;32mInstalling {module}...\033[0m")
    os.system(f"pip install {module}")

print("\n\033[1;36m✅ 20 Python modules have been installed successfully!\033[0m\n")
