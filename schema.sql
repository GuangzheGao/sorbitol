DROP TABLE IF EXISTS `groups`;
CREATE TABLE `groups` (
    `id` int(12) NOT NULL AUTO_INCREMENT,
    `name` varchar(512) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `email` varchar(200) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_user` (`username`),
  UNIQUE KEY `uk_email` (`email`),
  KEY `idx_user_password` (`username`,`password`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `boards`;
CREATE TABLE `boards` (
    `id` int(12) NOT NULL AUTO_INCREMENT,
    `title` varchar(512) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `visibility` char(1),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `activities`;
CREATE TABLE `activities` (
    `id` int(12) NOT NULL AUTO_INCREMENT,
    `user_id` int(12) NOT NULL,
    `board_id` int(12) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `lists`;
CREATE TABLE `lists` (
    `id` int(12) NOT NULL AUTO_INCREMENT,
    `board_id` int(12) NOT NULL,
    `title` varchar(512) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    KEY `idx_board_id` (`board_id`),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `cards`;
CREATE TABLE `cards` (
    `id` int(12) NOT NULL AUTO_INCREMENT,
    `list_id` int(12) NOT NULL,
    `title` varchar(512) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
    `id` int(12) NOT NULL AUTO_INCREMENT,
    `card_id` int(12) NOT NULL,
    `user_id` int(12) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `content` varchar(512) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
