import subprocess

def main():
    while True:
        cmd = input("¿Qué distribución usa (ingrese el número)? \n"
                    " 1 Debian/Ubuntu \n"
                    " 2 Fedora \n"
                    " 3 Arch/Manjaro/EndeavourOS \n"
                    " 4 OpenSUSE \n"
                    " 5 Gentoo \n"
                    " 6 RHEL Based (CentOS, AlmaLinux, RockyLinux) \n"
                    " 7 Solus \n"
                    " 8 MacOS"
                    " c Salir \n")

        if cmd == "1":
            print("Debian/Ubuntu")
            subprocess.run("sudo apt install yt-dlp", shell=True)
        elif cmd == "2":
            print("Fedora")
            subprocess.run("sudo dnf install yt-dlp", shell=True)
        elif cmd == "3":
            print("Arch, Manjaro, EndeavourOS")
            subprocess.run("sudo pacman -S yt-dlp", shell=True)
        elif cmd == "4":
            print("OpenSUSE")
            subprocess.run("sudo zypper install yt-dlp", shell=True)
        elif cmd == "5":
            print("Gentoo")
            subprocess.run("sudo emerge yt-dlp", shell=True)
        elif cmd == "6":
            print("RHEL Based")
            subprocess.run("sudo dnf install yt-dlp", shell=True)
        elif cmd == "7":
            print("Solus")
            subprocess.run("sudo eopkg install yt-dlp", shell=True)
        elif cmd == "8":
            print("MacOS")
            print("Necesitas tener homebrew instalado")
            subprocess.run("brew install yt-dlp", shell=True)
        elif cmd == "c":
            print("Saliendo...")
            break
        else:
            print("Ingrese una respuesta válida, como por ejemplo '2'.")

main()

