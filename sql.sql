/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 8.0.27 : Database - mm_hospital
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`mm_hospital` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `mm_hospital`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add login',7,'add_login'),(26,'Can change login',7,'change_login'),(27,'Can delete login',7,'delete_login'),(28,'Can view login',7,'view_login'),(29,'Can add patient',8,'add_patient'),(30,'Can change patient',8,'change_patient'),(31,'Can delete patient',8,'delete_patient'),(32,'Can view patient',8,'view_patient'),(33,'Can add schedule',9,'add_schedule'),(34,'Can change schedule',9,'change_schedule'),(35,'Can delete schedule',9,'delete_schedule'),(36,'Can view schedule',9,'view_schedule'),(37,'Can add doctor_rating',10,'add_doctor_rating'),(38,'Can change doctor_rating',10,'change_doctor_rating'),(39,'Can delete doctor_rating',10,'delete_doctor_rating'),(40,'Can view doctor_rating',10,'view_doctor_rating'),(41,'Can add doctor',11,'add_doctor'),(42,'Can change doctor',11,'change_doctor'),(43,'Can delete doctor',11,'delete_doctor'),(44,'Can view doctor',11,'view_doctor'),(45,'Can add appointment',12,'add_appointment'),(46,'Can change appointment',12,'change_appointment'),(47,'Can delete appointment',12,'delete_appointment'),(48,'Can view appointment',12,'view_appointment'),(49,'Can add prescription',13,'add_prescription'),(50,'Can change prescription',13,'change_prescription'),(51,'Can delete prescription',13,'delete_prescription'),(52,'Can view prescription',13,'view_prescription'),(53,'Can add booking',14,'add_booking'),(54,'Can change booking',14,'change_booking'),(55,'Can delete booking',14,'delete_booking'),(56,'Can view booking',14,'view_booking');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'hospital_modules','login'),(8,'hospital_modules','patient'),(9,'hospital_modules','schedule'),(10,'hospital_modules','doctor_rating'),(11,'hospital_modules','doctor'),(12,'hospital_modules','appointment'),(13,'hospital_modules','prescription'),(14,'hospital_modules','booking');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2023-06-06 05:17:06.713195'),(2,'auth','0001_initial','2023-06-06 05:17:07.063299'),(3,'admin','0001_initial','2023-06-06 05:17:07.181120'),(4,'admin','0002_logentry_remove_auto_add','2023-06-06 05:17:07.187601'),(5,'admin','0003_logentry_add_action_flag_choices','2023-06-06 05:17:07.193801'),(6,'contenttypes','0002_remove_content_type_name','2023-06-06 05:17:07.245336'),(7,'auth','0002_alter_permission_name_max_length','2023-06-06 05:17:07.271957'),(8,'auth','0003_alter_user_email_max_length','2023-06-06 05:17:07.306450'),(9,'auth','0004_alter_user_username_opts','2023-06-06 05:17:07.313463'),(10,'auth','0005_alter_user_last_login_null','2023-06-06 05:17:07.344867'),(11,'auth','0006_require_contenttypes_0002','2023-06-06 05:17:07.346879'),(12,'auth','0007_alter_validators_add_error_messages','2023-06-06 05:17:07.353853'),(13,'auth','0008_alter_user_username_max_length','2023-06-06 05:17:07.386669'),(14,'auth','0009_alter_user_last_name_max_length','2023-06-06 05:17:07.414594'),(15,'auth','0010_alter_group_name_max_length','2023-06-06 05:17:07.444515'),(16,'auth','0011_update_proxy_permissions','2023-06-06 05:17:07.450498'),(17,'auth','0012_alter_user_first_name_max_length','2023-06-06 05:17:07.482417'),(18,'hospital_modules','0001_initial','2023-06-06 05:17:07.491388'),(19,'sessions','0001_initial','2023-06-06 05:17:07.523305'),(20,'hospital_modules','0002_doctor_schedule_patient_doctor_rating','2023-06-06 05:44:44.281800'),(21,'hospital_modules','0003_doctor_email_doctor_photo','2023-06-06 06:06:40.136420'),(22,'hospital_modules','0004_patient_photo_alter_doctor_age_and_more','2023-06-06 06:32:13.481733'),(23,'hospital_modules','0005_patient_dob_appointment','2023-06-07 11:03:30.931127'),(24,'hospital_modules','0006_prescription','2023-06-08 05:19:28.025140'),(25,'hospital_modules','0007_booking','2023-06-19 05:48:29.112348'),(26,'hospital_modules','0007_alter_doctor_rating_rating','2023-07-11 06:07:23.146511');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('lvc5lleki0hxyvgivtfiln8jd378v7to','eyJsaWQiOjEwfQ:1qE60j:pzObA0fxAlKqiJTtp4jFb-NRJdfYw_V1dAAbALwBzZ4','2023-07-11 10:33:25.421541'),('qmu7irz63ch4ewbo40az69o1g21qtuve','eyJsaWQiOjF9:1qGGYx:nC2LQpupwrArlfuRuc7Ujf69Na4Y7uGK-mYpkxwWluY','2023-07-17 10:13:43.996248'),('3a2h484ypir0xl5kduhuvw4n8br34axe','eyJsaWQiOjEwfQ:1qJTGS:okYHO0PsdbF-L4F0EC2pIVit6CKQ3M2y0V1_GXCN_-U','2023-07-26 06:23:52.963620');

/*Table structure for table `hospital_modules_appointment` */

DROP TABLE IF EXISTS `hospital_modules_appointment`;

CREATE TABLE `hospital_modules_appointment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` varchar(200) NOT NULL,
  `token` int NOT NULL,
  `Schedule_id` bigint NOT NULL,
  `patient_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hospital_modules_appointment_Schedule_id_57272d14` (`Schedule_id`),
  KEY `hospital_modules_appointment_patient_id_c1a91a92` (`patient_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `hospital_modules_appointment` */

insert  into `hospital_modules_appointment`(`id`,`date`,`token`,`Schedule_id`,`patient_id`) values (1,'2023-07-11',1,1,3),(2,'2023-07-11',2,1,1),(3,'2023-07-11',3,1,1),(4,'2023-07-11',4,1,5),(5,'2023-07-11',1,2,1),(8,'2023-07-11',2,2,5),(9,'2023-07-11',3,2,3);

/*Table structure for table `hospital_modules_doctor` */

DROP TABLE IF EXISTS `hospital_modules_doctor`;

CREATE TABLE `hospital_modules_doctor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `d_name` varchar(200) NOT NULL,
  `age` int NOT NULL,
  `gender` varchar(200) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `qualification` varchar(200) NOT NULL,
  `login_id_id` bigint NOT NULL,
  `email` varchar(200) NOT NULL,
  `photo` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hospital_modules_doctor_login_id_id_26cbf5b5` (`login_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `hospital_modules_doctor` */

insert  into `hospital_modules_doctor`(`id`,`d_name`,`age`,`gender`,`phone`,`qualification`,`login_id_id`,`email`,`photo`) values (5,'nasif',24,'male','9207882996','MBBS,Neurosurgeon',6,'nasi@gmail.com','/static/pic/230607-110957.jpg'),(1,'hamza',33,'male','9993334736','MBBS,Pediatrics',1,'hamza@gmail.com','/static/pic/230606-155633.jpg'),(11,'anoop',40,'male','9895148606','MBBS',19,'anoop@gmail.com','/static/pic/230622-151206.jpg'),(9,'mohsin',30,'male','9895148606','MBBS,Neurosurgeon',17,'mohsin@gmail.com','/static/pic/230622-115319.jpg');

/*Table structure for table `hospital_modules_doctor_rating` */

DROP TABLE IF EXISTS `hospital_modules_doctor_rating`;

CREATE TABLE `hospital_modules_doctor_rating` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `doctor_id_id` bigint NOT NULL,
  `patient_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hospital_modules_doctor_rating_doctor_id_id_1b7c9138` (`doctor_id_id`),
  KEY `hospital_modules_doctor_rating_patient_id_id_92d43985` (`patient_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `hospital_modules_doctor_rating` */

insert  into `hospital_modules_doctor_rating`(`id`,`rating`,`date`,`doctor_id_id`,`patient_id_id`) values (1,'4','2023-07-11',1,5),(2,'5','2023-09-09',1,3);

/*Table structure for table `hospital_modules_login` */

DROP TABLE IF EXISTS `hospital_modules_login`;

CREATE TABLE `hospital_modules_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `user_type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `hospital_modules_login` */

insert  into `hospital_modules_login`(`id`,`username`,`password`,`user_type`) values (5,'minhajkp969@gmail.com','0123','doctor'),(1,'hamza@gmail.com','123','doctor'),(4,'minhajkp969@gmail.com','0123','doctor'),(6,'nasi@gmail.com','0123','doctor'),(7,'fath@gmail.com','0123','doctor'),(8,'zahra@gmail.com','0123','doctor'),(9,'admin','admin','admin'),(10,'zahra@gmail.com','1234','patient'),(12,'nasi@gmail.com','1234','patient'),(13,'kpmujeeb16@gmail.com','1234','patient'),(16,'nasiddsdc@gmail.com','0123','doctor'),(15,'mansoor3@gmail.com','1234','patient'),(17,'suhaima@gmail.com','123','doctor'),(0,'','',''),(19,'anoop@gmail.com','123','doctor'),(20,'anoop1@gmail.com','123','doctor'),(21,'effw@gmail.com','123','doctor'),(22,'sugu2@gmail.com','123','doctor');

/*Table structure for table `hospital_modules_patient` */

DROP TABLE IF EXISTS `hospital_modules_patient`;

CREATE TABLE `hospital_modules_patient` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `p_name` varchar(200) NOT NULL,
  `age` int NOT NULL,
  `gender` varchar(200) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `place` varchar(200) NOT NULL,
  `post` varchar(200) NOT NULL,
  `pin` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `login_id_id` bigint NOT NULL,
  `photo` varchar(200) NOT NULL,
  `dob` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hospital_modules_patient_login_id_id_8db1b19a` (`login_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `hospital_modules_patient` */

insert  into `hospital_modules_patient`(`id`,`p_name`,`age`,`gender`,`phone`,`place`,`post`,`pin`,`email`,`login_id_id`,`photo`,`dob`) values (1,'zahra',10,'female','9998766678','mattul','so','670302','zahra@gmail.com',10,'/static/pic/230622-110751.jpg','2023-06-13'),(5,'mansoor dalal',24,'male','9995123456','payyannur','payyannur','670123','mansoor3@gmail.com',15,'/static/pic/230612-150951.jpg','1999-12-31'),(3,'mufaida',34,'female','9895148606','mattul','mattul south','670302','mufaida@gmail.com',12,'/static/pic/230612-145446.jpg','1988-02-12');

/*Table structure for table `hospital_modules_prescription` */

DROP TABLE IF EXISTS `hospital_modules_prescription`;

CREATE TABLE `hospital_modules_prescription` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `drug_name` varchar(200) NOT NULL,
  `duration` varchar(200) NOT NULL,
  `dosage` varchar(200) NOT NULL,
  `route` varchar(200) NOT NULL,
  `instruction` varchar(200) NOT NULL,
  `appointment_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hospital_modules_prescription_appointment_id_f0c8a194` (`appointment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `hospital_modules_prescription` */

insert  into `hospital_modules_prescription`(`id`,`drug_name`,`duration`,`dosage`,`route`,`instruction`,`appointment_id`) values (6,'aaa','2','2','oral','after food',1),(7,'ss','3','2','oral','after food',1),(3,'amoxicillin 500g','4 days','2','oral','after food',1),(10,'amoxicillin 500g','4 days','3','oral','after food',2),(8,'ff','2','1','oral','after food',1),(11,'paracetamol 500g','dd','dd','dd','dd',16),(12,'sefs','xvx','xc','ff','dd',5),(13,'trt','gff','fgf','gf','tfg',5),(14,'hg','hg','g','h','ghj',5),(15,'hg','hg','g','h','ghj',5);

/*Table structure for table `hospital_modules_schedule` */

DROP TABLE IF EXISTS `hospital_modules_schedule`;

CREATE TABLE `hospital_modules_schedule` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` varchar(200) NOT NULL,
  `starting_time` varchar(200) NOT NULL,
  `ending_time` varchar(200) NOT NULL,
  `total_token` varchar(200) NOT NULL,
  `doctor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hospital_modules_schedule_doctor_id_7f984a5d` (`doctor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `hospital_modules_schedule` */

insert  into `hospital_modules_schedule`(`id`,`date`,`starting_time`,`ending_time`,`total_token`,`doctor_id`) values (1,'2023-07-14','10:30','01:29','10',5),(2,'2023-07-12','00:53','02:53','10',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
