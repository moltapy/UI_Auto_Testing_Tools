from ControlForm import *
from Handlers import *

background = "Src/background.jpg"

formsize = (0.12,0.048)
subsize = (540,270)

array_x = [0.04,0.20,0.36,0.52]
array_x_abnormal = [0.74]
array_y = [0.05+0.1*x for x in range(9)]

option_list_01 = ["祝者","陨星之忆"]

if __name__ == '__main__':

    # windows
    root = tk.Tk()
    window_main = WindowForm("咏月风雅UI自动化抽卡测试工具",master=root)

    ## subwindows
    window_sub_01 = None
    window_sub_02 = None

    # background
    background = BackgroundLabel(background,window_belong=window_main)
    background.place(0,0,1,1)
    # labels
    label_01 = LabelForm("图像资源文件夹",window_belong=window_main)
    label_01.place(array_x[0],array_y[0],*formsize)

    label_02 = LabelForm(" "*50,window_belong=window_main)
    label_02.place(array_x[1],array_y[0],0.5,0.048)

    label_03 = LabelForm("添加新祝者/陨星之忆",window_belong=window_main)
    label_03.place(array_x[0],array_y[1],*formsize)

    label_04 = LabelForm("删除祝者/陨星之忆",window_belong=window_main)
    label_04.place(array_x[0],array_y[2],*formsize)

    label_05 = LabelForm("浏览资源文件夹",window_belong=window_main)
    label_05.place(array_x[0],array_y[3],*formsize)

    label_06 = LabelForm("查询陨星之忆/祝者",window_belong=window_main)
    label_06.place(array_x[0],array_y[4],*formsize)

    label_07 = LabelForm("抽卡模式(以十连抽计数)",window_belong=window_main)
    label_07.place(array_x[0],array_y[5],*formsize)

    label_08 = LabelForm("图像识别线程数",window_belong=window_main)
    label_08.place(array_x[0],array_y[6],*formsize)

    label_09 = LabelForm("抽卡统计面板",window_belong=window_main)
    label_09.place(array_x[0],array_y[7],*formsize)

    label_10 = LabelForm("Windows桌面窗口连接",window_belong=window_main)
    label_10.place(array_x[0],array_y[8],*formsize)

    ## Buttons
    button_01 = ButtonForm(init_text="打开文件夹",window_belong=window_main,
                           func_handle=lambda: open_directory(label_02.string))
    button_01.place(array_x_abnormal[0],array_y[0],*formsize)

    button_02 = ButtonForm(init_text="打开子菜单",window_belong=window_main,
                           func_handle=lambda: open_subwindow(window_main,*subsize,title="祝者/陨星之忆添加",window_varname="window_sub_01"))
    button_02.place(array_x[1],array_y[1],*formsize)

    button_03 = ButtonForm(init_text="打开子菜单",window_belong=window_main,
                           func_handle=lambda: open_subwindow(window_main,*subsize,title="祝者/陨星之忆删除",window_varname="window_sub_02"))
    button_03.place(array_x[1],array_y[2],*formsize)

    button_04 = ButtonForm(init_text="浏览文件夹",window_belong=window_main,
                           func_handle=lambda :check_directory(label_02))
    button_04.place(array_x[1],array_y[3],*formsize)

    button_05 = ButtonForm(init_text="查询",window_belong=window_main,
<<<<<<< Updated upstream
                           func_handle=lambda:search_out(*[]))
=======
                           func_handle=lambda:search_out(Mapping[opmenu_01.string],entry_01.string))
>>>>>>> Stashed changes


    ## OptionMenu
    opmenu_01 = OptionForm(window_main,"请选择查询类型",*option_list_01)
    opmenu_01.place(array_x[1],array_y[4],*formsize)


    ## InputBox/Entry
    entry_01 = EntryForm(window_main,30)
    entry_01.place(array_x[2],array_y[4],*formsize)

    window_main.setwindow(1280, 720)
    window_main.mainloop()
    
