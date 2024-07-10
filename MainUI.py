from ControlForm import *

background = "Src/background.jpg"

if __name__ == '__main__':
    window = WindowForm("咏月风雅UI自动化抽卡测试工具")
    dirname = os.path.dirname(__file__)
    bg_path = os.path.join(dirname, background)
    image = Image.open(bg_path).convert('RGBA')
    alpha = 128
    image.putalpha(alpha)
    image_resized = image.resize((window.root.winfo_width(), window.root.winfo_height()), Image.Resampling.LANCZOS)
    bg_object = ImageTk.PhotoImage(image_resized)
    background = tk.Label(window.root, image=bg_object)
    background.place(relx=0, rely=0, relheight=1, relwidth=1)

    window.setwindow(1280, 720)
