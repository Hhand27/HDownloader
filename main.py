import subprocess

def videomp3():
    subprocess.run(f"yt-dlp -x --audio-format mp3 {link}", shell=True)

def videomp4():
    subprocess.run(f"yt-dlp -f best --recode-video mp4 {link}", shell=True)
    print("¡Done!")

while True:
    cmd = input("mp4, mp3 o exit : ").lower()

    if cmd == "exit":
        exit()
        
    link = input("Ingrese un link: ")

    if cmd == "mp3":
        videomp3()
    elif cmd == "mp4":
        videomp4()
    elif link == "exit":
        exit()
    else:
        print("Comando no válido, elige 'mp3' o 'mp4'.")
