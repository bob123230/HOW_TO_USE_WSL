import sys


def clear():
    import os

    os.system("cls" if os.name == "nt" else "clear")


clear()
print("""
WSL配置记·新篇章
你正在融合的使用WSL，当你想启动WSL里安装的VSCode时，***************。
你才意识到融合的奥秘不止无缝运行应用程序。
（你需要获得3个奥秘，你的WSL上安装了gimp,VSCode,jupyter lab，奥秘就藏在这三个程序里，以及你想用Windows Notepad写字）
""")
input("按回车键继续……")
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
                s = input(
                    "你想把图片导出到“桌面”，请输入导出路径（Windows的用户名是User）："
                )
                if s == "/mnt/c/Users/User/Desktop/":
                    print("获得：跨系统文件系统访问碎片1")
                    x.append("跨系统文件系统访问1")
                elif s == "/home/wsl/桌面/":
                    x = []
                    print(
                        "失败……奥秘已全部丢失……（提示：去欢迎使用WSL选择跨操作系统文件系统访问）"
                    )
                    sys.exit()
                else:
                    print("不存在，或不是你想要的目录")
            elif s == "code":
                print("""
WSL配置记·新篇章
你正在融合的使用WSL，当你想启动WSL里安装的VSCode时，竟然打开了Windows里的VSCode。
你才意识到融合的奥秘不止无缝运行应用程序。
（你需要获得3个奥秘，你的WSL上安装了gimp,VSCode,jupyter lab，奥秘就藏在这三个程序里，以及你想用Windows Notepad写字）
""")
                print("你打开了Windows里的VSCode，你觉得这？(接受/默认：不接受)")
                s = input()
                if s == "接受":
                    print("获得奥秘：VSCode集成")
                    x.append("VSCode集成")
                else:
                    x = []
                    print("失败……奥秘已全部丢失……（提示：去欢迎使用WSL选择VSCode集成）")
                    sys.exit()
            elif s == "jupyter-lab" or s == "jupyter lab":
                print(
                    "你以为jupyter会出现在WSL内部的Firefox浏览器里，结果却出现在了Windows的Edge浏览器里。"
                    "你觉得这？(接受/默认：不接受)"
                )
                s = input()
                if s == "接受":
                    print("获得奥秘：网络集成")
                    x.append("网络集成")
                else:
                    x = []
                    print("失败……奥秘已全部丢失……（提示：去欢迎使用WSL选择网络集成）")
                    sys.exit()
            elif s == "notepad.exe":
                print("获得：跨系统文件系统访问碎片2")
                x.append("跨系统文件系统访问2")
                print("直接打开了Windows里的notepad")
                s = input("文字写好了，你想保存到WSL的 /home/wsl/ 目录里，路径：")
                if (
                    s == "\\\\wsl$\\Ubuntu\\home\\wsl\\"
                    or s == "\\\\wsl.localhost\\Ubuntu\\home\\wsl\\"
                ):
                    print("获得：跨系统文件系统访问碎片3")
                    x.append("跨系统文件系统访问3")
                else:
                    print("路径不存在或者不是你想要的目录")
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
