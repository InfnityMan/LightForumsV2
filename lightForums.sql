-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 29, 2024 at 03:07 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lightForums`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `id` int(11) NOT NULL,
  `userName` varchar(60) NOT NULL,
  `userPassword` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`id`, `userName`, `userPassword`) VALUES
(2, 'guid3r', 'timetohelp'),
(5, 'weirdPerson', 'jojojojojo'),
(6, 'TrueSupporter', 'al;ksjdfa;'),
(8, 'applejack175', 'grapesarethebestfruit'),
(9, 'crazyTiger427', 'asfdasdfassdf'),
(10, 'helplessperson', 'asdjfkasdfasdf'),
(11, 'asdf', 'asdfasdfasdf');

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `threadID` int(11) DEFAULT NULL,
  `author` varchar(60) DEFAULT NULL,
  `creationDate` datetime DEFAULT current_timestamp(),
  `content` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`id`, `threadID`, `author`, `creationDate`, `content`) VALUES
(1, 10, 'guid3r', '2024-03-14 11:29:00', 'Don\'t worry, you can go to your teachers and I am sure they will be willing to help'),
(2, 10, 'guid3r', '2024-08-26 19:55:48', 'askdflasjd;lf');

-- --------------------------------------------------------

--
-- Table structure for table `threads`
--

CREATE TABLE `threads` (
  `id` int(11) NOT NULL,
  `author` varchar(60) DEFAULT NULL,
  `creationDate` datetime NOT NULL DEFAULT current_timestamp(),
  `content` longtext NOT NULL,
  `title` longtext NOT NULL,
  `comment_count` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `threads`
--

INSERT INTO `threads` (`id`, `author`, `creationDate`, `content`, `title`, `comment_count`) VALUES
(4, 'weirdPerson', '2024-03-13 21:15:33', 'I am doing horrible in studies, and I feel like I will just always fail', 'I struggle in school and fear I won\'t succeed', 0),
(5, 'TrueSupporter', '2024-03-13 21:31:05', '\"You are braver than you believe, stronger than you seem, and smarter than you think.\" - A.A. Milne', 'Inspirational Quote', 0),
(7, 'applejack175', '2024-03-13 23:37:51', 'I can\'t sleep at night. When I wake up, my mind is swarmed with thoughts, with stress. Someone please help me!', 'This anxiety is killing me!!!', 0),
(9, 'crazyTiger427', '2024-03-13 23:46:39', 'With sports and all the homework popping up, I don\'t think I can handle everything anymore. I need a break. Anyone have any ideas?', 'Sometimes, everyone needs a break!', 0),
(10, 'helplessperson', '2024-03-14 11:28:24', 'I do horrible in academics and everyone says I fail. I am constantly in stress.', 'I am accademically terrible', 2),
(11, 'guid3r', '2024-08-26 19:55:56', 'asdf', 'sadf', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `threads`
--
ALTER TABLE `threads`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `threads`
--
ALTER TABLE `threads`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
