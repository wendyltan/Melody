﻿# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define t = Character("Tingting")
define w = Character("Wendy")
define g = Character("Girl")
define m = Character("Mxin")


# 游戏在此开始。

label start:
    
    play music "classroom.mp3"
    
    scene bg classroom
    with fade
    
    "又是平凡无奇的一天呢……"
    "下课的钟声如往常一般按时响起，讲台上那个眉飞色舞的眼镜老师（至少我是这样叫的）喝了一口养生茶"
    "好了今天就到这"
    w "呼。。终于结束了么"
    "我伸了个懒腰，合上课本"
    "最近的大量作业大概已经让我精神有点疲倦了吧。我凝神看往窗外，思索着待会要去吃些什么以满足肉体的需求"
    w "精神的疲惫。。只有吃饱肚子才能缓和！那今天就去出冒菜吧！"
    "刚想起身，发现一个女孩子挡在我面前"
    
    show tingting smile
    with dissolve
    
    g "嘿！明儿还去爬山么！"
    "正在说话的是我的好朋友，婷婷，我们一起爬山竟然已经有两年了，时间过得真快"
    w "好啊！还是正常时间？"
    t "哈哈！好！那不见不散"
    
    hide tingting smile
    with dissolve
    "讲毕，她像一阵风一样挽着舍友溜了出去"
    "摇了摇头，我也准备去吃饭了"

label dorm_first_day:
    
    play music "dorm.mp3"
    
    scene bg dorm
    with fade
    
    
    w "呼。。。"
    "揉着手腕，看着刚完成的软件工程作业，我点了点头"
    "认真起来的话，这根本不算什么啊"
    "看着桌上的钥匙扣，不知道为什么竟然有点激动"
    "像这样期待的爬山时光，有多久没有了呢？"
    "已经两年了啊。。"
    "时间过得还真是太快了"
    "到底是怎么和他认识的呢"

    scene bg hid face wit mist
    with dissolve

    t "要不要一起去爬山呀？"

    scene bg dorm
    with dissolve

    w "只能说是缘分吧"

    m "wendy，借你实验报告我看看？懒得写啦"

    show mxin normal
    with dissolve

    "正在说话的是我的舍友，Mxin。和我不一样，他学习非常好，根本不需要为学习花上太多时间"

    w "又整天泡妹不做作业了？最近翘课很多哇"

    m "泡妹只是兴趣使然，学习才最重要啦老哥？"

    "（信你才怪啊。。！）"

    w "行吧。等下发你"

    m "wendy牛逼！话说明天你还去爬山诶？有什么发展么，和tingting"

    show mxin bad smile

    w "有个鬼啊！我们只是好朋友好不好！"

    m "诶~真无趣。。。"

    hide mxin bad smile
    with dissolve

    "说罢缓缓地回到了他的位置上，仿佛刚才一堆谈话都是xjb扯出来的一样"

    w "好朋友吗。。"

label north_gate_first_day:
    

    

    # 此处为游戏结尾。

    return
