# Manual review: 166_shoalcave_lowtideentranceroom.json

verdicts: {'ok': 7}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x08219F88 | 0x0826406F | ShoalCave_LowTideEntranceRoom_Text_AreYouPlanningOnGoingInThere | このさきに　すすむのかね？{FB}もし　よかったら\nあさせのしおと　あさせのかいがらを{FA}あつめてきて　くれないか{FB}ざいりょうが　あつまったら\nわたしが　いいもの　つくるんだがね | 你要向深处去吗？{FB}那么帮我收集一些浅滩海盐\n和浅滩贝壳怎么样？{FB}如果有足够的材料的话，\n我可以帮你制作点好东西。 | ok | PTR-OK, CN faithful |
| 1 | 0x08219F92 | 0x082640C5 | ShoalCave_LowTideEntranceRoom_Text_BringMe4ShoalSaltAndShells | あさせのしおと　あさせのかいがら\nそれぞれ　4つ　あれば{FA}かいがらのすずが　つくれるんだが⋯⋯{FB}かいがらのすずの　ざいりょう　なら\nまいにち　とれるよ | 如果浅滩海盐和\n浅滩贝壳各有4个的话，{FA}我就能制作贝壳之铃⋯⋯{FB}原材料每天都可以采到。 | ok | PTR-OK, CN faithful |
| 2 | 0x08219F29 | 0x0826417E | ShoalCave_LowTideEntranceRoom_Text_ExplainShellBell | ポケモンに　もたせてあげると　よろこぶよ{FB}なんたって　かいがらのすずの　ねいろは\nてんか　いっぴん　だからね{FB}かいがらのすずの　ざいりょう　なら\nまいにち　とれるから{FA}そろえば　また　つくらせて　もらうよ | 把这个让宝可梦携带的话，\n宝可梦肯定会喜欢上它的。{FB}啊，贝壳之铃发出的乐声⋯⋯\n那是多么美妙！{FB}原料每天都能采到，\n想要的话我还可以做更多。 | ok | FIXED: upstream typo 采到原 -> 采到 (fixed both repos, hex regenerated) |
| 3 | 0x08219F00 | 0x0826414B | ShoalCave_LowTideEntranceRoom_Text_MakeShellBellRightAway | かいがらのすず\nさっそく　つくらせて　もらうよ{FB}⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯{FB}よし　できたっ！ | 好的，我马上帮你\n做贝壳之铃。{FB}⋯⋯　⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯　⋯⋯{FB}好了！做完了！ | ok | PTR-OK, CN faithful |
| 4 | 0x08219F5E | 0x082641FE | ShoalCave_LowTideEntranceRoom_Text_NoSpaceInYourBag | つくっても　バッグが　いっぱいで\nもてない　ようだね⋯⋯{FB}せいりして　また　くると　いいよ | 如果我做好了的话\n你的包包里就没有空间了，{FB}腾出些地方再回来吧。 | ok | PTR-OK, CN faithful |
| 5 | 0x08219F9C | 0x082641E5 | ShoalCave_LowTideEntranceRoom_Text_WantedToMakeShellBell | そうかね⋯⋯\nかいがらのすず　つくりたかった⋯⋯ | 哎⋯⋯是吗⋯⋯\n真想做一个贝壳之铃啊⋯⋯ | ok | PTR-OK, CN faithful |
| 6 | 0x08219ED2 | 0x08264111 | ShoalCave_LowTideEntranceRoom_Text_WouldYouLikeShellBell | お！　あさせのしおと　あさせのかいがら！\nりょうも　じゅうぶんだ！{FB}これで　かいがらのすず\nつくっても　いいかね？ | 啊，是浅滩海盐和浅滩贝壳！\n数量足够了！{FB}想要把它们\n做成贝壳之铃吗？ | ok | PTR-OK, CN faithful |
