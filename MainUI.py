from ControlForm import *

background = "Src/background.jpg"

if __name__ == '__main__':
    root = tk.Tk()
    window_main = WindowForm("咏月风雅UI自动化抽卡测试工具",master=root)  
    # background
    background = BackgroundLabel(background,window_belong=window_main)
    background.place(0,0,1,1)
    # labels
    label_01 = LabelForm("123",window_belong=window_main)
    label_01.place(0.1,0.1,0.1,0.1)

    label_02 = LabelForm(" "*50,window_belong=window_main)
    label_02.place(0.3,0.1,0.1,0.1)

    label_03 = LabelForm("添加新祝者/陨星之忆",window_belong=window_main)
    label_03.place(0.1,0.2,0.1,0.1)

    #label_04 = LabelForm("")

    window_main.setwindow(1280, 720)
    window_main.mainloop()
    
