money = 5000000
name = None
name =input("输入姓名")
def main():
    print("--------主菜单---------")
    print(f"{name}，您好，欢迎来到ATM，请选择操作")
    print("查询余额\t【请输入查询】")
    print("存款\t\t【请输入存款】")
    print("取款\t\t【请输入取款】")
    print("退出\t\t【请输入退出】")
    return input("请输入您的选择")

def query(show_header):
    if show_header:
        print("--------查询余额-----------")
    print(f"{name}，您好，您的余额为{money}")
def saving(num):
    global money
    money += num
    print(f"您好，您存款{num}成功")
    query(False)
def getmoney(num):
    global money
    money -= num
    print(f"您好，您取款{num}成功")
    query(False)

while True:
    keyboard_input = main()
    if keyboard_input == "查询":
        query(True)
        continue
    elif keyboard_input == "存款":
        num = int(input("存多少钱呢？"))
        saving(num)
        continue
    elif keyboard_input == "取款":
        num = int(input("取多少钱呢"))
        getmoney(num)
        continue
    elif keyboard_input == "退出":
        print("程序退出")
        break
    else:
        print("输入错误程序退出")
