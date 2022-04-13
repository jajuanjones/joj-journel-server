DROP TABLE Entries;
DROP TABLE Moods;

CREATE TABLE `Entries` (
    `id` INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT,
    `concept` VARCHAR(20) NOT NULL,
    `entry` TEXT NOT NULL,
    `date` TEXT NOT NULL,
    `mood_id` INT NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Moods` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` VARCHAR(10) NOT NULL
);

INSERT INTO `Moods` VALUES (null, "ok");
INSERT INTO `Moods` VALUES (null, "happy");
INSERT INTO `Moods` VALUES (null, "angry");
INSERT INTO `Moods` VALUES (null, "sad");

INSERT INTO Entries VALUES (null, "Conversation", "Hi", "4/13/22", 2);
INSERT INTO Entries VALUES (null, "Conversation", "How are you?", "4/13/22", 2);
INSERT INTO Entries VALUES (null, "Conversation", "I'm well", "4/13/22", 2);