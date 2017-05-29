# ************************************************************
# Sequel Pro SQL dump
# Versión 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.6.24)
# Base de datos: senzupy
# Tiempo de Generación: 2017-05-29 00:15:37 +0000
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

DROP TABLE IF EXISTS `alertas_alertarecibida`;

CREATE TABLE `alertas_alertarecibida` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `leida` tinyint(1) NOT NULL,
  `fecha_hora_mensaje_leido` datetime(6) NOT NULL,
  `alerta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `alertas_alertarecibida_alerta_id_55146391_fk_alertas_alertas_id` (`alerta_id`),
  CONSTRAINT `alertas_alertarecibida_alerta_id_55146391_fk_alertas_alertas_id` FOREIGN KEY (`alerta_id`) REFERENCES `alertas_alertas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla alertas_alertas
# ------------------------------------------------------------

DROP TABLE IF EXISTS `alertas_alertas`;

CREATE TABLE `alertas_alertas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mensaje` longtext NOT NULL,
  `usuario` varchar(80) NOT NULL,
  `fecha_hora_mensaje` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla auth_group
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla auth_group_permissions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla auth_permission
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `cedula` varchar(60) NOT NULL,
  `first_name` varchar(80) NOT NULL,
  `last_name` varchar(80) NOT NULL,
  `es_medico` tinyint(1) NOT NULL,
  `es_paciente` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `cedula` (`cedula`),
  KEY `auth_user_first_name_fdcd781b` (`first_name`),
  KEY `auth_user_last_name_e48cdaa9` (`last_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `date_joined`, `email`, `username`, `cedula`, `first_name`, `last_name`, `es_medico`, `es_paciente`, `is_active`, `is_admin`, `is_superuser`)
VALUES
	(1,'pbkdf2_sha256$36000$HA40gBX1yw1o$M3Qli56mx+KMtp9L2r2bETIKrJncKL/YXyoG3OgleEQ=','2017-05-20 16:25:20.017169','2017-05-20 15:13:35.818861','alexis05batista@gmail.com','abatistab1','4-759-1445','alexis batista','batista',0,0,1,1,1);

/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;


# Volcado de tabla auth_user_groups
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_usuario_id_group_id_2d4e26e8_uniq` (`usuario_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_usuario_id_1458dadc_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla auth_user_user_permissions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissio_usuario_id_permission_id_a72d8789_uniq` (`usuario_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_usuario_id_453820ab_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla authtoken_token
# ------------------------------------------------------------

DROP TABLE IF EXISTS `authtoken_token`;

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`)
VALUES
	('b8139f1c9e920bd33e648e7b22790010e36299f5','2017-05-20 18:07:58.149103',1);

/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;


# Volcado de tabla django_admin_log
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla django_content_type
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`)
VALUES
	('s8l5lkbn2sbej1cfowyqk82s1ljwaaql','ZGRmZTE4YWQ4MTkzYjFiNWU2NzZhY2RmZmE1YWI1ZTQyM2ZlODkxNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZmQwMWQzZjIzNzBkOTljOWIyYmM5M2Q4ZmRhYjAwMWJjNGM5NDI3In0=','2017-06-03 16:25:20.019843');

/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;


# Volcado de tabla usuarios_citas
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_citas`;

CREATE TABLE `usuarios_citas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_creacion` datetime(6) NOT NULL,
  `cita_para` datetime(6) NOT NULL,
  `descripcion` longtext NOT NULL,
  `nota_para_la_cita` longtext NOT NULL,
  `estado` varchar(1) NOT NULL,
  `Medico_id` int(11) NOT NULL,
  `habitacion_id` int(11) NOT NULL,
  `paciente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuarios_citas_Medico_id_e1d0e542_fk_usuarios_medico_id` (`Medico_id`),
  KEY `usuarios_citas_habitacion_id_f95c928e_fk_usuarios_habitacion_id` (`habitacion_id`),
  KEY `usuarios_citas_paciente_id_34d02fcb_fk_usuarios_paciente_id` (`paciente_id`),
  CONSTRAINT `usuarios_citas_Medico_id_e1d0e542_fk_usuarios_medico_id` FOREIGN KEY (`Medico_id`) REFERENCES `usuarios_medico` (`id`),
  CONSTRAINT `usuarios_citas_habitacion_id_f95c928e_fk_usuarios_habitacion_id` FOREIGN KEY (`habitacion_id`) REFERENCES `usuarios_habitacion` (`id`),
  CONSTRAINT `usuarios_citas_paciente_id_34d02fcb_fk_usuarios_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `usuarios_paciente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_consulta_medica
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_consulta_medica`;

CREATE TABLE `usuarios_consulta_medica` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `detalles` longtext NOT NULL,
  `receta` longtext NOT NULL,
  `cita_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuarios_consulta_medica_cita_id_7069db5a_fk_usuarios_citas_id` (`cita_id`),
  CONSTRAINT `usuarios_consulta_medica_cita_id_7069db5a_fk_usuarios_citas_id` FOREIGN KEY (`cita_id`) REFERENCES `usuarios_citas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_entidad
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_entidad`;

CREATE TABLE `usuarios_entidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `nombre_legal` varchar(160) NOT NULL,
  `ruc` varchar(60) NOT NULL,
  `direccion` longtext NOT NULL,
  `telefono` varchar(160) NOT NULL,
  `horario` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_especialidad
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_especialidad`;

CREATE TABLE `usuarios_especialidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `especialidad` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `especialidad` (`especialidad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_habitacion
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_habitacion`;

CREATE TABLE `usuarios_habitacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(160) NOT NULL,
  `detalle` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_habitacion_en_pasillo
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_habitacion_en_pasillo`;

CREATE TABLE `usuarios_habitacion_en_pasillo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `habitacion_id` int(11) NOT NULL,
  `pasillo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_habitacion_en_p_habitacion_id_pasillo_id_4fd393f2_uniq` (`habitacion_id`,`pasillo_id`),
  KEY `usuarios_habitacion__pasillo_id_ad5104d8_fk_usuarios_` (`pasillo_id`),
  CONSTRAINT `usuarios_habitacion__habitacion_id_e6e180bc_fk_usuarios_` FOREIGN KEY (`habitacion_id`) REFERENCES `usuarios_habitacion` (`id`),
  CONSTRAINT `usuarios_habitacion__pasillo_id_ad5104d8_fk_usuarios_` FOREIGN KEY (`pasillo_id`) REFERENCES `usuarios_pasillo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_medico
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_medico`;

CREATE TABLE `usuarios_medico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `horario` longtext NOT NULL,
  `telefono` longtext NOT NULL,
  `sexo` varchar(1) NOT NULL,
  `fecha_registrado` datetime(6) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuarios_medico_usuario_id_43910484_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `usuarios_medico_usuario_id_43910484_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_medico_en_lugar
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_medico_en_lugar`;

CREATE TABLE `usuarios_medico_en_lugar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `medico_id` int(11) NOT NULL,
  `entidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_medico_en_lugar_medico_id_entidad_id_d70593b1_uniq` (`medico_id`,`entidad_id`),
  KEY `usuarios_medico_en_l_entidad_id_074de607_fk_usuarios_` (`entidad_id`),
  CONSTRAINT `usuarios_medico_en_l_entidad_id_074de607_fk_usuarios_` FOREIGN KEY (`entidad_id`) REFERENCES `usuarios_entidad` (`id`),
  CONSTRAINT `usuarios_medico_en_l_medico_id_3d607557_fk_usuarios_` FOREIGN KEY (`medico_id`) REFERENCES `usuarios_medico` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_medico_especialidad
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_medico_especialidad`;

CREATE TABLE `usuarios_medico_especialidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `medico_id` int(11) NOT NULL,
  `especialidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_medico_especial_medico_id_especialidad_i_132edc83_uniq` (`medico_id`,`especialidad_id`),
  KEY `usuarios_medico_espe_especialidad_id_f80107c9_fk_usuarios_` (`especialidad_id`),
  CONSTRAINT `usuarios_medico_espe_especialidad_id_f80107c9_fk_usuarios_` FOREIGN KEY (`especialidad_id`) REFERENCES `usuarios_especialidad` (`id`),
  CONSTRAINT `usuarios_medico_espe_medico_id_643bfdf2_fk_usuarios_` FOREIGN KEY (`medico_id`) REFERENCES `usuarios_medico` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_paciente
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_paciente`;

CREATE TABLE `usuarios_paciente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nacimiento` date NOT NULL,
  `direccion` varchar(800) NOT NULL,
  `telefono` varchar(25) DEFAULT NULL,
  `grupo_sanguineo` varchar(3) DEFAULT NULL,
  `peso` varchar(10) NOT NULL,
  `altura` varchar(10) NOT NULL,
  `reacciones_alergicas` longtext NOT NULL,
  `sexo` varchar(1) NOT NULL,
  `ocupacion` longtext,
  `nota_medica` longtext,
  `seguro_medico` varchar(200) DEFAULT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuarios_paciente_usuario_id_9a1be9db_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `usuarios_paciente_usuario_id_9a1be9db_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_paciente_en_lugar
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_paciente_en_lugar`;

CREATE TABLE `usuarios_paciente_en_lugar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `paciente_id` int(11) NOT NULL,
  `entidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_paciente_en_lugar_paciente_id_entidad_id_d0793d2b_uniq` (`paciente_id`,`entidad_id`),
  KEY `usuarios_paciente_en_entidad_id_cb457707_fk_usuarios_` (`entidad_id`),
  CONSTRAINT `usuarios_paciente_en_entidad_id_cb457707_fk_usuarios_` FOREIGN KEY (`entidad_id`) REFERENCES `usuarios_entidad` (`id`),
  CONSTRAINT `usuarios_paciente_en_paciente_id_faee952c_fk_usuarios_` FOREIGN KEY (`paciente_id`) REFERENCES `usuarios_paciente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_pasillo
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_pasillo`;

CREATE TABLE `usuarios_pasillo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(160) NOT NULL,
  `detalle` longtext NOT NULL,
  `en_la_sala_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuarios_pasillo_en_la_sala_id_6432c544_fk_usuarios_sala_id` (`en_la_sala_id`),
  CONSTRAINT `usuarios_pasillo_en_la_sala_id_6432c544_fk_usuarios_sala_id` FOREIGN KEY (`en_la_sala_id`) REFERENCES `usuarios_sala` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_sala
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_sala`;

CREATE TABLE `usuarios_sala` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(160) NOT NULL,
  `detalle` longtext NOT NULL,
  `en_lugar_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuarios_sala_en_lugar_id_e9bc3c81_fk_usuarios_entidad_id` (`en_lugar_id`),
  CONSTRAINT `usuarios_sala_en_lugar_id_e9bc3c81_fk_usuarios_entidad_id` FOREIGN KEY (`en_lugar_id`) REFERENCES `usuarios_entidad` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Volcado de tabla usuarios_tipo_cita
# ------------------------------------------------------------

DROP TABLE IF EXISTS `usuarios_tipo_cita`;

CREATE TABLE `usuarios_tipo_cita` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(160) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
