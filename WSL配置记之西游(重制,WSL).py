import time
import sys
import os

def over(grade: int):
    grades = ["S+", "S", "A+", "A", "B+", "B", "C+", "C", "D+", "D", "F+", "F"]
    if grade > 11:
        print("你的评级： F")
    else:
        print("你的评级：", grades[grade])
    if grade <= 1:
        print("九九八十一难")
    elif grade <= 3:
        print("融合派")
    elif grade <= 5:
        print("双重派")
    elif grade <= 7:
        print("你还没有领悟WSL的真谛")
    elif grade <= 9:
        print("隔离派")
    else:
        print("彻头彻尾的隔离派")
    print("失误数：", grade)
    os.system(
        "sudo apt autoremove gnome xfce4 thunar xfce4-session "
        "gnome-shell gnome-session -y && sudo snap remove code"
    )
    sys.exit()


faileds = 0


def failed(message: str = ""):
    print("失误")
    global faileds
    faileds += 1
    print(message)


def scrool(
    message: str, line_time: int = 1, letter_time: float = 0.1,
    split_: str = "\n"
):
    try:
        for i in message.split(split_):
            for j in i:
                print(j, end="", flush=True)
                time.sleep(letter_time)
            print()
            time.sleep(line_time)
    except KeyboardInterrupt:
        print("跳过剧情中……")


def choose(
        s: list, tip: str, right: int,
        failed_message: str, right_message: str,
        wrong_cmd:str = "", right_cmd:str = ""
):
    while True:
        print(tip)
        k = input()
        if k in s:
            if s.index(k) == right:
                os.system(right_cmd)
                print(right_message)
                break
            else:
                os.system(wrong_cmd)
                failed(failed_message)


def spchoose1(
        s: list, tip: str, right: int, failed_message: str,
        right_message: str
):
    while True:
        print(tip)
        k = input()
        if k in s:
            if s.index(k) == right:
                print(right_message)
                break
            else:
                print(failed_message)


def xiyou_and_wsl():
    print("正在准备……")
    os.system("sudo apt install jupyter-lab wine snapd thunar -y")
    os.system("sudo snap install code --classic")
    scrool("""
按Ctrl+C可以跳过剧情
第一幕 猴王问世

在傲来国，有一座山，山上有一块大石头。石头因为见风，化作了一个石猴。
一天，群猴说：谁能越过这个名为“双系统壁垒”的瀑布？越过去了，拜你为王！
""")
    choose(
        ["y", "n"],
        "要不要越过去？(y/n)",
        0,
        "西游记的剧情可不是这样的",
        "你越了过去，看见上面写着“WSL福地，融合洞洞天”",
    )
    scrool("""
你越了过去，喊道：没水，没水！
群猴也跟着过了去，说：这可是天造地设的好家当啊！
于是，群猴拜你为王。

一天，你突然想到，你以后会老死，你可不想以后老死，于是就去拜师了。

第二幕 拜师学艺

你去拜了师，师傅要叫你“网络集成之术”和“Windows应用召唤之术”。
你想向别人卖弄一下。
""")
    choose(
        ["1", "2"],
        "怎么用网络集成之术？\n[1]手动配置端口转发\n[2]无需配置",
        1,
        "你试了，却发现没用",
        "你试了，果然有用",
        "",
        "jupyter-lab"
    )
    choose(
        ["1", "2"],
        "怎么用Windows程序召唤之术？\n[1]直接念真言\n[2]使用兼容层",
        0,
        "你试了，却发现没用",
        "你试了，果然有用",
        "wine /mnt/c/Windows/notepad.exe",
        "notepad.exe"
    )
    scrool("""
祖师看到你卖弄，就把你逐出了师门。

第三幕 大闹天宫

孙悟空要把武器。
于是就去了龙宫。
孙悟空觉得什么武器也配不上，于是就去拿了那里的定海神针“如意VSCode”。虾兵蟹将很快就追上来了。
""")
    choose(
        ["1", "2"],
        """怎么使用VSCode？
[1]在WSL内部启动（指用X11/WSLg启动）
[2]在Windows中启动（指用Windows中的连WSL）""",
        1,
        "你一棍下去，虾兵蟹将：你这是在给我们做头部按摩吧？",
        "你一棍下去，虾兵蟹将都被打死了，龙宫的水都在晃动",
        "export DONT_PROMPT_WSL_INSTALL=1 && /snap/bin/code",
        "code"
    )
    scrool("""
天上的人看到了，觉得你应该当个官，就当个……弼wsl$温。
""")
    choose(
        ["1", "2"],
        "这官怎么当？\n[1]看守\\\\wsl$这个路径\n[2]配置Samba到wsl$",
        0,
        "天上的人来了：这点官你都做不好！！！",
        "",
    )
    scrool("""
后来才知道，这是一个很小的官。
于是自封“齐天大圣”。
天上的人又叫他看守蟠桃园。
天上的人说：“最大的桃子吃了能天地同寿。”
你参加不了蟠桃盛会，于是就打翻了蟠桃盛会。
并且想吃最大的桃子。
那个桃子是最大的呢？
""")
    choose(
        ["1", "2", "3"],
        "[1]双系统+ntfs-3g\n[2]Samba\n[3]/mnt/c",
        2,
        "你摘下来，却发现这根本不是最大的桃子",
        "",
        "",
        "echo '$ ls /mnt/c' && ls /mnt/c"
    )
    scrool("""
因为你大闹天宫，立刻导致天兵天将一起捉拿你
但是没成功
于是，如来就和你打赌，飞出如来的手掌心。
""")
    spchoose1(
        ["1", "2"],
        "向哪边飞？\n[1]西（隔离）\n[2]东（融合）",
        0,
        "西游记的剧情可不是这样的",
        "",
    )
    scrool("""
你没能飞出去，被压在五行山下。
你试图跑出来。
天上的人看到了，就贴了一张“sudo apt install gnome”的纸条，你就出不来了。

第四幕 三调GNOME桥

唐僧路过，就揭了纸条，把你救了出来。
路上又收了猪八戒和沙僧。
一天，遇到了一条大河。
旁边有一个妖怪。
你打败了妖怪。
拿到一张图纸。
1. 准备念真言
2. 念sudo apt install gnome
3. 等待生效
4. 念gnome-session建桥
""")
    installed = []
    while True:
        c = input("念真言：")
        if c == "sudo apt install gnome":
            os.system("sudo apt install gnome -y")
            installed.append("gnome")
        elif c == "gnome-session" and "gnome" in installed:
            os.system("gnome-session")
            break
        elif c == "sudo apt install thunar":
            os.system("sudo apt install thunar -y")
            installed.append("thunar")
        elif c == "thunar" and "thunar" in installed:
            os.system("thunar")
            print("隐藏剧情解锁")
            scrool("""
thunar随即化做一条法船。
唐僧师徒上了那船，那船却不往对面开。
船向左一段后，便一直向东开，路过了大唐，到了雷音寺。
如来佛祖本来想说：“你们没经历九九八十一难，就来见我了？”
但是看到了thunar。
于是，就说：“你们虽然没有经历九九八十一难，但是已经领悟了真经所说的道理，所以我把真经直接给你。”
唐僧师徒四人终于取得真经，返回大唐。
见真经上写着：
WSL之道乃融合而非隔离。
""")
            if faileds == 0:
                print("你的评级：", "R+")
                print("彻头彻尾的融合派")
            else:
                print("你的评级：", "R")
                print("WSL不该装桌面")
            print("失误数：", faileds)
            os.system(
                "sudo apt autoremove gnome xfce4 thunar xfce4-session "
                "gnome-shell gnome-session -y && sudo snap remove code"
            )
            sys.exit()
        else:
            print("此非真言")
    scrool("""
你正要过桥，桥就塌了。
才发现这图纸是假的。
于是你再次打败妖怪，获得另一张图纸。
1. 祭祀河神Xlaunch
2. 准备念真言
3. 念sudo apt install gnome
4. 等待真言生效
5. 念export DISPLAY=你的IP地址（例如192.168.110.85）
6. 念gnome-session建起GNOME桥
无需念sudo apt install gnome
""")
    ip = input("""
请在执行以下步骤后输入你的ip地址以继续
1.打开XLaunch
2.选择任意模式
3.选择start no client0
4.选择Disable access control
5.点击完成
输入你的DISPLAY：
""")
    xlaunched = True
    ipseted = False
    while True:
        c = input("念真言：")
        if c == f"export DISPLAY={ip}":
            os.system(f"export DISPLAY={ip}")
            ipseted = True
        elif c == "gnome-session" and ipseted:
            os.system("gnome-session")
            break
        elif c == "gnome-session" and not ipseted:
            os.system("gnome-session")
            print("桥又塌，真言有误")
        else:
            print("此非真言")
    scrool("""
走上桥，桥又塌了。
又有一只妖怪在旁边，哈哈大笑：这图纸是几年前的。以前还有用，现在，按照图纸，已经没有用了。
于是，你打死了那只妖怪，获得另一张图纸。
上面写着：
1. 以ubuntu-24.04-desktop-amd64.iso祭祀virtualbox
2. 让他建造GNOME桥
唐僧师徒按照图纸，桥果然成了。
但是，却举步维艰，过桥时已精疲力尽。

第五幕 小雷音寺

你看到了小雷音寺，以为是真的到西天了。
看到了黄眉童子假扮的如来。
他说：要取得真经，要念sudo apt install xfce4。
念！
等待真言生效
""")
    os.system("sudo apt install xfce4 -y")
    scrool("""
你拿着真经回去，半途一只怪鸟打翻了真经。
于是你回去。
才发现那原来是黄眉童子。
于是师徒四人就都被吸入人种袋了。
这时，弥勒佛祖赶来。
佛祖说：那黄眉童子是成全你们九九八十一难的，干的却是偷吃童男童女的勾当。
童子已经收拾了，但是，如果要放你们出人种袋，回答我几个问题。
""")
    choose(
        ["1", "2"], "为什么XFCE不是真经？\n[1]是桌面\n[2]是黄眉童子给的", 0, "", "对了"
    )
    choose(
        ["1", "2"],
        "为什么一路上你还没有取得真经？\n[1]方向错了，雷音寺在东方\n[2]磨难不够",
        0,
        "如果九九八十一难没有近，则我会让黄眉童子成全你们九九八十一难吗？",
        "对了。佛祖放唐僧师徒出来",
    )
    scrool("""
第六幕 雷音寺

向东行
没想到只有几难，就到了雷音。
唐僧师徒取到了真经。
其中一部叫做thunar。
唐僧质问：一路上桌面之物皆非真经，但是，nautilus, thunar, gedit……这些不都是桌面之物？
如来说：这两个，是不一样的。
唐僧师徒走了，如来发现他们只有八十难，于是叫他们过通天河。
请念真言以渡通天河
可念有：
thunar
gnome-session
xfce4-session
""")
    while True:
        c = input("念真言：")
        if c == "thunar":
            os.system("thunar")
            scrool("thunar如一舟，载着唐僧师徒过去了")
            break
        elif c == "gnome-session":
            os.system("gnome-session")
            failed("桥刚建成，就塌了")
        elif c == "xfce4-session":
            os.system("xfce4-session")
            failed("xfce如一舟，却开回了原点")
        else:
            print("此非真言")
    scrool("""
唐僧师徒四人终于取得真经，返回大唐。
见真经上写着：
WSL之道乃融合而非隔离。
""")
    over(faileds)


if __name__ == "__main__":
    xiyou_and_wsl()
