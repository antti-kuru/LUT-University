SELECT * FROM Player
INNER JOIN Ranking ON Player.playerid = Ranking.FK_playerid WHERE rank <= 10;
