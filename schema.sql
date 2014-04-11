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

DROP TABLE IF EXISTS `cards`;
CREATE TABLE `cards` (
    `id` int(12) NOT NULL AUTO_INCREMENT,
    `title` varchar(512) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `labels` int(12) NOT NULL DEFAULT 0,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `lists`;
CREATE TABLE `lists` (
    `id` int(12) NOT NULL AUTO_INCREMENT,
    `title` varchar(512) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `group_member`;
CREATE TABLE `group_member` (
  `group_id` int(12) NOT NULL,
  `member_id` int(12) NOT NULL,
  PRIMARY KEY (`group_id`, `member_id`),
  KEY `idx_group_id` (`group_id`),
  KEY `idx_member_id` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `card_member`;
CREATE TABLE `card_member` (
  `card_id` int(12) NOT NULL,
  `member_id` int(12) NOT NULL,
  PRIMARY KEY (`card_id`, `member_id`),
  KEY `idx_card_id` (`card_id`),
  KEY `idx_member_id` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `card_label`;
CREATE TABLE `card_label` (
  `card_id` int(12) NOT NULL,
  `label_id` int(12) NOT NULL,
  `label_name` varchar(512) NOT NULL,
  PRIMARY KEY (`card_id`, `label_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


