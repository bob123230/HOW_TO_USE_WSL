import sys
import time
import random


def clear():
    import os

    os.system("cls" if os.name == "nt" else "clear")


clear()
print("""
一天，你本来想开启Windows Sandbox，却在开启功能的菜单里看见了适用于Windows的Linux子系统（WSL）。
于是，你由于好奇，开启了它。
重启，你以为WSL会出现在启动菜单里，可重启时，并没有出现那个开始菜单。
你很疑惑，于是去查“如何将WSL添加到启动菜单”，教程指出需要安装一个发行版。
于是，你在终端里输入了wsl --install，安装了那个发行版。
安装以后，你却发现没有桌面，于是你决心一定要给他装个桌面......
（提示：去安装GNOME，如果不知道怎么装，那么去edge浏览器里查一下？）
（提示2：WSL是一个缩写，它的全写是Windows Subsystem for Linux，也就是适用于Windows的Linux子系统）
按回车键继续...
""")
input()
clear()
installed = []
xlaunched = False
ipseted = False
while True:
    clear()
    print("""
[1]Ubuntu
[2]Xlaunch
[3]Microsoft Edge
""")
    s = input()
    if s == "1":
        clear()
        while True:
            c = input("wsl@rong-he:~$ ")
            if c == "sudo apt install xfce4":
                print("正在安装xfce4")
                for i in range(5):
                    time.sleep(2)
                    print(f"{(i+1)*20}%")

                print("安装完成！")
                installed.append("xfce4")
            elif c == "sudo apt install gnome":
                print("正在安装gnome")

                for i in range(5):
                    time.sleep(2)
                    print(f"{(i+1)*20}%")
                print("安装完成！")
                installed.append("gnome")
            elif c == "sudo apt install thunar":
                print("正在安装thunar")

                for i in range(5):
                    time.sleep(0.4)
                    print(f"{(i+1)*20}%")
                print("安装完成！")
                installed.append("thunar")
            elif c == "xfce4-session" and "xfce4" in installed:
                clear()
                print("""
    X 所有应用程序|                               wsl
    -------------------------------------------------
    这虽然启动了桌面环境，但实际上不是真结局，因为WSL的哲学是融合，而你违背了这个哲学。
    你去edge里搜索WSL的哲学？
    """)
                sys.exit()
            elif (
                c == "gnome-session"
                and "gnome" in installed
                and (not ipseted or not xlaunched)
            ):
                print("""
    -----------
    | X   X   |
    |   __    |
    -----------
        |
    ----------
    哦，不，出现了错误。
    你尝试安装GNOME,但失败了。
    尝试先运行Xlaunch和export DISPLAY=192.168.110.85在运行gnome-session ？
    或者去查教程B？
    你失败了
    """)
                sys.exit()
            elif (
                c == "gnome-session" and "gnome" in installed and ipseted
                and xlaunched
            ):
                clear()
                print("你你你成成成功功运行行了了GGGNNNOMMME桌面面面面面，，，但但特特特特别卡卡卡卡卡，"
                      "因因因次不不不是真结局。。。。。。。。尝试安装轻量级的xfce桌面？（如果不知道怎么装，去edge里搜）")
                sys.exit()
            elif c == "thunar" and "thunar" in installed:
                print("""
    你成功运行了一个thunar文件管理器应用，这才是真结局！！！因为它符合了WSL的哲学：融合！
    （提示：注意终端里显示的计算机名）
    """)
                sys.exit()
            elif c == "export DISPLAY=192.168.110.85":
                ipseted = True
            elif c == "exit":
                print("注销")
                break
            else:
                print("未找到命令")
    elif s == "2":
        print("Xlaunch已启动,ip为192.168.110.85")
        xlaunched = True
        input("按回车键继续...")
    elif s == "3":
        clear()
        while True:
            s = input("""
搜索：
[1] 如何在WSL中安装GNOME桌面环境：教程A
[2] 如何在WSL中安装GNOME桌面环境：教程B
[3] 如何在WSL中安装GNOME桌面环境：随机教程
[4] 如何在WSL中安装XFCE4桌面环境
[5] WSL的哲学是什么
[6] 如何在WSL中安装Linux应用程序
[7] 退出Microsoft Edge
""")
            clear()
            if s == "1":
                print("""步骤：
1. 打开终端
2. 输入sudo apt install gnome
3. 等待安装完成
4. 输入gnome-session启动GNOME桌面环境
""")
            elif s == "4":
                print("""步骤：
1. 打开终端
2. 输入sudo apt install xfce4
3. 等待安装完成
4. 输入xfce4-session启动XFCE4桌面环境
""")
            elif s == "5":
                print("""
WSL的哲学是融合，而不是分离。
因此，运行WSL最佳的做法是运行单个应用程序，而不是整个桌面环境。
比如，运行thunar文件管理器，而不是运行整个GNOME或XFCE4桌面环境。
（提示：运行thunar就是解锁真结局的方式）
""")
            elif s == "7":
                break
            elif s == "2":
                print("""步骤：
1. 打开终端
2. 运行Xlaunch
3. 输入sudo apt install gnome
4. 等待安装完成
5. 输入export DISPLAY=你的IP地址（例如192.168.110.85）
6. 输入gnome-session启动GNOME桌面环境
""")
            elif s == "3":
                s = random.randint(1, 2)
                if s == 1:
                    print("""选中了A教程
步骤：
1. 打开终端
2. 输入sudo apt install gnome
3. 等待安装完成
4. 输入gnome-session启动GNOME桌面环境
""")
                else:
                    print("""选中了B教程
步骤：
1. 打开终端
2. 运行Xlaunch
3. 输入sudo apt install gnome
4. 等待安装完成
5. 输入export DISPLAY=你的IP地址（例如192.168.110.85）
6. 输入gnome-session启动GNOME桌面环境
""")
            elif s == "6":
                print(
                    "输入sudo apt install 软件名来安装Linux应用程序，比如sudo apt install "
                    "thunar会安装thunar文件管理器"
                )
            else:
                print("未找到相关内容")
