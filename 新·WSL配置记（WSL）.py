import sys
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()
print("""
注意事项：
确保在WSL中运行。
确保发行版是Ubuntu/Debian。
Windows的VSCode已安装。
确保linux和windows的用户名中均没有空格。

WSL配置记·新篇章
你正在融合的使用WSL，当你想启动WSL里安装的VSCode时，***************。
你才意识到融合的奥秘不止无缝运行应用程序。
（你需要获得3个奥秘，你的WSL上安装了gimp,VSCode,jupyter lab，奥秘就藏在这三个程序里，以及你想用Windows Notepad写字）
""")
input("按回车键继续……")
print("正在准备……")
if not os.path.exists("/bin/gimp"):
    x = os.system("sudo apt install gimp -y")
    if x != 0:
        print("你无法进入游戏，因为gimp未安装且无法安装。")
        sys.exit()
if os.popen("which code").read == "":
    print("你无法进入游戏：Windows的VSCode未安装。")
    sys.exit()
if not os.path.exists("/bin/jupyter-lab"):
    x = os.system("sudo apt install jupyterlab -y")
    if x != 0:
        print("你无法进入游戏，因为jupyterlab未安装且无法安装。")
        sys.exit()
windowsusername = input("请输入你的Windows用户名：")
while True:
    clear()
    x = []
    s = input("""
[1]Ubuntu
[2]欢迎使用WSL
""")
    if s == "1":

        clear()
        while True:
            s = input("wsl@rong-he:~$ ")
            if s == "gimp":
                os.system("gimp > /dev/null 2>&1 &")
                input(
                    """gimp将会打开，请任意作图，并保存为图片.xcf，同时保存到“桌面”，然后关闭窗口
若无法输入中文，请复制：图片.xcf
按回车继续"""
                )
                os.system("pkill gimp")

                if os.path.exists(f"/mnt/c/Users/{windowsusername}/Desktop/图片"
                                  ".xcf"):
                    print("获得：跨系统文件系统访问碎片1")
                    x.append("跨系统文件系统访问1")
                    os.system(f"rm /mnt/c/Users/{windowsusername}/Desktop/"
                              "图片.xcf")
                elif os.path.exists(os.path.expanduser("~/桌面/图片.xcf")):
                    x = []
                    print(
                        "失败……奥秘已全部丢失……（提示：去欢迎使用WSL选择跨操作系统文件系统访问）"
                    )
                    os.system("rm ~/桌面/图片.xcf")
                    sys.exit()
                else:
                    print("你似乎没有正确保存图片")
            elif s == "code":
                print("""
WSL配置记·新篇章
你正在融合的使用WSL，当你想启动WSL里安装的VSCode时，竟然打开了Windows里的VSCode。
你才意识到融合的奥秘不止无缝运行应用程序。
（你需要获得3个奥秘，你的WSL上安装了gimp,VSCode,jupyter lab，奥秘就藏在这三个程序里，以及你想用Windows Notepad写字）
""")
                print("你打开了Windows里的VSCode，你觉得这？(接受/默认：不接受)")
                os.system("code &")
                s = input()
                if s == "接受":
                    print("获得奥秘：VSCode集成")
                    x.append("VSCode集成")
                else:
                    x = []
                    print("失败……奥秘已全部丢失……（提示：去欢迎使用WSL选择VSCode集成）")
                    sys.exit()
                os.system("pkill code")
            elif s == "jupyter-lab" or s == "jupyter lab":
                print(
                    "你以为jupyter会出现在WSL内部的浏览器里，结果却出现在了Windows的浏览器里。你觉得这？"
                    "(接受/默认：不接受)"
                )
                os.system("jupyter-lab > /dev/null 2>&1 &")
                s = input()
                if s == "接受":
                    print("获得奥秘：网络集成")
                    x.append("网络集成")
                else:
                    x = []
                    print("失败……奥秘已全部丢失……（提示：去欢迎使用WSL选择网络集成）")
                    sys.exit()
                os.system("pkill jupyter-lab")

            elif s == "notepad.exe":
                print("获得：跨系统文件系统访问碎片2")
                x.append("跨系统文件系统访问2")
                os.system("notepad.exe &")
                print("直接打开了Windows里的notepad")
                s = input(
                    "请写一个文本文档，并保存到文本文档.txt，保存到你的~/目录下，然后按回车"
                )
                if os.path.exists(os.path.expanduser("~/文本文档.txt")):
                    print("获得：跨系统文件系统访问碎片3")
                    x.append("跨系统文件系统访问3")
                    os.system("rm ~/文本文档.txt")
                else:
                    print("你似乎没有正确保存")
            elif s == "exit":
                break
            else:
                print("未找到命令")
            if (
                ("跨系统文件系统访问1" in x)
                and ("VSCode集成" in x)
                and ("网络集成" in x)
                and ("跨系统文件系统访问2" in x)
                and ("跨系统文件系统访问3" in x)
            ):
                print("成功！你获取了更多融合！")
                sys.exit()
    elif s == "2":
        while True:
            clear()
            print("""
[1]跨系统文件访问
[2]网络集成
[3]VSCode集成
[4]退出
""")
            s = input()
            if s == "1":
                print("""
你可以在WSL内通过/mnt/c来访问Windows的C盘。
你可以在Windows里通过\\\\wsl$\\来访问WSL的文件系统。
你可以在WSL终端中运行Windows命令。
""")
            elif s == "2":
                print("""
你可以在WSL中生成网络应用，然后在Windows的浏览器中打开它。
""")
            elif s == "3":
                print("""
你可以在WSL中输入code命令来打开Windows里的VSCode。并使用Remote - WSL扩展。
""")
            elif s == "4":
                break
            input("按回车继续")
