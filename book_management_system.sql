/*
 Navicat Premium Data Transfer

 Source Server         : MyLinuxServe
 Source Server Type    : MySQL
 Source Server Version : 80036 (8.0.36)
 Source Host           : 13.78.119.4:3306
 Source Schema         : book_management_system

 Target Server Type    : MySQL
 Target Server Version : 80036 (8.0.36)
 File Encoding         : 65001

 Date: 15/05/2024 02:25:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `admin_id` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `admin_name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `password` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `right_col` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`admin_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('201801', '中南', '123456', '入库 借书 还书 注销');
INSERT INTO `admin` VALUES ('201802', '任雯倩', '111111', '入库 借书 还书');
INSERT INTO `admin` VALUES ('201803', '李丹清', '2222', '入库 借书 还书 注销');
INSERT INTO `admin` VALUES ('202401', '中南', '123', '入库 借书 还书 注销');
INSERT INTO `admin` VALUES ('202402', 'cxk', '111111', '入库 借书 还书 注销');
INSERT INTO `admin` VALUES ('202403', 'man', '111', '入库 借书 还书 注销');

-- ----------------------------
-- Table structure for announcements
-- ----------------------------
DROP TABLE IF EXISTS `announcements`;
CREATE TABLE `announcements`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of announcements
-- ----------------------------
INSERT INTO `announcements` VALUES (5, '欢迎使用书海图书管理系统', '1715529600000');
INSERT INTO `announcements` VALUES (6, '第二个公告', '1715616000000');
INSERT INTO `announcements` VALUES (7, '公告三', '1715616000000');
INSERT INTO `announcements` VALUES (8, '系统更新v0.1', '1715616000000');
INSERT INTO `announcements` VALUES (9, '系统更新v0.2', '1715616000000');
INSERT INTO `announcements` VALUES (10, '系统更新公告v0.3', '1715616000000');
INSERT INTO `announcements` VALUES (11, '系统更新v0.4', '1715616000000');
INSERT INTO `announcements` VALUES (12, '系统更新v0.5', '1715616000000');

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book`  (
  `isbn` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `book_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `author` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `press` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `class_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`isbn`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES ('978704015109X', 'ERP原理与应用实训', '汪清明', '高等教育出版社', '管理社会科学');
INSERT INTO `book` VALUES ('9787040273243', '管理信息系统', '黄梯云', '高等教育出版社', '管理社会科学');
INSERT INTO `book` VALUES ('978710800982x', '万历十五年', '[美]黄仁宇', '生活.读书.新知三联书店', '中国史');
INSERT INTO `book` VALUES ('9787115275790', 'JavaScript 高级程序设计-第3版', '[美] Nicholas C. Zakas 著', '李松峰', '曹力 译');
INSERT INTO `book` VALUES ('9787115335500', '深入浅出node.js', '朴灵', '人民邮电出版社', '自动化技术、计算机技术');
INSERT INTO `book` VALUES ('9787115373991', 'Flask Web开发: 基于Python的Web应用开发实战', '(美) 格林布戈著;安道译', '人民邮电出版社', '计算机技术');
INSERT INTO `book` VALUES ('9787115488763', 'Python深度学习', '弗朗索瓦.肖莱', '人民邮电出版社', '自动化技术、计算机技术');
INSERT INTO `book` VALUES ('9787121204869', '移动设计', '傅小贞', '电子工业出版社', '自动化技术、计算机技术');
INSERT INTO `book` VALUES ('9787226044094', '音乐词典', '高天康', '甘肃人民出版社', '音乐');
INSERT INTO `book` VALUES ('9787302292609', ' 用友ERP生产管理系统实验教程:U8.72版', '张莉莉', '清华大学出版社', '管理社会科学');
INSERT INTO `book` VALUES ('9787302423287', '机器学习', '周志华', '清华大学出版社', '自动化技术、计算机技术');
INSERT INTO `book` VALUES ('9787302469001', ' 计算机导论', '杨月江', '清华大学出版社', '计算机');
INSERT INTO `book` VALUES ('9787543862326', '中国知青终结', '邓贤', '湖南人民出版社', '中国文学');
INSERT INTO `book` VALUES ('9787810823620', 'ERP原理与实践', '苟娟琼,常丹', '北京交通大学出版社', '管理社会科学');

-- ----------------------------
-- Table structure for comments
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `comment` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` int(1) UNSIGNED ZEROFILL NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of comments
-- ----------------------------
INSERT INTO `comments` VALUES (1, '161001222', '你好', '1715529600000', 1);
INSERT INTO `comments` VALUES (2, '161001228', '这里是留言页面吗？', '1715529600000', 1);
INSERT INTO `comments` VALUES (3, '161001228', '还真是', '1715529600000', 1);
INSERT INTO `comments` VALUES (4, '161001228', '你好', '1715529600000', 1);
INSERT INTO `comments` VALUES (5, '161001228', 'hello？', '1715529600000', 1);
INSERT INTO `comments` VALUES (6, '82092401', '玩原神玩的', '1715529600000', 1);
INSERT INTO `comments` VALUES (7, '82092401', '为什么没有原神相关书籍？\n', '1715529600000', 1);
INSERT INTO `comments` VALUES (8, '82092401', '你好', '1715529600000', 1);
INSERT INTO `comments` VALUES (9, '82092401', '你好', '1715529600000', 1);
INSERT INTO `comments` VALUES (10, '82092401', '我爱中南', '1715529600000', 1);

-- ----------------------------
-- Table structure for comments_admin
-- ----------------------------
DROP TABLE IF EXISTS `comments_admin`;
CREATE TABLE `comments_admin`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `comment_id` int NOT NULL,
  `admin_id` int NOT NULL,
  `comment` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of comments_admin
-- ----------------------------
INSERT INTO `comments_admin` VALUES (1, 1, 201801, '您有什么问题？', '1715529600000');
INSERT INTO `comments_admin` VALUES (2, 1, 201801, '您的问题已经解决！', '1715529600000');
INSERT INTO `comments_admin` VALUES (3, 8, 201801, '不好', '1715529600000');
INSERT INTO `comments_admin` VALUES (4, 7, 201801, '玩牛魔原神', '1715529600000');
INSERT INTO `comments_admin` VALUES (5, 9, 202401, '你好', '1715529600000');
INSERT INTO `comments_admin` VALUES (6, 9, 202401, '你好', '1715529600000');

-- ----------------------------
-- Table structure for inventory
-- ----------------------------
DROP TABLE IF EXISTS `inventory`;
CREATE TABLE `inventory`  (
  `barcode` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `isbn` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `storage_date` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `location` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `withdraw` tinyint(1) NULL DEFAULT NULL,
  `status` tinyint(1) NULL DEFAULT NULL,
  `admin` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`barcode`) USING BTREE,
  INDEX `isbn`(`isbn` ASC) USING BTREE,
  INDEX `admin`(`admin` ASC) USING BTREE,
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`isbn`) REFERENCES `book` (`isbn`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `inventory_ibfk_2` FOREIGN KEY (`admin`) REFERENCES `admin` (`admin_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of inventory
-- ----------------------------
INSERT INTO `inventory` VALUES ('100001', '9787302469001', '1715184000000', '1楼', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('102341', '9787302423287', '1514736000000', '1楼,02书架,3层,4排', 0, 0, '201801');
INSERT INTO `inventory` VALUES ('102342', '9787302423287', '1514736000000', '1楼,02书架,3层,4排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('102343', '9787302423287', '1514736000000', '1楼,02书架,3层,4排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('102344', '9787302423287', '1514736000000', '1楼,02书架,3层,4排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('102345', '9787302423287', '1547130451000', '1楼,02书架,3层,4排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('102346', '9787115373991', '1547222400000', '1楼,02书架,3层,4排', 0, 0, '201801');
INSERT INTO `inventory` VALUES ('102347', '9787115373991', '1547222400000', '1楼,02书架,3层,4排', 0, 0, '201801');
INSERT INTO `inventory` VALUES ('102348', '9787115373991', '1547222400000', '1楼,02书架,3层,4排', 0, 0, '201801');
INSERT INTO `inventory` VALUES ('103425', '9787302423287', '1715270400000', '2', 0, 1, '202401');
INSERT INTO `inventory` VALUES ('104341', '9787115335500', '1514995200000', '1楼,04书架,3层,4排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('104342', '9787115335500', '1514995200000', '1楼,04书架,3层,4排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('104343', '9787115335500', '1514995200000', '1楼,04书架,3层,4排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('104344', '9787121204869', '1546358400000', '1楼,04书架,3层,4排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('104345', '9787121204869', '1514822400000', '1楼,04书架,3层,4排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('111111', '978704015109X', '1715270400000', '一楼', 0, 1, '202401');
INSERT INTO `inventory` VALUES ('113456', '978704015109X', '1715270400000', '1楼东侧', 0, 0, '202401');
INSERT INTO `inventory` VALUES ('123555', '978704015109X', '1715270400000', '2楼', 0, 0, '202401');
INSERT INTO `inventory` VALUES ('142999', '9787040273243', '1715270400000', '1楼', 0, 1, '202401');
INSERT INTO `inventory` VALUES ('201232', '978704015109X', '1515168000000', '2楼,01书架,2层,3排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('201233', '978704015109X', '1515168000000', '2楼,01书架,2层,3排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('202331', '9787040273243', '1515772800000', '2楼,02书架,3层,3排', 0, 0, '201802');
INSERT INTO `inventory` VALUES ('202332', '9787040273243', '1515772800000', '2楼,02书架,3层,3排', 0, 1, '201802');
INSERT INTO `inventory` VALUES ('203771', '9787810823620', '1517328000000', '2楼,03书架,7层,7排', 0, 1, '201802');
INSERT INTO `inventory` VALUES ('203772', '9787810823620', '1517328000000', '2楼,03书架,7层,7排', 0, 1, '201802');
INSERT INTO `inventory` VALUES ('203773', '9787810823620', '1517328000000', '2楼,03书架,7层,7排', 0, 1, '201802');
INSERT INTO `inventory` VALUES ('205162', '9787115373991', '1715529600000', '二楼东侧', 0, 0, '202401');
INSERT INTO `inventory` VALUES ('211411', '9787302292609', '1514736000000', '2楼,11书架,4层,1排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('211412', '9787302292609', '1514736000000', '2楼,11书架,4层,1排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('211413', '9787302292609', '1514736000000', '2楼,11书架,4层,1排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('215502', '9787115373991', '1715529600000', '二楼东侧', 0, 1, '202401');
INSERT INTO `inventory` VALUES ('283872', '9787115373991', '1715529600000', '二楼东侧', 0, 1, '202401');
INSERT INTO `inventory` VALUES ('308371', '9787115275790', '1516377600000', '3楼,08书架,3层,7排', 0, 0, '201801');
INSERT INTO `inventory` VALUES ('308372', '9787115275790', '1516377600000', '3楼,08书架,3层,7排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('308373', '9787115275790', '1516377600000', '3楼,08书架,3层,7排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('309331', '9787115488763', '1515081600000', '3楼,09书架,3层,3排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('309332', '9787115488763', '1515081600000', '3楼,09书架,3层,3排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('309333', '9787115488763', '1515081600000', '3楼,09书架,3层,3排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('310321', '978710800982x', '1517587200000', '3楼,10书架,3层,2排', 0, 1, '201802');
INSERT INTO `inventory` VALUES ('310322', '978710800982x', '1517587200000', '3楼,10书架,3层,2排', 0, 1, '201802');
INSERT INTO `inventory` VALUES ('310323', '978710800982x', '1517587200000', '3楼,10书架,3层,2排', 0, 1, '201802');
INSERT INTO `inventory` VALUES ('401281', '9787226044094', '1515772800000', '4楼,01书架,2层,8排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('401282', '9787226044094', '1515772800000', '4楼,01书架,2层,8排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('411361', '9787543862326', '1516982400000', '4楼,11书架,3层,6排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('411362', '9787543862326', '1516982400000', '4楼,11书架,3层,6排', 0, 1, '201801');
INSERT INTO `inventory` VALUES ('720617', '9787115373991', '1715529600000', '二楼东侧', 0, 1, '202401');
INSERT INTO `inventory` VALUES ('749411', '9787115373991', '1715529600000', '二楼东侧', 0, 1, '202401');
INSERT INTO `inventory` VALUES ('757549', '978704015109X', '1715270400000', '1楼', 0, 1, '202401');
INSERT INTO `inventory` VALUES ('789654', '9787040273243', '1715270400000', '12', 0, 1, '202401');
INSERT INTO `inventory` VALUES ('803993', '978704015109X', '1715270400000', '1楼', 0, 1, '202401');
INSERT INTO `inventory` VALUES ('890976', '9787040273243', '1715270400000', '2楼', 0, 1, '202401');
INSERT INTO `inventory` VALUES ('891561', '978704015109X', '1715270400000', '1楼', 0, 1, '202401');

-- ----------------------------
-- Table structure for readbook
-- ----------------------------
DROP TABLE IF EXISTS `readbook`;
CREATE TABLE `readbook`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `barcode` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `card_id` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `start_date` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `borrow_admin` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `end_date` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `return_admin` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `due_date` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `barcode`(`barcode` ASC) USING BTREE,
  INDEX `card_id`(`card_id` ASC) USING BTREE,
  INDEX `borrow_admin`(`borrow_admin` ASC) USING BTREE,
  INDEX `return_admin`(`return_admin` ASC) USING BTREE,
  CONSTRAINT `readbook_ibfk_1` FOREIGN KEY (`barcode`) REFERENCES `inventory` (`barcode`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `readbook_ibfk_2` FOREIGN KEY (`card_id`) REFERENCES `student` (`card_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 28 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of readbook
-- ----------------------------
INSERT INTO `readbook` VALUES (1, '102341', '16000001', '1544371200000', '201801', '1546704000000', '201801', '1547827200000');
INSERT INTO `readbook` VALUES (2, '102342', '16000002', '1545926400000', '201801', '1546876800000', '201801', '1549382400000');
INSERT INTO `readbook` VALUES (3, '310321', '16000001', '1546012800000', '201801', '1546790400000', '201801', '1549468800000');
INSERT INTO `readbook` VALUES (4, '203773', '16000001', '1546012800000', '201801', '1546790400000', '201802', '1549468800000');
INSERT INTO `readbook` VALUES (5, '310322', '16000002', '1546012800000', '201801', '1546876800000', '201802', '1549468800000');
INSERT INTO `readbook` VALUES (7, '309333', '16000001', '1546358400000', '201801', '1547222400000', '201801', '1549814400000');
INSERT INTO `readbook` VALUES (8, '102341', '16000001', '1547222400000', '201801', NULL, NULL, '1550678400000');
INSERT INTO `readbook` VALUES (9, '211411', '16000003', '1547222400000', '201801', NULL, NULL, '1550678400000');
INSERT INTO `readbook` VALUES (10, '202331', '16000003', '1547222400000', '201801', NULL, NULL, '1550678400000');
INSERT INTO `readbook` VALUES (11, '102347', '16000001', '1547222400000', '201801', NULL, NULL, '1550678400000');
INSERT INTO `readbook` VALUES (12, '102348', '16000001', '1715011200000', '201801', NULL, NULL, '1718467200000');
INSERT INTO `readbook` VALUES (13, NULL, NULL, '1715097600000', '202401', NULL, NULL, '1718553600000');
INSERT INTO `readbook` VALUES (14, '310321', '2401', '1715097600000', '202401', '1715097600000', '202401', '1718553600000');
INSERT INTO `readbook` VALUES (15, '308371', '2401', '1715097600000', '202401', '1715097600000', '202401', '1718553600000');
INSERT INTO `readbook` VALUES (16, '203771', '2401', '1715097600000', '202401', '1715184000000', '202401', '1718553600000');
INSERT INTO `readbook` VALUES (17, '310321', '2401', '1715184000000', '202401', '1715270400000', '202401', '1718640000000');
INSERT INTO `readbook` VALUES (23, '310321', '16000001', '1715356800000', '161001222', '1715356800000', '161001222', '1718812800000');
INSERT INTO `readbook` VALUES (24, '111111', '2401', '1715529600000', '82092401', '1715529600000', '82092401', '1718985600000');
INSERT INTO `readbook` VALUES (25, '113456', '2401', '1715529600000', '82092401', NULL, NULL, '1718985600000');
INSERT INTO `readbook` VALUES (26, '123555', '2401', '1715529600000', '82092401', NULL, NULL, '1718985600000');
INSERT INTO `readbook` VALUES (27, '205162', '2401', '1715529600000', '82092401', NULL, NULL, '1718985600000');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `card_id` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `student_id` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `password` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `student_name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `sex` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `telephone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `enroll_date` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `valid_date` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `loss` tinyint(1) NULL DEFAULT NULL,
  `debt` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`card_id`) USING BTREE,
  INDEX `student_id`(`student_id` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('16000001', '161001222', '123', '许致立', '女', '18921902722', '1693526400000', '1914422400000', 1, 0);
INSERT INTO `student` VALUES ('16000002', '161001228', '123', '丹清', '女', '18367890001', '1693526400000', '1914422400000', 0, 0);
INSERT INTO `student` VALUES ('16000003', '161001227', '123', '任雯', '女', '18890209433', '1693526400000', '1914422400000', 0, 0);
INSERT INTO `student` VALUES ('2401', '82092401', '123456', '刻晴', '女', '18921902722', '1693526400000', '1914422400000', 0, 0);
INSERT INTO `student` VALUES ('2402', '82092402', '123456', '牢大', '男', '18367890001', '1693526400000', '1914422400000', 0, 0);
INSERT INTO `student` VALUES ('2403', '82092403', '123456', '刻晴', '女', '18890209433', '1693526400000', '1914422400000', 0, 0);

SET FOREIGN_KEY_CHECKS = 1;
