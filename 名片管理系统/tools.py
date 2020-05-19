#存放所有名片
card_list = []

def show_menu():
    print("--------------------------")
    print("|欢迎使用【名片管理系统】|")
    print("|      1.新建名片        |")
    print("|      2.显示全部        |")
    print("|      3.查询名片        |")
    print("|      0.退出系统        |")
    print("--------------------------")

def new_card():
    """新增名片"""
    print("-"*40)
    print("新增名片")
    #1.输入信息
    name_str = input("请输入姓名")
    phone_str = input("请输入电话")
    qq_str = input("请输入qq")
    email_str = input("请输入邮箱")
    # 2.建立名片自字典
    card_dict ={"name":name_str,
                "phone":phone_str,
                "qq":qq_str,
                "email":email_str}
    # 3添加列表
    card_list.append(card_dict)
    print(card_list)
    # 4.提示添加成功
    print("%s的名片添加成功！"%name_str)

def show_card():
    """显示所有名片"""
    print("_" * 40)
    print("显示所有名片")
    #判断
    if len(card_list)==0:
        print("没有名片，请使用新增功能增加名片")
        return#return之后的代码不执行

    #打印表头
    for name in ["姓名","电话","qq","邮箱"]:
       print(name,end="\t\t")

    print("")

     #打印分隔线
    print("_"*40)

    #遍历所有名片依次输出字典信息
    for card_dict in card_list:

         print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                           card_dict["phone"],
                                           card_dict["qq"],
                                           card_dict["email"]))

def search_card():
    """搜索名片"""
    print("-" * 40)
    print("搜索名片")
    #1.提示用户需要搜索的姓名
    find_name= input("请输入需要搜索的姓名")
    #2.遍历名片列表，查询搜索姓名，没找到提示没找到
    for card_dict in card_list:
        if card_dict["name"]==find_name:
            print("姓名\t\t电话\t\tqq\t\t邮箱")
            print("_"*40)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                              card_dict["phone"],
                                              card_dict["qq"],
                                              card_dict["email"]))
            #TODO针对找到的名片进行修改，删除操作
            deal_card(card_dict)

            break
    else:
        print("抱歉，没有找到%s"%find_name)


def deal_card(find_dict):
    print(find_dict)
    action_str = input("请选择要执行的操作：1.修改 2.删除 0.返回上级菜单")
    if action_str =="1":
        while True:
            action_str = input("修改1.姓名 2.电话 3.qq 4.邮箱 0退出  ：")
            if action_str =="1":
                find_dict["name"] = input("姓名：")
            if action_str =="2":
                find_dict["phone"] = input("电话：")
            if action_str =="3":
                find_dict["qq"] = input("qq：")
            if action_str =="4":
                find_dict["email"] = input("邮箱：")
            if action_str =="0":
               print("修改名片成功")
    elif action_str =="2":
        card_list.remove(find_dict)
        print("删除名片成功")