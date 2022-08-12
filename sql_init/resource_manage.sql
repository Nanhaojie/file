/*
 Navicat Premium Data Transfer

 Source Server         : 172.16.1.10
 Source Server Type    : MySQL
 Source Server Version : 50732
 Source Host           : 172.16.1.10:3306
 Source Schema         : resource_manage

 Target Server Type    : MySQL
 Target Server Version : 50732
 File Encoding         : 65001

 Date: 11/08/2022 16:05:36
*/
create database if not exists resource_manage default character set UTF8mb4 collate utf8mb4_unicode_ci;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

use resource_manage;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
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
) ENGINE = InnoDB AUTO_INCREMENT = 41 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

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
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add 用户操作日志', 6, 'add_useroperatelog');
INSERT INTO `auth_permission` VALUES (22, 'Can change 用户操作日志', 6, 'change_useroperatelog');
INSERT INTO `auth_permission` VALUES (23, 'Can delete 用户操作日志', 6, 'delete_useroperatelog');
INSERT INTO `auth_permission` VALUES (24, 'Can view 用户操作日志', 6, 'view_useroperatelog');
INSERT INTO `auth_permission` VALUES (25, 'Can add 用户信息', 7, 'add_userprofile');
INSERT INTO `auth_permission` VALUES (26, 'Can change 用户信息', 7, 'change_userprofile');
INSERT INTO `auth_permission` VALUES (27, 'Can delete 用户信息', 7, 'delete_userprofile');
INSERT INTO `auth_permission` VALUES (28, 'Can view 用户信息', 7, 'view_userprofile');
INSERT INTO `auth_permission` VALUES (29, 'Can add 公用电脑ip地址', 8, 'add_publicip');
INSERT INTO `auth_permission` VALUES (30, 'Can change 公用电脑ip地址', 8, 'change_publicip');
INSERT INTO `auth_permission` VALUES (31, 'Can delete 公用电脑ip地址', 8, 'delete_publicip');
INSERT INTO `auth_permission` VALUES (32, 'Can view 公用电脑ip地址', 8, 'view_publicip');
INSERT INTO `auth_permission` VALUES (33, 'Can add 文件审批日志', 9, 'add_approvelog');
INSERT INTO `auth_permission` VALUES (34, 'Can change 文件审批日志', 9, 'change_approvelog');
INSERT INTO `auth_permission` VALUES (35, 'Can delete 文件审批日志', 9, 'delete_approvelog');
INSERT INTO `auth_permission` VALUES (36, 'Can view 文件审批日志', 9, 'view_approvelog');
INSERT INTO `auth_permission` VALUES (37, 'Can add 文件', 10, 'add_file');
INSERT INTO `auth_permission` VALUES (38, 'Can change 文件', 10, 'change_file');
INSERT INTO `auth_permission` VALUES (39, 'Can delete 文件', 10, 'delete_file');
INSERT INTO `auth_permission` VALUES (40, 'Can view 文件', 10, 'view_file');

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
  INDEX `django_admin_log_user_id_c564eba6_fk_users_userprofile_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (9, 'files', 'approvelog');
INSERT INTO `django_content_type` VALUES (10, 'files', 'file');
INSERT INTO `django_content_type` VALUES (8, 'files', 'publicip');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (6, 'users', 'useroperatelog');
INSERT INTO `django_content_type` VALUES (7, 'users', 'userprofile');

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
) ENGINE = InnoDB AUTO_INCREMENT = 41 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2022-08-09 17:58:08.449671');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2022-08-09 17:58:08.539833');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2022-08-09 17:58:08.679840');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2022-08-09 17:58:08.929686');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2022-08-09 17:58:08.939814');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2022-08-09 17:58:08.958419');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2022-08-09 17:58:08.961699');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2022-08-09 17:58:08.971730');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2022-08-09 17:58:08.991844');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2022-08-09 17:58:09.011727');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2022-08-09 17:58:09.031705');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0010_alter_group_name_max_length', '2022-08-09 17:58:09.051703');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0011_update_proxy_permissions', '2022-08-09 17:58:09.081703');
INSERT INTO `django_migrations` VALUES (14, 'users', '0001_initial', '2022-08-09 17:58:09.301712');
INSERT INTO `django_migrations` VALUES (15, 'admin', '0001_initial', '2022-08-09 17:58:09.615488');
INSERT INTO `django_migrations` VALUES (16, 'admin', '0002_logentry_remove_auto_add', '2022-08-09 17:58:09.885410');
INSERT INTO `django_migrations` VALUES (17, 'admin', '0003_logentry_add_action_flag_choices', '2022-08-09 17:58:09.895361');
INSERT INTO `django_migrations` VALUES (18, 'files', '0001_initial', '2022-08-09 17:58:09.955499');
INSERT INTO `django_migrations` VALUES (19, 'files', '0002_uploadhost', '2022-08-09 17:58:09.985372');
INSERT INTO `django_migrations` VALUES (20, 'files', '0003_auto_20191025_1533', '2022-08-09 17:58:10.051810');
INSERT INTO `django_migrations` VALUES (21, 'files', '0004_auto_20191025_1548', '2022-08-09 17:58:10.101842');
INSERT INTO `django_migrations` VALUES (22, 'files', '0005_auto_20191028_1001', '2022-08-09 17:58:10.151814');
INSERT INTO `django_migrations` VALUES (23, 'files', '0006_auto_20191104_1702', '2022-08-09 17:58:10.201848');
INSERT INTO `django_migrations` VALUES (24, 'files', '0007_auto_20191104_1711', '2022-08-09 17:58:10.331958');
INSERT INTO `django_migrations` VALUES (25, 'files', '0008_auto_20191105_1537', '2022-08-09 17:58:10.401988');
INSERT INTO `django_migrations` VALUES (26, 'files', '0009_auto_20191105_1723', '2022-08-09 17:58:10.681831');
INSERT INTO `django_migrations` VALUES (27, 'files', '0010_auto_20191106_0908', '2022-08-09 17:58:10.711996');
INSERT INTO `django_migrations` VALUES (28, 'files', '0011_auto_20191106_1649', '2022-08-09 17:58:10.761834');
INSERT INTO `django_migrations` VALUES (29, 'sessions', '0001_initial', '2022-08-09 17:58:10.801997');
INSERT INTO `django_migrations` VALUES (30, 'users', '0002_auto_20190820_0952', '2022-08-09 17:58:10.902005');
INSERT INTO `django_migrations` VALUES (31, 'users', '0003_auto_20190820_1014', '2022-08-09 17:58:10.942005');
INSERT INTO `django_migrations` VALUES (32, 'users', '0004_auto_20190829_1134', '2022-08-09 17:58:11.065234');
INSERT INTO `django_migrations` VALUES (33, 'users', '0005_auto_20190829_1450', '2022-08-09 17:58:11.115236');
INSERT INTO `django_migrations` VALUES (34, 'users', '0006_auto_20191025_1128', '2022-08-09 17:58:11.275249');
INSERT INTO `django_migrations` VALUES (35, 'users', '0007_auto_20191025_1533', '2022-08-09 17:58:11.295157');
INSERT INTO `django_migrations` VALUES (36, 'users', '0008_userprofile_sub_role', '2022-08-09 17:58:11.375232');
INSERT INTO `django_migrations` VALUES (37, 'users', '0009_auto_20191105_1537', '2022-08-09 17:58:11.395117');
INSERT INTO `django_migrations` VALUES (38, 'users', '0010_auto_20191106_0923', '2022-08-09 17:58:11.415232');
INSERT INTO `django_migrations` VALUES (39, 'users', '0011_auto_20191106_1118', '2022-08-09 17:58:11.545119');
INSERT INTO `django_migrations` VALUES (40, 'users', '0012_auto_20191106_1649', '2022-08-09 17:58:11.645255');

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
INSERT INTO `django_session` VALUES ('dnt0etfb0zpgjyvc3idlqigmvgav97hv', 'ZTE5ODljMDQ1NTVmYjE4MzMyZjJlZGUyNzJhY2RmMGUyNDI5OTE2Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tZUJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NThkOWM5YmEyNmQ3YjgyYmFjN2ViOTQwZjlhOTY0MTcyNjY5M2U5In0=', '2022-08-25 10:00:58.602677');
INSERT INTO `django_session` VALUES ('r2b75gqk5sbqik2o4s650v59qwmhi6ox', 'ZTE5ODljMDQ1NTVmYjE4MzMyZjJlZGUyNzJhY2RmMGUyNDI5OTE2Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tZUJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NThkOWM5YmEyNmQ3YjgyYmFjN2ViOTQwZjlhOTY0MTcyNjY5M2U5In0=', '2022-08-24 14:30:42.936809');
INSERT INTO `django_session` VALUES ('tjhyicifff6g3s02rhn9x1namxmtcipp', 'ZTE5ODljMDQ1NTVmYjE4MzMyZjJlZGUyNzJhY2RmMGUyNDI5OTE2Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tZUJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NThkOWM5YmEyNmQ3YjgyYmFjN2ViOTQwZjlhOTY0MTcyNjY5M2U5In0=', '2022-08-24 18:09:09.217701');

-- ----------------------------
-- Table structure for files_approvelog
-- ----------------------------
DROP TABLE IF EXISTS `files_approvelog`;
CREATE TABLE `files_approvelog`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fileno` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `filename` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `owner` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `add_time` datetime(6) NULL,
  `approve_time` datetime(6) NULL,
  `isapprove` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for files_file
-- ----------------------------
DROP TABLE IF EXISTS `files_file`;
CREATE TABLE `files_file`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fileno` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `filename` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `filepath` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `owner` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `add_time` datetime(6) NULL,
  `first_check` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `second_check` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `isapprove` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for files_publicip
-- ----------------------------
DROP TABLE IF EXISTS `files_publicip`;
CREATE TABLE `files_publicip`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host_ip` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for users_useroperatelog
-- ----------------------------
DROP TABLE IF EXISTS `users_useroperatelog`;
CREATE TABLE `users_useroperatelog`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `modify_time` datetime(6) NULL,
  `userno` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `comment` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `filename` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fileno` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for users_userprofile
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile`;
CREATE TABLE `users_userprofile`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NULL,
  `department` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_superuser` int(11) NOT NULL,
  `role` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `userno` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `sub_role` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `add_time` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users_userprofile
-- ----------------------------
INSERT INTO `users_userprofile` VALUES (1, 'pbkdf2_sha256$150000$MDw6GUXMo5EY$m/UojDG5VHmUC9hOQzNKheIJ+A9IxEjBoVJP3s1QZto=', '2022-08-11 10:00:58.572745', 'admin', '', '', '', 0, 1, '2022-08-10 14:16:34.137289', '研发部', 0, '2', '123', '0', '2022-08-10 14:16:34.137334');

-- ----------------------------
-- Table structure for users_userprofile_groups
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile_groups`;
CREATE TABLE `users_userprofile_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `users_userprofile_groups_userprofile_id_group_id_823cf2fc_uniq`(`userprofile_id`, `group_id`) USING BTREE,
  INDEX `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `users_userprofile_gr_userprofile_id_a4496a80_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for users_userprofile_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile_user_permissions`;
CREATE TABLE `users_userprofile_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `users_userprofile_user_p_userprofile_id_permissio_d0215190_uniq`(`userprofile_id`, `permission_id`) USING BTREE,
  INDEX `users_userprofile_us_permission_id_393136b6_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `users_userprofile_us_permission_id_393136b6_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `users_userprofile_us_userprofile_id_34544737_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
