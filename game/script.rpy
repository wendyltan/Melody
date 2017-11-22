# 游戏的脚本可置于此文件中。

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
    w "或许是食物的召唤吧。。跑得这么快。不管怎么说我肚子也有点饿了，先去吃饭好了"

label dorm_first_day:
    
    play music "dorm.mp3"
    
    scene bg dorm
    with fade
    
    "填饱肚子的我回到宿舍，面对着的是眼镜老师留下的软工作业。"
    "对于我这样不爱拖沓的人，一旦有了什么事就想马上把它弄完"
    "可能因为这样才会经常有发自内心的疲惫吧。"
    
    
    w "呼。。。"
    "揉着手腕，看着刚完成的软件工程作业，我点了点头"
    "认真起来的话，这根本不算什么啊"
    "看着桌上的钥匙扣，不知道为什么竟然有点激动"
    "像这样期待的爬山时光，有多久没有了呢？"
    "已经两年了啊。。"
    "时间过得还真是太快了"
    "到底是怎么和她认识的呢"

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

    m "多谢wendy哥！话说明天你还去爬山诶？有什么发展么，和tingting"

    show mxin bad smile

    w "有个鬼啊！我们只是好朋友好不好！"

    m "诶~真无趣。。。"

    hide mxin bad smile
    with dissolve

    "说罢缓缓地回到了他的位置上，仿佛刚才一堆谈话都是xjb扯出来的一样"

    w "好朋友吗。。"
    
    "就这样，约定的周六到来了"

label north_gate_first_day:
    
    play music "outdoor!.mp3"
    scene bg northgate
    with dissolve
    
    "像往常一样，我按时到了北门等着"
    "一般她都会慢个几分钟"
    "男生嘛，早点来等也是好的"
    "揣着兜里的钥匙扣，有点紧张"
    "（不知道她喜不喜欢这种设计的呢。。）"
    "这两个像木牌一样的钥匙扣是我在x宝上定制的，自己设计的图案，为了纪念两周年的爬山友谊"
    "大概是重感情吧？总想用点小东西来纪念一下"

    t "来这么早呀，没等太久吧"

    show tingting smile
    with dissolve

    w "哈哈没有啊，才刚到一分钟"

    t "那咱走吧~"

    show bg outdoor
    with fade

    t "wendy这周就要体测了！你准备的怎么样？嘿嘿"

    "我就是个体育白痴，从以前到现在一直都是，即使到了大学也没像其他男生一样去锻炼肌肉什么的"
    "宅在宿舍，过着小埋一样的生活才比较符合我的风格"

    w "唔。。没怎么准备诶，这两天跑了一下步，还是很方的。你呢"

    t "我平常走动比较多，这两天就没怎么跑，不过每周的爬山还是帮了不少忙的，主要是减肥嘿嘿。。"

    "这大概就是所谓的谦虚吧，我觉得tingting即使没怎么运动也比我强不少。"

    w "还能再减？真强啊。。"

    "她有点不好意思地笑了笑"

    t "可以啊！告诉你哦，我之前测了测体重，有轻了好多的，开心！"

    w "女生啊，女生。。。"
    
    "话说回来她的确是有参加学校的一个什么BXZ协会，常常出去骑车郊游竞走啥的，就很运动"

    w "你还泡养生茶，还那么早睡，轻了也是应该的啊"

    t "养生茶什么的，就跑泡过几次冬瓜茶，还不太熟悉呢"

    w "emmmm。。"
    
    menu:
        "告诉你一个很好的养生茶配方。。":
             jump yangsheng
       
        "养生不太熟悉，马上转移话题":
            jump not_yangsheng
        
        
    
label yangsheng:
    w "告诉你哦，我妈说用枸杞和红枣啊菊花等一起泡会比较好喝哦~听说会有自然的甜味"
    t "诶~是这样吗。我平常没有甜味的时候都选择加糖的呢！"
    
    show tingting surprised
    with dissolve
    
    t "感觉学到了新知识！"
    w "哈哈哈不了不了，我自己也没泡过，就当是给你参考下"
    
    jump end_yangsheng
    
  
    
label not_yangsheng:
    w "唔。。养生什么的我也不是很懂，最近还经常爆肝，熬夜到一点，感觉被掏空"
    "虽然Mxin都不觉得一点是晚啦。。"
    
    show tingting unhappy
    with dissolve
    
    t "你啊，整天就这么晚睡，不像我，早早就睡了，身体倍儿棒"
    w "。。。。"
    w "好了好了我知道了"
    "（这家伙分明在幸灾乐祸嘛）"
    
    jump end_yangsheng
    

label end_yangsheng:
    "就这样我们一路扯着零碎小事上了山"

    # 此处为游戏结尾。

    return
