/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : fafaerapis

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 07/09/2018 13:22:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 122 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (9, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (10, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (11, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add Bookmark', 6, 'add_bookmark');
INSERT INTO `auth_permission` VALUES (22, 'Can change Bookmark', 6, 'change_bookmark');
INSERT INTO `auth_permission` VALUES (23, 'Can delete Bookmark', 6, 'delete_bookmark');
INSERT INTO `auth_permission` VALUES (24, 'Can add User Setting', 7, 'add_usersettings');
INSERT INTO `auth_permission` VALUES (25, 'Can change User Setting', 7, 'change_usersettings');
INSERT INTO `auth_permission` VALUES (26, 'Can delete User Setting', 7, 'delete_usersettings');
INSERT INTO `auth_permission` VALUES (27, 'Can add User Widget', 8, 'add_userwidget');
INSERT INTO `auth_permission` VALUES (28, 'Can change User Widget', 8, 'change_userwidget');
INSERT INTO `auth_permission` VALUES (29, 'Can delete User Widget', 8, 'delete_userwidget');
INSERT INTO `auth_permission` VALUES (30, 'Can add log entry', 9, 'add_log');
INSERT INTO `auth_permission` VALUES (31, 'Can change log entry', 9, 'change_log');
INSERT INTO `auth_permission` VALUES (32, 'Can delete log entry', 9, 'delete_log');
INSERT INTO `auth_permission` VALUES (33, 'Can view Bookmark', 6, 'view_bookmark');
INSERT INTO `auth_permission` VALUES (34, 'Can view log entry', 9, 'view_log');
INSERT INTO `auth_permission` VALUES (35, 'Can view User Setting', 7, 'view_usersettings');
INSERT INTO `auth_permission` VALUES (36, 'Can view User Widget', 8, 'view_userwidget');
INSERT INTO `auth_permission` VALUES (37, 'Can add 用户信息', 10, 'add_user');
INSERT INTO `auth_permission` VALUES (38, 'Can change 用户信息', 10, 'change_user');
INSERT INTO `auth_permission` VALUES (39, 'Can delete 用户信息', 10, 'delete_user');
INSERT INTO `auth_permission` VALUES (40, 'Can view 用户信息', 10, 'view_user');
INSERT INTO `auth_permission` VALUES (41, 'Can add 内容详情', 11, 'add_banner');
INSERT INTO `auth_permission` VALUES (42, 'Can change 内容详情', 11, 'change_banner');
INSERT INTO `auth_permission` VALUES (43, 'Can delete 内容详情', 11, 'delete_banner');
INSERT INTO `auth_permission` VALUES (44, 'Can add 内容', 12, 'add_profile');
INSERT INTO `auth_permission` VALUES (45, 'Can change 内容', 12, 'change_profile');
INSERT INTO `auth_permission` VALUES (46, 'Can delete 内容', 12, 'delete_profile');
INSERT INTO `auth_permission` VALUES (47, 'Can add 个人资料', 13, 'add_profiledetail');
INSERT INTO `auth_permission` VALUES (48, 'Can change 个人资料', 13, 'change_profiledetail');
INSERT INTO `auth_permission` VALUES (49, 'Can delete 个人资料', 13, 'delete_profiledetail');
INSERT INTO `auth_permission` VALUES (50, 'Can add 联系方式', 13, 'add_contactdetail');
INSERT INTO `auth_permission` VALUES (51, 'Can change 联系方式', 13, 'change_contactdetail');
INSERT INTO `auth_permission` VALUES (52, 'Can delete 联系方式', 13, 'delete_contactdetail');
INSERT INTO `auth_permission` VALUES (53, 'Can view 轮播图', 11, 'view_banner');
INSERT INTO `auth_permission` VALUES (54, 'Can view 联系方式', 14, 'view_contactdetail');
INSERT INTO `auth_permission` VALUES (55, 'Can view 简介', 12, 'view_profile');
INSERT INTO `auth_permission` VALUES (56, 'Can view 个人资料', 13, 'view_profiledetail');
INSERT INTO `auth_permission` VALUES (58, 'Can add 歌手', 15, 'add_singer');
INSERT INTO `auth_permission` VALUES (59, 'Can change 歌手', 15, 'change_singer');
INSERT INTO `auth_permission` VALUES (60, 'Can delete 歌手', 15, 'delete_singer');
INSERT INTO `auth_permission` VALUES (61, 'Can add 专辑', 16, 'add_album');
INSERT INTO `auth_permission` VALUES (62, 'Can change 专辑', 16, 'change_album');
INSERT INTO `auth_permission` VALUES (63, 'Can delete 专辑', 16, 'delete_album');
INSERT INTO `auth_permission` VALUES (64, 'Can add 歌曲', 17, 'add_song');
INSERT INTO `auth_permission` VALUES (65, 'Can change 歌曲', 17, 'change_song');
INSERT INTO `auth_permission` VALUES (66, 'Can delete 歌曲', 17, 'delete_song');
INSERT INTO `auth_permission` VALUES (67, 'Can add 电台', 18, 'add_audiolist');
INSERT INTO `auth_permission` VALUES (68, 'Can change 电台', 18, 'change_audiolist');
INSERT INTO `auth_permission` VALUES (69, 'Can delete 电台', 18, 'delete_audiolist');
INSERT INTO `auth_permission` VALUES (70, 'Can view 专辑', 16, 'view_album');
INSERT INTO `auth_permission` VALUES (71, 'Can view 电台', 18, 'view_audiolist');
INSERT INTO `auth_permission` VALUES (72, 'Can view 歌手', 15, 'view_singer');
INSERT INTO `auth_permission` VALUES (73, 'Can view 歌曲', 17, 'view_song');
INSERT INTO `auth_permission` VALUES (74, 'Can add 专辑详情页', 19, 'add_albumdetail');
INSERT INTO `auth_permission` VALUES (75, 'Can change 专辑详情页', 19, 'change_albumdetail');
INSERT INTO `auth_permission` VALUES (76, 'Can delete 专辑详情页', 19, 'delete_albumdetail');
INSERT INTO `auth_permission` VALUES (77, 'Can add 电台详情页', 20, 'add_audiolistdetail');
INSERT INTO `auth_permission` VALUES (78, 'Can change 电台详情页', 20, 'change_audiolistdetail');
INSERT INTO `auth_permission` VALUES (79, 'Can delete 电台详情页', 20, 'delete_audiolistdetail');
INSERT INTO `auth_permission` VALUES (80, 'Can view 专辑详情页', 19, 'view_albumdetail');
INSERT INTO `auth_permission` VALUES (81, 'Can view 电台详情页', 20, 'view_audiolistdetail');
INSERT INTO `auth_permission` VALUES (82, 'Can view 电台', 18, 'view_audio');
INSERT INTO `auth_permission` VALUES (83, 'Can add 电台详情页', 21, 'add_audiodetail');
INSERT INTO `auth_permission` VALUES (84, 'Can change 电台详情页', 21, 'change_audiodetail');
INSERT INTO `auth_permission` VALUES (85, 'Can delete 电台详情页', 21, 'delete_audiodetail');
INSERT INTO `auth_permission` VALUES (86, 'Can add 电台', 18, 'add_audio');
INSERT INTO `auth_permission` VALUES (87, 'Can change 电台', 18, 'change_audio');
INSERT INTO `auth_permission` VALUES (88, 'Can delete 电台', 18, 'delete_audio');
INSERT INTO `auth_permission` VALUES (89, 'Can view 电台详情页', 21, 'view_audiodetail');
INSERT INTO `auth_permission` VALUES (90, 'Can add 相册', 22, 'add_gallery');
INSERT INTO `auth_permission` VALUES (91, 'Can change 相册', 22, 'change_gallery');
INSERT INTO `auth_permission` VALUES (92, 'Can delete 相册', 22, 'delete_gallery');
INSERT INTO `auth_permission` VALUES (93, 'Can add 照片', 23, 'add_photo');
INSERT INTO `auth_permission` VALUES (94, 'Can change 照片', 23, 'change_photo');
INSERT INTO `auth_permission` VALUES (95, 'Can delete 照片', 23, 'delete_photo');
INSERT INTO `auth_permission` VALUES (96, 'Can view 相册', 22, 'view_gallery');
INSERT INTO `auth_permission` VALUES (97, 'Can view 照片', 23, 'view_photo');
INSERT INTO `auth_permission` VALUES (98, 'Can add 相册明细', 24, 'add_gallerydetail');
INSERT INTO `auth_permission` VALUES (99, 'Can change 相册明细', 24, 'change_gallerydetail');
INSERT INTO `auth_permission` VALUES (100, 'Can delete 相册明细', 24, 'delete_gallerydetail');
INSERT INTO `auth_permission` VALUES (101, 'Can view 相册明细', 24, 'view_gallerydetail');
INSERT INTO `auth_permission` VALUES (102, 'Can add 视频合集明细', 25, 'add_videocollectiondetail');
INSERT INTO `auth_permission` VALUES (103, 'Can change 视频合集明细', 25, 'change_videocollectiondetail');
INSERT INTO `auth_permission` VALUES (104, 'Can delete 视频合集明细', 25, 'delete_videocollectiondetail');
INSERT INTO `auth_permission` VALUES (105, 'Can add 视频合集', 26, 'add_videocollection');
INSERT INTO `auth_permission` VALUES (106, 'Can change 视频合集', 26, 'change_videocollection');
INSERT INTO `auth_permission` VALUES (107, 'Can delete 视频合集', 26, 'delete_videocollection');
INSERT INTO `auth_permission` VALUES (108, 'Can add 视频', 27, 'add_video');
INSERT INTO `auth_permission` VALUES (109, 'Can change 视频', 27, 'change_video');
INSERT INTO `auth_permission` VALUES (110, 'Can delete 视频', 27, 'delete_video');
INSERT INTO `auth_permission` VALUES (111, 'Can view 视频', 27, 'view_video');
INSERT INTO `auth_permission` VALUES (112, 'Can view 视频合集', 26, 'view_videocollection');
INSERT INTO `auth_permission` VALUES (113, 'Can view 视频合集明细', 25, 'view_videocollectiondetail');
INSERT INTO `auth_permission` VALUES (114, 'Can add Token', 28, 'add_token');
INSERT INTO `auth_permission` VALUES (115, 'Can change Token', 28, 'change_token');
INSERT INTO `auth_permission` VALUES (116, 'Can delete Token', 28, 'delete_token');
INSERT INTO `auth_permission` VALUES (117, 'Can view Token', 28, 'view_token');
INSERT INTO `auth_permission` VALUES (118, 'Can add 文章', 29, 'add_article');
INSERT INTO `auth_permission` VALUES (119, 'Can change 文章', 29, 'change_article');
INSERT INTO `auth_permission` VALUES (120, 'Can delete 文章', 29, 'delete_article');
INSERT INTO `auth_permission` VALUES (121, 'Can view 文章', 29, 'view_article');

-- ----------------------------
-- Table structure for authtoken_token
-- ----------------------------
DROP TABLE IF EXISTS `authtoken_token`;
CREATE TABLE `authtoken_token`  (
  `key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `created` datetime(6) NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`) USING BTREE,
  UNIQUE INDEX `user_id`(`user_id`) USING BTREE,
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of authtoken_token
-- ----------------------------
INSERT INTO `authtoken_token` VALUES ('b44bc93b2396c0845722a470300b137cc76f849a', '2018-08-11 11:35:31.950732', 1);

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2018-08-08 18:48:35.688122', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"last_login\"]}}]', 10, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 30 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (28, 'authtoken', 'token');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (11, 'mp', 'banner');
INSERT INTO `django_content_type` VALUES (14, 'mp', 'contactdetail');
INSERT INTO `django_content_type` VALUES (12, 'mp', 'profile');
INSERT INTO `django_content_type` VALUES (13, 'mp', 'profiledetail');
INSERT INTO `django_content_type` VALUES (16, 'music', 'album');
INSERT INTO `django_content_type` VALUES (19, 'music', 'albumdetail');
INSERT INTO `django_content_type` VALUES (18, 'music', 'audio');
INSERT INTO `django_content_type` VALUES (21, 'music', 'audiodetail');
INSERT INTO `django_content_type` VALUES (20, 'music', 'audiolistdetail');
INSERT INTO `django_content_type` VALUES (15, 'music', 'singer');
INSERT INTO `django_content_type` VALUES (17, 'music', 'song');
INSERT INTO `django_content_type` VALUES (29, 'news', 'article');
INSERT INTO `django_content_type` VALUES (22, 'photos', 'gallery');
INSERT INTO `django_content_type` VALUES (24, 'photos', 'gallerydetail');
INSERT INTO `django_content_type` VALUES (23, 'photos', 'photo');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (10, 'users', 'user');
INSERT INTO `django_content_type` VALUES (27, 'videos', 'video');
INSERT INTO `django_content_type` VALUES (26, 'videos', 'videocollection');
INSERT INTO `django_content_type` VALUES (25, 'videos', 'videocollectiondetail');
INSERT INTO `django_content_type` VALUES (6, 'xadmin', 'bookmark');
INSERT INTO `django_content_type` VALUES (9, 'xadmin', 'log');
INSERT INTO `django_content_type` VALUES (7, 'xadmin', 'usersettings');
INSERT INTO `django_content_type` VALUES (8, 'xadmin', 'userwidget');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 42 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2018-08-08 17:14:28.022244');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2018-08-08 17:14:28.265594');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2018-08-08 17:14:28.923833');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2018-08-08 17:14:29.061469');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2018-08-08 17:14:29.072404');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2018-08-08 17:14:29.083375');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2018-08-08 17:14:29.095343');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2018-08-08 17:14:29.102350');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2018-08-08 17:14:29.119303');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2018-08-08 17:14:29.131255');
INSERT INTO `django_migrations` VALUES (11, 'users', '0001_initial', '2018-08-08 17:14:29.913155');
INSERT INTO `django_migrations` VALUES (12, 'admin', '0001_initial', '2018-08-08 17:14:30.223334');
INSERT INTO `django_migrations` VALUES (13, 'admin', '0002_logentry_remove_auto_add', '2018-08-08 17:14:30.242276');
INSERT INTO `django_migrations` VALUES (14, 'sessions', '0001_initial', '2018-08-08 17:14:30.370931');
INSERT INTO `django_migrations` VALUES (15, 'xadmin', '0001_initial', '2018-08-08 17:14:31.184755');
INSERT INTO `django_migrations` VALUES (16, 'xadmin', '0002_log', '2018-08-08 17:14:31.564741');
INSERT INTO `django_migrations` VALUES (17, 'xadmin', '0003_auto_20160715_0100', '2018-08-08 17:14:31.720357');
INSERT INTO `django_migrations` VALUES (18, 'mp', '0001_initial', '2018-08-08 22:12:25.530232');
INSERT INTO `django_migrations` VALUES (19, 'users', '0002_user_is_mp_user', '2018-08-08 22:12:25.748930');
INSERT INTO `django_migrations` VALUES (20, 'mp', '0002_auto_20180808_2216', '2018-08-08 22:16:28.613589');
INSERT INTO `django_migrations` VALUES (21, 'mp', '0003_profiledetail_order', '2018-08-08 22:19:32.655089');
INSERT INTO `django_migrations` VALUES (22, 'mp', '0004_auto_20180808_2228', '2018-08-08 22:28:10.493985');
INSERT INTO `django_migrations` VALUES (32, 'authtoken', '0001_initial', '2018-08-11 11:01:39.230130');
INSERT INTO `django_migrations` VALUES (33, 'authtoken', '0002_auto_20160226_1747', '2018-08-11 11:01:39.429598');
INSERT INTO `django_migrations` VALUES (34, 'videos', '0001_initial', '2018-08-11 12:26:33.082007');
INSERT INTO `django_migrations` VALUES (35, 'photos', '0001_initial', '2018-08-11 16:15:22.705303');
INSERT INTO `django_migrations` VALUES (36, 'music', '0001_initial', '2018-08-11 16:48:41.118987');
INSERT INTO `django_migrations` VALUES (39, 'music', '0002_auto_20180812_1612', '2018-08-12 16:12:35.310042');
INSERT INTO `django_migrations` VALUES (40, 'news', '0001_initial', '2018-08-22 23:30:31.268916');
INSERT INTO `django_migrations` VALUES (41, 'mp', '0005_auto_20180906_1535', '2018-09-06 15:35:12.424478');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('84phyhgs8i6l8tputqw1c9colxa5e0qh', 'MTFiYTJmNGUzMmNjMTE5MGNiZTZmMGY1NmEzNDRiNzRjMDNlMTA0ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImQzY2Y2MTg3ZDY1YjYzMGY3MWFjYjYzY2JiOGUyYWVhYWNkODE2NmEiLCJMSVNUX1FVRVJZIjpbWyJtdXNpYyIsImFsYnVtZGV0YWlsIl0sIiJdfQ==', '2018-08-23 18:00:55.210658');
INSERT INTO `django_session` VALUES ('gilvowvxcruy7xr3ipjm0rvc65dh9ctn', 'OWZiYmNkZDFmNmVlMGJlNGVlZTBmMjgzZTJmOTM2ZjU2OWE4NzI0Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImQzY2Y2MTg3ZDY1YjYzMGY3MWFjYjYzY2JiOGUyYWVhYWNkODE2NmEiLCJuYXZfbWVudSI6Ilt7XCJ0aXRsZVwiOiBcIlx1NTZmZVx1NzI0N1x1N2JhMVx1NzQwNlwiLCBcIm1lbnVzXCI6IFt7XCJ0aXRsZVwiOiBcIlx1NzZmOFx1NTE4Y1wiLCBcInVybFwiOiBcIi94YWRtaW4vcGhvdG9zL2dhbGxlcnkvXCIsIFwiaWNvblwiOiBcImZhIGZhLXBpY3R1cmUtb1wiLCBcIm9yZGVyXCI6IDIwfSwge1widGl0bGVcIjogXCJcdTcxNjdcdTcyNDdcIiwgXCJ1cmxcIjogXCIveGFkbWluL3Bob3Rvcy9waG90by9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMjF9LCB7XCJ0aXRsZVwiOiBcIlx1NzZmOFx1NTE4Y1x1NjYwZVx1N2VjNlwiLCBcInVybFwiOiBcIi94YWRtaW4vcGhvdG9zL2dhbGxlcnlkZXRhaWwvXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDIyfV0sIFwiZmlyc3RfaWNvblwiOiBcImZhIGZhLXBpY3R1cmUtb1wiLCBcImZpcnN0X3VybFwiOiBcIi94YWRtaW4vcGhvdG9zL2dhbGxlcnkvXCJ9LCB7XCJ0aXRsZVwiOiBcIlx1NWMwZlx1N2EwYlx1NWU4Zlx1N2JhMVx1NzQwNlwiLCBcIm1lbnVzXCI6IFt7XCJ0aXRsZVwiOiBcIlx1OGY2ZVx1NjRhZFx1NTZmZVwiLCBcInVybFwiOiBcIi94YWRtaW4vbXAvYmFubmVyL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiA3fSwge1widGl0bGVcIjogXCJcdTdiODBcdTRlY2JcIiwgXCJ1cmxcIjogXCIveGFkbWluL21wL3Byb2ZpbGUvXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDh9LCB7XCJ0aXRsZVwiOiBcIlx1NGUyYVx1NGViYVx1OGQ0NFx1NjU5OVwiLCBcInVybFwiOiBcIi94YWRtaW4vbXAvcHJvZmlsZWRldGFpbC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogOX0sIHtcInRpdGxlXCI6IFwiXHU4MDU0XHU3Y2ZiXHU2NWI5XHU1ZjBmXCIsIFwidXJsXCI6IFwiL3hhZG1pbi9tcC9jb250YWN0ZGV0YWlsL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiAxMH1dLCBcImZpcnN0X3VybFwiOiBcIi94YWRtaW4vbXAvYmFubmVyL1wifSwge1widGl0bGVcIjogXCJcdTY1YjBcdTk1ZmJcdTdiYTFcdTc0MDZcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTY1ODdcdTdhZTBcIiwgXCJ1cmxcIjogXCIveGFkbWluL25ld3MvYXJ0aWNsZS9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMjN9XSwgXCJmaXJzdF91cmxcIjogXCIveGFkbWluL25ld3MvYXJ0aWNsZS9cIn0sIHtcInRpdGxlXCI6IFwiXHU3NTI4XHU2MjM3XHU3YmExXHU3NDA2XCIsIFwibWVudXNcIjogW3tcInRpdGxlXCI6IFwiXHU3NTI4XHU2MjM3XHU0ZmUxXHU2MDZmXCIsIFwidXJsXCI6IFwiL3hhZG1pbi91c2Vycy91c2VyL1wiLCBcImljb25cIjogXCJmYSBmYS11c2VyXCIsIFwib3JkZXJcIjogM31dLCBcImZpcnN0X2ljb25cIjogXCJmYSBmYS11c2VyXCIsIFwiZmlyc3RfdXJsXCI6IFwiL3hhZG1pbi91c2Vycy91c2VyL1wifSwge1widGl0bGVcIjogXCJcdTdiYTFcdTc0MDZcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTY1ZTVcdTVmZDdcdThiYjBcdTVmNTVcIiwgXCJ1cmxcIjogXCIveGFkbWluL3hhZG1pbi9sb2cvXCIsIFwiaWNvblwiOiBcImZhIGZhLWNvZ1wiLCBcIm9yZGVyXCI6IDZ9XSwgXCJmaXJzdF9pY29uXCI6IFwiZmEgZmEtY29nXCIsIFwiZmlyc3RfdXJsXCI6IFwiL3hhZG1pbi94YWRtaW4vbG9nL1wifSwge1widGl0bGVcIjogXCJcdTg5YzZcdTk4OTFcdTdiYTFcdTc0MDZcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTg5YzZcdTk4OTFcdTU0MDhcdTk2YzZcIiwgXCJ1cmxcIjogXCIveGFkbWluL3ZpZGVvcy92aWRlb2NvbGxlY3Rpb24vXCIsIFwiaWNvblwiOiBcImZhIGZhLXZpZGVvLWNhbWVyYVwiLCBcIm9yZGVyXCI6IDE3fSwge1widGl0bGVcIjogXCJcdTg5YzZcdTk4OTFcIiwgXCJ1cmxcIjogXCIveGFkbWluL3ZpZGVvcy92aWRlby9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTh9LCB7XCJ0aXRsZVwiOiBcIlx1ODljNlx1OTg5MVx1NTQwOFx1OTZjNlx1NjYwZVx1N2VjNlwiLCBcInVybFwiOiBcIi94YWRtaW4vdmlkZW9zL3ZpZGVvY29sbGVjdGlvbmRldGFpbC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTl9XSwgXCJmaXJzdF9pY29uXCI6IFwiZmEgZmEtdmlkZW8tY2FtZXJhXCIsIFwiZmlyc3RfdXJsXCI6IFwiL3hhZG1pbi92aWRlb3MvdmlkZW9jb2xsZWN0aW9uL1wifSwge1widGl0bGVcIjogXCJcdThiYTRcdThiYzFcdTU0OGNcdTYzODhcdTY3NDNcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTdlYzRcIiwgXCJ1cmxcIjogXCIveGFkbWluL2F1dGgvZ3JvdXAvXCIsIFwiaWNvblwiOiBcImZhIGZhLWdyb3VwXCIsIFwib3JkZXJcIjogMn0sIHtcInRpdGxlXCI6IFwiXHU2NzQzXHU5NjUwXCIsIFwidXJsXCI6IFwiL3hhZG1pbi9hdXRoL3Blcm1pc3Npb24vXCIsIFwiaWNvblwiOiBcImZhIGZhLWxvY2tcIiwgXCJvcmRlclwiOiA0fV0sIFwiZmlyc3RfaWNvblwiOiBcImZhIGZhLWdyb3VwXCIsIFwiZmlyc3RfdXJsXCI6IFwiL3hhZG1pbi9hdXRoL2dyb3VwL1wifSwge1widGl0bGVcIjogXCJcdTk3ZjNcdTRlNTBcdTdiYTFcdTc0MDZcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTZiNGNcdTYyNGJcIiwgXCJ1cmxcIjogXCIveGFkbWluL211c2ljL3Npbmdlci9cIiwgXCJpY29uXCI6IFwiZmEgZmEtbXVzaWNcIiwgXCJvcmRlclwiOiAxMX0sIHtcInRpdGxlXCI6IFwiXHU0ZTEzXHU4ZjkxXCIsIFwidXJsXCI6IFwiL3hhZG1pbi9tdXNpYy9hbGJ1bS9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTJ9LCB7XCJ0aXRsZVwiOiBcIlx1NzUzNVx1NTNmMFwiLCBcInVybFwiOiBcIi94YWRtaW4vbXVzaWMvYXVkaW8vXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDEzfSwge1widGl0bGVcIjogXCJcdTZiNGNcdTY2ZjJcIiwgXCJ1cmxcIjogXCIveGFkbWluL211c2ljL3NvbmcvXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDE0fSwge1widGl0bGVcIjogXCJcdTRlMTNcdThmOTFcdThiZTZcdTYwYzVcdTk4NzVcIiwgXCJ1cmxcIjogXCIveGFkbWluL211c2ljL2FsYnVtZGV0YWlsL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiAxNX0sIHtcInRpdGxlXCI6IFwiXHU3NTM1XHU1M2YwXHU4YmU2XHU2MGM1XHU5ODc1XCIsIFwidXJsXCI6IFwiL3hhZG1pbi9tdXNpYy9hdWRpb2RldGFpbC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTZ9XSwgXCJmaXJzdF9pY29uXCI6IFwiZmEgZmEtbXVzaWNcIiwgXCJmaXJzdF91cmxcIjogXCIveGFkbWluL211c2ljL3Npbmdlci9cIn1dIiwiTElTVF9RVUVSWSI6W1sibmV3cyIsImFydGljbGUiXSwiIl19', '2018-09-05 23:34:35.269296');
INSERT INTO `django_session` VALUES ('j67gi6tzly9hx59p1m5ticl037ummusy', 'OTZiZGM3YjU5YTA4ZmFkM2Q5Yzk2YjNlNjNiYjY2ZWI0MThkM2RmMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImQzY2Y2MTg3ZDY1YjYzMGY3MWFjYjYzY2JiOGUyYWVhYWNkODE2NmEiLCJuYXZfbWVudSI6Ilt7XCJ0aXRsZVwiOiBcIlx1NTZmZVx1NzI0N1x1N2JhMVx1NzQwNlwiLCBcIm1lbnVzXCI6IFt7XCJ0aXRsZVwiOiBcIlx1NzZmOFx1NTE4Y1wiLCBcInVybFwiOiBcIi94YWRtaW4vcGhvdG9zL2dhbGxlcnkvXCIsIFwiaWNvblwiOiBcImZhIGZhLXBpY3R1cmUtb1wiLCBcIm9yZGVyXCI6IDIwfSwge1widGl0bGVcIjogXCJcdTcxNjdcdTcyNDdcIiwgXCJ1cmxcIjogXCIveGFkbWluL3Bob3Rvcy9waG90by9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMjF9LCB7XCJ0aXRsZVwiOiBcIlx1NzZmOFx1NTE4Y1x1NjYwZVx1N2VjNlwiLCBcInVybFwiOiBcIi94YWRtaW4vcGhvdG9zL2dhbGxlcnlkZXRhaWwvXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDIyfV0sIFwiZmlyc3RfaWNvblwiOiBcImZhIGZhLXBpY3R1cmUtb1wiLCBcImZpcnN0X3VybFwiOiBcIi94YWRtaW4vcGhvdG9zL2dhbGxlcnkvXCJ9LCB7XCJ0aXRsZVwiOiBcIlx1NWMwZlx1N2EwYlx1NWU4Zlx1N2JhMVx1NzQwNlwiLCBcIm1lbnVzXCI6IFt7XCJ0aXRsZVwiOiBcIlx1OGY2ZVx1NjRhZFx1NTZmZVwiLCBcInVybFwiOiBcIi94YWRtaW4vbXAvYmFubmVyL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiA3fSwge1widGl0bGVcIjogXCJcdTdiODBcdTRlY2JcIiwgXCJ1cmxcIjogXCIveGFkbWluL21wL3Byb2ZpbGUvXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDh9LCB7XCJ0aXRsZVwiOiBcIlx1NGUyYVx1NGViYVx1OGQ0NFx1NjU5OVwiLCBcInVybFwiOiBcIi94YWRtaW4vbXAvcHJvZmlsZWRldGFpbC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogOX0sIHtcInRpdGxlXCI6IFwiXHU4MDU0XHU3Y2ZiXHU2NWI5XHU1ZjBmXCIsIFwidXJsXCI6IFwiL3hhZG1pbi9tcC9jb250YWN0ZGV0YWlsL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiAxMH1dLCBcImZpcnN0X3VybFwiOiBcIi94YWRtaW4vbXAvYmFubmVyL1wifSwge1widGl0bGVcIjogXCJcdTY1YjBcdTk1ZmJcdTdiYTFcdTc0MDZcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTY1ODdcdTdhZTBcIiwgXCJ1cmxcIjogXCIveGFkbWluL25ld3MvYXJ0aWNsZS9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMjN9XSwgXCJmaXJzdF91cmxcIjogXCIveGFkbWluL25ld3MvYXJ0aWNsZS9cIn0sIHtcInRpdGxlXCI6IFwiXHU3NTI4XHU2MjM3XHU3YmExXHU3NDA2XCIsIFwibWVudXNcIjogW3tcInRpdGxlXCI6IFwiXHU3NTI4XHU2MjM3XHU0ZmUxXHU2MDZmXCIsIFwidXJsXCI6IFwiL3hhZG1pbi91c2Vycy91c2VyL1wiLCBcImljb25cIjogXCJmYSBmYS11c2VyXCIsIFwib3JkZXJcIjogM31dLCBcImZpcnN0X2ljb25cIjogXCJmYSBmYS11c2VyXCIsIFwiZmlyc3RfdXJsXCI6IFwiL3hhZG1pbi91c2Vycy91c2VyL1wifSwge1widGl0bGVcIjogXCJcdTdiYTFcdTc0MDZcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTY1ZTVcdTVmZDdcdThiYjBcdTVmNTVcIiwgXCJ1cmxcIjogXCIveGFkbWluL3hhZG1pbi9sb2cvXCIsIFwiaWNvblwiOiBcImZhIGZhLWNvZ1wiLCBcIm9yZGVyXCI6IDZ9XSwgXCJmaXJzdF9pY29uXCI6IFwiZmEgZmEtY29nXCIsIFwiZmlyc3RfdXJsXCI6IFwiL3hhZG1pbi94YWRtaW4vbG9nL1wifSwge1widGl0bGVcIjogXCJcdTg5YzZcdTk4OTFcdTdiYTFcdTc0MDZcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTg5YzZcdTk4OTFcdTU0MDhcdTk2YzZcIiwgXCJ1cmxcIjogXCIveGFkbWluL3ZpZGVvcy92aWRlb2NvbGxlY3Rpb24vXCIsIFwiaWNvblwiOiBcImZhIGZhLXZpZGVvLWNhbWVyYVwiLCBcIm9yZGVyXCI6IDE3fSwge1widGl0bGVcIjogXCJcdTg5YzZcdTk4OTFcIiwgXCJ1cmxcIjogXCIveGFkbWluL3ZpZGVvcy92aWRlby9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTh9LCB7XCJ0aXRsZVwiOiBcIlx1ODljNlx1OTg5MVx1NTQwOFx1OTZjNlx1NjYwZVx1N2VjNlwiLCBcInVybFwiOiBcIi94YWRtaW4vdmlkZW9zL3ZpZGVvY29sbGVjdGlvbmRldGFpbC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTl9XSwgXCJmaXJzdF9pY29uXCI6IFwiZmEgZmEtdmlkZW8tY2FtZXJhXCIsIFwiZmlyc3RfdXJsXCI6IFwiL3hhZG1pbi92aWRlb3MvdmlkZW9jb2xsZWN0aW9uL1wifSwge1widGl0bGVcIjogXCJcdThiYTRcdThiYzFcdTU0OGNcdTYzODhcdTY3NDNcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTdlYzRcIiwgXCJ1cmxcIjogXCIveGFkbWluL2F1dGgvZ3JvdXAvXCIsIFwiaWNvblwiOiBcImZhIGZhLWdyb3VwXCIsIFwib3JkZXJcIjogMn0sIHtcInRpdGxlXCI6IFwiXHU2NzQzXHU5NjUwXCIsIFwidXJsXCI6IFwiL3hhZG1pbi9hdXRoL3Blcm1pc3Npb24vXCIsIFwiaWNvblwiOiBcImZhIGZhLWxvY2tcIiwgXCJvcmRlclwiOiA0fV0sIFwiZmlyc3RfaWNvblwiOiBcImZhIGZhLWdyb3VwXCIsIFwiZmlyc3RfdXJsXCI6IFwiL3hhZG1pbi9hdXRoL2dyb3VwL1wifSwge1widGl0bGVcIjogXCJcdTk3ZjNcdTRlNTBcdTdiYTFcdTc0MDZcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTZiNGNcdTYyNGJcIiwgXCJ1cmxcIjogXCIveGFkbWluL211c2ljL3Npbmdlci9cIiwgXCJpY29uXCI6IFwiZmEgZmEtbXVzaWNcIiwgXCJvcmRlclwiOiAxMX0sIHtcInRpdGxlXCI6IFwiXHU0ZTEzXHU4ZjkxXCIsIFwidXJsXCI6IFwiL3hhZG1pbi9tdXNpYy9hbGJ1bS9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTJ9LCB7XCJ0aXRsZVwiOiBcIlx1NzUzNVx1NTNmMFwiLCBcInVybFwiOiBcIi94YWRtaW4vbXVzaWMvYXVkaW8vXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDEzfSwge1widGl0bGVcIjogXCJcdTZiNGNcdTY2ZjJcIiwgXCJ1cmxcIjogXCIveGFkbWluL211c2ljL3NvbmcvXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDE0fSwge1widGl0bGVcIjogXCJcdTRlMTNcdThmOTFcdThiZTZcdTYwYzVcdTk4NzVcIiwgXCJ1cmxcIjogXCIveGFkbWluL211c2ljL2FsYnVtZGV0YWlsL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiAxNX0sIHtcInRpdGxlXCI6IFwiXHU3NTM1XHU1M2YwXHU4YmU2XHU2MGM1XHU5ODc1XCIsIFwidXJsXCI6IFwiL3hhZG1pbi9tdXNpYy9hdWRpb2RldGFpbC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTZ9XSwgXCJmaXJzdF9pY29uXCI6IFwiZmEgZmEtbXVzaWNcIiwgXCJmaXJzdF91cmxcIjogXCIveGFkbWluL211c2ljL3Npbmdlci9cIn1dIn0=', '2018-09-19 20:17:04.422755');
INSERT INTO `django_session` VALUES ('nx3zd1xnvi83n8obtr6ub21d48cvgy19', 'ZDIwNzAwN2YwMDU1NWYxMWQ4MGEzMmU3YTZiMDEwZmQ1ZDY1YWMxZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImQzY2Y2MTg3ZDY1YjYzMGY3MWFjYjYzY2JiOGUyYWVhYWNkODE2NmEifQ==', '2018-08-26 16:19:50.670281');
INSERT INTO `django_session` VALUES ('qw1q0gzqq1ohr7bzy5poo37kp8mi3i9v', 'M2RiZDEyZjY4MTY0ZmMzZmZjZDk4NzY0YzQ2YmMzYzVmMjBhNjNmNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImQzY2Y2MTg3ZDY1YjYzMGY3MWFjYjYzY2JiOGUyYWVhYWNkODE2NmEiLCJMSVNUX1FVRVJZIjpbWyJuZXdzIiwiYXJ0aWNsZSJdLCIiXSwibmF2X21lbnUiOiJbe1widGl0bGVcIjogXCJcdTU2ZmVcdTcyNDdcdTdiYTFcdTc0MDZcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTc2ZjhcdTUxOGNcIiwgXCJ1cmxcIjogXCIveGFkbWluL3Bob3Rvcy9nYWxsZXJ5L1wiLCBcImljb25cIjogXCJmYSBmYS1waWN0dXJlLW9cIiwgXCJvcmRlclwiOiAyMH0sIHtcInRpdGxlXCI6IFwiXHU3MTY3XHU3MjQ3XCIsIFwidXJsXCI6IFwiL3hhZG1pbi9waG90b3MvcGhvdG8vXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDIxfSwge1widGl0bGVcIjogXCJcdTc2ZjhcdTUxOGNcdTY2MGVcdTdlYzZcIiwgXCJ1cmxcIjogXCIveGFkbWluL3Bob3Rvcy9nYWxsZXJ5ZGV0YWlsL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiAyMn1dLCBcImZpcnN0X2ljb25cIjogXCJmYSBmYS1waWN0dXJlLW9cIiwgXCJmaXJzdF91cmxcIjogXCIveGFkbWluL3Bob3Rvcy9nYWxsZXJ5L1wifSwge1widGl0bGVcIjogXCJcdTVjMGZcdTdhMGJcdTVlOGZcdTdiYTFcdTc0MDZcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdThmNmVcdTY0YWRcdTU2ZmVcIiwgXCJ1cmxcIjogXCIveGFkbWluL21wL2Jhbm5lci9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogN30sIHtcInRpdGxlXCI6IFwiXHU3YjgwXHU0ZWNiXCIsIFwidXJsXCI6IFwiL3hhZG1pbi9tcC9wcm9maWxlL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiA4fSwge1widGl0bGVcIjogXCJcdTRlMmFcdTRlYmFcdThkNDRcdTY1OTlcIiwgXCJ1cmxcIjogXCIveGFkbWluL21wL3Byb2ZpbGVkZXRhaWwvXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDl9LCB7XCJ0aXRsZVwiOiBcIlx1ODA1NFx1N2NmYlx1NjViOVx1NWYwZlwiLCBcInVybFwiOiBcIi94YWRtaW4vbXAvY29udGFjdGRldGFpbC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTB9XSwgXCJmaXJzdF91cmxcIjogXCIveGFkbWluL21wL2Jhbm5lci9cIn0sIHtcInRpdGxlXCI6IFwiXHU2NWIwXHU5NWZiXHU3YmExXHU3NDA2XCIsIFwibWVudXNcIjogW3tcInRpdGxlXCI6IFwiXHU2NTg3XHU3YWUwXCIsIFwidXJsXCI6IFwiL3hhZG1pbi9uZXdzL2FydGljbGUvXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDIzfV0sIFwiZmlyc3RfdXJsXCI6IFwiL3hhZG1pbi9uZXdzL2FydGljbGUvXCJ9LCB7XCJ0aXRsZVwiOiBcIlx1NzUyOFx1NjIzN1x1N2JhMVx1NzQwNlwiLCBcIm1lbnVzXCI6IFt7XCJ0aXRsZVwiOiBcIlx1NzUyOFx1NjIzN1x1NGZlMVx1NjA2ZlwiLCBcInVybFwiOiBcIi94YWRtaW4vdXNlcnMvdXNlci9cIiwgXCJpY29uXCI6IFwiZmEgZmEtdXNlclwiLCBcIm9yZGVyXCI6IDN9XSwgXCJmaXJzdF9pY29uXCI6IFwiZmEgZmEtdXNlclwiLCBcImZpcnN0X3VybFwiOiBcIi94YWRtaW4vdXNlcnMvdXNlci9cIn0sIHtcInRpdGxlXCI6IFwiXHU3YmExXHU3NDA2XCIsIFwibWVudXNcIjogW3tcInRpdGxlXCI6IFwiXHU2NWU1XHU1ZmQ3XHU4YmIwXHU1ZjU1XCIsIFwidXJsXCI6IFwiL3hhZG1pbi94YWRtaW4vbG9nL1wiLCBcImljb25cIjogXCJmYSBmYS1jb2dcIiwgXCJvcmRlclwiOiA2fV0sIFwiZmlyc3RfaWNvblwiOiBcImZhIGZhLWNvZ1wiLCBcImZpcnN0X3VybFwiOiBcIi94YWRtaW4veGFkbWluL2xvZy9cIn0sIHtcInRpdGxlXCI6IFwiXHU4OWM2XHU5ODkxXHU3YmExXHU3NDA2XCIsIFwibWVudXNcIjogW3tcInRpdGxlXCI6IFwiXHU4OWM2XHU5ODkxXHU1NDA4XHU5NmM2XCIsIFwidXJsXCI6IFwiL3hhZG1pbi92aWRlb3MvdmlkZW9jb2xsZWN0aW9uL1wiLCBcImljb25cIjogXCJmYSBmYS12aWRlby1jYW1lcmFcIiwgXCJvcmRlclwiOiAxN30sIHtcInRpdGxlXCI6IFwiXHU4OWM2XHU5ODkxXCIsIFwidXJsXCI6IFwiL3hhZG1pbi92aWRlb3MvdmlkZW8vXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDE4fSwge1widGl0bGVcIjogXCJcdTg5YzZcdTk4OTFcdTU0MDhcdTk2YzZcdTY2MGVcdTdlYzZcIiwgXCJ1cmxcIjogXCIveGFkbWluL3ZpZGVvcy92aWRlb2NvbGxlY3Rpb25kZXRhaWwvXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDE5fV0sIFwiZmlyc3RfaWNvblwiOiBcImZhIGZhLXZpZGVvLWNhbWVyYVwiLCBcImZpcnN0X3VybFwiOiBcIi94YWRtaW4vdmlkZW9zL3ZpZGVvY29sbGVjdGlvbi9cIn0sIHtcInRpdGxlXCI6IFwiXHU4YmE0XHU4YmMxXHU1NDhjXHU2Mzg4XHU2NzQzXCIsIFwibWVudXNcIjogW3tcInRpdGxlXCI6IFwiXHU3ZWM0XCIsIFwidXJsXCI6IFwiL3hhZG1pbi9hdXRoL2dyb3VwL1wiLCBcImljb25cIjogXCJmYSBmYS1ncm91cFwiLCBcIm9yZGVyXCI6IDJ9LCB7XCJ0aXRsZVwiOiBcIlx1Njc0M1x1OTY1MFwiLCBcInVybFwiOiBcIi94YWRtaW4vYXV0aC9wZXJtaXNzaW9uL1wiLCBcImljb25cIjogXCJmYSBmYS1sb2NrXCIsIFwib3JkZXJcIjogNH1dLCBcImZpcnN0X2ljb25cIjogXCJmYSBmYS1ncm91cFwiLCBcImZpcnN0X3VybFwiOiBcIi94YWRtaW4vYXV0aC9ncm91cC9cIn0sIHtcInRpdGxlXCI6IFwiXHU5N2YzXHU0ZTUwXHU3YmExXHU3NDA2XCIsIFwibWVudXNcIjogW3tcInRpdGxlXCI6IFwiXHU2YjRjXHU2MjRiXCIsIFwidXJsXCI6IFwiL3hhZG1pbi9tdXNpYy9zaW5nZXIvXCIsIFwiaWNvblwiOiBcImZhIGZhLW11c2ljXCIsIFwib3JkZXJcIjogMTF9LCB7XCJ0aXRsZVwiOiBcIlx1NGUxM1x1OGY5MVwiLCBcInVybFwiOiBcIi94YWRtaW4vbXVzaWMvYWxidW0vXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDEyfSwge1widGl0bGVcIjogXCJcdTc1MzVcdTUzZjBcIiwgXCJ1cmxcIjogXCIveGFkbWluL211c2ljL2F1ZGlvL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiAxM30sIHtcInRpdGxlXCI6IFwiXHU2YjRjXHU2NmYyXCIsIFwidXJsXCI6IFwiL3hhZG1pbi9tdXNpYy9zb25nL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiAxNH0sIHtcInRpdGxlXCI6IFwiXHU0ZTEzXHU4ZjkxXHU4YmU2XHU2MGM1XHU5ODc1XCIsIFwidXJsXCI6IFwiL3hhZG1pbi9tdXNpYy9hbGJ1bWRldGFpbC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTV9LCB7XCJ0aXRsZVwiOiBcIlx1NzUzNVx1NTNmMFx1OGJlNlx1NjBjNVx1OTg3NVwiLCBcInVybFwiOiBcIi94YWRtaW4vbXVzaWMvYXVkaW9kZXRhaWwvXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDE2fV0sIFwiZmlyc3RfaWNvblwiOiBcImZhIGZhLW11c2ljXCIsIFwiZmlyc3RfdXJsXCI6IFwiL3hhZG1pbi9tdXNpYy9zaW5nZXIvXCJ9XSJ9', '2018-09-06 00:29:41.263874');

-- ----------------------------
-- Table structure for mp_banner
-- ----------------------------
DROP TABLE IF EXISTS `mp_banner`;
CREATE TABLE `mp_banner`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `order` int(11) NOT NULL,
  `add_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `update_time` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of mp_banner
-- ----------------------------
INSERT INTO `mp_banner` VALUES (1, '陈一发儿', '陈一发儿', 'banner\\2018\\08\\01.jpg', 10, '2018-08-08 22:16:00.000000', 0, '2018-09-06 15:35:11.882953');
INSERT INTO `mp_banner` VALUES (2, '陈一发儿', '陈一发儿', 'banner\\2018\\08\\33.jpg', 20, '2018-08-08 22:17:00.000000', 0, '2018-09-06 15:35:11.882953');
INSERT INTO `mp_banner` VALUES (3, '陈一发儿', '陈一发儿', 'banner\\2018\\08\\45.jpg', 30, '2018-08-08 22:17:00.000000', 0, '2018-09-06 15:35:11.882953');
INSERT INTO `mp_banner` VALUES (5, 'test', 'test', 'banner\\2018\\08\\mp.png', 10, '2018-08-09 10:53:00.000000', 1, '2018-09-06 15:35:11.882953');

-- ----------------------------
-- Table structure for mp_profile
-- ----------------------------
DROP TABLE IF EXISTS `mp_profile`;
CREATE TABLE `mp_profile`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `avatar` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `add_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `update_time` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of mp_profile
-- ----------------------------
INSERT INTO `mp_profile` VALUES (1, '陈一发儿', '山城降生，前设计院院花，直播界泥石流，不睡者，万儿之母，暴击女王，斗鱼主机区的解放者，约德尔人&霍比特人的女王，67373统治者暨418094守护者，大泳池划水的卡丽熙 ，打碎三观之人，花式飙车界，网', 'avatar\\2018\\08\\IMG_3522.JPG', '2018-08-08 22:13:00.000000', 0, '2018-09-06 15:35:12.068468');

-- ----------------------------
-- Table structure for mp_profiledetail
-- ----------------------------
DROP TABLE IF EXISTS `mp_profiledetail`;
CREATE TABLE `mp_profiledetail`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `type` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `add_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `order` int(11) NOT NULL,
  `update_time` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of mp_profiledetail
-- ----------------------------
INSERT INTO `mp_profiledetail` VALUES (1, '生日', '10.13', 'profile', 'content\\2018\\08\\birthday.png', '2018-08-08 22:19:00.000000', 0, 10, '2018-09-06 15:35:12.242964');
INSERT INTO `mp_profiledetail` VALUES (2, '住址', '上海市', 'profile', 'content\\2018\\08\\location.png', '2018-08-08 22:20:00.000000', 0, 20, '2018-09-06 15:35:12.242964');
INSERT INTO `mp_profiledetail` VALUES (3, '职业', '斗鱼主播', 'profile', 'content\\2018\\08\\job.png', '2018-08-08 22:21:00.000000', 0, 30, '2018-09-06 15:35:12.242964');
INSERT INTO `mp_profiledetail` VALUES (4, '房间', 'www.douyu.com/67373', 'profile', 'content\\2018\\08\\room.png', '2018-08-08 22:21:00.000000', 0, 40, '2018-09-06 15:35:12.242964');
INSERT INTO `mp_profiledetail` VALUES (5, '微博', '陈一发儿', 'contact', 'content\\2018\\08\\weibo.png', '2018-08-08 22:22:00.000000', 0, 50, '2018-09-06 15:35:12.242964');
INSERT INTO `mp_profiledetail` VALUES (6, '邮件', 'chenyifaer888@163.com', 'contact', 'content\\2018\\08\\email.png', '2018-08-08 22:22:00.000000', 0, 60, '2018-09-06 15:35:12.242964');
INSERT INTO `mp_profiledetail` VALUES (7, '淘宝', 'https://67373.taobao.com', 'contact', 'content\\2018\\08\\taobao.png', '2018-08-08 22:23:00.000000', 0, 70, '2018-09-06 15:35:12.242964');
INSERT INTO `mp_profiledetail` VALUES (8, '个人主页', 'www.chenyifaer.com', 'contact', 'content\\2018\\08\\website.png', '2018-08-08 22:23:00.000000', 0, 80, '2018-09-06 15:35:12.242964');
INSERT INTO `mp_profiledetail` VALUES (9, '公众号', '陈一发儿粉丝后援会', 'contact', 'content\\2018\\08\\mp.png', '2018-08-08 22:24:00.000000', 0, 90, '2018-09-06 15:35:12.242964');

-- ----------------------------
-- Table structure for music_album
-- ----------------------------
DROP TABLE IF EXISTS `music_album`;
CREATE TABLE `music_album`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `cover_img` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `background_img` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `release_date` date NOT NULL,
  `release_company` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `singer_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `music_album_singer_id_3f20c279_fk_music_singer_id`(`singer_id`) USING BTREE,
  INDEX `music_album_user_id_5762717f_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `music_album_singer_id_3f20c279_fk_music_singer_id` FOREIGN KEY (`singer_id`) REFERENCES `music_singer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `music_album_user_id_5762717f_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of music_album
-- ----------------------------
INSERT INTO `music_album` VALUES (1, '童话镇', '童话镇', 'album\\cover\\2018\\08\\IMG_3520.JPG', 'singer\\background\\2018\\08\\20.jpg', '2018-08-11', '陈一发儿', '2018-08-11 16:50:46.158610', '2018-08-11 16:50:46.217487', 0, 1, 1);
INSERT INTO `music_album` VALUES (2, '阿婆说', '阿婆说', 'album\\cover\\2018\\08\\IMG_3527.JPG', 'singer\\background\\2018\\08\\01.jpg', '2018-08-11', '陈一发儿', '2018-08-11 16:51:36.554119', '2018-08-11 16:51:36.608942', 0, 1, 1);

-- ----------------------------
-- Table structure for music_albumdetail
-- ----------------------------
DROP TABLE IF EXISTS `music_albumdetail`;
CREATE TABLE `music_albumdetail`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `album_id` int(11) NOT NULL,
  `song_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `music_albumdetail_album_id_song_id_6ea7428d_uniq`(`album_id`, `song_id`) USING BTREE,
  INDEX `music_albumdetail_song_id_e0e78baa_fk_music_song_id`(`song_id`) USING BTREE,
  INDEX `music_albumdetail_user_id_2a51321a_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `music_albumdetail_album_id_9d946951_fk_music_album_id` FOREIGN KEY (`album_id`) REFERENCES `music_album` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `music_albumdetail_song_id_e0e78baa_fk_music_song_id` FOREIGN KEY (`song_id`) REFERENCES `music_song` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `music_albumdetail_user_id_2a51321a_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for music_audio
-- ----------------------------
DROP TABLE IF EXISTS `music_audio`;
CREATE TABLE `music_audio`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `singer_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `music_audio_singer_id_ea25b71d_fk_music_singer_id`(`singer_id`) USING BTREE,
  INDEX `music_audio_user_id_bc56bdeb_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `music_audio_singer_id_ea25b71d_fk_music_singer_id` FOREIGN KEY (`singer_id`) REFERENCES `music_singer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `music_audio_user_id_bc56bdeb_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for music_audiodetail
-- ----------------------------
DROP TABLE IF EXISTS `music_audiodetail`;
CREATE TABLE `music_audiodetail`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `audio_id` int(11) NOT NULL,
  `song_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `music_audiodetail_audio_id_song_id_6f2a36e4_uniq`(`audio_id`, `song_id`) USING BTREE,
  INDEX `music_audiodetail_song_id_8100da92_fk_music_song_id`(`song_id`) USING BTREE,
  INDEX `music_audiodetail_user_id_685cb8fe_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `music_audiodetail_audio_id_18f9efec_fk_music_audio_id` FOREIGN KEY (`audio_id`) REFERENCES `music_audio` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `music_audiodetail_song_id_8100da92_fk_music_song_id` FOREIGN KEY (`song_id`) REFERENCES `music_song` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `music_audiodetail_user_id_685cb8fe_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for music_singer
-- ----------------------------
DROP TABLE IF EXISTS `music_singer`;
CREATE TABLE `music_singer`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `avatar` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `background_img` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `birthday` date NULL DEFAULT NULL,
  `gender` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of music_singer
-- ----------------------------
INSERT INTO `music_singer` VALUES (1, '陈一发儿', '陈一发儿', 'singer\\avatar\\2018\\08\\IMG_3520.JPG', 'singer\\background\\2018\\08\\03.jpg', '2018-08-11', 'female', '重庆市', '2018-08-11 16:49:40.762355', '2018-08-11 20:58:14.048941', 0);

-- ----------------------------
-- Table structure for music_song
-- ----------------------------
DROP TABLE IF EXISTS `music_song`;
CREATE TABLE `music_song`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `duration` decimal(6, 3) NOT NULL,
  `hits` int(11) NOT NULL,
  `file` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `singer_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `music_song_singer_id_d091b2db_fk_music_singer_id`(`singer_id`) USING BTREE,
  INDEX `music_song_user_id_36fad657_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `music_song_singer_id_d091b2db_fk_music_singer_id` FOREIGN KEY (`singer_id`) REFERENCES `music_singer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `music_song_user_id_36fad657_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for news_article
-- ----------------------------
DROP TABLE IF EXISTS `news_article`;
CREATE TABLE `news_article`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `date` date NOT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `hits` int(11) NOT NULL,
  `is_top` int(11) NOT NULL,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE,
  INDEX `news_article_user_id_f2dc4c3b_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `news_article_user_id_f2dc4c3b_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for photos_gallery
-- ----------------------------
DROP TABLE IF EXISTS `photos_gallery`;
CREATE TABLE `photos_gallery`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `date` date NOT NULL,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `photos_gallery_user_id_5fadc1e3_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `photos_gallery_user_id_5fadc1e3_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of photos_gallery
-- ----------------------------
INSERT INTO `photos_gallery` VALUES (1, '相册1', '相册1', '2018-08-10', '2018-08-11 16:16:46.760881', '2018-08-11 16:16:46.760881', 0, 1);
INSERT INTO `photos_gallery` VALUES (2, '相册2', '相册2', '2018-08-11', '2018-08-11 16:16:59.794371', '2018-08-11 16:16:59.794371', 0, 1);
INSERT INTO `photos_gallery` VALUES (3, '相册3', '相册3', '2018-08-11', '2018-08-11 16:22:53.950874', '2018-08-11 16:22:53.985788', 0, 2);

-- ----------------------------
-- Table structure for photos_gallerydetail
-- ----------------------------
DROP TABLE IF EXISTS `photos_gallerydetail`;
CREATE TABLE `photos_gallerydetail`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `gallery_id` int(11) NOT NULL,
  `photo_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `photos_gallerydetail_gallery_id_photo_id_b03e02fd_uniq`(`gallery_id`, `photo_id`) USING BTREE,
  INDEX `photos_gallerydetail_photo_id_01e680d0_fk_photos_photo_id`(`photo_id`) USING BTREE,
  INDEX `photos_gallerydetail_user_id_b537b8a6_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `photos_gallerydetail_gallery_id_94509aae_fk_photos_gallery_id` FOREIGN KEY (`gallery_id`) REFERENCES `photos_gallery` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `photos_gallerydetail_photo_id_01e680d0_fk_photos_photo_id` FOREIGN KEY (`photo_id`) REFERENCES `photos_photo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `photos_gallerydetail_user_id_b537b8a6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for photos_photo
-- ----------------------------
DROP TABLE IF EXISTS `photos_photo`;
CREATE TABLE `photos_photo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `file` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `date` date NOT NULL,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `photos_photo_user_id_2c88c04a_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `photos_photo_user_id_2c88c04a_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for users_user
-- ----------------------------
DROP TABLE IF EXISTS `users_user`;
CREATE TABLE `users_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NULL,
  `nickname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `birthday` date NULL DEFAULT NULL,
  `gender` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `mobile` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `avatar` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `update_time` datetime(6) NULL,
  `is_valid` int(11) NOT NULL,
  `is_del` int(11) NOT NULL,
  `is_mp_user` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users_user
-- ----------------------------
INSERT INTO `users_user` VALUES (1, 'pbkdf2_sha256$36000$sz3bEgSxrM4h$B2lo4tOocG/BI5GLGoXIDeEpzBWVVrDUr0BdpPeX6Qo=', '2018-09-06 15:32:33.603952', 1, 'admin', '', '', 'admin@admin.com', 1, 1, '2018-08-08 17:17:00.000000', 'admin', NULL, NULL, 'male', '北京', NULL, 'avatar\\2018\\08\\IMG_4442.JPG', '2018-08-08 17:17:00.000000', 1, 0, 0);
INSERT INTO `users_user` VALUES (2, 'pbkdf2_sha256$36000$vw5JKDvY2AHW$buuq9d4Rx5XJbxyS2gKufxu2CGiQ/itpMRjMvqXEl1o=', '2018-08-11 16:25:00.000000', 0, 'test', '', '', 'test@test.com', 1, 1, '2018-08-09 11:33:00.000000', '测试', NULL, NULL, 'female', 'beijing', NULL, 'avatar\\2018\\08\\gifIMG_2492.GIF', '2018-08-09 11:33:00.000000', 1, 0, 0);

-- ----------------------------
-- Table structure for users_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `users_user_groups`;
CREATE TABLE `users_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `users_user_groups_user_id_group_id_b88eab82_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `users_user_groups_group_id_9afc8d0e_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for users_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `users_user_user_permissions`;
CREATE TABLE `users_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `users_user_user_permissions_user_id_permission_id_43338c45_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `users_user_user_perm_permission_id_0b93982e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users_user_user_permissions
-- ----------------------------
INSERT INTO `users_user_user_permissions` VALUES (2, 2, 41);
INSERT INTO `users_user_user_permissions` VALUES (3, 2, 42);
INSERT INTO `users_user_user_permissions` VALUES (8, 2, 43);
INSERT INTO `users_user_user_permissions` VALUES (4, 2, 53);
INSERT INTO `users_user_user_permissions` VALUES (7, 2, 90);
INSERT INTO `users_user_user_permissions` VALUES (6, 2, 91);
INSERT INTO `users_user_user_permissions` VALUES (9, 2, 92);
INSERT INTO `users_user_user_permissions` VALUES (5, 2, 96);

-- ----------------------------
-- Table structure for videos_video
-- ----------------------------
DROP TABLE IF EXISTS `videos_video`;
CREATE TABLE `videos_video`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `file` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `date` date NOT NULL,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `videos_video_user_id_5a0149a4_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `videos_video_user_id_5a0149a4_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for videos_videocollection
-- ----------------------------
DROP TABLE IF EXISTS `videos_videocollection`;
CREATE TABLE `videos_videocollection`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `date` date NOT NULL,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `videos_videocollection_user_id_caffa172_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `videos_videocollection_user_id_caffa172_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of videos_videocollection
-- ----------------------------
INSERT INTO `videos_videocollection` VALUES (4, '专辑MV', '专辑MV', '2018-08-11', '2018-08-11 13:08:54.782934', '2018-08-11 13:08:54.782934', 0, 1);
INSERT INTO `videos_videocollection` VALUES (5, '直播那些事', '直播那些事', '2018-08-11', '2018-08-11 13:57:53.627324', '2018-08-11 13:57:53.627324', 0, 1);
INSERT INTO `videos_videocollection` VALUES (6, '直播集锦', '直播集锦', '2018-08-11', '2018-08-11 14:19:45.416508', '2018-08-11 15:39:23.174734', 0, 2);
INSERT INTO `videos_videocollection` VALUES (7, '直播集锦2', '直播集锦2', '2018-08-11', '2018-08-11 15:40:16.137281', '2018-08-11 15:40:16.157239', 0, 2);

-- ----------------------------
-- Table structure for videos_videocollectiondetail
-- ----------------------------
DROP TABLE IF EXISTS `videos_videocollectiondetail`;
CREATE TABLE `videos_videocollectiondetail`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_del` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `video_id` int(11) NOT NULL,
  `video_collection_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `videos_videocollectionde_video_collection_id_vide_0c071ea1_uniq`(`video_collection_id`, `video_id`) USING BTREE,
  INDEX `videos_videocollectiondetail_user_id_71bf9d8c_fk_users_user_id`(`user_id`) USING BTREE,
  INDEX `videos_videocollecti_video_id_c13d4a44_fk_videos_vi`(`video_id`) USING BTREE,
  CONSTRAINT `videos_videocollecti_video_collection_id_7b59c7dc_fk_videos_vi` FOREIGN KEY (`video_collection_id`) REFERENCES `videos_videocollection` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `videos_videocollecti_video_id_c13d4a44_fk_videos_vi` FOREIGN KEY (`video_id`) REFERENCES `videos_video` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `videos_videocollectiondetail_user_id_71bf9d8c_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for xadmin_bookmark
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_bookmark`;
CREATE TABLE `xadmin_bookmark`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `url_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `query` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `xadmin_bookmark_content_type_id_60941679_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `xadmin_bookmark_user_id_42d307fc_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `xadmin_bookmark_content_type_id_60941679_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for xadmin_log
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_log`;
CREATE TABLE `xadmin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NULL,
  `ip_addr` char(39) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id`(`content_type_id`) USING BTREE,
  INDEX `xadmin_log_user_id_bb16a176_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 67 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of xadmin_log
-- ----------------------------
INSERT INTO `xadmin_log` VALUES (1, '2018-08-08 18:34:27.954098', '127.0.0.1', '1', 'admin', 'change', '修改 last_login，nickname，gender，address 和 avatar', 10, 1);
INSERT INTO `xadmin_log` VALUES (2, '2018-08-08 18:56:33.274965', '127.0.0.1', '1', 'admin', 'change', '修改 last_login', 10, 1);
INSERT INTO `xadmin_log` VALUES (3, '2018-08-08 21:05:12.913457', '127.0.0.1', '1', 'admin', 'change', '修改 last_login', 10, 1);
INSERT INTO `xadmin_log` VALUES (4, '2018-08-08 22:14:16.754138', '127.0.0.1', '1', '陈一发儿', 'create', '已添加。', 12, 1);
INSERT INTO `xadmin_log` VALUES (5, '2018-08-08 22:17:25.622376', '127.0.0.1', '1', '陈一发儿', 'create', '已添加。', 11, 1);
INSERT INTO `xadmin_log` VALUES (6, '2018-08-08 22:17:39.012787', '127.0.0.1', '2', '陈一发儿', 'create', '已添加。', 11, 1);
INSERT INTO `xadmin_log` VALUES (7, '2018-08-08 22:17:51.158932', '127.0.0.1', '3', '陈一发儿', 'create', '已添加。', 11, 1);
INSERT INTO `xadmin_log` VALUES (8, '2018-08-08 22:20:50.944148', '127.0.0.1', '1', '生日', 'create', '已添加。', 13, 1);
INSERT INTO `xadmin_log` VALUES (9, '2018-08-08 22:21:24.843967', '127.0.0.1', '2', '住址', 'create', '已添加。', 13, 1);
INSERT INTO `xadmin_log` VALUES (10, '2018-08-08 22:21:50.553356', '127.0.0.1', '3', '职业', 'create', '已添加。', 13, 1);
INSERT INTO `xadmin_log` VALUES (11, '2018-08-08 22:22:22.227105', '127.0.0.1', '4', '房间', 'create', '已添加。', 13, 1);
INSERT INTO `xadmin_log` VALUES (12, '2018-08-08 22:22:46.523290', '127.0.0.1', '5', '微博', 'create', '已添加。', 13, 1);
INSERT INTO `xadmin_log` VALUES (13, '2018-08-08 22:23:08.598649', '127.0.0.1', '6', '邮件', 'create', '已添加。', 13, 1);
INSERT INTO `xadmin_log` VALUES (14, '2018-08-08 22:23:34.890317', '127.0.0.1', '7', '淘宝', 'create', '已添加。', 13, 1);
INSERT INTO `xadmin_log` VALUES (15, '2018-08-08 22:24:01.479817', '127.0.0.1', '8', '个人主页', 'create', '已添加。', 13, 1);
INSERT INTO `xadmin_log` VALUES (16, '2018-08-08 22:24:22.398547', '127.0.0.1', '9', '公众号', 'create', '已添加。', 13, 1);
INSERT INTO `xadmin_log` VALUES (17, '2018-08-09 10:50:06.316922', '127.0.0.1', '4', 'test', 'create', '已添加。', 11, 1);
INSERT INTO `xadmin_log` VALUES (18, '2018-08-09 10:52:17.046619', '127.0.0.1', '4', 'test', 'change', '修改 is_del', 11, 1);
INSERT INTO `xadmin_log` VALUES (19, '2018-08-09 10:52:22.851033', '127.0.0.1', '4', 'test', 'delete', '', 11, 1);
INSERT INTO `xadmin_log` VALUES (20, '2018-08-09 10:53:41.442880', '127.0.0.1', '5', 'test', 'create', '已添加。', 11, 1);
INSERT INTO `xadmin_log` VALUES (21, '2018-08-09 11:33:35.846850', '127.0.0.1', '2', 'test', 'create', '已添加。', 10, 1);
INSERT INTO `xadmin_log` VALUES (22, '2018-08-09 11:34:13.896780', '127.0.0.1', '57', 'mp | 轮播图 | test', 'create', '已添加。', 2, 1);
INSERT INTO `xadmin_log` VALUES (23, '2018-08-09 11:34:36.769575', '127.0.0.1', '2', 'test', 'change', '修改 user_permissions，is_staff，nickname 和 address', 10, 1);
INSERT INTO `xadmin_log` VALUES (24, '2018-08-09 11:35:59.438406', '127.0.0.1', '2', 'test', 'change', '修改 last_login 和 user_permissions', 10, 1);
INSERT INTO `xadmin_log` VALUES (25, '2018-08-09 12:04:02.519009', '127.0.0.1', NULL, '', 'delete', '批量删除 1 个 权限', NULL, 1);
INSERT INTO `xadmin_log` VALUES (26, '2018-08-09 12:08:46.237590', '127.0.0.1', '5', 'test', 'delete', '', 11, 1);
INSERT INTO `xadmin_log` VALUES (28, '2018-08-09 12:28:41.639615', '127.0.0.1', '5', 'test', 'delete', '', 11, 1);
INSERT INTO `xadmin_log` VALUES (29, '2018-08-09 16:27:19.618039', '127.0.0.1', '1', '英', 'create', '已添加。', 15, 1);
INSERT INTO `xadmin_log` VALUES (30, '2018-08-09 16:29:02.899825', '127.0.0.1', '1', '我的青春我做主', 'create', '已添加。', 17, 1);
INSERT INTO `xadmin_log` VALUES (31, '2018-08-09 16:31:47.689207', '127.0.0.1', '2', 'Bad Blood', 'create', '已添加。', 17, 1);
INSERT INTO `xadmin_log` VALUES (32, '2018-08-09 16:35:57.416326', '127.0.0.1', '3', 'Style', 'create', '已添加。', 17, 1);
INSERT INTO `xadmin_log` VALUES (33, '2018-08-09 16:54:22.187388', '127.0.0.1', '4', '123', 'create', '已添加。', 17, 1);
INSERT INTO `xadmin_log` VALUES (34, '2018-08-09 16:54:29.322310', '127.0.0.1', NULL, '', 'delete', '批量删除 1 个 歌曲', NULL, 1);
INSERT INTO `xadmin_log` VALUES (35, '2018-08-09 17:31:54.672849', '127.0.0.1', '1', '电台1', 'create', '已添加。', 18, 1);
INSERT INTO `xadmin_log` VALUES (36, '2018-08-09 17:32:01.842674', '127.0.0.1', '2', '电台2', 'create', '已添加。', 18, 1);
INSERT INTO `xadmin_log` VALUES (37, '2018-08-09 18:00:50.435430', '127.0.0.1', '1', '童话镇', 'create', '已添加。', 16, 1);
INSERT INTO `xadmin_log` VALUES (38, '2018-08-09 21:33:43.954223', '127.0.0.1', '1', '电台1', 'create', '已添加。', 21, 1);
INSERT INTO `xadmin_log` VALUES (39, '2018-08-09 21:33:48.841244', '127.0.0.1', '2', '电台2', 'create', '已添加。', 21, 1);
INSERT INTO `xadmin_log` VALUES (40, '2018-08-10 13:07:05.950231', '127.0.0.1', '1', 'test', 'create', '已添加。', 22, 1);
INSERT INTO `xadmin_log` VALUES (41, '2018-08-10 13:10:04.964436', '127.0.0.1', '1', '照片1', 'create', '已添加。', 23, 1);
INSERT INTO `xadmin_log` VALUES (42, '2018-08-10 13:10:17.757372', '127.0.0.1', '2', '照片2', 'create', '已添加。', 23, 1);
INSERT INTO `xadmin_log` VALUES (43, '2018-08-10 13:10:29.251605', '127.0.0.1', '1', 'test', 'create', '已添加。', 24, 1);
INSERT INTO `xadmin_log` VALUES (44, '2018-08-10 13:41:27.121223', '127.0.0.1', '2', 'test', 'create', '已添加。', 24, 1);
INSERT INTO `xadmin_log` VALUES (45, '2018-08-10 14:49:30.644500', '127.0.0.1', '2', 'test1', 'create', '已添加。', 22, 1);
INSERT INTO `xadmin_log` VALUES (46, '2018-08-10 14:49:49.808038', '127.0.0.1', '3', '照片3', 'create', '已添加。', 23, 1);
INSERT INTO `xadmin_log` VALUES (47, '2018-08-10 14:49:58.791578', '127.0.0.1', '3', 'test1', 'create', '已添加。', 24, 1);
INSERT INTO `xadmin_log` VALUES (48, '2018-08-10 19:44:39.561625', '127.0.0.1', '1', '直播那些事', 'create', '已添加。', 26, 1);
INSERT INTO `xadmin_log` VALUES (49, '2018-08-10 19:45:03.716002', '127.0.0.1', '2', '直播的乐趣', 'create', '已添加。', 26, 1);
INSERT INTO `xadmin_log` VALUES (50, '2018-08-10 19:52:33.949431', '127.0.0.1', '1', '斗鱼直播节-陈一发儿专访', 'create', '已添加。', 27, 1);
INSERT INTO `xadmin_log` VALUES (51, '2018-08-10 19:52:59.226387', '127.0.0.1', '2', '阿婆说', 'create', '已添加。', 27, 1);
INSERT INTO `xadmin_log` VALUES (52, '2018-08-10 19:53:37.365886', '127.0.0.1', '3', '弦上有春秋', 'create', '已添加。', 27, 1);
INSERT INTO `xadmin_log` VALUES (53, '2018-08-10 19:53:54.106631', '127.0.0.1', '2', '专辑MV', 'change', '修改 name 和 desc', 26, 1);
INSERT INTO `xadmin_log` VALUES (54, '2018-08-10 19:54:04.626270', '127.0.0.1', '1', '直播那些事', 'create', '已添加。', 25, 1);
INSERT INTO `xadmin_log` VALUES (55, '2018-08-10 19:54:12.907814', '127.0.0.1', '2', '专辑MV', 'create', '已添加。', 25, 1);
INSERT INTO `xadmin_log` VALUES (56, '2018-08-10 19:54:28.656024', '127.0.0.1', '3', '直播那些事', 'create', '已添加。', 25, 1);
INSERT INTO `xadmin_log` VALUES (57, '2018-08-10 23:48:29.347382', '127.0.0.1', '4', '照片4', 'create', '已添加。', 23, 1);
INSERT INTO `xadmin_log` VALUES (58, '2018-08-11 13:08:54.802852', '127.0.0.1', '4', '专辑MV', 'create', '已添加。', 26, 1);
INSERT INTO `xadmin_log` VALUES (59, '2018-08-11 14:19:45.456393', '127.0.0.1', '6', '直播集锦', 'create', '已添加。', 26, 1);
INSERT INTO `xadmin_log` VALUES (60, '2018-08-11 14:33:23.911775', '127.0.0.1', '6', '直播集锦', 'change', '修改 user', 26, 1);
INSERT INTO `xadmin_log` VALUES (61, '2018-08-11 15:25:47.117725', '127.0.0.1', '6', '直播集锦', 'change', '修改 desc', 26, 1);
INSERT INTO `xadmin_log` VALUES (62, '2018-08-11 15:27:16.385408', '127.0.0.1', '6', '直播集锦', 'change', '修改 desc', 26, 1);
INSERT INTO `xadmin_log` VALUES (63, '2018-08-11 16:25:23.946452', '127.0.0.1', '2', 'test', 'change', '修改 last_login 和 user_permissions', 10, 1);
INSERT INTO `xadmin_log` VALUES (64, '2018-08-11 20:47:46.362049', '127.0.0.1', '2', 'test', 'change', '修改 last_login 和 avatar', 10, 1);
INSERT INTO `xadmin_log` VALUES (65, '2018-08-11 20:48:34.163427', '127.0.0.1', '2', 'test', 'change', '修改 avatar', 10, 1);
INSERT INTO `xadmin_log` VALUES (66, '2018-08-12 14:52:53.819564', '127.0.0.1', '2', 'test', 'change', '修改 email', 10, 1);

-- ----------------------------
-- Table structure for xadmin_usersettings
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_usersettings`;
CREATE TABLE `xadmin_usersettings`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `value` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `xadmin_usersettings_user_id_edeabe4a_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of xadmin_usersettings
-- ----------------------------
INSERT INTO `xadmin_usersettings` VALUES (1, 'dashboard:home:pos', '', 1);
INSERT INTO `xadmin_usersettings` VALUES (2, 'dashboard:home:pos', '', 2);

-- ----------------------------
-- Table structure for xadmin_userwidget
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_userwidget`;
CREATE TABLE `xadmin_userwidget`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `widget_type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `value` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `xadmin_userwidget_user_id_c159233a_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
