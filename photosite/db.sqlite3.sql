BEGIN TRANSACTION;
CREATE TABLE `main_categorymodel` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	varchar ( 16 ) NOT NULL,
	`description`	text NOT NULL,
	`date`	date NOT NULL,
	`image`	varchar ( 100 ) NOT NULL
);
INSERT INTO `main_categorymodel` (id,name,description,date,image) VALUES (61,'PHOTOSETS','Различные фотосеты.','2017-03-09','category/photosets_9O7kmSc.jpg'),
 (62,'RACES','Репортажные фото с соревнований.','2017-03-09','category/races_RkTuSUH.jpg'),
 (63,'WIP','gsdgsdgs','2017-03-09','category/wip_DoSaNwK.jpg'),
 (64,'PHOTO','Фото на разные темы.','2017-03-09','category/photo_NElKOHE.jpg'),
 (65,'Detailng','Фото с акцентом на детали.','2017-03-09','category/IMG_1368_RDijE5d.JPG'),
 (66,'Путешествия','Фото с различных путешествий.','2017-03-09','category/greecevac-86_76ICoRb.jpg'),
 (67,'Под водой.','Подводная съемка','2017-03-09','category/greecevac-53_lXIZwxp.jpg');
CREATE TABLE `django_session` (
	`session_key`	varchar ( 40 ) NOT NULL,
	`session_data`	text NOT NULL,
	`expire_date`	datetime NOT NULL,
	PRIMARY KEY(`session_key`)
);
INSERT INTO `django_session` (session_key,session_data,expire_date) VALUES ('lxab4j6hs2kw7s8v2qgthtieec9cmxvy','MzBhOTlhZjBjNzRmNGNlZTU3YWQyZGEwN2M3ZTEzYWMwYWIwOWVlOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYmQ3NWY3NjRmMWNiMmFlZDkyNTkwMmFiMzljNjMwMGFjOTJhZDg0In0=','2017-03-15 16:34:41.723508'),
 ('ynhx99mx3njlk26h8efyz6eahimb3pto','ZDEwMGUwNDc2NmZlMzVkN2I3NWQ5ZTVkNzQ0NTNhNzIzMzE0NmFmMzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2ExZDU4Y2ZhNzc3NDQxZDBiOTA3OTc4NDA3N2M2NzhkMmNkMDJkOSIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2017-03-23 04:46:04.830325'),
 ('lq9ed9sahljtguame4xcajk1ndm9bf3h','YTEyYTUwNWVjY2E5YjRlMmRiODdkNjliY2FmM2ZiNTkyNTMxNGIzNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjBiZDc1Zjc2NGYxY2IyYWVkOTI1OTAyYWIzOWM2MzAwYWM5MmFkODQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-03-23 05:58:33.553154'),
 ('4q0z31nex266pbkz4f6ldojiigoihxor','MzBhOTlhZjBjNzRmNGNlZTU3YWQyZGEwN2M3ZTEzYWMwYWIwOWVlOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYmQ3NWY3NjRmMWNiMmFlZDkyNTkwMmFiMzljNjMwMGFjOTJhZDg0In0=','2017-03-26 10:23:42.191948'),
 ('lyui070nsgq92b71xw9xxqcxefqwe8jd','ZjEzMjU3OTk4MWQyOWU0Mzc3YTU0YTEyMTVlMDYyZGI2MTc4Zjc5YTp7Il9hdXRoX3VzZXJfaGFzaCI6IjdhMWQ1OGNmYTc3NzQ0MWQwYjkwNzk3ODQwNzdjNjc4ZDJjZDAyZDkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2017-03-29 07:21:33.497204');
CREATE TABLE `django_migrations` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`app`	varchar ( 255 ) NOT NULL,
	`name`	varchar ( 255 ) NOT NULL,
	`applied`	datetime NOT NULL
);
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (1,'contenttypes','0001_initial','2017-03-01 14:07:51.979620'),
 (2,'auth','0001_initial','2017-03-01 14:07:52.039623'),
 (3,'admin','0001_initial','2017-03-01 14:07:52.108627'),
 (4,'admin','0002_logentry_remove_auto_add','2017-03-01 14:07:52.159630'),
 (5,'contenttypes','0002_remove_content_type_name','2017-03-01 14:07:52.322639'),
 (6,'auth','0002_alter_permission_name_max_length','2017-03-01 14:07:52.434646'),
 (7,'auth','0003_alter_user_email_max_length','2017-03-01 14:07:52.511650'),
 (8,'auth','0004_alter_user_username_opts','2017-03-01 14:07:52.602655'),
 (9,'auth','0005_alter_user_last_login_null','2017-03-01 14:07:52.654658'),
 (10,'auth','0006_require_contenttypes_0002','2017-03-01 14:07:52.669659'),
 (11,'auth','0007_alter_validators_add_error_messages','2017-03-01 14:07:52.722662'),
 (12,'auth','0008_alter_user_username_max_length','2017-03-01 14:07:52.775665'),
 (13,'sessions','0001_initial','2017-03-01 14:07:52.809667'),
 (14,'main','0001_initial','2017-03-01 14:08:03.226263'),
 (15,'main','0002_auto_20170301_2145','2017-03-01 14:45:51.180983'),
 (16,'main','0003_imagemodel_date','2017-03-01 15:26:56.357983'),
 (17,'main','0004_auto_20170301_2358','2017-03-01 16:58:51.817449'),
 (18,'main','0005_auto_20170302_0231','2017-03-01 19:31:10.590157'),
 (19,'main','0006_auto_20170302_0238','2017-03-01 19:38:13.408341'),
 (20,'main','0007_auto_20170302_0249','2017-03-01 19:49:17.656333'),
 (21,'main','0008_auto_20170302_1128','2017-03-02 04:28:58.580372'),
 (22,'main','0009_auto_20170302_1242','2017-03-02 05:42:55.873057'),
 (23,'main','0010_auto_20170302_1245','2017-03-02 05:45:11.549623'),
 (24,'main','0011_auto_20170302_1553','2017-03-02 08:53:07.107066'),
 (25,'main','0012_auto_20170302_1555','2017-03-02 08:55:48.498203'),
 (26,'main','0013_auto_20170302_1604','2017-03-02 09:04:19.178266'),
 (27,'main','0014_auto_20170309_1238','2017-03-09 05:38:32.807092'),
 (28,'content','0001_initial','2017-03-09 05:38:33.023113'),
 (29,'content','0002_imagemodel_author','2017-03-10 07:51:16.247446'),
 (30,'content','0003_auto_20170314_2246','2017-03-14 15:46:58.171338'),
 (31,'content','0004_auto_20170314_2335','2017-03-14 16:35:28.875821'),
 (32,'content','0005_auto_20170315_1133','2017-03-15 04:33:48.948114');
CREATE TABLE `django_content_type` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`app_label`	varchar ( 100 ) NOT NULL,
	`model`	varchar ( 100 ) NOT NULL
);
INSERT INTO `django_content_type` (id,app_label,model) VALUES (1,'admin','logentry'),
 (2,'auth','user'),
 (3,'auth','group'),
 (4,'auth','permission'),
 (5,'contenttypes','contenttype'),
 (6,'sessions','session'),
 (8,'main','categorymodel'),
 (9,'content','imagemodel');
CREATE TABLE `django_admin_log` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`object_id`	text,
	`object_repr`	varchar ( 200 ) NOT NULL,
	`action_flag`	smallint unsigned NOT NULL,
	`change_message`	text NOT NULL,
	`content_type_id`	integer,
	`user_id`	integer NOT NULL,
	`action_time`	datetime NOT NULL,
	FOREIGN KEY(`user_id`) REFERENCES `auth_user`(`id`),
	FOREIGN KEY(`content_type_id`) REFERENCES `django_content_type`(`id`)
);
CREATE TABLE `content_imagemodel` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	varchar ( 32 ) NOT NULL,
	`image`	varchar ( 100 ) NOT NULL,
	`rating`	integer unsigned NOT NULL,
	`description`	text NOT NULL,
	`category_id`	integer NOT NULL,
	`date`	date NOT NULL,
	`author_id`	integer NOT NULL,
	FOREIGN KEY(`author_id`) REFERENCES `auth_user`(`id`),
	FOREIGN KEY(`category_id`) REFERENCES `main_categorymodel`(`id`)
);
INSERT INTO `content_imagemodel` (id,name,image,rating,description,category_id,date,author_id) VALUES (5,'somephoto1','photosets.jpg',1,'Фотка1',61,'2017-03-14',4),
 (6,'somephoto2','races.jpg',2,'Фотка1',62,'2017-03-14',4),
 (7,'somephoto3','wip.jpg',3,'Фотка1',63,'2017-03-14',4),
 (8,'somephoto4','photo.jpg',4,'Фотка1',64,'2017-03-14',4),
 (11,'Процесс1','images/back1-1_uZCpQdU.jpg',1,'Процесс1',63,'2017-03-14',4),
 (12,'Луна','images/IMG_2176_1_1_mXvqSUd.jpg',0,'Луна, первая проба',66,'2017-03-14',4),
 (13,'Степан Борисович Кравченко','images/IMG_6762.JPG',0,'Различные фотосеты.',64,'2017-03-14',4),
 (14,'Totjanno','images/8.jpg',0,'Portret',64,'2017-03-14',4);
CREATE TABLE `auth_user_user_permissions` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`user_id`	integer NOT NULL,
	`permission_id`	integer NOT NULL,
	FOREIGN KEY(`user_id`) REFERENCES `auth_user`(`id`),
	FOREIGN KEY(`permission_id`) REFERENCES `auth_permission`(`id`)
);
CREATE TABLE `auth_user_groups` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`user_id`	integer NOT NULL,
	`group_id`	integer NOT NULL,
	FOREIGN KEY(`group_id`) REFERENCES `auth_group`(`id`),
	FOREIGN KEY(`user_id`) REFERENCES `auth_user`(`id`)
);
CREATE TABLE `auth_user` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`password`	varchar ( 128 ) NOT NULL,
	`last_login`	datetime,
	`is_superuser`	bool NOT NULL,
	`first_name`	varchar ( 30 ) NOT NULL,
	`last_name`	varchar ( 30 ) NOT NULL,
	`email`	varchar ( 254 ) NOT NULL,
	`is_staff`	bool NOT NULL,
	`is_active`	bool NOT NULL,
	`date_joined`	datetime NOT NULL,
	`username`	varchar ( 150 ) NOT NULL UNIQUE
);
INSERT INTO `auth_user` (id,password,last_login,is_superuser,first_name,last_name,email,is_staff,is_active,date_joined,username) VALUES (1,'pbkdf2_sha256$30000$fB4OpMyjaABc$OiVAV9SumZjZLwBsRPkb4qI5WKJyyBuy/pbPlvbn+Lg=','2017-03-15 07:17:06.669204',1,'','','django@django.dj',1,1,'2017-03-01 16:33:46.967376','django'),
 (2,'pbkdf2_sha256$30000$UFICCzflVXMa$3BFoXoORTXHXajSXik+iDS63QGUaBXbXRUsY8U0z4ck=','2017-03-14 18:53:51.914727',0,'Степан','Кравченко','jjj@gg.tt',0,1,'2017-03-01 16:35:08.255026','zlobniyy'),
 (3,'pbkdf2_sha256$30000$9cka4f4VUr2Y$tBmivAx8snK5ZgrWCbQNnwGgXCCCnAPTkKsgEPpMfts=','2017-03-15 07:21:33.360204',0,'Степан','Кравченко','jjj@gg.tt',0,1,'2017-03-04 10:06:40.066390','stepan'),
 (4,'pbkdf2_sha256$30000$25w2BBYJN7k8$gxwOJACOz7qUSeFXbaiMz7BwzfFp+bXUPJddoXTF488=',NULL,0,'Пользователь','Неизвестный','jj@jj.jj',0,1,'2017-03-10 07:49:57.726595','Anonymous');
CREATE TABLE `auth_permission` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`content_type_id`	integer NOT NULL,
	`codename`	varchar ( 100 ) NOT NULL,
	`name`	varchar ( 255 ) NOT NULL,
	FOREIGN KEY(`content_type_id`) REFERENCES `django_content_type`(`id`)
);
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,2,'add_user','Can add user'),
 (5,2,'change_user','Can change user'),
 (6,2,'delete_user','Can delete user'),
 (7,3,'add_group','Can add group'),
 (8,3,'change_group','Can change group'),
 (9,3,'delete_group','Can delete group'),
 (10,4,'add_permission','Can add permission'),
 (11,4,'change_permission','Can change permission'),
 (12,4,'delete_permission','Can delete permission'),
 (13,5,'add_contenttype','Can add content type'),
 (14,5,'change_contenttype','Can change content type'),
 (15,5,'delete_contenttype','Can delete content type'),
 (16,6,'add_session','Can add session'),
 (17,6,'change_session','Can change session'),
 (18,6,'delete_session','Can delete session'),
 (22,8,'add_categorymodel','Can add categorymodel'),
 (23,8,'change_categorymodel','Can change categorymodel'),
 (24,8,'delete_categorymodel','Can delete categorymodel'),
 (25,9,'add_imagemodel','Can add imagemodel'),
 (26,9,'change_imagemodel','Can change imagemodel'),
 (27,9,'delete_imagemodel','Can delete imagemodel');
CREATE TABLE `auth_group_permissions` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`group_id`	integer NOT NULL,
	`permission_id`	integer NOT NULL,
	FOREIGN KEY(`group_id`) REFERENCES `auth_group`(`id`),
	FOREIGN KEY(`permission_id`) REFERENCES `auth_permission`(`id`)
);
CREATE TABLE `auth_group` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	varchar ( 80 ) NOT NULL UNIQUE
);
CREATE INDEX `django_session_de54fa62` ON `django_session` (
	`expire_date`	
);
CREATE UNIQUE INDEX `django_content_type_app_label_76bd3d3b_uniq` ON `django_content_type` (
	`app_label`	,
	`model`	
);
CREATE INDEX `django_admin_log_e8701ad4` ON `django_admin_log` (
	`user_id`	
);
CREATE INDEX `django_admin_log_417f1b1c` ON `django_admin_log` (
	`content_type_id`	
);
CREATE INDEX `content_imagemodel_b583a629` ON `content_imagemodel` (
	`category_id`	
);
CREATE INDEX `content_imagemodel_4f331e2f` ON `content_imagemodel` (
	`author_id`	
);
CREATE UNIQUE INDEX `auth_user_user_permissions_user_id_14a6b632_uniq` ON `auth_user_user_permissions` (
	`user_id`	,
	`permission_id`	
);
CREATE INDEX `auth_user_user_permissions_e8701ad4` ON `auth_user_user_permissions` (
	`user_id`	
);
CREATE INDEX `auth_user_user_permissions_8373b171` ON `auth_user_user_permissions` (
	`permission_id`	
);
CREATE UNIQUE INDEX `auth_user_groups_user_id_94350c0c_uniq` ON `auth_user_groups` (
	`user_id`	,
	`group_id`	
);
CREATE INDEX `auth_user_groups_e8701ad4` ON `auth_user_groups` (
	`user_id`	
);
CREATE INDEX `auth_user_groups_0e939a4f` ON `auth_user_groups` (
	`group_id`	
);
CREATE UNIQUE INDEX `auth_permission_content_type_id_01ab375a_uniq` ON `auth_permission` (
	`content_type_id`	,
	`codename`	
);
CREATE INDEX `auth_permission_417f1b1c` ON `auth_permission` (
	`content_type_id`	
);
CREATE UNIQUE INDEX `auth_group_permissions_group_id_0cd325b0_uniq` ON `auth_group_permissions` (
	`group_id`	,
	`permission_id`	
);
CREATE INDEX `auth_group_permissions_8373b171` ON `auth_group_permissions` (
	`permission_id`	
);
CREATE INDEX `auth_group_permissions_0e939a4f` ON `auth_group_permissions` (
	`group_id`	
);
COMMIT;
