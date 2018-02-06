# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define t = Character("Tingting")
define g = Character("Girl")
define m = Character("Mxin")
define c = Character("Cong")
define y = Character("Yuan")
define w = Character("[povname]")

#define image here that can show in specific position
image cong = Image("tingting smile.png",xalign=1.0)
image yuan = Image("tingting smile.png",xalign=-1.0)


init python:
    
    #the good feeling for ting of wendy
    Melody = 0
    

# 游戏在此开始。
            
label start:
    
    play music "classroom.mp3"
    
    scene bg classroom
    with fade


    #let player enter their name
    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
             povname = "Wendy"
    
        
    "又是平凡无奇的一天呢……"
    "下课的钟声如往常一般按时响起，讲台上那个眉飞色舞的眼镜老师（至少我是这样叫的）喝了一口养生茶"
    "好了今天就到这"
    w "呼。。终于结束了么"
    "我伸了个懒腰，合上课本"
    "最近的大量作业大概已经让我精神有点疲倦了吧。我凝神看往窗外，思索着待会要去吃些什么以满足肉体的需求"
    w "精神的疲惫。。只有吃饱肚子才能缓和！那今天就去出冒菜吧！"
    "刚想起身，发现一个女孩子挡在我面前"
    
    show tingting smile with dissolve
    
    
    g "嘿！明儿还去爬山么！"
    "正在说话的是我的好朋友，婷婷，我们一起爬山竟然已经有两年了，时间过得真快"
    w "好啊！还是正常时间？"
    t "哈哈！好！那不见不散"
    
    hide tingting smile with dissolve
    
    "讲毕，她像一阵风一样挽着舍友溜了出去"
    w "或许是食物的召唤吧。。跑得这么快。不管怎么说我肚子也有点饿了，先去吃饭好了"
    
    stop music fadeout 1.0 

label dorm_first_day:
    
    play music "dorm.mp3" fadein 1.0
    
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

    scene bg hid_face_with_mist
    with fade

    t "要不要一起去爬山呀？"

    scene bg dorm
    with dissolve

    w "只能说是缘分吧"

    m "wendy，借你实验报告我看看？懒得写啦"

    show mxin normal with dissolve
   

    "正在说话的是我的舍友，Mxin。和我不一样，他学习非常好，根本不需要为学习花上太多时间"

    w "又整天泡妹不做作业了？最近翘课很多哇"

    m "泡妹只是兴趣使然，学习才最重要啦老哥？"

    "（信你才怪啊。。！）"

    w "行吧。等下发你"

    m "多谢wendy哥！话说明天你还去爬山诶？有什么发展么，和tingting"

    show mxin bad smile with dissolve

    w "有个鬼啊！我们只是好朋友好不好！"

    m "诶~真无趣。。。"

    hide mxin bad smile with dissolve
    

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

    show tingting smile with dissolve
   

    w "哈哈没有啊，才刚到一分钟"

    t "那咱走吧~"

    show bg outdoor with fade
    

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
    
    show tingting surprised with dissolve
    
    
    t "感觉学到了新知识！"
    w "哈哈哈不了不了，我自己也没泡过，就当是给你参考下"
    $ Melody+=1
    
    jump end_yangsheng
    
  
    
label not_yangsheng:
    w "唔。。养生什么的我也不是很懂，最近还经常爆肝，熬夜到一点，感觉被掏空"
    "虽然Mxin都不觉得一点是晚啦。。"
    
    show tingting unhappy with dissolve
    
    
    t "你啊，整天就这么晚睡，不像我，早早就睡了，身体倍儿棒"
    w "。。。。"
    w "好了好了我知道了"
    "（这家伙分明在幸灾乐祸嘛）"
    
    jump end_yangsheng
    

label end_yangsheng:
    "就这样我们一路扯着零碎小事上了山"
    
label mountain_top:
    
    play music  "mountain_top.mp3"
    
    scene bg mountain_top
    with fade
    
    "封尘市的这座山一直是这样"
    "山顶的这个看台就刚好可以看到大半个城市的样貌"
    "即使早上有雾，还是很美的景观"
    "虽然我不是个特别喜欢这种一览众山小的角度"
    "（不得不说每次看都有新的感觉呢。。）"
    w "tingting，等我拍几张照。"
    "拿出手机开始找角度，但是发现找来找去都是那样"
    "索性就随便拍了一张，苦笑"
    "大概自己的摄影技术从一开始就没进展吧"
    t "好啦？那我也拍几张，等我下哦"

    show tingting smile with dissolve


    "她端起手机，眯起眼睛找了一下角度"

    t "其实我想拍全景"

    w "光看起来有点太亮了，要不要我帮你遮一下？"

    t "嘿嘿，好啊"

    "我的手成盖状挡在她的手机上。总算使得拍摄光线稍微少了一些。"

    t "嗯唔。。我看看。。"

    "她拿着手机就转了起来，缓缓地"

    "全景就是麻烦啊，我想到"

    show tingting disappointed with dissolve
    

    t "还是不太行诶，我再试一次"

    w "好好"

    "不知是否帮忙遮挡的原因，我离得似乎有点近"

    "tingting还是很可爱的"

    "一丝不苟在拍照的样子竟觉得有点看不腻"

    "！"

    "摇了摇头"

    "不行，我在想什么啊，咱们只是好朋友"

    t "哈哈，这回好了"

    show tingting smile with dissolve
   

    "她给我看手机刚拍的图，的确是比刚才要好多了"

    "至少没有很暗看不清图片了"

    w "还行啊，不过转来转去有点麻烦这就是我不爱全景的原因"

    t "这，这样啊。。"
    
    "她看起来似乎对照片已经满足了，但仍在查看细节部分"
    
    menu:
        "提起钥匙扣":
            $ memo = True
            jump memory_key
        "还是算了吧，太突兀":
            $ memo = False
            jump no_key

label memory_key:
    
    "我决定和她说起这个钥匙扣的事情"

    w "tingting，你过来一下，嘿嘿"

    show tingting confused with dissolve
    

    t "什么呀，神神秘秘的"

    "我拿出钥匙扣，黑檀木材质在阳光下显露出一股古朴的气息"

    w "给咱俩定做的钥匙扣！寻思着咱们都爬了两年多的山了，你也知道的，我总想将某段重要的回忆保存下来，或许钥匙扣正是这样的一个载体吧。"

    t "哈哈哈你可真有意思。不过我也很珍惜这段美好的时光，虽然我没有你这么有心~"

    w "你挑一个吧~咱俩各一半"

    "tingting闭上眼随手摸了一个"

    show tingting surprised with dissolve
    

    t "诶~我这一半有bzs的字，你那一半应该就没了吧？"

    "bsz是我们爬的这座山的名字"

    "我笑了笑"

    w "没有也不影响咱们是山友的事实，至少我这一半还有‘登山队’三个字？"

    t "那我会好好挂在钥匙扣上陪着我的"

    "阳光照耀着我俩，我觉得此刻，一定是我人生中最美好的一个瞬间了"
    
    $ Melody+=1
    
    jump end_mountain
    
label no_key:
    
    "握紧了口袋里的钥匙扣"

    "我还是退缩了"

    "突然送钥匙扣什么的啊，很矫情嘛"

    "有很奇怪，明明也不是什么特别重要的事？"

    "或许她心里根本没有觉得爬山是非常特别的事吧？"

    "可能只是对我来说而已"

    show tingting confused with dissolve
    

    t "wendy怎么了嘛~突然愣住了"

    "拍完照的她甚至压了一下腿，然后发现我已经呆住了"

    w "哈哈。。没事没事，刚在想一些事"

    t "噗。。想些啥呢！难道是最近的感情出了啥问题？"

    "我连连摆手"

    w "没，没啦！最近都没有什么感情的事"

    "tingting 似乎还不太相信，撇了撇嘴，但也只好作罢"

    
    jump end_mountain

label end_mountain:
    
    t "那我们下山吧，开始晒了"

    w "好的。"
    
    if not memo:
         "但是不知道为何，我心里有点压抑和后悔的感觉"

label playground:
    
    play music "playground.mp3"
    
    scene bg playground
    with fade
    
    "体测的日子很快就到了"
    "今天的天气格外晴朗，可能是时间比较早的关系，太阳光很充足，均匀的洒在操场上"
    "趁着考试前跑了几天，自我感觉还是很好的"
    w "这回体测应该好多了吧"
    "依稀记得上一年虽然也及格了，但是跑完1000之后整个人那种虚脱的感觉"
    "恶心，想吐，很不好受"
    "我苦笑了下"
    "还是太弱啊，都是因为平常太宅了"

    "操场上人还不算多，我决定先把心头最大的石头--1000米解决"

    c "你也来了啊，这么早，wendy"

    y "我们俩刚做完别的项目"

    show cong at right with dissolve
    

    show yuan at left with dissolve
    

    "正在说话的是同班的两个同学，cong 和yuan。看来是来的很早的样子，其他项目都已经做完了"

    "我凝神直视跑道"

    w "一起跑1000米？"

    c "可以啊！"

    "yuan 开始做原地热身运动，身为前旗队队员，我觉得对于他跑1000应该并非难事"

    w "yuan等我一下啊待会儿，嘿嘿"

    show yuan shy with dissolve
    

    y "哈哈没有，我跑的很慢的啦"

    "请要跑1000的同学，过来这边带胸牌和准备！"
    
    hide cong with dissolve
    
    hide yuan with dissolve
    

    "响起了工作人员的声音，我吸了口气，过去领了牌子带上，在跑道上小碎步地做着要出发的姿态"

    "突然，我不经意地瞄到操场入口那里"

    "是tingting"

    "今天扎着个单马尾，穿着普通的短运动裤和运动上衣，可能是觉得待会跑步会出汗吧，脖子上还围着一条毛巾拿来擦汗，这不禁让我想起古装电视剧里面的跑堂的店小二。"

    "她似乎看到了我，朝我挥挥手"

    "各就各位。。预备。。跑！"

    "砰地一声枪响之后，我随众人向前冲去，经过tingting的时候，她似乎朝我说了一句‘加油’？"

    "。。。"
    "。。。"
    
    scene bg sky
    with fade
    
    "我瘫倒在地上，虽然不是瘫倒，但实际也差不了多少。"

    "大口大口吸着气。最后一圈的加速耗尽了我几乎全部体力。"

    "一屁股坐在操场旁的水泥地上。缓和着跳动过快的心。"

    "tingting 递过来一大瓶宝以水。"

    show tingting smile with dissolve
    

    t "辛苦了！来喝点水吧"

    "我接过水，啪地一声扭开，然后开始吨吨吨。。。"

    t "哈哈你喝慢点！一次喝太多也不是太好哦，最好等缓一会再接着喝"

    "我擦了擦嘴角溢出的水"

    w "倒是你，你跑了没呀"

    "tingting笑道"

    t "还没有啊~我准备跑了"

    w "好，我看着你跑给你加油鼓劲"

    t "别，，！我会不好意思的！"

    w "你就正常的跑就行了，别管我，哈哈"

    "。。。"
    
    scene bg running
    with fade

    "她开始跑了，每个步伐都非常稳，左右臂有规律的在滑动着，马尾随着气流一上一下地跳动着"

    "我坐在操场内看着她缓缓从内圈跑过，女生的话跑800就行了"

    "而我相信她是完全没有问题的"

    scene girl callback memo
    with fade

    g "wendy，你看我跑的比你快多了吧"
    g "你追不上我追不上我，嘿嘿~"

    "少女银铃般的笑声和运动场，此情奇景我以前是否在哪里遭遇过?"

    scene bg playground
    with fade

    t "呼。。！"

    "tingting冲线了，800米也只是一瞬间的事情。"

    w "好棒！快过来歇会吧。"

    "tingting缓缓走过来，脚步竟然有点虚浮，差点崴到脚"

    t "诶？！"

    w "哇。。！你没事吧，吓死我了以为你要跌了"
    
    "赶忙做出要扶住她的姿态"
    
    "这家伙还真不让人省心，不会是假装轻松的？可能我被她机灵的伪装骗过了"

    show tingting shy with dissolve
    

    t "没，没有啦，只是刚跑完脚有点软，我歇一会儿就好"

    w "看你满头大汗的，先擦一下吧"
    
    menu:
        "拿起她的毛巾帮忙擦汗":
            jump use_tower
        "递上毛巾和水":
            jump offer_tower

label use_tower:
    
    
    "她的脸上一开始露出一股诧异的神情，但是转而化作一股微笑"
    
    "我们就这样，站在操场边上的树下聊了一下午"
    
    "真希望这样的时光不会结束呀。。"
    
    $ Melody+=1
    
    jump playground_end
    
    
    

label offer_tower:
    
    "她接过水咕噜咕噜地喝了起来，汗水在阳光下闪烁着"
    
    show tingting smile with dissolve
    
    t "谢谢哦！"
    
    "她的笑容是那样的令人目眩神迷"
    
    jump playground_end
    

label playground_end:
    
    play music "classroom.mp3" fadein 1.0 fadeout 1.0
    
    scene bg classroom
    with fade
    
    "体测过后，无聊的日常也接着进行"
    
    "我抬头看向窗外，十一月的天气逐渐转凉，树叶也变得萧索了呢"
    
    "这种好天气，居然要听z师傅讲这些狗屁不通的东西，真是痛苦。"
    
    "我无聊的转起笔来，连续上三节课的都是犯罪啊！！心里想"
    
    "目光投向右边第二排"
    
    "今天她也很认真的听着老师讲课"
    
    scene bg girl_on_class
    with fade
    
    "究竟是什么能让她这么认真呢"
    
    "但是我很喜欢她的眼神，那是一种对知识渴望的眼神，可以看出来不是假的"
    
    scene bg classroom
    with fade
    
    "体测时她那双有神的黑色眼瞳突然在我脑海里闪过"
    
    "唔。。为什么我会这么在意她呢"
    
    "这二十几年来，这是唯一让我心动的人"
    
    "她的热情，她的认真，一直感动着我"
    
    "还有那双眼睛"
    
    if Melody>=2:
        
        "她似乎注意到了注视她的灼灼目光，四周张望，正好与我四目相对"
        
        w "哈。。。！"
        
        "我赶紧低下头"
        
        "其实，，为什么我会低下头呢"
        
        
    "诶大家注意，这个地方我可是要考的"
    
    "老师带着狡诈的眼神扫视大家，像是一头看着待宰羔羊的恶狼"
    
    "我一个寒战坐直了身子"
    
    w "还是先认真上课吧。。"

label exam_review:
    
    play music "dorm.mp3"  fadeout 1.0 fadein 1.0
    
    scene bg dorm
    with fade
    
    "转眼又到了复习周"
    
    "这个学期也普普通通地过了呢"
    
    "想了想，自己定的目标完全没完成嘛"
    
    "苦笑了下，摇了摇头，准备收拾去图书馆学习的书本明天去占位置"
    
    m "怎么，不约tt一起去么？"
    
    "拿书本的手突然楞在半空中"
    
    "mxin说得对啊。没有什么比在一起学习要开心的呀"
    
    "我啪地一下做到电脑前打开了微信"
    
    
    menu:
        "发送信息":
            $Melody +=1
            jump message_sent
        
        "不发送信息，独自前往":
             $Melody -=1
             jump message_not_sent
       

#lead to libary story
label message_sent:
    
    #插入微信截图以及打字音效

    scene bg dorm
    with fade
    
    show bg wechat
    with dissolve
    
    w "婷婷，明天开始一起去图书馆学习么！"
    
    "等了两分钟之后，有了回信"
    
    t "好啊！你想去哪儿"
    
    w "我们早点去中央图书室占位如何？"
    
    t "好主意！中央图书室有很多座位呢，还有隔间，环境很安静呢！"
    
    w "那就这样吧！明天我取得早的话我占个位,靠近花园那边的座位可以？"
    
    t "嗯嗯可以哦"
    
    w "明天见！"
    
    hide bg wechat
    with dissolve
    
    "关掉微信，我把最后一本书放进书包，然后往床上一躺"
    
    "两周的复习，要一起加油啦！"
    
    jump libray_learn


#lead to bad end
label message_not_sent:
    
    "想了一下，还是把微信关掉了"
    
    w "复习的时候还是一个人吧，两个人的话容易分神啊"
    
    "脑海里浮现出她甜甜的微笑和卡姿兰大眼睛"
    
    "唉。。。"
    
    "我把最后一本书放进书包，然后往床上一躺"
    
    "两周的。。要自己加油啦！"
    
    jump libray_learn

label libray_learn:
    
    play music "library.mp3" 
    
    scene bg library
    with fade
    
    "学校的图书馆有六层，而且面积十分地大，建筑风格是欧式的，连上下的步行楼梯都是用古老的木材建造的"
        
    "一楼是阅览厅，二楼是中央图书室，三楼以上是馆藏"
    
    "二楼户外还有一个花鸟庭院，是闲暇放松的好去处"
    
    "每当到了复习周，就会有很多人来占座学习"
    
    "我倒是觉得，平常不学的话，这个时候抱佛脚虽然有用，但是意义不大"
    
    "我信步走到二楼，找到靠近庭院的一个小隔间，阳光刚好能从窗户的缝隙偷过来一点"
    
    "拿出 ‘人工智能在生活中的应用‘ 这本书和笔记本，我开始复习"
    
    
    if Melody >=3:
        #邀请了过来
        
        t "早呀！"
        
        w "哦，早啊，来来来，还好我来的早，迟一点就没位置了，二楼可是十分受欢迎的呢~"
        
        show tingting smile
        with dissolve
        
        "她今天穿着很普通的长袖水手服，头发也放了下来，双眼炯炯有神，充满斗志"
        
        t "我今天必须把这本人工智能看到一半！之前在宿舍真是太难专注了"
        
        w "哈哈好，一起加油，不懂得我们在相互探讨"

        hide tingting smile
        with dissolve
        
        "。。。"
        
        "。。。"
        
        
        "阳光透过窗洒在桌子上，落到我的手旁"
        
        "我停下手中的笔，握住这缕阳光"
        
        "tingting似乎还在很专心地思考问题，完全没注意到我开始开小差了"
        
        w "啊这么一想，肚子开始饿了呢"
        
        "才学了两个小时就累了，我的战斗力还是太弱了"
        
        "她专注的思考问题的样子让我不忍心打扰她"
        
        "毕竟中午去吃什么，并不是一个大问题"
        
        "她仿佛似乎遇到了瓶颈，一时皱起了眉头"
        
        "拿起笔帽，嘴唇轻咬"
        
        w "遇到什么问题了么"
        
        "我笑道"
        
        t "嗯嗯是啊，你帮我看看这个问题，关于人工智能的应用。。。"
        
        scene bg figure problem
        with fade
        
        
        "说着就过来我这边，贴近后背直接指着书给我看"
        
        w "笨，，笨蛋！靠太近了啊（小声咕哝）"
        
        t "啥？"
        
        "一脸不解的样子我也真是拿她没办法"
        
        w "咳咳，没啥事，总之这道题是这样的，首先。。。"
        
        t "嗯嗯，哦原来是这样子。。。"
            
    else:
        
        "过了不久我突然不大淡定，书本内容太枯燥，实在太容易分神"
        
        "我起身准备去泡一杯咖啡，就在二层的楼梯拐角处，有一部自助咖啡机"
        
        w "喝点咖啡应该有助于提神吧。。"
        
        "我缓步走向咖啡机"
        
        
    
    # 此处为游戏结尾。

    return
