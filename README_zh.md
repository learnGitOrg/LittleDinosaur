Product vision:
本产品旨在让各位辛勤劳作的打工人在枯燥无趣的生活中能够获得一份简单的乐趣，提升士气的同时进而提高打工效率以便榨取剩余价值。

本产品灵感来源于chrome内置的断网后的恐龙跑酷小游戏以及安卓内置钓猫彩蛋。

娱乐作为人类生命活动中不可或缺的一部分，自太古洪荒便开始以长盛不衰的生命力发展着，跨过千年岁月来到如今，高度信息化的时代催生出了无数繁复多样的娱乐方式，从宏伟辉煌的网络游戏狂欢到如日中天的短视频平台，还有深不可测的单机游戏世界供给我们探索，可以说，任何拥有现代电子设备的打工人都是不应该缺乏娱乐方式的。
然而，这些娱乐方式都或多或少有着一些缺点。
想像一下在你辛勤劳作了一整天之后打开英雄联盟想要在召唤师峡谷来一场酣畅淋漓的战斗放松一下进入游戏却发现下路和辅助因为一个兵骂了起来在一番污言秽语之后两人双双挂机而你纵使以自己精湛的技术在对位上碾压对手奈何双拳难敌四手在一番负隅顽抗后依然无能为力输掉比赛退出到比赛结算界面一看原来自己已经十二连败顺便掉了个段。对于一个已然身心疲惫，满心期待着通过网络游戏来放松一下的打工人来说，这会对他的心灵造成多么巨大的伤害啊！

通过上面的例子可以看出，选择网络游戏作为娱乐方式的一大缺点就是它提供的服务是不稳定的，即无法确保用户通过此方式能得到放松，甚至有概率对用户造成伤害，这显然是一个无法忽视的巨大缺陷。
不仅是网络游戏，其他娱乐方式也多多少少包含着一些难以忽视的问题，短视频纵使能以小段的信息片段吸引用户不断看下去，但高质量作品的缺乏却会导致用户往往在结束观看后感觉自己在浪费时间——“我花了这么多时间看了个什么玩意儿啊！”进而萌发罪恶感；而单机游戏引以为傲的游戏性在另一方面亦提高了用户的上手难度，且其动辄数十小时的游戏时长也很容易让打工人望而却步。
总的来说，服务不稳定，趣味不足，需要花费大块时间可以说是当前大部分娱乐方式的通病。

那么有没有一种既简单又稳定还不需要特意去花费时间与精力的娱乐方式供打工人选择呢？

我们从几个软件内置的小游戏中找到了灵感。
Chrome，谷歌旗下浏览器，作为一款浏览器来说它的确是十分优秀的，但让我总是选择使用这款浏览器的原因却是因为其内置的小游戏。如果我们在断网的情况下打开chrome，我们便会发现在断网提示上方出现了一个像素小恐龙，倘若此时按下空格键，恐龙前方的道路便会延伸出去，一款简单的二维像素风跑酷游戏就这样开始了。这是一个非常简单有效的设计：用户不必特意去启动游戏，这显然极大地降低了对用户的启动性的要求（用户不必特意去思考自己应该去玩什么，而只需要选择是否要玩）而另一方面，它也准确地抓住了用户需求：断网时往往正是用户无事可做之时，那此时又有谁能够拒绝这样一款已经自动打开等待游玩的游戏呢？这甚至为这款浏览器平添了一丝人文关怀：即便是断网了这款浏览器也能以某种方式服务用户。当然，这款小游戏也满足了作为一款游戏的基本要求：它简单而有趣，可爱的像素小恐龙更是让人讨厌不起来。
在安卓7.0之后，如果连续点击版本号，安卓手机的任务栏中会出现一个新的图标——一个名为empty dish的碟子，在点击之后，会出现四个食物选项：bits fish chicken treat，在选择其中一种食物之后，empty dish就会被替换为这种食物，这个彩蛋到此似乎就结束了——然而事实并非如此。在一段不确定的时间之后，用户的手机会收到一条信息：A cat is here! 点击通知，用户会进入一个界面，里面会展示用户得到的小猫——原来这是一个用食物钓猫的游戏！它是如此的简单，以至于用户需要的操作时间不超过五秒，它也不需要额外花费用户的精力，用户只需放好食物等待猫猫上钩，时间的不确定性也弹性地限制用户不必特意进行等待，但它却能给用户带来一点难能可贵的惊喜与情趣：用户获得的每一只猫都是独一无二的，它有着唯一的编号，有着独一无二的花纹，用户还能对每一只猫进行命名和分享，这与前面的小恐龙游戏是异曲同工的——简单，有趣，可爱。

聊了这么多之后，终于要回到正题了：我们究竟想要做一个怎样的产品？

简单来说，这是一款桌面宠物，暂定名为Little Rabbit。以下是我们当前想要实现的功能：

在大部分情况下，它只会隐藏在后台，但在特殊情况下（诸如断网，用户长时间未操作），它会从角落中蹦出来，请求与用户互动，用户可以通过简单的操作与它进行游戏。



Two scenarios:
1. Little Rabbit降低生活压力
张三是一名刚刚毕业的大学生，刚刚在深圳找到了自己的第一份工作，成为了一个普通的互联网公司的一名普通程序员。张三在大学时期特别喜欢玩各种网游，在刚刚入职时，张三还保持着每天游戏的习惯，但是在工作一段时间后，张三发现自己渐渐越来越腾不出时间去玩网游了，而网络游戏快速的版本更迭也使张三渐渐觉得力不从心了，这便产生了一个恶性循环——工作压力大导致没有时间玩游戏，游戏玩得少导致技术变差，技术变差导致玩得不开心，玩得不开心导致工作压力大。终于，张三决定戒掉网游，士气低迷的张三决定为自己寻找一个替代品，最后，他找到了Little Rabbit，简介里的小恐龙似乎挺可爱的，张三想着，不过这个桌面宠物体量并不大，玩法应该也不多，张三跟着游戏引导试着和小白兔玩了玩，放了块食物就继续工作去了。
张三今天的工作格外的困难，这对于刚刚戒掉网游心神不宁的张三更是雪上加霜，一堆不明所以的bug搞的张三焦头烂额，就在张三几近崩溃之时， 一只小白兔偷偷摸摸地从屏幕边缘跑了出来，小白兔儿滑稽的动作顿时就把张三逗笑了，他调出了小白兔，玩了一会儿，顿时感觉自己冷静了不少，在一番苦战之后，终于解决了bug。
在接下来的日子里，张三努力地适应着没有网游的生活，虽然刚刚步入社会的压力仍然让他有些焦虑，但是每当他看到这个小东西在屏幕里面跑来跑去的时候，都会感到一阵轻松。就这样，Little Rabbit陪着张三度过了一段最为艰难的时光。

2. Little Rabbit提升生活乐趣
李四是一名二十多岁的工程师，供职于某家国企，在几年的工作后生活渐渐稳定了下来，但稳定的同时李四也越发觉得生活平淡如水乏善可陈，李四从小就热爱学习，对于同龄人热衷的游戏，视频之流都是没有什么兴趣的，也因此缺少了和他人交际的共同语言。为了改变这一现状，李四决定选择Little Rabbit来拉近和同龄人之间的距离，起初李四并不觉得屏幕里这个会偷偷蹦来蹦去的小东西有什么好玩的，只是当做一个宠物来养，无聊的时候就调出来玩玩小游戏消磨一下时间。
这天，李四正在午休时间百无聊赖地玩着Little Rabbit，想着怎么和同事们打好关系，这时，隔壁桌的小花因为一个工作问题来请教李四，看到屏幕的那一刻小花就被屏幕上可爱的身影吸引了，李四借此久违地和同时聊起了天。
自此以后，同事们眼中李四死板的形象渐渐被改变了，大家渐渐愿意去和李四交流，而在于大家交流之后，李四也渐渐开始了解同龄人的兴趣爱好和其中的乐趣，就这样，借助Little Rabbit，李四改变了自己枯燥的生活，改善了与同事之间的关系，提升了自己生活的乐趣。

Features:
1.轻量级娱乐工具，操作简单，耗费精力少，低启动性要求，高度趣味性，仅消耗极少的碎片时间
2.用户可以通过右键快捷栏主动唤出宠物与其交互。
3.用户可以联网下载不同种类的宠物，也可上传自制宠物，但产品可以完全离线运行