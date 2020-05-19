import tools

while True:
    #TODO（）显示菜单
    tools.show_menu()

    action_str = input("请输入希望执行的操作：")
    print("您输入的操作是【%s】"%action_str)


#pass为占位符不具有实际操作
    if action_str in ["1","2","3"]:
       if action_str=="1":
           tools.new_card()
       if action_str=="2":
           tools.show_card()
       if action_str=="3":
           tools.search_card()
    elif action_str =="0":
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("您输入的不正确，请重新输入")