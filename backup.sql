-- MySQL dump 10.13  Distrib 8.0.37, for Win64 (x86_64)
--
-- Host: localhost    Database: cricbuzz_livestats
-- ------------------------------------------------------
-- Server version	8.0.37

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
/*!40000 ALTER TABLE `crud_player_info` ENABLE KEYS */;
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

-- Dump completed on 2025-09-08 20:02:49
