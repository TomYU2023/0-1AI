# 1、定义变量
c1 ='可乐'
c2 ='牛奶'

# 2、经过一系列操作，实现c1和c2变量值的交换①把c1水杯中的可乐倒入temp空杯中
temp = c1
# ② 把c2杯中的牛奶倒入c1杯中
c1 = c2
# ③ 把临时杯中的可乐倒入c2水杯中
c2 = temp

# 3、使用print()打印c1和c2的结果
print(f'c1杯中:{c1}')
print(f'c2杯中:{c2}')

proof = int(input('请输入您血液中酒精含量(mg):'))
# 3、还要进一步判断，判断是酒驾还是醉驾
if proof >= 20:
    if proof >= 80:
        print('您已构成醉驾驾驶，涉嫌危险驾驶罪!')
    else:
        print('您血液中酒驾含量在20mg-80mg之间，不够成醉酒驾驶，属于酒驾!')
else:
        print('不构成酒驾!')
print('=====================这里是if-elif-else=====================')

# 三目运算符
print('您血液中酒精含量为:',proof,'mg') if proof >= 20 else print('您血液中酒精含量小于20mg')
print('=====================这里是三目运算符=====================')