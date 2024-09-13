import subprocess

while True:
    cmd = input("mp4 o mp3: ").lower()

    link = input("Ingrese un link: ")

    if cmd == "mp3":
        subprocess.run(f"yt-dlp -x --audio-format mp3 {link}", shell=True)
    elif cmd == "mp4":
        subprocess.run(f"yt-dlp {link}", shell=True)
    elif cmd == "exit":
        exit()
    else:
        print("Comando no válido, elige 'mp3' o 'mp4'.")
