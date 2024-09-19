import subprocess

def install_yt_dlp(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr.decode()}")

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
                    " 8 MacOS\n"
                    " c Salir \n")

        if cmd == "1":
            print("Instalando yt-dlp en Debian/Ubuntu...")
            install_yt_dlp("sudo apt install -y yt-dlp")
        elif cmd == "2":
            print("Instalando yt-dlp en Fedora...")
            install_yt_dlp("sudo dnf install -y yt-dlp")
        elif cmd == "3":
            print("Instalando yt-dlp en Arch, Manjaro, EndeavourOS...")
            install_yt_dlp("sudo pacman -S --noconfirm yt-dlp")
        elif cmd == "4":
            print("Instalando yt-dlp en OpenSUSE...")
            install_yt_dlp("sudo zypper install -y yt-dlp")
        elif cmd == "5":
            print("Instalando yt-dlp en Gentoo...")
            install_yt_dlp("sudo emerge yt-dlp")
        elif cmd == "6":
            print("Instalando yt-dlp en RHEL Based...")
            install_yt_dlp("sudo dnf install -y yt-dlp")
        elif cmd == "7":
            print("Instalando yt-dlp en Solus...")
            install_yt_dlp("sudo eopkg install yt-dlp")
        elif cmd == "8":
            print("Instalando yt-dlp en MacOS...")
            homebrew_installed = input("¿Tienes Homebrew instalado (Y, N)? : ").strip().lower()
            if homebrew_installed == "y":
                install_yt_dlp("brew install yt-dlp")
            elif homebrew_installed == "n":
                install_homebrew = input("¿Desea instalar Homebrew (Y, N)? : ").strip().lower()
                if install_homebrew == "y":
                    install_yt_dlp('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
                    install_yt_dlp("brew install yt-dlp")
                else:
                    print("Saliendo...")
                    break
            else:
                print("Respuesta no válida. Saliendo...")
                break

        elif cmd == "c":
            print("Saliendo...")
            break
        else:
            print("Ingrese una respuesta válida, como por ejemplo '2'.")

if __name__ == "__main__":
    main()

