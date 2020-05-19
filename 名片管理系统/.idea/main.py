action_str = input("请输入希望执行的操作：")
print("您输入的操作是%d"%action_str)

if action_str in ["1","2","3"]:
    pass#占位符，没有任何操作
elif action_str =="0":
    pass
else:
    printf("你输入的数字操作不正确，请重新输入")