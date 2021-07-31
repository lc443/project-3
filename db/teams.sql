CREATE DATABASE mlbTeamsData;
use mlbTeamsData;

CREATE TABLE IF NOT EXISTS teams (
    `id` int AUTO_INCREMENT,
    `team_name` VARCHAR(50) CHARACTER SET utf8,
    `salary_in_millions` NUMERIC(5, 2),
    `wins` INT,
    PRIMARY KEY (`id`)
);
INSERT INTO teams VALUES
    (1, 'Nationals',     81.34, 98),
    (2, 'Reds',          82.20, 97),
    (3, 'Yankees',      197.96, 95),
    (4, 'Giants',       117.62, 94),
    (5, 'Braves',        83.31, 94),
    (6, 'Athletics',     55.37, 94),
    (7, 'Rangers',      120.51, 93),
    (8, 'Orioles',       81.43, 93),
    (9, 'Rays',          64.17, 90),
    (10, 'Angels',       154.49, 89),
    (11, 'Tigers',       132.30, 88),
    (12, 'Cardinals',    110.30, 88),
    (13, 'Dodgers',       95.14, 86),
    (14, 'White Sox',     96.92, 85),
    (15, 'Brewers',       97.65, 83),
    (16, 'Phillies',     174.54, 81),
    (17, 'Diamondbacks',  74.28, 81),
    (18, 'Pirates',       63.43, 79),
    (19, 'Padres',        55.24, 76),
    (20,'Mariners',      81.97, 75),
    (21, 'Mets',          93.35, 74),
    (22, 'Blue Jays',     75.48, 73),
    (23, 'Royals',        60.91, 72),
    (24, 'Marlins',      118.07, 69),
    (25, 'Red Sox',      173.18, 69),
    (26, 'Indians',       78.43, 68),
    (27, 'Twins',         94.08, 66),
    (28, 'Rockies',       78.06, 64),
    (29, 'Cubs',          88.19, 61),
    (30, 'Astros',        60.65, 55);
