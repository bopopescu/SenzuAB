# ************************************************************
# Sequel Pro SQL dump
# Versión 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.6.24)
# Base de datos: senzupy
# Tiempo de Generación: 2017-05-29 00:53:47 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Volcado de tabla alertas_alertarecibida
# ------------------------------------------------------------



# Volcado de tabla alertas_alertas
# ------------------------------------------------------------



# Volcado de tabla auth_group
# ------------------------------------------------------------



# Volcado de tabla auth_group_permissions
# ------------------------------------------------------------



# Volcado de tabla auth_permission
# ------------------------------------------------------------

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
	(1,'Can add log entry',1,'add_logentry'),
	(2,'Can change log entry',1,'change_logentry'),
	(3,'Can delete log entry',1,'delete_logentry'),
	(4,'Can add permission',2,'add_permission'),
	(5,'Can change permission',2,'change_permission'),
	(6,'Can delete permission',2,'delete_permission'),
	(7,'Can add group',3,'add_group'),
	(8,'Can change group',3,'change_group'),
	(9,'Can delete group',3,'delete_group'),
	(10,'Can add content type',4,'add_contenttype'),
	(11,'Can change content type',4,'change_contenttype'),
	(12,'Can delete content type',4,'delete_contenttype'),
	(13,'Can add session',5,'add_session'),
	(14,'Can change session',5,'change_session'),
	(15,'Can delete session',5,'delete_session'),
	(16,'Can add Token',6,'add_token'),
	(17,'Can change Token',6,'change_token'),
	(18,'Can delete Token',6,'delete_token'),
	(19,'Can add Alertas recibidas',7,'add_alertarecibida'),
	(20,'Can change Alertas recibidas',7,'change_alertarecibida'),
	(21,'Can delete Alertas recibidas',7,'delete_alertarecibida'),
	(22,'Can add Alerta',8,'add_alertas'),
	(23,'Can change Alerta',8,'change_alertas'),
	(24,'Can delete Alerta',8,'delete_alertas'),
	(25,'Can add Usuario',9,'add_usuario'),
	(26,'Can change Usuario',9,'change_usuario'),
	(27,'Can delete Usuario',9,'delete_usuario'),
	(28,'Can add Cita',10,'add_citas'),
	(29,'Can change Cita',10,'change_citas'),
	(30,'Can delete Cita',10,'delete_citas'),
	(31,'Can add Consulta Medica',11,'add_consulta_medica'),
	(32,'Can change Consulta Medica',11,'change_consulta_medica'),
	(33,'Can delete Consulta Medica',11,'delete_consulta_medica'),
	(34,'Can add Entidad',12,'add_entidad'),
	(35,'Can change Entidad',12,'change_entidad'),
	(36,'Can delete Entidad',12,'delete_entidad'),
	(37,'Can add Especialidad',13,'add_especialidad'),
	(38,'Can change Especialidad',13,'change_especialidad'),
	(39,'Can delete Especialidad',13,'delete_especialidad'),
	(40,'Can add Habitacion',14,'add_habitacion'),
	(41,'Can change Habitacion',14,'change_habitacion'),
	(42,'Can delete Habitacion',14,'delete_habitacion'),
	(43,'Can add Medico',15,'add_medico'),
	(44,'Can change Medico',15,'change_medico'),
	(45,'Can delete Medico',15,'delete_medico'),
	(46,'Can add Paciente',16,'add_paciente'),
	(47,'Can change Paciente',16,'change_paciente'),
	(48,'Can delete Paciente',16,'delete_paciente'),
	(49,'Can add Pasillo',17,'add_pasillo'),
	(50,'Can change Pasillo',17,'change_pasillo'),
	(51,'Can delete Pasillo',17,'delete_pasillo'),
	(52,'Can add Sala',18,'add_sala'),
	(53,'Can change Sala',18,'change_sala'),
	(54,'Can delete Sala',18,'delete_sala'),
	(55,'Can add Tipo de cita',19,'add_tipo_cita'),
	(56,'Can change Tipo de cita',19,'change_tipo_cita'),
	(57,'Can delete Tipo de cita',19,'delete_tipo_cita');

/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;


# Volcado de tabla auth_user
# ------------------------------------------------------------

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `date_joined`, `email`, `username`, `cedula`, `first_name`, `last_name`, `es_medico`, `es_paciente`, `is_active`, `is_admin`, `is_superuser`)
VALUES
	(1,'pbkdf2_sha256$36000$HA40gBX1yw1o$M3Qli56mx+KMtp9L2r2bETIKrJncKL/YXyoG3OgleEQ=','2017-05-20 16:25:20.017169','2017-05-20 15:13:35.818861','alexis05batista@gmail.com','abatistab1','4-759-1445','alexis batista','batista',0,0,1,1,1);

/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;


# Volcado de tabla auth_user_groups
# ------------------------------------------------------------



# Volcado de tabla auth_user_user_permissions
# ------------------------------------------------------------



# Volcado de tabla authtoken_token
# ------------------------------------------------------------

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`)
VALUES
	('b8139f1c9e920bd33e648e7b22790010e36299f5','2017-05-20 18:07:58.149103',1);

/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;


# Volcado de tabla django_admin_log
# ------------------------------------------------------------



# Volcado de tabla django_content_type
# ------------------------------------------------------------

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;

INSERT INTO `django_content_type` (`id`, `app_label`, `model`)
VALUES
	(1,'admin','logentry'),
	(7,'alertas','alertarecibida'),
	(8,'alertas','alertas'),
	(3,'auth','group'),
	(2,'auth','permission'),
	(6,'authtoken','token'),
	(4,'contenttypes','contenttype'),
	(5,'sessions','session'),
	(10,'usuarios','citas'),
	(11,'usuarios','consulta_medica'),
	(12,'usuarios','entidad'),
	(13,'usuarios','especialidad'),
	(14,'usuarios','habitacion'),
	(15,'usuarios','medico'),
	(16,'usuarios','paciente'),
	(17,'usuarios','pasillo'),
	(18,'usuarios','sala'),
	(19,'usuarios','tipo_cita'),
	(9,'usuarios','usuario');

/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;


# Volcado de tabla django_migrations
# ------------------------------------------------------------

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
	(1,'contenttypes','0001_initial','2017-05-20 15:11:29.047704'),
	(2,'contenttypes','0002_remove_content_type_name','2017-05-20 15:11:29.154897'),
	(3,'auth','0001_initial','2017-05-20 15:11:29.394582'),
	(4,'auth','0002_alter_permission_name_max_length','2017-05-20 15:11:29.427138'),
	(5,'auth','0003_alter_user_email_max_length','2017-05-20 15:11:29.436071'),
	(6,'auth','0004_alter_user_username_opts','2017-05-20 15:11:29.444326'),
	(7,'auth','0005_alter_user_last_login_null','2017-05-20 15:11:29.452659'),
	(8,'auth','0006_require_contenttypes_0002','2017-05-20 15:11:29.455279'),
	(9,'auth','0007_alter_validators_add_error_messages','2017-05-20 15:11:29.466589'),
	(10,'auth','0008_alter_user_username_max_length','2017-05-20 15:11:29.474091'),
	(11,'usuarios','0001_initial','2017-05-20 15:11:31.326981'),
	(12,'admin','0001_initial','2017-05-20 15:11:31.439182'),
	(13,'admin','0002_logentry_remove_auto_add','2017-05-20 15:11:31.499324'),
	(14,'alertas','0001_initial','2017-05-20 15:11:31.642669'),
	(15,'authtoken','0001_initial','2017-05-20 15:11:31.715642'),
	(16,'authtoken','0002_auto_20160226_1747','2017-05-20 15:11:31.908114'),
	(17,'sessions','0001_initial','2017-05-20 15:11:31.960849');

/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;


# Volcado de tabla django_session
# ------------------------------------------------------------

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`)
VALUES
	('s8l5lkbn2sbej1cfowyqk82s1ljwaaql','ZGRmZTE4YWQ4MTkzYjFiNWU2NzZhY2RmZmE1YWI1ZTQyM2ZlODkxNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZmQwMWQzZjIzNzBkOTljOWIyYmM5M2Q4ZmRhYjAwMWJjNGM5NDI3In0=','2017-06-03 16:25:20.019843');

/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;


# Volcado de tabla usuarios_citas
# ------------------------------------------------------------



# Volcado de tabla usuarios_consulta_medica
# ------------------------------------------------------------



# Volcado de tabla usuarios_entidad
# ------------------------------------------------------------



# Volcado de tabla usuarios_especialidad
# ------------------------------------------------------------



# Volcado de tabla usuarios_habitacion
# ------------------------------------------------------------



# Volcado de tabla usuarios_habitacion_en_pasillo
# ------------------------------------------------------------



# Volcado de tabla usuarios_medico
# ------------------------------------------------------------



# Volcado de tabla usuarios_medico_en_lugar
# ------------------------------------------------------------



# Volcado de tabla usuarios_medico_especialidad
# ------------------------------------------------------------



# Volcado de tabla usuarios_paciente
# ------------------------------------------------------------



# Volcado de tabla usuarios_paciente_en_lugar
# ------------------------------------------------------------



# Volcado de tabla usuarios_pasillo
# ------------------------------------------------------------



# Volcado de tabla usuarios_sala
# ------------------------------------------------------------



# Volcado de tabla usuarios_tipo_cita
# ------------------------------------------------------------




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
