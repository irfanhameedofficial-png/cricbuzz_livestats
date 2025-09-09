-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: cricbuzz_livestats
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `crud_player_info`
--

DROP TABLE IF EXISTS `crud_player_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `crud_player_info` (
  `player_id` int NOT NULL,
  `player_name` text,
  `player_country` text,
  `player_role` text,
  `matches_played` int DEFAULT NULL,
  `runs_scored` int DEFAULT NULL,
  `wickets_taken` int DEFAULT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crud_player_info`
--

LOCK TABLES `crud_player_info` WRITE;
/*!40000 ALTER TABLE `crud_player_info` DISABLE KEYS */;
INSERT INTO `crud_player_info` VALUES (1,'Irfan','India','All-Rounder',125,5625,218);
/*!40000 ALTER TABLE `crud_player_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `highest_score`
--

DROP TABLE IF EXISTS `highest_score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `highest_score` (
  `match_format` text,
  `highest_score` int DEFAULT NULL,
  `name` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `highest_score`
--

LOCK TABLES `highest_score` WRITE;
/*!40000 ALTER TABLE `highest_score` DISABLE KEYS */;
INSERT INTO `highest_score` VALUES ('ODI',264,'Rohit'),('Test',400,'B Lara'),('T20',172,'Finch');
/*!40000 ALTER TABLE `highest_score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hundreds`
--

DROP TABLE IF EXISTS `hundreds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hundreds` (
  `id` int NOT NULL,
  `name` text,
  `odi_hundreds` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hundreds`
--

LOCK TABLES `hundreds` WRITE;
/*!40000 ALTER TABLE `hundreds` DISABLE KEYS */;
INSERT INTO `hundreds` VALUES (25,'Tendulkar',49),(29,'S Ganguly',22),(35,'Inzamam-ul-Haq',10),(38,'R Ponting',30),(101,'Mahela',19),(102,'S Jayasuriya',28),(104,'Sangakkara',25),(105,'Dilshan',22),(212,'H Gibbs',21),(213,'Kallis',17),(240,'B Lara',19),(247,'Gayle',25),(314,'Amla',27),(370,'de Villiers',25),(521,'Ross Taylor',21),(576,'Rohit',32),(1413,'Kohli',51),(1739,'Warner',22),(3703,'S Anwar',20),(8019,'Root',19),(8359,'Babar Azam',19),(8520,'de Kock',21);
/*!40000 ALTER TABLE `hundreds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ind_allrounder_players`
--

DROP TABLE IF EXISTS `ind_allrounder_players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ind_allrounder_players` (
  `id` int NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `runs` int DEFAULT NULL,
  `wickets` int DEFAULT NULL,
  `match_format` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ind_allrounder_players`
--

LOCK TABLES `ind_allrounder_players` WRITE;
/*!40000 ALTER TABLE `ind_allrounder_players` DISABLE KEYS */;
INSERT INTO `ind_allrounder_players` VALUES (587,'Ravindra Jadeja',3886,330,'ODI'),(8683,'Shardul Thakur',377,33,'ODI'),(8808,'Axar Patel',1653,55,'ODI'),(9647,'Hardik Pandya',4653,156,'ODI'),(10945,'Washington Sundar',752,32,'ODI'),(11195,'Shivam Dube',0,0,'ODI'),(12086,'Abhishek Sharma',0,0,'ODI'),(14701,'Nitish Kumar Reddy',343,8,'ODI');
/*!40000 ALTER TABLE `ind_allrounder_players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indian_players`
--

DROP TABLE IF EXISTS `indian_players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `indian_players` (
  `id` int NOT NULL,
  `name` text,
  `role` text,
  `battingStyle` text,
  `bowlingStyle` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indian_players`
--

LOCK TABLES `indian_players` WRITE;
/*!40000 ALTER TABLE `indian_players` DISABLE KEYS */;
INSERT INTO `indian_players` VALUES (576,'Rohit Sharma','BATSMEN','Right-hand bat','Right-arm offbreak'),(587,'Ravindra Jadeja','ALL ROUNDER','Left-hand bat','Left-arm orthodox'),(1413,'Virat Kohli','BATSMEN','Right-hand bat','Right-arm medium'),(7915,'Suryakumar Yadav','BATSMEN','Right-hand bat','Right-arm offbreak'),(8257,'Karun Nair','BATSMEN','Right-hand bat','Right-arm offbreak'),(8271,'Sanju Samson','WICKET KEEPER','Right-hand bat',NULL),(8292,'Kuldeep Yadav','BOWLER','Left-hand bat','Left-arm wrist-spin'),(8683,'Shardul Thakur','ALL ROUNDER','Right-hand bat','Right-arm fast-medium'),(8733,'KL Rahul','WICKET KEEPER','Right-hand bat',NULL),(8808,'Axar Patel','ALL ROUNDER','Left-hand bat','Left-arm orthodox'),(9311,'Jasprit Bumrah','BOWLER','Right-hand bat','Right-arm fast'),(9428,'Shreyas Iyer','BATSMEN','Right-hand bat','Right-arm legbreak'),(9429,'Sarfaraz Khan','BATSMEN','Right-hand bat','Right-arm legbreak'),(9647,'Hardik Pandya','ALL ROUNDER','Right-hand bat','Right-arm fast-medium'),(9716,'Abhimanyu Easwaran','BATSMEN','Right-hand bat','Right-arm legbreak'),(10276,'Ishan Kishan','WICKET KEEPER','Left-hand bat',NULL),(10551,'Prasidh Krishna','BOWLER','Right-hand bat','Right-arm fast'),(10636,'Rajat Patidar','BATSMEN','Right-hand bat','Right-arm offbreak'),(10744,'Rishabh Pant','WICKET KEEPER','Left-hand bat',NULL),(10754,'Mukesh Kumar','BOWLER','Right-hand bat','Right-arm fast-medium'),(10808,'Mohammed Siraj','BOWLER','Right-hand bat','Right-arm fast'),(10896,'Rinku Singh','BATSMEN','Left-hand bat','Right-arm offbreak'),(10945,'Washington Sundar','ALL ROUNDER','Left-hand bat','Right-arm offbreak'),(11195,'Shivam Dube','ALL ROUNDER','Left-hand bat','Right-arm medium'),(11808,'Shubman Gill','BATSMEN','Right-hand bat','Right-arm offbreak'),(11813,'Ruturaj Gaikwad','BATSMEN','Right-hand bat','Right-arm offbreak'),(12086,'Abhishek Sharma','ALL ROUNDER','Left-hand bat','Left-arm orthodox'),(12926,'Varun Chakaravarthy','BOWLER','Right-hand bat','Right-arm legbreak'),(13217,'Arshdeep Singh','BOWLER','Left-hand bat','Left-arm fast-medium'),(13866,'Sai Sudharsan','BATSMEN','Left-hand bat','Right-arm legbreak'),(13940,'Yashasvi Jaiswal','BATSMEN','Left-hand bat','Right-arm legbreak'),(14504,'Tilak Varma','BATSMEN','Left-hand bat','Right-arm offbreak'),(14659,'Ravi Bishnoi','BOWLER','Right-hand bat','Right-arm legbreak'),(14691,'Dhruv Jurel','WICKET KEEPER','Right-hand bat',NULL),(14701,'Nitish Kumar Reddy','ALL ROUNDER','Right-hand bat','Right-arm fast-medium'),(14726,'Akash Deep','BOWLER','Right-hand bat','Right-arm fast-medium'),(24729,'Harshit Rana','BOWLER','Right-hand bat','Right-arm fast-medium');
/*!40000 ALTER TABLE `indian_players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recent_matches`
--

DROP TABLE IF EXISTS `recent_matches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recent_matches` (
  `series_name` text,
  `match_desc` text,
  `teams` text,
  `venue` text,
  `city` text,
  `match_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recent_matches`
--

LOCK TABLES `recent_matches` WRITE;
/*!40000 ALTER TABLE `recent_matches` DISABLE KEYS */;
INSERT INTO `recent_matches` VALUES ('South Africa tour of England, 2025','3rd ODI','England vs South Africa','The Rose Bowl','Southampton','2025-09-07 15:30:00'),('South Africa tour of England, 2025','1st ODI','England vs South Africa','Headingley','Leeds','2025-09-02 17:30:00'),('South Africa tour of England, 2025','2nd ODI','South Africa vs England','Lord\'s','London','2025-09-04 17:30:00'),('United Arab Emirates T20I Tri-Series 2025','Final','Pakistan vs Afghanistan','Sharjah Cricket Stadium','Sharjah','2025-09-07 20:30:00'),('United Arab Emirates T20I Tri-Series 2025','3rd Match','Afghanistan vs United Arab Emirates','Sharjah Cricket Stadium','Sharjah','2025-09-01 20:30:00'),('United Arab Emirates T20I Tri-Series 2025','5th Match','Pakistan vs United Arab Emirates','Sharjah Cricket Stadium','Sharjah','2025-09-04 20:30:00'),('United Arab Emirates T20I Tri-Series 2025','6th Match','Afghanistan vs United Arab Emirates','Sharjah Cricket Stadium','Sharjah','2025-09-05 20:30:00'),('United Arab Emirates T20I Tri-Series 2025','4th Match','Afghanistan vs Pakistan','Sharjah Cricket Stadium','Sharjah','2025-09-02 20:30:00'),('ICC Cricket World Cup League Two 2023-27','85th Match','Canada vs Scotland','Maple Leaf North-West Ground','King City','2025-09-06 20:00:00'),('ICC Cricket World Cup League Two 2023-27','84th Match','Scotland vs Namibia','Maple Leaf North-West Ground','King City','2025-09-04 20:00:00'),('ICC Cricket World Cup League Two 2023-27','83rd Match','Namibia vs Canada','Maple Leaf North-West Ground','King City','2025-09-02 20:00:00'),('Netherlands tour of Bangladesh 2025','3rd T20I','Bangladesh vs Netherlands','Sylhet International Cricket Stadium','Sylhet','2025-09-03 17:30:00'),('Netherlands tour of Bangladesh 2025','2nd T20I','Netherlands vs Bangladesh','Sylhet International Cricket Stadium','Sylhet','2025-09-01 17:30:00'),('Sri Lanka tour of Zimbabwe, 2025','3rd T20I','Zimbabwe vs Sri Lanka','Harare Sports Club','Harare','2025-09-07 17:00:00'),('Sri Lanka tour of Zimbabwe, 2025','1st T20I','Zimbabwe vs Sri Lanka','Harare Sports Club','Harare','2025-09-03 17:00:00'),('Sri Lanka tour of Zimbabwe, 2025','2nd T20I','Sri Lanka vs Zimbabwe','Harare Sports Club','Harare','2025-09-06 17:00:00'),('Sweden tour of Isle Of Man 2025','4th Match','Isle of Man vs Sweden','Cronkbourne Sports and Social Club Ground','Tromode','2025-09-07 20:00:00'),('Sweden tour of Isle Of Man 2025','3rd T20I','Isle of Man vs Sweden','Cronkbourne Sports and Social Club Ground','Tromode','2025-09-07 15:30:00'),('Sweden tour of Isle Of Man 2025','1st T20I','Isle of Man vs Sweden','Cronkbourne Sports and Social Club Ground','Tromode','2025-09-06 15:30:00'),('Sweden tour of Isle Of Man 2025','2nd T20I','Isle of Man vs Sweden','Cronkbourne Sports and Social Club Ground','Tromode','2025-09-06 20:00:00'),('Caribbean Premier League 2025','25th Match','St Kitts and Nevis Patriots vs Guyana Amazon Warriors','Providence Stadium','Guyana','2025-09-08 05:30:00'),('Caribbean Premier League 2025','19th Match','Trinbago Knight Riders vs St Kitts and Nevis Patriots','Brian Lara Stadium','Tarouba, Trinidad','2025-09-01 20:30:00'),('Caribbean Premier League 2025','23rd Match','Trinbago Knight Riders vs Guyana Amazon Warriors','Providence Stadium','Guyana','2025-09-07 04:30:00'),('Caribbean Premier League 2025','24th Match','Barbados Royals vs Saint Lucia Kings','Kensington Oval','Bridgetown, Barbados','2025-09-07 20:30:00'),('Caribbean Premier League 2025','21st Match','Barbados Royals vs Guyana Amazon Warriors','Kensington Oval','Bridgetown, Barbados','2025-09-05 04:30:00'),('Caribbean Premier League 2025','20th Match','Trinbago Knight Riders vs Saint Lucia Kings','Brian Lara Stadium','Tarouba, Trinidad','2025-09-04 04:30:00'),('Caribbean Premier League 2025','22nd Match','Barbados Royals vs Antigua and Barbuda Falcons','Kensington Oval','Bridgetown, Barbados','2025-09-06 04:30:00'),('T20 Blast 2025','Quarter Final 4','Warwickshire vs Somerset','The Cooper Associates County Ground','Taunton','2025-09-06 23:00:00'),('T20 Blast 2025','Quarter Final 3','Kent vs Lancashire','Emirates Old Trafford','Manchester','2025-09-06 19:00:00'),('T20 Blast 2025','Quarter Final 2','Hampshire vs Durham','Riverside Ground','Chester-le-Street','2025-09-05 23:00:00'),('T20 Blast 2025','Quarter Final 1','Northamptonshire vs Surrey','Kennington Oval','London','2025-09-03 23:00:00'),('Uttar Pradesh Premier League 2025','Final','Meerut Mavericks vs Kashi Rudras','Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium','Lucknow','2025-09-06 19:30:00'),('Uttar Pradesh Premier League 2025','Eliminator','Lucknow Falcons vs Gaur Gorakhapur Lions','Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium','Lucknow','2025-09-03 19:30:00'),('Uttar Pradesh Premier League 2025','Qualifier 2','Meerut Mavericks vs Lucknow Falcons','Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium','Lucknow','2025-09-04 19:30:00'),('Uttar Pradesh Premier League 2025','30th Match','Lucknow Falcons vs Kashi Rudras','Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium','Lucknow','2025-09-01 19:30:00'),('Uttar Pradesh Premier League 2025','Qualifier 1','Kashi Rudras vs Meerut Mavericks','Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium','Lucknow','2025-09-03 15:00:00'),('Kerala Cricket League 2025','Semi Final 2 (1st v 4th)','Kochi Blue Tigers vs Calicut Globstars','Greenfield International Stadium','Thiruvananthapuram','2025-09-05 18:45:00'),('Kerala Cricket League 2025','27th Match','Adani Trivandrum Royals vs Alleppey Ripples','Greenfield International Stadium','Thiruvananthapuram','2025-09-03 14:30:00'),('Kerala Cricket League 2025','24th Match','Calicut Globstars vs Aries Kollam Sailors','Greenfield International Stadium','Thiruvananthapuram','2025-09-01 18:45:00'),('Kerala Cricket League 2025','Final','Kochi Blue Tigers vs Aries Kollam Sailors','Greenfield International Stadium','Thiruvananthapuram','2025-09-07 18:45:00'),('Kerala Cricket League 2025','30th Match','Calicut Globstars vs Thrissur Titans','Greenfield International Stadium','Thiruvananthapuram','2025-09-04 18:45:00'),('Kerala Cricket League 2025','29th Match','Alleppey Ripples vs Aries Kollam Sailors','Greenfield International Stadium','Thiruvananthapuram','2025-09-04 14:30:00'),('Kerala Cricket League 2025','26th Match','Adani Trivandrum Royals vs Thrissur Titans','Greenfield International Stadium','Thiruvananthapuram','2025-09-02 18:45:00'),('Kerala Cricket League 2025','28th Match','Aries Kollam Sailors vs Kochi Blue Tigers','Greenfield International Stadium','Thiruvananthapuram','2025-09-03 18:45:00'),('Kerala Cricket League 2025','Semi Final 1 (2nd v 3rd)','Thrissur Titans vs Aries Kollam Sailors','Greenfield International Stadium','Thiruvananthapuram','2025-09-05 14:30:00'),('Kerala Cricket League 2025','25th Match','Calicut Globstars vs Kochi Blue Tigers','Greenfield International Stadium','Thiruvananthapuram','2025-09-02 14:30:00'),('Kerala Cricket League 2025','23rd Match','Alleppey Ripples vs Thrissur Titans','Greenfield International Stadium','Thiruvananthapuram','2025-09-01 14:30:00'),('Duleep Trophy 2025','2nd Semi-Final','West Zone vs Central Zone','BCCI Centre of Excellence Ground B','Bengaluru','2025-09-04 09:30:00'),('Duleep Trophy 2025','1st Semi-Final','South Zone vs North Zone','BCCI Centre of Excellence Ground','Bengaluru','2025-09-04 09:30:00'),('New Zealand A tour of South Africa, 2025','3rd Unofficial ODI','South Africa A vs New Zealand A','LC de Villiers Oval','Pretoria','2025-09-03 13:30:00'),('New Zealand A tour of South Africa, 2025','2nd Unofficial ODI','New Zealand A vs South Africa A','LC de Villiers Oval','Pretoria','2025-09-01 13:30:00'),('Czech Republic Women tour Estonia 2025','2nd T20I','Estonia Women vs Czech Republic Women','Estonian National Cricket and Rugby Field','Tallinn','2025-09-06 18:00:00'),('Czech Republic Women tour Estonia 2025','3rd T20I','Czech Republic Women vs Estonia Women','Estonian National Cricket and Rugby Field','Tallinn','2025-09-07 12:30:00'),('Czech Republic Women tour Estonia 2025','1st T20I','Czech Republic Women vs Estonia Women','Estonian National Cricket and Rugby Field','Tallinn','2025-09-06 13:30:00'),('Womens ICC T20 Tri-Series 2025','5th Match','Jersey Women vs Brazil Women','New Farnley Cricket Club','Leeds','2025-09-03 15:00:00'),('Womens ICC T20 Tri-Series 2025','3rd Match','Jersey Women vs Isle of Man Women','New Farnley Cricket Club','Leeds','2025-09-01 20:00:00'),('Womens ICC T20 Tri-Series 2025','6th Match','Brazil Women vs Jersey Women','New Farnley Cricket Club','Leeds','2025-09-03 20:00:00'),('Womens ICC T20 Tri-Series 2025','4th Match','Jersey Women vs Isle of Man Women','New Farnley Cricket Club','Leeds','2025-09-02 15:00:00'),('Womens ICC T20 Tri-Series 2025','2nd Match','Brazil Women vs Isle of Man Women','New Farnley Cricket Club','Leeds','2025-09-01 15:00:00'),('Womens ICC T20 Tri-Series 2025','7th Match','Jersey Women vs Brazil Women','New Farnley Cricket Club','Leeds','2025-09-04 15:00:00'),('Japan Women tour of Fiji 2025','2nd T20I','Japan Women vs Fiji Women','Albert Park 1','Suva','2025-09-06 03:30:00'),('Japan Women tour of Fiji 2025','1st T20I','Japan Women vs Fiji Women','Albert Park 1','Suva','2025-09-05 07:30:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','3rd place play-off','Tanzania Women vs Uganda Women','Namibia Cricket Ground',' Windhoek','2025-09-06 13:00:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','Final','Namibia Women vs Zimbabwe Women','Namibia Cricket Ground',' Windhoek','2025-09-06 17:20:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','5th Place Play-off 1st Semi-Final','Kenya Women vs Nigeria Women','High Performance Oval','Windhoek','2025-09-04 13:00:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','2nd semi-final','Tanzania Women vs Namibia Women','Namibia Cricket Ground',' Windhoek','2025-09-04 17:20:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','10th Match, Group A','Namibia Women vs Sierra Leone Women','High Performance Oval','Windhoek','2025-09-03 13:00:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','5th Place Play-off','Rwanda Women vs Kenya Women','High Performance Oval','Windhoek','2025-09-06 17:20:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','7th Place Play-off','Nigeria Women vs Sierra Leone Women','High Performance Oval','Windhoek','2025-09-06 13:00:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','8th Match, Group B','Rwanda Women vs Uganda Women','High Performance Oval','Windhoek','2025-09-01 17:20:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','5th Place Play-off 2nd Semi-Final','Rwanda Women vs Sierra Leone Women','High Performance Oval','Windhoek','2025-09-04 17:20:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','12th Match, Group A','Nigeria Women vs Zimbabwe Women','High Performance Oval','Windhoek','2025-09-03 17:20:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','11th Match, Group B','Kenya Women vs Uganda Women','Namibia Cricket Ground',' Windhoek','2025-09-03 17:20:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','7th Match, Group A','Nigeria Women vs Namibia Women','Namibia Cricket Ground',' Windhoek','2025-09-01 17:20:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','9th Match, Group B','Tanzania Women vs Rwanda Women','Namibia Cricket Ground',' Windhoek','2025-09-03 13:00:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','1st semi-final','Uganda Women vs Zimbabwe Women','Namibia Cricket Ground',' Windhoek','2025-09-04 13:00:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','5th Match, Group A','Sierra Leone Women vs Zimbabwe Women','Namibia Cricket Ground',' Windhoek','2025-09-01 13:00:00'),('ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','6th Match, Group B','Tanzania Women vs Kenya Women','High Performance Oval','Windhoek','2025-09-01 13:00:00'),('Womens Caribbean Premier League 2025','1st Match','Guyana Amazon Warriors Women vs Trinbago Knight Riders Women','Providence Stadium','Guyana','2025-09-06 23:30:00'),('Womens Caribbean Premier League 2025','2nd Match','Guyana Amazon Warriors Women vs Barbados Royals Women','Providence Stadium','Guyana','2025-09-08 00:30:00');
/*!40000 ALTER TABLE `recent_matches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recent_matches10`
--

DROP TABLE IF EXISTS `recent_matches10`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recent_matches10` (
  `id` int NOT NULL AUTO_INCREMENT,
  `series_name` varchar(255) DEFAULT NULL,
  `match_desc` varchar(100) DEFAULT NULL,
  `teams` varchar(255) DEFAULT NULL,
  `venue` varchar(255) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `match_date` datetime DEFAULT NULL,
  `winner` varchar(100) DEFAULT NULL,
  `victory_margin` int DEFAULT NULL,
  `victory_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recent_matches10`
--

LOCK TABLES `recent_matches10` WRITE;
/*!40000 ALTER TABLE `recent_matches10` DISABLE KEYS */;
INSERT INTO `recent_matches10` VALUES (1,'South Africa tour of England, 2025','3rd ODI','England vs South Africa','The Rose Bowl','Southampton','2025-09-07 15:30:00','ENG',342,'runs'),(2,'South Africa tour of England, 2025','1st ODI','England vs South Africa','Headingley','Leeds','2025-09-02 17:30:00','RSA',7,'wkts'),(3,'South Africa tour of England, 2025','2nd ODI','South Africa vs England','Lord\'s','London','2025-09-04 17:30:00','RSA',5,'runs'),(4,'United Arab Emirates T20I Tri-Series 2025','Final','Pakistan vs Afghanistan','Sharjah Cricket Stadium','Sharjah','2025-09-07 20:30:00','PAK',75,'runs'),(5,'United Arab Emirates T20I Tri-Series 2025','6th Match','Afghanistan vs United Arab Emirates','Sharjah Cricket Stadium','Sharjah','2025-09-05 20:30:00','AFG',4,'runs'),(6,'United Arab Emirates T20I Tri-Series 2025','5th Match','Pakistan vs United Arab Emirates','Sharjah Cricket Stadium','Sharjah','2025-09-04 20:30:00','PAK',31,'runs'),(7,'United Arab Emirates T20I Tri-Series 2025','4th Match','Afghanistan vs Pakistan','Sharjah Cricket Stadium','Sharjah','2025-09-02 20:30:00','AFG',18,'runs'),(9,'ICC Cricket World Cup League Two 2023-27','83rd Match','Namibia vs Canada','Maple Leaf North-West Ground','King City','2025-09-02 20:00:00','NAM',24,'runs'),(10,'ICC Cricket World Cup League Two 2023-27','84th Match','Scotland vs Namibia','Maple Leaf North-West Ground','King City','2025-09-04 20:00:00','SCO',55,'runs'),(12,'Sri Lanka tour of Zimbabwe, 2025','3rd T20I','Zimbabwe vs Sri Lanka','Harare Sports Club','Harare','2025-09-07 17:00:00','SL',8,'wkts'),(13,'Sri Lanka tour of Zimbabwe, 2025','2nd T20I','Sri Lanka vs Zimbabwe','Harare Sports Club','Harare','2025-09-06 17:00:00','ZIM',5,'wkts'),(14,'Sri Lanka tour of Zimbabwe, 2025','1st T20I','Zimbabwe vs Sri Lanka','Harare Sports Club','Harare','2025-09-03 17:00:00','SL',4,'wkts'),(17,'Sweden tour of Isle Of Man 2025','2nd T20I','Isle of Man vs Sweden','Cronkbourne Sports and Social Club Ground','Tromode','2025-09-06 20:00:00','SWE',3,'wkts'),(18,'Sweden tour of Isle Of Man 2025','1st T20I','Isle of Man vs Sweden','Cronkbourne Sports and Social Club Ground','Tromode','2025-09-06 15:30:00','SWE',10,'wkts'),(19,'Caribbean Premier League 2025','25th Match','St Kitts and Nevis Patriots vs Guyana Amazon Warriors','Providence Stadium','Guyana','2025-09-08 05:30:00','SNP',5,'runs'),(20,'Caribbean Premier League 2025','24th Match','Barbados Royals vs Saint Lucia Kings','Kensington Oval','Bridgetown, Barbados','2025-09-07 20:30:00','BR',27,'runs'),(21,'Caribbean Premier League 2025','23rd Match','Trinbago Knight Riders vs Guyana Amazon Warriors','Providence Stadium','Guyana','2025-09-07 04:30:00','GAW',3,'wkts'),(22,'Caribbean Premier League 2025','22nd Match','Barbados Royals vs Antigua and Barbuda Falcons','Kensington Oval','Bridgetown, Barbados','2025-09-06 04:30:00','ABF',4,'wkts'),(23,'Caribbean Premier League 2025','21st Match','Barbados Royals vs Guyana Amazon Warriors','Kensington Oval','Bridgetown, Barbados','2025-09-05 04:30:00','GAW',4,'wkts'),(24,'Caribbean Premier League 2025','20th Match','Trinbago Knight Riders vs Saint Lucia Kings','Brian Lara Stadium','Tarouba, Trinidad','2025-09-04 04:30:00','SLK',7,'wkts'),(25,'T20 Blast 2025','Quarter Final 4','Warwickshire vs Somerset','The Cooper Associates County Ground','Taunton','2025-09-06 23:00:00','SOM',4,'wkts'),(26,'T20 Blast 2025','Quarter Final 1','Northamptonshire vs Surrey','Kennington Oval','London','2025-09-03 23:00:00','NHNTS',7,'runs'),(27,'T20 Blast 2025','Quarter Final 2','Hampshire vs Durham','Riverside Ground','Chester-le-Street','2025-09-05 23:00:00','HAM',26,'runs'),(28,'T20 Blast 2025','Quarter Final 3','Kent vs Lancashire','Emirates Old Trafford','Manchester','2025-09-06 19:00:00','LANCS',3,'wkts'),(29,'Uttar Pradesh Premier League 2025','Qualifier 2','Meerut Mavericks vs Lucknow Falcons','Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium','Lucknow','2025-09-04 19:30:00','MRM',19,'runs'),(30,'Uttar Pradesh Premier League 2025','Qualifier 1','Kashi Rudras vs Meerut Mavericks','Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium','Lucknow','2025-09-03 15:00:00','KRD',5,'runs'),(31,'Uttar Pradesh Premier League 2025','Final','Meerut Mavericks vs Kashi Rudras','Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium','Lucknow','2025-09-06 19:30:00','KRD',8,'wkts'),(32,'Uttar Pradesh Premier League 2025','Eliminator','Lucknow Falcons vs Gaur Gorakhapur Lions','Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium','Lucknow','2025-09-03 19:30:00','LFC',23,'runs'),(33,'Kerala Cricket League 2025','Final','Kochi Blue Tigers vs Aries Kollam Sailors','Greenfield International Stadium','Thiruvananthapuram','2025-09-07 18:45:00','KBT',75,'runs'),(34,'Kerala Cricket League 2025','26th Match','Adani Trivandrum Royals vs Thrissur Titans','Greenfield International Stadium','Thiruvananthapuram','2025-09-02 18:45:00','ATR',17,'runs'),(35,'Kerala Cricket League 2025','Semi Final 2 (1st v 4th)','Kochi Blue Tigers vs Calicut Globstars','Greenfield International Stadium','Thiruvananthapuram','2025-09-05 18:45:00','KBT',15,'runs'),(36,'Kerala Cricket League 2025','Semi Final 1 (2nd v 3rd)','Thrissur Titans vs Aries Kollam Sailors','Greenfield International Stadium','Thiruvananthapuram','2025-09-05 14:30:00','AKS',10,'wkts'),(37,'Kerala Cricket League 2025','30th Match','Calicut Globstars vs Thrissur Titans','Greenfield International Stadium','Thiruvananthapuram','2025-09-04 18:45:00','TST',4,'wkts'),(38,'Kerala Cricket League 2025','29th Match','Alleppey Ripples vs Aries Kollam Sailors','Greenfield International Stadium','Thiruvananthapuram','2025-09-04 14:30:00','AKS',4,'wkts'),(39,'Kerala Cricket League 2025','28th Match','Aries Kollam Sailors vs Kochi Blue Tigers','Greenfield International Stadium','Thiruvananthapuram','2025-09-03 18:45:00','KBT',6,'wkts'),(40,'Kerala Cricket League 2025','27th Match','Adani Trivandrum Royals vs Alleppey Ripples','Greenfield International Stadium','Thiruvananthapuram','2025-09-03 14:30:00','ATR',110,'runs'),(41,'Kerala Cricket League 2025','25th Match','Calicut Globstars vs Kochi Blue Tigers','Greenfield International Stadium','Thiruvananthapuram','2025-09-02 14:30:00','KBT',3,'wkts'),(44,'New Zealand A tour of South Africa, 2025','3rd Unofficial ODI','South Africa A vs New Zealand A','LC de Villiers Oval','Pretoria','2025-09-03 13:30:00','NZA',18,'runs'),(45,'Czech Republic Women tour Estonia 2025','3rd T20I','Czech Republic Women vs Estonia Women','Estonian National Cricket and Rugby Field','Tallinn','2025-09-07 12:30:00','ESTW',7,'wkts'),(46,'Czech Republic Women tour Estonia 2025','2nd T20I','Estonia Women vs Czech Republic Women','Estonian National Cricket and Rugby Field','Tallinn','2025-09-06 18:00:00','ESTW',115,'runs'),(47,'Czech Republic Women tour Estonia 2025','1st T20I','Czech Republic Women vs Estonia Women','Estonian National Cricket and Rugby Field','Tallinn','2025-09-06 13:30:00','ESTW',1,'wkt'),(49,'Womens ICC T20 Tri-Series 2025','6th Match','Brazil Women vs Jersey Women','New Farnley Cricket Club','Leeds','2025-09-03 20:00:00','BRAW',20,'runs'),(50,'Womens ICC T20 Tri-Series 2025','7th Match','Jersey Women vs Brazil Women','New Farnley Cricket Club','Leeds','2025-09-04 15:00:00','BRAW',8,'wkts'),(51,'Womens ICC T20 Tri-Series 2025','4th Match','Jersey Women vs Isle of Man Women','New Farnley Cricket Club','Leeds','2025-09-02 15:00:00','IOMW',7,'wkts'),(52,'Japan Women tour of Fiji 2025','1st T20I','Japan Women vs Fiji Women','Albert Park 1','Suva','2025-09-05 07:30:00','JPNW',23,'runs'),(53,'Japan Women tour of Fiji 2025','2nd T20I','Japan Women vs Fiji Women','Albert Park 1','Suva','2025-09-06 03:30:00','JPNW',104,'runs'),(54,'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','10th Match, Group A','Namibia Women vs Sierra Leone Women','High Performance Oval','Windhoek','2025-09-03 13:00:00','NAMW',152,'runs'),(55,'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','5th Place Play-off 2nd Semi-Final','Rwanda Women vs Sierra Leone Women','High Performance Oval','Windhoek','2025-09-04 17:20:00','RWAW',50,'runs'),(56,'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','Final','Namibia Women vs Zimbabwe Women','Namibia Cricket Ground',' Windhoek','2025-09-06 17:20:00','ZIMW',9,'wkts'),(57,'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','5th Place Play-off 1st Semi-Final','Kenya Women vs Nigeria Women','High Performance Oval','Windhoek','2025-09-04 13:00:00','KENW',7,'runs'),(58,'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','3rd place play-off','Tanzania Women vs Uganda Women','Namibia Cricket Ground',' Windhoek','2025-09-06 13:00:00','TANW',6,'runs'),(59,'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','5th Place Play-off','Rwanda Women vs Kenya Women','High Performance Oval','Windhoek','2025-09-06 17:20:00','RWAW',6,'runs'),(60,'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','11th Match, Group B','Kenya Women vs Uganda Women','Namibia Cricket Ground',' Windhoek','2025-09-03 17:20:00','UGAW',8,'wkts'),(61,'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','7th Place Play-off','Nigeria Women vs Sierra Leone Women','High Performance Oval','Windhoek','2025-09-06 13:00:00','NGAW',85,'runs'),(62,'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','9th Match, Group B','Tanzania Women vs Rwanda Women','Namibia Cricket Ground',' Windhoek','2025-09-03 13:00:00','TANW',18,'runs'),(63,'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','1st semi-final','Uganda Women vs Zimbabwe Women','Namibia Cricket Ground',' Windhoek','2025-09-04 13:00:00','ZIMW',5,'wkts'),(64,'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','2nd semi-final','Tanzania Women vs Namibia Women','Namibia Cricket Ground',' Windhoek','2025-09-04 17:20:00','NAMW',8,'wkts'),(65,'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025','12th Match, Group A','Nigeria Women vs Zimbabwe Women','High Performance Oval','Windhoek','2025-09-03 17:20:00','ZIMW',10,'wkts'),(67,'ICC Womens T20 World Cup East Asia Pacific Qualifier 2025','2nd Match, Group B','Papua New Guinea Women vs Japan Women','Albert Park 2','Suva','2025-09-09 03:00:00','PNGW',45,'runs'),(68,'Womens Caribbean Premier League 2025','2nd Match','Guyana Amazon Warriors Women vs Barbados Royals Women','Providence Stadium','Guyana','2025-09-08 00:30:00','BRW',7,'wkts'),(69,'Womens Caribbean Premier League 2025','1st Match','Guyana Amazon Warriors Women vs Trinbago Knight Riders Women','Providence Stadium','Guyana','2025-09-06 23:30:00','GAWW',6,'runs');
/*!40000 ALTER TABLE `recent_matches10` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `runs_odi`
--

DROP TABLE IF EXISTS `runs_odi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `runs_odi` (
  `id` int NOT NULL,
  `name` text,
  `matches` int DEFAULT NULL,
  `innings` int DEFAULT NULL,
  `runs` int DEFAULT NULL,
  `average` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `runs_odi`
--

LOCK TABLES `runs_odi` WRITE;
/*!40000 ALTER TABLE `runs_odi` DISABLE KEYS */;
INSERT INTO `runs_odi` VALUES (25,'Tendulkar',463,452,18426,44.83),(104,'Sangakkara',404,380,14234,41.99),(1413,'Kohli',302,290,14181,57.88),(38,'R Ponting',375,365,13704,42.04),(102,'S Jayasuriya',445,433,13430,32.36),(101,'Mahela',448,418,12650,33.38),(35,'Inzamam-ul-Haq',378,350,11739,39.53),(213,'Kallis',328,314,11579,44.36),(29,'S Ganguly',311,300,11363,41.02),(576,'Rohit',273,265,11168,48.77),(27,'Dravid',344,318,10889,39.17),(265,'Dhoni',350,297,10773,50.58),(247,'Gayle',301,294,10480,37.83),(240,'B Lara',299,289,10405,40.49),(105,'Dilshan',330,303,10290,39.27),(34,'M Yousuf',288,273,9720,41.72),(36,'A Gilchrist',287,279,9619,35.89),(370,'de Villiers',228,218,9577,53.5),(3864,'M Azharuddin',334,308,9378,36.92),(3531,'A Silva',308,296,9284,34.9),(25,'Tendulkar',463,452,18426,44.83),(104,'Sangakkara',404,380,14234,41.99),(1413,'Kohli',302,290,14181,57.88),(38,'R Ponting',375,365,13704,42.04),(102,'S Jayasuriya',445,433,13430,32.36),(101,'Mahela',448,418,12650,33.38),(35,'Inzamam-ul-Haq',378,350,11739,39.53),(213,'Kallis',328,314,11579,44.36),(29,'S Ganguly',311,300,11363,41.02),(576,'Rohit',273,265,11168,48.77),(27,'Dravid',344,318,10889,39.17),(265,'Dhoni',350,297,10773,50.58),(247,'Gayle',301,294,10480,37.83),(240,'B Lara',299,289,10405,40.49),(105,'Dilshan',330,303,10290,39.27),(34,'M Yousuf',288,273,9720,41.72),(36,'A Gilchrist',287,279,9619,35.89),(370,'de Villiers',228,218,9577,53.5),(3864,'M Azharuddin',334,308,9378,36.92),(3531,'A Silva',308,296,9284,34.9);
/*!40000 ALTER TABLE `runs_odi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `series_2024`
--

DROP TABLE IF EXISTS `series_2024`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `series_2024` (
  `series_name` text,
  `host_country` text,
  `match_type` text,
  `start_date` date DEFAULT NULL,
  `total_matches` int DEFAULT NULL,
  `id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `series_2024`
--

LOCK TABLES `series_2024` WRITE;
/*!40000 ALTER TABLE `series_2024` DISABLE KEYS */;
INSERT INTO `series_2024` VALUES ('Sri Lanka tour of New Zealand, 2024-25','New Zealand','ODI, T20','2024-12-23',8,8553),('Gulf Cricket T20I Championship, 2024','UAE','T20','2024-12-13',16,9297),('Pakistan tour of South Africa, 2024 -25','South Africa','ODI, T20, TEST','2024-12-10',8,8044),('Afghanistan tour of Zimbabwe, 2024-25','Zimbabwe','ODI, T20, TEST','2024-12-09',8,9171),('ICC Mens T20 World Cup Americas Sub Regional Qualifier, 2024','America','T20','2024-12-06',36,9265),('Africa Continental Cup 2024','Africa','T20','2024-12-04',19,9289),('Sri Lanka tour of South Africa, 2024','South Africa','TEST','2024-11-27',2,8058),('Pakistan tour of Zimbabwe, 2024','Zimbabwe','ODI, T20','2024-11-24',6,8494),('England tour of New Zealand, 2024','New Zealand','TEST','2024-11-23',4,7853),('ICC Mens T20 World Cup Africa Sub Regional Qualifier C 2024','Africa','T20','2024-11-23',15,9132),('India tour of Australia, 2024-25','Australia','TEST','2024-11-22',6,7745),('ICC Mens T20 World Cup Asia Qualifier B 2024','Asia','T20','2024-11-19',21,9129),('Bangladesh tour of West Indies, 2024','West Indies','ODI, T20, TEST','2024-11-17',9,8116),('Netherlands tour of Oman, 2024','Oman','T20','2024-11-13',3,9125),('Myanmar tour of Indonesia, 2024','Indonesia','T20','2024-11-12',6,9146),('New Zealand tour of Sri Lanka, 2024','Sri Lanka','ODI, T20','2024-11-09',5,9083),('India tour of South Africa, 2024','South Africa','T20','2024-11-08',4,8404),('Afghanistan v Bangladesh in UAE, 2024','UAE','ODI','2024-11-06',3,9091),('Pakistan tour of Australia, 2024','Australia','ODI, T20','2024-11-03',6,7781),('England tour of West Indies, 2024','West Indies','ODI, T20','2024-10-31',8,8107),('Bahrain in Uganda 2024','Uganda','T20','2024-10-28',2,9157),('South Africa tour of Bangladesh, 2024','Bangladesh','TEST','2024-10-21',2,9033),('ICC Mens T20 World Cup Sub Regional Africa Qualifier Group B, 2024','Africa','T20','2024-10-19',15,9041),('Quadrangular T20I Series in Bhutan, 2024','Bhutan','T20','2024-10-19',10,9025),('Seychelles tour of Kenya, Only T20I','Kenya','T20','2024-10-18',1,9115),('Nepal tour of United States of America 2024','USA','T20','2024-10-17',3,9043),('New Zealand tour of India, 2024','India','TEST','2024-10-16',3,8395),('West Indies tour of Sri Lanka, 2024','Sri Lanka','ODI, T20','2024-10-13',6,9009),('Rwanda tour of Malawi 2024','Malawi','T20','2024-10-09',5,9057),('England tour of Pakistan, 2024','Pakistan','TEST','2024-10-07',3,8497),('Serbia tour of Gibraltar, 2024','Gibraltar','T20','2024-09-30',2,9017),('Namibia T20I Tri-Series 2024','Namibia','T20','2024-09-29',6,8947),('ICC Mens T20 World Cup Sub Regional East Asia-Pacific Qualifier B, 2024','Asia','T20','2024-09-28',12,8598),('Canada T20I Tri-Series 2024','Canada','T20','2024-09-28',6,8955),('Ireland v South Africa in UAE, 2024','UAE','ODI, T20','2024-09-26',5,7981),('T20I Tri-Series in South Korea, 2024','South Korea','T20','2024-09-25',2,8969),('ICC Mens T20 World Cup Africa Sub Regional Qualifier A 2024','Africa','T20','2024-09-21',15,8835),('Bangladesh tour of India, 2024','India','T20, TEST','2024-09-19',5,8393),('New Zealand tour of Sri Lanka, 2024','Sri Lanka','TEST','2024-09-18',2,8818),('Afghanistan v South Africa in UAE, 2024','UAE','ODI','2024-09-18',3,8661),('Australia tour of England, 2024','England','ODI, T20','2024-09-11',8,6794),('Afghanistan v New Zealand in India, 2024','India','TEST','2024-09-09',1,8625),('Australia tour of Scotland, 2024','Scotland','T20','2024-09-04',3,8552),('ICC Mens T20 World Cup Asia Qualifier A 2024','Asia','T20','2024-08-30',21,8764),('Netherlands T20I Tri-Series, 2024','Netherlands','T20','2024-08-23',6,8632),('ICC Mens T20 World Cup Sub Regional Europe Qualifier C, 2024','Europe','T20','2024-08-21',24,8596),('Bangladesh tour of Pakistan, 2024','Pakistan','TEST','2024-08-21',2,8495),('Malaysia T20I Tri Nations Cup, 2024','Malaysia','T20','2024-08-21',7,8686),('ICC Mens T20 World Cup Sub Regional East Asia-Pacific Qualifier A, 2024','Asia','T20','2024-08-17',12,8587),('Sri Lanka tour of England, 2024','England','TEST','2024-08-14',4,6787),('Spain tour of Croatia, 2024','Croatia','T20','2024-08-02',5,8578),('South Africa tour of West Indies, 2024','West Indies','T20, TEST','2024-07-31',6,8238),('India tour of Sri Lanka, 2024','Sri Lanka','ODI, T20','2024-07-27',6,8528),('Zimbabwe tour of Ireland, 2024','Ireland','TEST','2024-07-25',1,7979),('Nigeria tour of Kenya 2024','Kenya','T20','2024-07-12',5,8476),('ICC Mens T20 World Cup Sub Regional Europe Qualifier B, 2024','Europe','T20','2024-07-07',22,8337),('India tour of Zimbabwe, 2024','Zimbabwe','T20','2024-07-06',5,7546),('West Indies tour of England, 2024','England','TEST','2024-07-03',4,6780),('Serbia tour of Slovenia, 2024','Slovenia','T20','2024-06-29',3,8422),('Kenya Quadrangular Cup 2024','Kenya','T20','2024-06-28',20,8382),('Jersey tour of Guernsey, 2024','Guernsey','T20','2024-06-22',3,8413),('Estonia tour of Cyprus 2024','Cyprus','T20','2024-06-17',6,8310),('Jersey tour of Denmark, 2024','Denmark','T20','2024-06-15',3,8260),('Nordic T20I Cup 2024','Nordic','T20','2024-06-14',3,8332),('ICC Mens T20 World Cup Sub Regional Europe Qualifier A, 2024','Europe','T20','2024-06-09',24,8256),('Guernsey tour of Belgium, 2024','Belgium','T20','2024-06-08',4,8294),('ICC Mens T20 World Cup 2024','USA, West Indies','T20','2024-06-01',55,7476),('Belgium tour of Austria, 2024','Austria','T20','2024-05-25',4,8247),('Continental Cup 2024','Romania','T20','2024-05-24',8,8166),('South Africa tour of West Indies, 2024','West Indies','T20','2024-05-23',3,8103),('Pakistan tour of England, 2024','England','T20','2024-05-22',4,6773),('Bangladesh tour of USA, 2024','USA','T20','2024-05-21',3,7700),('Netherlands T20I Tri-Series, 2024','Netherlands','T20','2024-05-18',6,7819),('Pakistan tour of Ireland, 2024','Ireland','T20','2024-05-10',3,7808),('Mdina Cup 2024','Mdina','T20','2024-05-09',7,8080),('Mongolia tour of Japan, 2024','Japan','T20','2024-05-07',7,7896),('Zimbabwe tour of Bangladesh, 2024','Bangladesh','T20','2024-05-03',5,7706),('Thailand tour of Indonesia 2024','Indonesia','T20','2024-05-01',5,8042),('New Zealand tour of Pakistan, 2024','Pakistan','T20','2024-04-18',5,7679),('Jersey tour of Spain, 2024','Spain','T20','2024-04-14',2,7817),('ACC Mens T20I Premier Cup, 2024','Oman','T20','2024-04-12',24,7667),('Central American Cricket Championships 2024','Costa Rica','T20','2024-04-11',5,7900),('Canada tour of USA, 2024','USA','T20','2024-04-07',5,7693),('Namibia tour of Oman, 2024','Oman','T20','2024-04-01',5,7727),('Lesotho tour of Eswatini, 2024','Eswatini','T20','2024-03-29',5,7790),('Mens African Games, 2024','Africa','T20','2024-03-17',16,7672),('Papua New Guinea tour of Malaysia, 2024','Malaysia','T20','2024-03-16',2,7686),('Scotland tour of United Arab Emirates 2024','UAE','T20','2024-03-11',3,7590),('Hong Kong T20I Tri-Series, 2024','Hong Kong','T20','2024-03-10',5,7644),('Hong Kong Friendship Cup, 2024','Hong Kong','T20','2024-03-09',1,7637),('Malaysia Open T20I Championship, 2024','Malaysia','T20','2024-03-05',12,7586),('Sri Lanka tour of Bangladesh, 2024','Bangladesh','ODI, T20, TEST','2024-03-04',8,7534),('Papua New Guinea tour of Oman 2024','Oman','ODI, T20','2024-03-03',5,7623),('Afghanistan v Ireland in UAE, 2024','UAE','ODI, T20, TEST','2024-02-28',7,7485),('Hong Kong tour of Qatar 2024','Qatar','T20','2024-02-27',3,7618),('Nepal T20I Tri-Series 2024','Nepal','T20','2024-02-27',7,7583),('Australia tour of New Zealand, 2024','New Zealand','T20, TEST','2024-02-21',5,6899),('ICC Cricket World Cup League Two 2023-27','Europe','ODI','2024-02-15',85,7572),('East Asia Cup 2024','Asia','T20','2024-02-14',7,7558),('Quadrangular Twenty20 Series in Thailand 2024','Thailand','T20','2024-02-12',8,7579),('Canada tour of Nepal, 2024','Nepal','ODI','2024-02-08',3,7553),('Afghanistan tour of Sri Lanka, 2024','Sri Lanka','ODI, T20, TEST','2024-02-02',7,7481),('South Africa tour of New Zealand, 2024','New Zealand','TEST','2024-01-29',3,6892),('ACC Mens T20I Challenger Cup 2024','Oman','T20','2024-01-27',22,7511),('England tour of India, 2024','India','TEST','2024-01-25',5,6927),('Pakistan tour of New Zealand, 2024','New Zealand','T20','2024-01-12',5,6885),('Afghanistan tour of India, 2024','India','T20','2024-01-11',3,6920),('West Indies tour of Australia, 2024','Australia','ODI, T20, TEST','2024-01-10',9,6297),('Zimbabwe tour of Sri Lanka 2024','Sri Lanka','ODI, T20','2024-01-06',6,7411);
/*!40000 ALTER TABLE `series_2024` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venue`
--

DROP TABLE IF EXISTS `venue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venue` (
  `venue` text,
  `city` text,
  `country` text,
  `capacity` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venue`
--

LOCK TABLES `venue` WRITE;
/*!40000 ALTER TABLE `venue` DISABLE KEYS */;
INSERT INTO `venue` VALUES ('Punjab Cricket Association IS Bindra Stadium','Mohali','India','30000'),('Nehru Stadium','Kochi','India','60000'),('Keenan Stadium','Jamshedpur','India','19000'),('Narendra Modi Stadium','Ahmedabad','India','132000'),('Arun Jaitley Stadium','Delhi','India','48000'),('Newlands','Cape Town','South Africa','25000'),('Bourda','Georgetown, Guyana','West Indies','25000'),('Queen\'s Park Oval','Port of Spain, Trinidad','West Indies','25000'),('Kensington Oval','Bridgetown, Barbados','West Indies','28000'),('Antigua Recreation Ground','St John\'s, Antigua','West Indies','9000'),('Sabina Park','Kingston, Jamaica','West Indies','20000'),('Arnos Vale Ground','Kingstown, St Vincent','West Indies','18000'),('Riverside Ground','Chester-le-Street','England','5000 (17000 for internationals)'),('Sophia Gardens','Cardiff','Wales','5500 (15000 after redevelopment)'),('County Ground','Bristol','England','7000 (15000 ODIs)'),('Durham University Ground','Durham','England','8500'),('Emirates Old Trafford','Manchester','England','19000'),('Headingley','Leeds','England','17000'),('St Lawrence Ground','Canterbury','England','15000'),('Asgiriya Stadium','Kandy','Sri Lanka','10300'),('Harare Sports Club','Harare','Zimbabwe','10000');
/*!40000 ALTER TABLE `venue` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-09 16:14:47
