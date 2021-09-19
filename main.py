from pytube import YouTube

import tkinter as tk
from tkinter import ttk

root = tk.Tk()


DESTINO_DEFAULT = '/sua_maquina/pasta'

# Cria canvas
canvas1 = tk.Canvas(root, width=600, height=300)
canvas1.pack()

# Campo link do vídeo
text_video_default = tk.StringVar()
text_video_default.set('https://www.youtube.com/watch?v=9bZkp7q19f0')
entry1 = tk.Entry(root, textvariable=text_video_default)

label_link = tk.Label(root, text='Link do Youtube')
canvas1.create_window(300, 40, width=500, window=label_link)
canvas1.create_window(300, 60, width=500, window=entry1)

# Campo destino do vídeo
text_destino_default = tk.StringVar()
text_destino_default.set(DESTINO_DEFAULT)

entry2 = tk.Entry(root, textvariable=text_destino_default)
label_destino = tk.Label(root, text='Pasta destino')
canvas1.create_window(300, 80, width=500, window=label_destino)
canvas1.create_window(300, 100, width=500, window=entry2)


def video_finalizado():
    """ Label informando que finalizou """
    texto_finalizado = tk.Label(root, text='Finalizado')
    canvas1.create_window(300, 260, window=texto_finalizado)

def busca_formatos():
    """ Busca formatos disponiveis de video """
    link = entry1.get()
    yt = YouTube(link)
    label_finalizado = tk.Label(root, text='')
    canvas1.create_window(300, 260, window=label_finalizado)

    # Filtra formatos e coloca no campo
    formatos_video = yt.streams.filter(progressive=True).order_by('resolution').desc()
    entry3["values"] = [ stream.resolution for stream in formatos_video ]
    
    label1 = tk.Label(root, text=yt.title)
    canvas1.create_window(300, 230, window=label1)

# Campo de formatos de vídeos
label1 = tk.Label(root, text='Formatos disponíveis')
canvas1.create_window(300, 120, window=label1)
entry3 = ttk.Combobox(root, values=[])
canvas1.create_window(300, 140, width=500, window=entry3)

def download_video():
    """ Realiza download do video para pasta destino """
    link = entry1.get()
    destino = entry2.get()
    formato = entry3.get()
    
    yt = YouTube(link)
    stream = yt.streams.filter(progressive=True, res=formato).first()
    stream.download(destino)
    yt.register_on_complete_callback(video_finalizado())

# Botão que busca formatos do vídeo
button1 = tk.Button(text='Buscar formatos', command=busca_formatos)
canvas1.create_window(150, 180, window=button1)

# Botão que faz o Download do vídeo
button2 = tk.Button(text='Download do video', command=download_video)
canvas1.create_window(300, 180, window=button2)

root.mainloop()