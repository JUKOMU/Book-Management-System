-- 创建 admin 表
CREATE TABLE admin (
  admin_id VARCHAR(6) NOT NULL,
  admin_name VARCHAR(32),
  password VARCHAR(24),
  right VARCHAR(32),
  PRIMARY KEY (admin_id)
);


-- 创建 book 表
CREATE TABLE book (
  isbn VARCHAR(13) NOT NULL,
  book_name VARCHAR(64),
  author VARCHAR(64),
  press VARCHAR(32),
  class_name VARCHAR(64),
  PRIMARY KEY (isbn)
);

-- 创建 inventory 表
CREATE TABLE inventory (
  barcode VARCHAR(6) NOT NULL,
  isbn VARCHAR(13),
  storage_date VARCHAR(13),
  location VARCHAR(32),
  withdraw BOOLEAN,
  status BOOLEAN,
  admin VARCHAR(6),
  PRIMARY KEY (barcode),
  FOREIGN KEY (isbn) REFERENCES book (isbn) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (admin) REFERENCES admin (admin_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- 插入 admin 数据
INSERT INTO admin (admin_id, admin_name, password, right_col) VALUES 
('201801', '李华', '123', '入库 借书 还书 注销'),
('201802', '任雯倩', '111111', '入库 借书 还书'),
('201803', '李丹清', '2222', '入库 借书 还书 注销');

-- 插入 book 数据
INSERT INTO book (isbn, book_name, author, press, class_name) VALUES 
('978704015109X', 'ERP原理与应用实训', '汪清明', '高等教育出版社', '管理社会科学'),
('9787040273243', '管理信息系统', '黄梯云', '高等教育出版社', '管理社会科学'),
('9787115335500', '深入浅出node.js', '朴灵', '人民邮电出版社', '自动化技术、计算机技术'),
('9787121204869', '移动设计', '傅小贞', '电子工业出版社', '自动化技术、计算机技术'),
('9787302292609', ' 用友ERP生产管理系统实验教程:U8.72版', '张莉莉', '清华大学出版社', '管理社会科学'),
('978710800982x', '万历十五年', '[美]黄仁宇', '生活.读书.新知三联书店', '中国史'),
('9787115488763', 'Python深度学习', '弗朗索瓦.肖莱', '人民邮电出版社', '自动化技术、计算机技术'),
('9787226044094', '音乐词典', '高天康', '甘肃人民出版社', '音乐'),
('9787115275790', 'JavaScript 高级程序设计-第3版', '[美] Nicholas C. Zakas 著', '李松峰', '曹力 译'),
('9787302423287', '机器学习', '周志华', '清华大学出版社', '自动化技术、计算机技术'),
('9787543862326', '中国知青终结', '邓贤', '湖南人民出版社', '中国文学'),
('9787810823620', 'ERP原理与实践', '苟娟琼,常丹', '北京交通大学出版社', '管理社会科学'),
('9787115373991', 'Flask Web开发: 基于Python的Web应用开发实战', '(美) 格林布戈著;安道译', '人民邮电出版社', '计算机技术');

-- 插入 inventory 数据
INSERT INTO inventory (barcode, isbn, storage_date, location, withdraw, status, admin) VALUES 
('102341', '9787302423287', '1514736000000', '1楼,02书架,3层,4排', 0, 0, '201801'),
('102342', '9787302423287', '1514736000000', '1楼,02书架,3层,4排', 0, 1, '201801'),
('102343', '9787302423287', '1514736000000', '1楼,02书架,3层,4排', 0, 1, '201801'),
('102344', '9787302423287', '1514736000000', '1楼,02书架,3层,4排', 0, 1, '201801'),
('211411', '9787302292609', '1514736000000', '2楼,11书架,4层,1排', 0, 1, '201801'),
('211412', '9787302292609', '1514736000000', '2楼,11书架,4层,1排', 0, 1, '201801'),
('211413', '9787302292609', '1514736000000', '2楼,11书架,4层,1排', 0, 1, '201801'),
('201231', '978704015109X', '1515168000000', '2楼,01书架,2层,3排', 0, 1, '201801'),
('201232', '978704015109X', '1515168000000', '2楼,01书架,2层,3排', 0, 1, '201801'),
('201233', '978704015109X', '1515168000000', '2楼,01书架,2层,3排', 0, 1, '201801'),
('202331', '9787040273243', '1515772800000', '2楼,02书架,3层,3排', 0, 0, '201802'),
('202332', '9787040273243', '1515772800000', '2楼,02书架,3层,3排', 0, 1, '201802'),
('104341', '9787115335500', '1514995200000', '1楼,04书架,3层,4排', 0, 1, '201801'),
('104342', '9787115335500', '1514995200000', '1楼,04书架,3层,4排', 0, 1, '201801'),
('104343', '9787115335500', '1514995200000', '1楼,04书架,3层,4排', 0, 1, '201801'),
('104344', '9787121204869', '1546358400000', '1楼,04书架,3层,4排', 0, 1, '201801'),
('104345', '9787121204869', '1514822400000', '1楼,04书架,3层,4排', 0, 1, '201801'),
('310321', '978710800982x', '1517587200000', '3楼,10书架,3层,2排', 0, 1, '201802'),
('310322', '978710800982x', '1517587200000', '3楼,10书架,3层,2排', 0, 1, '201802'),
('310323', '978710800982x', '1517587200000', '3楼,10书架,3层,2排', 0, 1, '201802'),
('309331', '9787115488763', '1515081600000', '3楼,09书架,3层,3排', 0, 1, '201801'),
('309332', '9787115488763', '1515081600000', '3楼,09书架,3层,3排', 0, 1, '201801'),
('309333', '9787115488763', '1515081600000', '3楼,09书架,3层,3排', 0, 1, '201801'),
('401281', '9787226044094', '1515772800000', '4楼,01书架,2层,8排', 0, 1, '201801'),
('401282', '9787226044094', '1515772800000', '4楼,01书架,2层,8排', 0, 1, '201801'),
('308371', '9787115275790', '1516377600000', '3楼,08书架,3层,7排', 0, 1, '201801'),
('308372', '9787115275790', '1516377600000', '3楼,08书架,3层,7排', 0, 1, '201801'),
('308373', '9787115275790', '1516377600000', '3楼,08书架,3层,7排', 0, 1, '201801'),
('411361', '9787543862326', '1516982400000', '4楼,11书架,3层,6排', 0, 1, '201801'),
('411362', '9787543862326', '1516982400000', '4楼,11书架,3层,6排', 0, 1, '201801'),
('203771', '9787810823620', '1517328000000', '2楼,03书架,7层,7排', 0, 1, '201802'),
('203772', '9787810823620', '1517328000000', '2楼,03书架,7层,7排', 0, 1, '201802'),
('203773', '9787810823620', '1517328000000', '2楼,03书架,7层,7排', 0, 1, '201802'),
('102345', '9787302423287', '1547130451000', '1楼,02书架,3层,4排', 0, 1, '201801'),
('102346', '9787115373991', '1547222400000', '1楼,02书架,3层,4排', 0, 0, '201801'),
('102347', '9787115373991', '1547222400000', '1楼,02书架,3层,4排', 0, 0, '201801'),
('102348', '9787115373991', '1547222400000', '1楼,02书架,3层,4排', 0, 1, '201801');
-- 创建 student 表
CREATE TABLE student (
  card_id VARCHAR(8) NOT NULL,
  student_id VARCHAR(9),
  student_name VARCHAR(32),
  sex VARCHAR(2),
  telephone VARCHAR(11),
  enroll_date VARCHAR(13),
  valid_date VARCHAR(13),
  loss TINYINT(1),
  debt TINYINT(1),
  PRIMARY KEY (card_id)
);

-- 插入 student 数据
INSERT INTO student (card_id, student_id, student_name, sex, telephone, enroll_date, valid_date, loss, debt) VALUES 
('16000001', '161001222', '许致立', '女', '18921902722', '1472659200000', '1593446400000', 0, 0),
('16000002', '161001228', '丹清', '女', '18367890001', '1472659200000', '1593446400000', 0, 0),
('16000003', '161001227', '任雯', '女', '18890209433', '1472659200000', '1593446400000', 0, 0);

-- 创建 readbook 表
CREATE TABLE readbook (
  id INT NOT NULL AUTO_INCREMENT,
  barcode VARCHAR(6),
  card_id VARCHAR(8),
  start_date VARCHAR(13),
  borrow_admin VARCHAR(6),
  end_date VARCHAR(13),
  return_admin VARCHAR(6),
  due_date VARCHAR(13),
  PRIMARY KEY (id),
  FOREIGN KEY (barcode) REFERENCES inventory (barcode) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (card_id) REFERENCES student (card_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (borrow_admin) REFERENCES admin (admin_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (return_admin) REFERENCES admin (admin_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- 插入 readbook 数据
INSERT INTO readbook (id, barcode, card_id, start_date, borrow_admin, end_date, return_admin, due_date) VALUES 
(1, '102341', '16000001', '1544371200000', '201801', '1546704000000', '201801', '1547827200000'),
(2, '102342', '16000002', '1545926400000', '201801', '1546876800000', '201801', '1549382400000'),
(3, '310321', '16000001', '1546012800000', '201801', '1546790400000', '201801', '1549468800000'),
(4, '203773', '16000001', '1546012800000', '201801', '1546790400000', '201802', '1549468800000'),
(5, '310322', '16000002', '1546012800000', '201801', '1546876800000', '201802', '1549468800000'),
(7, '309333', '16000001', '1546358400000', '201801', '1547222400000', '201801', '1549814400000'),
(8, '102341', '16000001', '1547222400000', '201801', NULL, NULL, '1550678400000'),
(9, '211411', '16000003', '1547222400000', '201801', NULL, NULL, '1550678400000'),
(10, '202331', '16000003', '1547222400000', '201801', NULL, NULL, '1550678400000'),
(11, '102347', '16000001', '1547222400000', '201801', NULL, NULL, '1550678400000');

