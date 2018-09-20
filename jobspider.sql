-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: jobspider
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `job_ai`
--

DROP TABLE IF EXISTS `job_ai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job_ai` (
  `url` varchar(300) NOT NULL,
  `url_obj_id` varchar(60) NOT NULL,
  `title` varchar(100) NOT NULL,
  `salary_min` float DEFAULT NULL,
  `salary_max` float DEFAULT NULL,
  `job_city` varchar(100) DEFAULT NULL,
  `experience_year` varchar(30) DEFAULT NULL,
  `education_need` varchar(30) DEFAULT NULL,
  `publish_date` varchar(20) DEFAULT NULL,
  `job_advantage_tags` varchar(100) DEFAULT NULL,
  `position_info` longtext,
  `job_classification` varchar(50) DEFAULT NULL,
  `crawl_time` datetime NOT NULL,
  `crawl_update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`url_obj_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='人工智能表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_ai`
--

LOCK TABLES `job_ai` WRITE;
/*!40000 ALTER TABLE `job_ai` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_ai` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_arithmetic`
--

DROP TABLE IF EXISTS `job_arithmetic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job_arithmetic` (
  `url` varchar(300) NOT NULL,
  `url_obj_id` varchar(60) NOT NULL,
  `title` varchar(100) NOT NULL,
  `salary_min` float DEFAULT NULL,
  `salary_max` float DEFAULT NULL,
  `job_city` varchar(100) DEFAULT NULL,
  `experience_year` varchar(30) DEFAULT NULL,
  `education_need` varchar(30) DEFAULT NULL,
  `publish_date` varchar(20) DEFAULT NULL,
  `job_advantage_tags` varchar(100) DEFAULT NULL,
  `position_info` longtext,
  `job_classification` varchar(50) DEFAULT NULL,
  `crawl_time` datetime NOT NULL,
  `crawl_update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`url_obj_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='arithmetic算法表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_arithmetic`
--

LOCK TABLES `job_arithmetic` WRITE;
/*!40000 ALTER TABLE `job_arithmetic` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_arithmetic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_bigdata`
--

DROP TABLE IF EXISTS `job_bigdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job_bigdata` (
  `url` varchar(300) NOT NULL,
  `url_obj_id` varchar(60) NOT NULL,
  `title` varchar(100) NOT NULL,
  `salary_min` float DEFAULT NULL,
  `salary_max` float DEFAULT NULL,
  `job_city` varchar(100) DEFAULT NULL,
  `experience_year` varchar(30) DEFAULT NULL,
  `education_need` varchar(30) DEFAULT NULL,
  `publish_date` varchar(20) DEFAULT NULL,
  `job_advantage_tags` varchar(100) DEFAULT NULL,
  `position_info` longtext,
  `job_classification` varchar(50) DEFAULT NULL,
  `crawl_time` datetime NOT NULL,
  `crawl_update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`url_obj_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='大数据表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_bigdata`
--

LOCK TABLES `job_bigdata` WRITE;
/*!40000 ALTER TABLE `job_bigdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_bigdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_cplus`
--

DROP TABLE IF EXISTS `job_cplus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job_cplus` (
  `url` varchar(300) NOT NULL,
  `url_obj_id` varchar(60) NOT NULL,
  `title` varchar(100) NOT NULL,
  `salary_min` float DEFAULT NULL,
  `salary_max` float DEFAULT NULL,
  `job_city` varchar(100) DEFAULT NULL,
  `experience_year` varchar(30) DEFAULT NULL,
  `education_need` varchar(30) DEFAULT NULL,
  `publish_date` varchar(20) DEFAULT NULL,
  `job_advantage_tags` varchar(100) DEFAULT NULL,
  `position_info` longtext,
  `job_classification` varchar(50) DEFAULT NULL,
  `crawl_time` datetime NOT NULL,
  `crawl_update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`url_obj_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='C++表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_cplus`
--

LOCK TABLES `job_cplus` WRITE;
/*!40000 ALTER TABLE `job_cplus` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_cplus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_go`
--

DROP TABLE IF EXISTS `job_go`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job_go` (
  `url` varchar(300) NOT NULL,
  `url_obj_id` varchar(60) NOT NULL,
  `title` varchar(100) NOT NULL,
  `salary_min` float DEFAULT NULL,
  `salary_max` float DEFAULT NULL,
  `job_city` varchar(100) DEFAULT NULL,
  `experience_year` varchar(30) DEFAULT NULL,
  `education_need` varchar(30) DEFAULT NULL,
  `publish_date` varchar(20) DEFAULT NULL,
  `job_advantage_tags` varchar(100) DEFAULT NULL,
  `position_info` longtext,
  `job_classification` varchar(50) DEFAULT NULL,
  `crawl_time` datetime NOT NULL,
  `crawl_update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`url_obj_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Go语言表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_go`
--

LOCK TABLES `job_go` WRITE;
/*!40000 ALTER TABLE `job_go` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_go` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_java`
--

DROP TABLE IF EXISTS `job_java`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job_java` (
  `url` varchar(300) NOT NULL,
  `url_obj_id` varchar(60) NOT NULL,
  `title` varchar(100) NOT NULL,
  `salary_min` float DEFAULT NULL,
  `salary_max` float DEFAULT NULL,
  `job_city` varchar(100) DEFAULT NULL,
  `experience_year` varchar(30) DEFAULT NULL,
  `education_need` varchar(30) DEFAULT NULL,
  `publish_date` varchar(20) DEFAULT NULL,
  `job_advantage_tags` varchar(100) DEFAULT NULL,
  `position_info` longtext,
  `job_classification` varchar(50) DEFAULT NULL,
  `crawl_time` datetime NOT NULL,
  `crawl_update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`url_obj_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='JAVA表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_java`
--

LOCK TABLES `job_java` WRITE;
/*!40000 ALTER TABLE `job_java` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_java` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_python`
--

DROP TABLE IF EXISTS `job_python`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job_python` (
  `url` varchar(300) NOT NULL,
  `url_obj_id` varchar(60) NOT NULL,
  `title` varchar(100) NOT NULL,
  `salary_min` float DEFAULT NULL,
  `salary_max` float DEFAULT NULL,
  `job_city` varchar(100) DEFAULT NULL,
  `experience_year` varchar(30) DEFAULT NULL,
  `education_need` varchar(30) DEFAULT NULL,
  `publish_date` varchar(20) DEFAULT NULL,
  `job_advantage_tags` varchar(100) DEFAULT NULL,
  `position_info` longtext,
  `job_classification` varchar(50) DEFAULT NULL,
  `crawl_time` datetime NOT NULL,
  `crawl_update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`url_obj_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='python表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_python`
--

LOCK TABLES `job_python` WRITE;
/*!40000 ALTER TABLE `job_python` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_python` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_test`
--

DROP TABLE IF EXISTS `job_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job_test` (
  `url` varchar(300) NOT NULL,
  `url_obj_id` varchar(60) NOT NULL,
  `title` varchar(100) NOT NULL,
  `salary_min` float DEFAULT NULL,
  `salary_max` float DEFAULT NULL,
  `job_city` varchar(100) DEFAULT NULL,
  `experience_year` varchar(30) DEFAULT NULL,
  `education_need` varchar(30) DEFAULT NULL,
  `publish_date` varchar(20) DEFAULT NULL,
  `job_advantage_tags` varchar(100) DEFAULT NULL,
  `position_info` longtext,
  `job_classification` varchar(50) DEFAULT NULL,
  `crawl_time` datetime NOT NULL,
  `crawl_update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`url_obj_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Go语言表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_test`
--

LOCK TABLES `job_test` WRITE;
/*!40000 ALTER TABLE `job_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_test` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-20  9:49:17
