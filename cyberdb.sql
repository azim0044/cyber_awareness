-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 28, 2024 at 03:32 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cyberdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `admin_username` varchar(255) DEFAULT NULL,
  `admin_password` varchar(255) DEFAULT NULL,
  `admin_name` varchar(255) DEFAULT NULL,
  `admin_email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_username`, `admin_password`, `admin_name`, `admin_email`) VALUES
(1, 'admin', '$2a$12$/4xDnBuF0HVvYxRGF6K2DOmTMT5gs7wfvRWxx5.g9zqHcjqism1P.', 'Muhamad Admin bin Abdul Admin', 'admin@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `answer`
--

CREATE TABLE `answer` (
  `answer_id` int(11) NOT NULL,
  `question_id` int(11) DEFAULT NULL,
  `question1_answer1_t` text DEFAULT NULL,
  `question1_answer2_f` text DEFAULT NULL,
  `question1_answer3_f` text DEFAULT NULL,
  `question1_answer4_f` text DEFAULT NULL,
  `question2_answer1_t` text DEFAULT NULL,
  `question2_answer2_f` text DEFAULT NULL,
  `question2_answer3_f` text DEFAULT NULL,
  `question2_answer4_f` text DEFAULT NULL,
  `question3_answer1_t` text DEFAULT NULL,
  `question3_answer2_f` text DEFAULT NULL,
  `question3_answer3_f` text DEFAULT NULL,
  `question3_answer4_f` text DEFAULT NULL,
  `question4_answer1_t` text DEFAULT NULL,
  `question4_answer2_f` text DEFAULT NULL,
  `question4_answer3_f` text DEFAULT NULL,
  `question4_answer4_f` text DEFAULT NULL,
  `question5_answer1_t` text DEFAULT NULL,
  `question5_answer2_f` text DEFAULT NULL,
  `question5_answer3_f` text DEFAULT NULL,
  `question5_answer4_f` text DEFAULT NULL,
  `question6_answer1_t` text DEFAULT NULL,
  `question6_answer2_f` text DEFAULT NULL,
  `question6_answer3_f` text DEFAULT NULL,
  `question6_answer4_f` text DEFAULT NULL,
  `question7_answer1_t` text DEFAULT NULL,
  `question8_answer1_t` text DEFAULT NULL,
  `question9_answer1_t` text DEFAULT NULL,
  `question10_answer1_t` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE `question` (
  `question_id` int(11) NOT NULL,
  `topic_id` int(11) DEFAULT NULL,
  `question_1` text DEFAULT NULL,
  `question_2` text DEFAULT NULL,
  `question_3` text DEFAULT NULL,
  `question_4` text DEFAULT NULL,
  `question_5` text DEFAULT NULL,
  `question_6` text DEFAULT NULL,
  `question_7` text DEFAULT NULL,
  `question_8` text DEFAULT NULL,
  `question_9` text DEFAULT NULL,
  `question_10` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `quiz_history`
--

CREATE TABLE `quiz_history` (
  `history_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `topic_id` int(11) DEFAULT NULL,
  `time_complete` varchar(15) DEFAULT NULL,
  `date_complete` date DEFAULT NULL,
  `quiz_status` varchar(15) DEFAULT NULL,
  `retake` varchar(8) DEFAULT 'false',
  `retake_taken` int(11) DEFAULT 1,
  `score1` int(11) DEFAULT NULL,
  `score2` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `topic`
--

CREATE TABLE `topic` (
  `topic_id` int(11) NOT NULL,
  `topic_title` varchar(255) DEFAULT NULL,
  `topic_description` text DEFAULT NULL,
  `topic_video` varchar(255) DEFAULT NULL,
  `topic_upload_date` date DEFAULT NULL,
  `topic_register_by` int(11) DEFAULT NULL,
  `topic_lesson` text DEFAULT NULL,
  `popup_question` text DEFAULT NULL,
  `popup_answer` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `user_username` varchar(255) DEFAULT NULL,
  `user_password` varchar(255) DEFAULT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL,
  `account_status` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `user_username`, `user_password`, `user_name`, `user_email`, `account_status`) VALUES
(1, 'azim', '$2a$12$/4xDnBuF0HVvYxRGF6K2DOmTMT5gs7wfvRWxx5.g9zqHcjqism1P.', 'Muhamad Azim bin Mohd Fauzi', 'azim@gmail.com', 1),
(2, 'aa', '$2b$12$0I.NxHcvsJFHv0CjHhbaIeOlUlOKHTTK3KAHa5hzzxFpkIY682VAm', 'sdfnsd', 'aa@dd', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `answer`
--
ALTER TABLE `answer`
  ADD PRIMARY KEY (`answer_id`),
  ADD KEY `question_id` (`question_id`);

--
-- Indexes for table `question`
--
ALTER TABLE `question`
  ADD PRIMARY KEY (`question_id`),
  ADD KEY `topic_id` (`topic_id`);

--
-- Indexes for table `quiz_history`
--
ALTER TABLE `quiz_history`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `topic_id` (`topic_id`);

--
-- Indexes for table `topic`
--
ALTER TABLE `topic`
  ADD PRIMARY KEY (`topic_id`),
  ADD KEY `topic_register_by` (`topic_register_by`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `answer`
--
ALTER TABLE `answer`
  MODIFY `answer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
  MODIFY `question_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `quiz_history`
--
ALTER TABLE `quiz_history`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `topic`
--
ALTER TABLE `topic`
  MODIFY `topic_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `answer`
--
ALTER TABLE `answer`
  ADD CONSTRAINT `answer_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`question_id`);

--
-- Constraints for table `question`
--
ALTER TABLE `question`
  ADD CONSTRAINT `question_ibfk_1` FOREIGN KEY (`topic_id`) REFERENCES `topic` (`topic_id`);

--
-- Constraints for table `quiz_history`
--
ALTER TABLE `quiz_history`
  ADD CONSTRAINT `quiz_history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `quiz_history_ibfk_2` FOREIGN KEY (`topic_id`) REFERENCES `topic` (`topic_id`);

--
-- Constraints for table `topic`
--
ALTER TABLE `topic`
  ADD CONSTRAINT `topic_ibfk_1` FOREIGN KEY (`topic_register_by`) REFERENCES `admin` (`admin_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
