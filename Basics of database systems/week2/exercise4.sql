INSERT INTO Matches VALUES(
    101,
    (SELECT FK_playerid FROM Ranking WHERE rank = (SELECT MIN(rank) FROM Ranking)),
    (SELECT FK_Playerid FROM Ranking WHERE rank = (SELECT MAX(rank) FROM Ranking)),
    '0-0',
    'unplayed',
    0
);

