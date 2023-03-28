-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: sadpea
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `driver`
--

DROP TABLE IF EXISTS `driver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `driver` (
  `DriverID` int NOT NULL AUTO_INCREMENT,
  `FirstName` char(50) DEFAULT NULL,
  `LastName` char(50) DEFAULT NULL,
  PRIMARY KEY (`DriverID`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `driver`
--

LOCK TABLES `driver` WRITE;
/*!40000 ALTER TABLE `driver` DISABLE KEYS */;
INSERT INTO `driver` VALUES (1,'James','Mary'),(2,'Robert','Patricia'),(3,'John','Jennifer'),(4,'Michael','Linda'),(5,'David','Elizabeth'),(6,'William','Barbara'),(7,'Richard','Susan'),(8,'Joseph','Jessica'),(9,'Thomas','Sarah'),(10,'Charles','Karen'),(11,'Christopher','Lisa'),(12,'Daniel','Nancy'),(13,'Matthew','Betty'),(14,'Anthony','Margaret'),(15,'Mark','Sandra'),(16,'Donald','Ashley'),(17,'Steven','Kimberly'),(18,'Paul','Emily'),(19,'Andrew','Donna'),(20,'Joshua','Michelle'),(21,'Kenneth','Carol'),(22,'Kevin','Amanda'),(23,'Brian','Dorothy'),(24,'George','Melissa'),(25,'Timothy','Deborah'),(26,'Ronald','Stephanie'),(27,'Edward','Rebecca'),(28,'Jason','Sharon'),(29,'Jeffrey','Laura'),(30,'Ryan','Cynthia'),(31,'Jacob','Kathleen'),(32,'Gary','Amy'),(33,'Nicholas','Angela'),(34,'Eric','Shirley'),(35,'Jonathan','Anna'),(36,'Stephen','Brenda'),(37,'Larry','Pamela'),(38,'Justin','Emma'),(39,'Scott','Nicole'),(40,'Brandon','Helen'),(41,'Benjamin','Samantha'),(42,'Samuel','Katherine'),(43,'Gregory','Christine'),(44,'Alexander','Debra'),(45,'Frank','Rachel'),(46,'Patrick','Carolyn'),(47,'Raymond','Janet'),(48,'Jack','Catherine'),(49,'Dennis','Maria'),(50,'Jerry','Heather');
/*!40000 ALTER TABLE `driver` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-27 14:10:36
