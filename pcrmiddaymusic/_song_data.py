# 歌曲简介: [歌曲来源, 歌曲id, 前缀说明, 歌曲名称, 演唱者, B站视频BV号(只使用其封面), 活动介绍(可为空)]
SONG_DATA = {
    "初音的礼物大作战ed": ['qq', 215041130, "第一次活动: ", "Smiley Contrast", "大桥彩香/小清水亜美", "BV1WC4y1p72H", "初音为了鼓励在牧场努力工作的栞，准备送给栞一件惊喜大礼。初音的礼物大作战就此开幕！"],
    "小小甜心冒险家ed": ['qq', 217508272, "第二次活动: ", "Little Adventure", "诸星堇/小倉唯/日高里菜", "BV1qZ4y1H7Aa", "想让镜华辅导学习的未奏希，找到了正在精灵之森游玩的镜华与美美。在镜华的辅导下开始学习了，但是……"],
    "吸血鬼猎人with伊莉亚ed": ['qq', 235068773, "第三次活动: ", "Peaceful*ちゃんぷるー", "内田真礼/高森奈津美", "BV1At4y1X7Rd", "为了打败传说中意图统治世界的吸血鬼，真步和香织，踏上了成为吸血鬼猎人的旅途！"],
    "危险假日！海边的美食家公主ed": ['qq', 213442914, "第四次活动: ", "えがおのマイホーム", "悠木碧/堀江由衣", "BV1mZ4y1K7Ut", "在繁华街的抽奖中「美食殿堂」的成员们获得了「魅力南国之旅」的招待券。这本该成为一个最棒的假期，然而……"],
    "珠希与美冬的无人岛0金币生活ed": ['qq', 221048633, "第五次活动: ", "キンキラ☆ハピネス！", "松嵜麗/田所梓/今井麻美/沼倉愛美", "BV1aW411Q7zp", "在流传着「实现愿望之岛」的海岸边，珠希与美冬突然困意袭来。等到醒来的时候，已经身处无人岛？"],
    "黑铁的亡灵ed": ['qq', 221048634, "第六次活动: ", "Aloofness Code", "川澄綾子/高桥智秋/茅原实里/下田麻美", "BV1Ht411y7AL", "纯想要解决王宫的骚乱，却迟迟不能查明凶手。敌人究竟是谁？王宫骑士团，四人的战斗即将开始！"],
    "不给布丁就捣蛋！约定的万圣节派对ed": ['qq', 228368072, "第七次活动: ", "もっと!ふたりのパ〜ティ〜ナイト", "大坪由佳/雨宮天", "BV1iE411b7fQ", "在万圣节的夜里，从街上感受到强大灵力的忍，与宫子出发前往调查。而那却是，恐怖一夜的开端……"],
    "暮光破坏者ed": ['qq', 232903630, "第八次活动: ", "サイツヨでしょ、でしょ", "髙野麻美/佳村遥", "BV1Yb411T7En", "将各自的目的藏于心中，前往同各方向的流夏、杏奈及七七香与潜伏的巨大邪恶之战即将拉开序幕！"],
    "忘却的颂歌ed": ['qq', 228368073, "第九次活动: ", "Ding Dong Holy Night♪", "芹澤優/植田佳奈", "BV1ZJ41167We", "黑暗悄悄逼近圣诞节前热闹的街道，而当黑暗笼罩了千歌及「咲恋救济院」时，狂乱的圣诞节即将掀开序幕……"],
    "新春破晓之星大危机ed": ['qq', 244056944, "第十次活动: ", "TwinkleStars", "種田梨沙/早见沙织/东山奈央", "BV1c4411M7WN", "在除夕迫在眉睫的日子里，因为想留下今年最后的回忆而接受委托的3人，为了准备新年而前往街上采买时……"],
    "情人节之战！正中红心的甜蜜战斗ed": ['qq', 232903629, "第十一次活动: ", "SUPER CHOCOLATE", "生天目仁美/阿澄佳奈", "BV1dp4y1D79H", "交织了各式各样感情的情人节……而现在，惠理子与静流间炽热的巧克力战争即将掀开序幕！"],
    "王都的名侦探 叹息的追缉者ed": ['qq', 235068774, "第十二次活动: ", "未解決な想い", "小松未可子/水濑祈", "BV1of4y1Q74p", "因马车比赛而热闹非凡的城镇发生了多起悬疑事件，无法视作是偶然的意外——藏在暗地里的恶意……王都的名侦探，将挑战这前所未有的艰难事件！"],
    "在阿斯特朗盛开的双轮之花ed": ['163', 1380874627, "第十三次活动(玛娜莉亚魔法学院联动): ", "Crossing Destiny", "日笠陽子/福原綾香", "BV1gK4y1x75x", "当安与古蕾娅正在玛娜莉亚魔法学院帮忙露做功课时，突然被一道不可思议的光包围了……双轮之花，即将在这个异世界盛开！"],
    "将军道中记 白翼的武士ed": ['qq', 244056941, "第十四次活动: ", "白翼のグローリエ", "大空直美/佐藤聡美/長妻樹里/大関英里/辻あゆみ", "BV1m4411y74C", "求救的呼喊声，今日也回响在八百八町中……纯白之翼将要除恶，我若不做将军、谁做将军！"],
    "Re:从零开始聚集的异世界餐桌ed": ['bili', "BV1Bz411z7Cp", "第十五次活动(Re:0联动): ", "Re:lation", "高桥李依/水濑祈/村川梨衣", "BV1Bz411z7Cp", "由异世界来到了兰德索尔的爱蜜莉雅等人与「美食殿堂」的成员们一同追查一起失踪事件，但是……"],
    "铃奈的彩虹舞台ed": ['qq', 248110954, "第十六次活动: ", "背伸びFirst Kiss", "伊藤静/久野美咲/上坂堇", "BV1Xt41157gz", "那里会是座雨未曾停歇的南国之岛……贯穿下着悲伤之泪的雨云的虹桥，宣告着最棒的假期将要揭开序幕！"],
    "盛夏的真步真步王国！浪花拍岸的灵魂之夏ed": ['qq', 248110953, "第十七次活动: ", "We Are Golden", "内田真礼/小松未可子/高森奈津美", "BV1qJ411j72y", "真步带着她最珍视的玩偶们，与公会成员们造访了夏季的海边。本应一起度过一段快乐的时光，可玩偶们却突然失去了踪影……？"],
    "森林的胆小鬼与神圣学院的问题儿童ed": ['qq', 248113890, "第十八次活动: ", "なかよしセンセーション", "小原好美/佐仓绫音/種崎敦美", "BV1oz4y1D7R5", "碧作为交换生造访了圣德蕾莎女子学院，而在那里等着她的，是充满个性的问题儿童们！"],
    "小小勇敢的万圣节之夜ed": ['qq', 248113891, "第十九次活动: ", "トリックホリック(Trick Holic)", "日高里菜/小倉唯/诸星堇", "BV1j7411Z7Rz", "小小甜心一行人原本打算到幽灵鬼屋去要糖果，却反而被关在了屋内……怀着小小勇气的冒险谭，即将展开！"],
    "龙的探索者们ed": ['qq', 261407114, "第二十次活动: ", "in flames", "藤田茜/小市眞琴/大西沙織", "BV1gE411c7bg", "为了暗中调查公会「龙族巢穴」而联袂前往的智与茉莉，她们到达的是……充满谜团的未开发之地，艾尔皮斯岛！"],
    "礼物大恐慌！兰德索尔的圣诞老人们ed": ['qq', 261407130, "第二十一次活动: ", "Call Me Darling!", "日笠陽子/福原綾香/木戸衣吹", "BV1Tg4y1i7Ym", "仅有一人能够当上圣诞老人。而成为了圣诞老人候补的伊莉亚等人为了将喜悦分送给城里的人们，在兰德索尔中来回穿梭着……"],
    "狂奔！兰德索尔的公会竞速赛ed": ['qq', 267175838, "第二十二次活动: ", "SAI＊KOUスタートダッシュ", "M・A・O/立花理香/悠木碧/伊藤美来", "BV17T4y1u7Pr", "赌上豪华奖品与福气公会的称号，「美食殿堂」与铃莓将携手挑战「新春兰德索尔的公会竞速赛」！"],
    "二人是魔法少女Misty&Purely ed": ['qq', 267175904, "第二十三次活动: ", "木もれびモンタージュ", "水濑祈/小清水亜美", "BV1Ea4y1v79c", "巨大的灾难悄悄逼近了兰德索尔。就在此时，有两名少女挺身而出。以爱与希望变身吧！魔法侦探&魔法猎人！"],
    "星光公主Re:M@ster！ed": ['bili', "BV1yE411V7YP", "第二十四次活动(偶像大师灰姑娘女孩星光舞台联动): ", "Great Journey", "大桥彩音/福原绫香/原纱友里", "BV1yE411V7YP", "公会「new generations」的三位成员，突然出现在「美食殿堂」一行人面前。以最顶尖偶像为目标，冒险即将揭开序幕！"],
    "恩赐的财团与神圣学院的问题儿童ed": ['qq', 269759310, "第二十五次活动: ", "青春スピナー", "佐仓绫音/種崎敦美/小原好美", "BV1VT4y1E7zV", "「圣德蕾莎女子学院(好朋友社)」的三人参加了全新的特别讲座。在成功的报酬的面前，那名为上进心的私心此刻正熊熊燃烧！"],
    "牧场的四农士，贫穷牧场奋斗记！ed": ['qq', 269759305, "第二十六次活动: ", "Heartful Place", "新田恵海/小岩井小鸟", "BV1654y1v7eo", "面对突如其来的公会征收骚动，「伊丽莎白牧场」的成员们团结一心挺身奋战！"],
    "不可思议之国的璃乃ed": ['qq', 275615975, "第二十七次活动: ", "フェアリーテイルは夢の中", "阿澄佳奈", "BV1WK4y1t7cU", "璃乃等人被书卷进了不可思议的国度，为了守护面临毁灭危机的绘本世界，璃乃等人身为「救世主」的战役即将展开！"],
    "七夕剑客旅情谭ed": ['qq', 275615978, "第二十八次活动: ", "黄昏太平旅路唄", "佐藤利奈", "BV13D4y1S72P", ""],
    "美里夏日应援！逐梦的盛夏棒球队ed": ['bili', "BV1ah411Z7Dm", "第二十九次活动: ", "あの夏のメモリー", "国府田麻理子", "BV1Rk4y1m74f", ""],
    "快乐互换的天使们ed": ['bili', "BV1jk4y1y71x", "第三十次活动: ", "ねぇねぇPlease!", "原紗友里/浅倉杏美", "BV11V41127dj", ""],
	"呐喊!绝叫!万圣鬼节ed": ['bili', "BV19i4y1E7Fs", "第三十一次活动: ", "Paradox", "早见沙织/木户衣吹", "BV19i4y1E7Fs", ""],
    "小望角色歌": ['qq', 215041131, "", "君の笑顔が見たいから", "日笠陽子", "BV1Ni4y187WU", ""],
    "千歌角色歌": ['qq', 214032974, "", "風への誓い", "福原綾香", "BV1v4411a7bx", ""],
    "纺希角色歌": ['qq', 217508273, "", "アマノジャクハート!", "木戸衣吹", "BV1X54y1q7bF", ""],
    "凯露角色歌": ['qq', 231005151, "主线第八章ed, ", "Absolute Secret", "立花理香", "BV1rQ4y1M7sB", ""],
    "慈乐之音live": ['qq', 214032971, "主线第九章ed, ", "Shining Future", "日笠陽子/福原綾香/木戸衣吹", "BV1XJ411u7Hu", ""],
    "前作op": ['163', 1309896539, "主线第十三章ed, ", "つなぐもの", "種田梨沙/東山奈央/早見沙織", "BV1kE411e7Xi", ""],
    "游戏第一部op": ['qq', 231005146, "", "Lost Princess", "M・A・O/伊藤美来/立花理香", "BV12J411w7EM", ""],
    "游戏第一部ed": ['qq', 231005147, "", "Connecting Happy!!", "M・A・O/伊藤美来/立花理香", "BV1J64y1T7gr", ""],
    "游戏第二部op": ['qq', 256334989, "", "Mirage Game", "M・A・O/伊藤美来/立花理香/種田梨沙/东山奈央/早見沙織/近藤玲奈", "BV1qz411B7ZG", ""],
    "游戏第二部ed": ['qq', 256335010, "", "Yes! Precious Harmony!", "M・A・O/伊藤美来/立花理香", "BV1v7411J7ub", ""],
}