CREATE DATABASE IF NOT EXISTS `hw4`;
USE `hw4`;

DROP TABLE IF EXISTS `playlist_rating`;
DROP TABLE IF EXISTS `song_rating`;
DROP TABLE IF EXISTS `album_rating`;
DROP TABLE IF EXISTS `playlist_songs`;
DROP TABLE IF EXISTS `playlist`;
DROP TABLE IF EXISTS `genre`;
DROP TABLE IF EXISTS `song`;
DROP TABLE IF EXISTS `album`;
DROP TABLE IF EXISTS `artist`;
DROP TABLE IF EXISTS `user`;

CREATE TABLE `artist` (
  `artist_name` varchar(50) NOT NULL,
  PRIMARY KEY (`artist_name`)
);

INSERT INTO `artist` VALUES 
("eluo28"),
("hershey"),
("krusty"),
("test");

CREATE TABLE `album` (
  `album_id` integer NOT NULL,
  `album_name` varchar(50) NOT NULL,
  `released_by` varchar(30) NOT NULL,
  `release_date` date NOT NULL,
  PRIMARY KEY (`album_id`),
  CONSTRAINT `uc_album` UNIQUE (`album_name`, `released_by`),
  FOREIGN KEY (`released_by`) references `artist` (`artist_name`) ON DELETE CASCADE
);

INSERT INTO `album` VALUES 
(1,"17","eluo28","2008-11-11"),
(2,"the goat","hershey","2008-11-11"),
(3,"wow","krusty","2008-11-11"),
(4,"yer","krusty","2008-11-11"),
(5,"wow2","krusty","2008-11-11"),
(6,"wow3","krusty","2008-11-11"),
(7,"wow4","krusty","2008-11-11");

CREATE TABLE `song` (
  `song_id` integer NOT NULL,
  `song_title` varchar(50) NOT NULL,
  `recorded_by` varchar(50) NOT NULL,
  `release_date` date NOT NULL,
  `album_id` integer,
  PRIMARY KEY (`song_id`),
  CONSTRAINT `uc_song` UNIQUE (`song_title`, `recorded_by`),
  FOREIGN KEY (`album_id`) references `album` (`album_id`) ON DELETE CASCADE
);

INSERT INTO `song` VALUES 
(1,"everyone dies in my nightmares","hershey","2008-11-11",1),
(2,"introduction","hershey","2008-11-11",2),
(3,"wow first song","krusty","2008-11-11",3),
(4,"single","eluo28","2008-11-11",NULL),
(5,"single2","krusty","2008-11-11",NULL),
(6,"single3","krusty","2008-11-11",NULL);

CREATE TABLE `genre` (
  `song_id` integer NOT NULL,
  `genre_name` varchar(20) NOT NULL,
  PRIMARY KEY (`song_id`,`genre_name`),
  FOREIGN KEY (`song_id`) references `song` (`song_id`) ON DELETE CASCADE
);

INSERT INTO `genre` VALUES 
(1,"Rock"),
(2,"Rock"),
(3,"Rock"),
(4,"Pop"),
(1,"Pop"),
(2,"R&B"),
(3,"R&B"),
(4,"Rock"),
(3,"Kpop");

CREATE TABLE `user` (
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`username`)
);

INSERT INTO `user` VALUES 
("user1"),
("user2"),
("user3"),
("user4");

CREATE TABLE `playlist` (
  `playlist_id` integer NOT NULL,
  `playlist_title` varchar(50) NOT NULL,
  `created_at` datetime NOT NULL,
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`playlist_id`),
  CONSTRAINT `uc_playlist` UNIQUE (`playlist_title`, `username`),
  FOREIGN KEY (`username`) references `user` (`username`) ON DELETE CASCADE
);

INSERT INTO `playlist` VALUES 
(1,"playlist 1","2022-06-18 10:34:09","user1"),
(2,"playlist 2","2022-06-18 10:34:09","user2"),
(3,"playlist 3","2022-06-18 10:34:09","user1"),
(4,"playlist 4","2022-06-18 10:34:09","user3");

CREATE TABLE `playlist_songs` (
  `playlist_id` integer NOT NULL,
  `song_id` integer NOT NULL,
  PRIMARY KEY (`playlist_id`,`song_id`),
  FOREIGN KEY (`playlist_id`) references `playlist` (`playlist_id`) ON DELETE CASCADE,
  FOREIGN KEY (`song_id`) references `song` (`song_id`) ON DELETE CASCADE
);

INSERT INTO `playlist_songs` VALUES 
(1,1),
(2,1),
(3,2),
(4,2),
(1,4),
(2,3);

CREATE TABLE `song_rating` (
  `song_id` integer NOT NULL,
  `username` varchar(50) NOT NULL,
  `rating` integer NOT NULL,
  `created_at` date NOT NULL,
  PRIMARY KEY (`username`,`song_id`),
  FOREIGN KEY (`username`) references `user` (`username`) ON DELETE CASCADE,
  FOREIGN KEY (`song_id`) references `song` (`song_id`) ON DELETE CASCADE
);


INSERT INTO `song_rating` VALUES 
(1,"user1",3,"1992-11-11"),
(2,"user2",4,"1992-11-11"),
(3,"user1",1,"1992-11-11"),
(2,"user1",5,"1992-11-11"),
(4,"user2",2,"1992-11-11"),
(4,"user4",5,"1992-11-11"),
(5,"user3",3,"1992-11-11"),
(6,"user2",3,"1992-11-11"),
(5,"user1",4,"1992-11-11"),
(6,"user1",2,"1992-11-11");

CREATE TABLE `playlist_rating` (
  `playlist_id` integer NOT NULL,
  `username` varchar(50) NOT NULL,
  `rating` integer NOT NULL,
  `created_at` date NOT NULL,
  PRIMARY KEY (`username`,`playlist_id`),
  FOREIGN KEY (`username`) references `user` (`username`) ON DELETE CASCADE,
  FOREIGN KEY (`playlist_id`) references `playlist` (`playlist_id`) ON DELETE CASCADE
);

CREATE TABLE `album_rating` (
  `album_id` integer NOT NULL,
  `username` varchar(50) NOT NULL,
  `rating` integer NOT NULL,
  `created_at` date NOT NULL,
  PRIMARY KEY (`username`,`album_id`),
  FOREIGN KEY (`username`) references `user` (`username`) ON DELETE CASCADE,
  FOREIGN KEY (`album_id`) references `album` (`album_id`) ON DELETE CASCADE
);


INSERT INTO `album_rating` VALUES 
(1,"user1",3,"1992-11-11"),
(2,"user2",2,"1992-11-11"),
(3,"user1",1,"1992-11-11"),
(2,"user1",5,"1992-11-11"),
(4,"user1",1,"1992-11-11"),
(4,"user3",1,"1992-11-11");


