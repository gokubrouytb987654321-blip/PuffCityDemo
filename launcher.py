import os, sys, time, socket, threading, webbrowser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import tkinter as tk

def find_game():
    base = Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parent))
    exe_dir = Path(sys.executable).resolve().parent
    for c in (base / 'PuffHouse', base, exe_dir / '_internal' / 'PuffHouse',
              exe_dir / 'PuffHouse', exe_dir, Path(__file__).resolve().parent):
        if (c / 'index.html').exists():
            return c
    from tkinter import messagebox
    r = tk.Tk(); r.withdraw()
    messagebox.showerror('Puff City', 'Fichiers du jeu introuvables (index.html).\nRecompile avec build_PuffCity_EXE.bat')
    sys.exit(1)

GAME = find_game()
PORT = 0

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

class LocalServer(ThreadingHTTPServer):
    allow_reuse_address = True

def find_port():
    s = socket.socket(); s.bind(('127.0.0.1', 0)); p = s.getsockname()[1]; s.close(); return p

def main():
    global PORT
    PORT = find_port()
    os.chdir(GAME)
    server = LocalServer(('127.0.0.1', PORT), QuietHandler)
    threading.Thread(target=server.serve_forever, daemon=True).start()

    root = tk.Tk(); root.overrideredirect(True); root.configure(bg='#0b1019')
    w,h=620,350
    sw,sh=root.winfo_screenwidth(),root.winfo_screenheight()
    root.geometry(f'{w}x{h}+{(sw-w)//2}+{(sh-h)//2}')
    tk.Label(root,text='PUFF CITY',font=('Segoe UI',34,'bold'),fg='#ff70ae',bg='#0b1019').pack(pady=(65,5))
    tk.Label(root,text='Chargement du jeu…',font=('Segoe UI',15),fg='#f4f6ff',bg='#0b1019').pack()
    tk.Label(root,text='ChatGPT  •  TTNVR  •  LBBP  •  LBB',font=('Segoe UI',9),fg='#aeb8ca',bg='#0b1019').pack(side='bottom',pady=22)
    root.update()
    root.after(5000, lambda: (root.destroy(), webbrowser.open(f'http://127.0.0.1:{PORT}/index.html')))
    root.mainloop()
    try:
        server.shutdown(); server.server_close()
    except Exception:
        pass

if __name__ == '__main__': main()