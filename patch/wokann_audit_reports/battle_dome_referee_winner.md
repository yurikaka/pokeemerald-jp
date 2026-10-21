# Battle Dome referee declarations

Checked `../pokeemerald_wokann_dev` branch `dev`,
`data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc`.

After a double knockout, the Draw script compares seeds and branches into the
ordinary match-win or match-loss path. These paths call PlayerWonDraw,
OpponentWonDraw, or TuckerWonDraw, which display the three
`RefereesDecidedWinner*` texts. Their meaning is the winner of the match.
The generic declarations have no final-round requirement.

Only after the player declaration does the script resolve match winners,
increment FRONTIER_DATA_BATTLE_NUM, and compare it against DOME_ROUNDS_COUNT.
When the tournament is complete, separate PlayerIsLv50Champ/PlayerIsLvOpenChamp
texts announce the champion. Japanese likewise distinguishes しょうしゃ
(winner) in the referee declarations from ゆうしょう (tournament victory).

Replace 冠军 with 胜者 only in the three referee declarations in batch 200.
Both terms occupy two Chinese characters, so their text widths are unchanged.
Keep placeholders and actual tournament championship declarations unchanged.
The old referee wording was inherited from the US localization and is also
present in the expansion localization.
