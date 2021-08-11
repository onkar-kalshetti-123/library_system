-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: student_management
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `admin_data`
--

DROP TABLE IF EXISTS `admin_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_data` (
  `User_ID` int NOT NULL,
  `Password` varchar(45) NOT NULL,
  UNIQUE KEY `User_ID_UNIQUE` (`User_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_data`
--

LOCK TABLES `admin_data` WRITE;
/*!40000 ALTER TABLE `admin_data` DISABLE KEYS */;
INSERT INTO `admin_data` VALUES (11110,'1234'),(11111,'Suraj@123');
/*!40000 ALTER TABLE `admin_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_name`
--

DROP TABLE IF EXISTS `books_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_name` (
  `BOOK_NAME` varchar(45) DEFAULT NULL,
  `DEPARTMENT` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_name`
--

LOCK TABLES `books_name` WRITE;
/*!40000 ALTER TABLE `books_name` DISABLE KEYS */;
INSERT INTO `books_name` VALUES ('Unknowbooks','OTHER'),(' advanced C programming','Computer Science'),(' advanced java programming','Computer Science'),(' core java programming','Computer Science'),('DBMS ','Computer Science'),('Andriod devlopment','Computer Science'),('Green Technology','Computer Science'),('Artifical Inteligence','Computer Science'),('Machine lerning','Computer Science'),('oprating system','Computer Science'),('computer networks','Computer Science'),('Iot','Computer Science'),('Fundamental and Algorithm','Computer Science'),('Game prograaming','Computer Science'),('Physics-2','OTHER'),('Physics-1','OTHER'),('chemistery','OTHER'),('chemistery-2','OTHER'),('DATA SCience','Computer Science'),('MARATHI -1','LANGUAGE'),('DBMS','Computer Science'),('Marathi','Select');
/*!40000 ALTER TABLE `books_name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrow_books`
--

DROP TABLE IF EXISTS `borrow_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrow_books` (
  `STUDENT_ID` int DEFAULT NULL,
  `EMAIL_ID` varchar(45) DEFAULT NULL,
  `BOOK_NAME` varchar(45) DEFAULT NULL,
  `DEPARTMENT` varchar(45) DEFAULT NULL,
  `FROMDATE` date DEFAULT NULL,
  `TODATE` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrow_books`
--

LOCK TABLES `borrow_books` WRITE;
/*!40000 ALTER TABLE `borrow_books` DISABLE KEYS */;
INSERT INTO `borrow_books` VALUES (11110,'librarymanager987@gmail.com','unknownbook','OTHER','2020-09-16','2020-09-16');
/*!40000 ALTER TABLE `borrow_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_data`
--

DROP TABLE IF EXISTS `student_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_data` (
  `student_id` int NOT NULL,
  `student_FirstName` varchar(45) NOT NULL,
  `student_LastName` varchar(45) NOT NULL,
  `student_ID_Card_No` varchar(45) DEFAULT NULL,
  `student_class` varchar(45) NOT NULL,
  PRIMARY KEY (`student_id`),
  UNIQUE KEY `student_id_UNIQUE` (`student_id`),
  UNIQUE KEY `ID_Card_no_UNIQUE` (`student_ID_Card_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_data`
--

LOCK TABLES `student_data` WRITE;
/*!40000 ALTER TABLE `student_data` DISABLE KEYS */;
INSERT INTO `student_data` VALUES (1,'keshav','Lad','22472','TYCS'),(2,'Admin','library','11110','Staff'),(3,'Yash','Pagare','22474','FYCS'),(4,'Sanket','Thorat','22473','TYCS'),(5,'Aniket','pardhe','22475','TYCS'),(6,'Aditya','kamble','22476','FYCS'),(7,'Pranay','Jadhav','22477','TyCs'),(8,'Rohan','Khambe','22478','TYCS'),(9,'Prathmesh','Rahate','22479','Tycs'),(10,'Satish','Yadav','22480','TyCS'),(11,'prem','Kanta','22481','TYCS'),(12,'Aman','mulani','22482','Tycs'),(13,'sushant','Padwal','22483','TYCS'),(14,'Mangesh','patl','22484','TYCS'),(15,'Sonu','Pagare','22485','TYCS'),(16,'Vikas','mundhe','22486','TYCS'),(17,'Sanjay','patil','22487','TYCS'),(18,'Darpan','patil','22488','TYCS'),(19,'Virendra','Pawar','22489','TYCS'),(20,'Jitendra','Pawar','22490','TYCS'),(21,'salman','khan','22491','FYCS'),(22,'Hardik','Pandya','22492','FyCS'),(23,'Krunal','Pnadya','22493','SYCS'),(24,'Vyanket','Rajput','22494','TYCS'),(25,'Saddam','Mulla','22495','SYCS'),(26,'Amitabh','Patil','22496','SYCS');
/*!40000 ALTER TABLE `student_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-12 20:06:11
