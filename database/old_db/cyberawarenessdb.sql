-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 21, 2023 at 06:49 PM
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
-- Database: `cyberawarenessdb`
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
(1, 'admin', '$2b$12$DFlVD2gMIBvbEm6YO2STmujWpEvflFkcwUEAQxf.G4VphoH3f4wJG', 'Muhamad Azim bin Mohd Fauzi', 'admin@gmail.com');

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
  `question7_answer2_f` text DEFAULT NULL,
  `question7_answer3_f` text DEFAULT NULL,
  `question7_answer4_f` text DEFAULT NULL,
  `question8_answer1_t` text DEFAULT NULL,
  `question8_answer2_f` text DEFAULT NULL,
  `question8_answer3_f` text DEFAULT NULL,
  `question8_answer4_f` text DEFAULT NULL,
  `question9_answer1_t` text DEFAULT NULL,
  `question9_answer2_f` text DEFAULT NULL,
  `question9_answer3_f` text DEFAULT NULL,
  `question9_answer4_f` text DEFAULT NULL,
  `question10_answer1_t` text DEFAULT NULL,
  `question10_answer2_f` text DEFAULT NULL,
  `question10_answer3_f` text DEFAULT NULL,
  `question10_answer4_f` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `answer`
--

INSERT INTO `answer` (`answer_id`, `question_id`, `question1_answer1_t`, `question1_answer2_f`, `question1_answer3_f`, `question1_answer4_f`, `question2_answer1_t`, `question2_answer2_f`, `question2_answer3_f`, `question2_answer4_f`, `question3_answer1_t`, `question3_answer2_f`, `question3_answer3_f`, `question3_answer4_f`, `question4_answer1_t`, `question4_answer2_f`, `question4_answer3_f`, `question4_answer4_f`, `question5_answer1_t`, `question5_answer2_f`, `question5_answer3_f`, `question5_answer4_f`, `question6_answer1_t`, `question6_answer2_f`, `question6_answer3_f`, `question6_answer4_f`, `question7_answer1_t`, `question7_answer2_f`, `question7_answer3_f`, `question7_answer4_f`, `question8_answer1_t`, `question8_answer2_f`, `question8_answer3_f`, `question8_answer4_f`, `question9_answer1_t`, `question9_answer2_f`, `question9_answer3_f`, `question9_answer4_f`, `question10_answer1_t`, `question10_answer2_f`, `question10_answer3_f`, `question10_answer4_f`) VALUES
(1, 1, 'All of it', 'A minimum of 12 characters', 'At least one special character', 'At least one number digit', ' #[Ih4v3Th3Mos7P0W3rfuLlpAsSw0Rd3veRmAd3]', 'ABC-123', 'password1', 'PASSWORD1', 'Implementing account lockout policies.', 'Disabling all password-related security features.', 'Allowing users to have weak passwords', 'Allowing users to have weak passwords', 'Compromised user accounts and unauthorized access.', 'Increased network bandwidth usage.', 'Improved system performance.', 'Improved system performance.', 'Educated users are less likely to fall for social engineering tactics.', 'Users can manually stop password spraying attacks.', 'Password spraying attacks don\'t target user accounts', 'Password spraying attacks don\'t target user accounts', 'MFA adds an extra layer of security, making it more difficult for attackers to gain unauthorized access.', 'MFA has no impact on password spraying attacks.', 'MFA increases the success rate of password spraying attacks.', 'MFA has no impact on password spraying attacks.', 'Brute force attacks focus on a single user account, while password spraying targets multiple accounts.', 'Password spraying uses complex algorithms to guess passwords.', 'Password spraying uses complex algorithms to guess passwords.', 'Password spraying only works on accounts with weak passwords.', 'Gain unauthorized access to a specific user account.', 'Extract sensitive information from the target system.', 'Distribute malware across the network.', 'Conduct denial-of-service attacks on the server.', 'Password spraying targets multiple user accounts simultaneously.', 'Brute force attacks use precomputed tables for password guessing.', 'Password spraying relies on a single, well-known password for all accounts.', ' Brute force attacks focus on exploiting system vulnerabilities rather than user credentials.', 'Implementing two-factor authentication (2FA).', 'Enforcing password complexity requirements.', 'Blocking all external network traffic.', 'Using default credentials for all user accounts.');

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

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`question_id`, `topic_id`, `question_1`, `question_2`, `question_3`, `question_4`, `question_5`, `question_6`, `question_7`, `question_8`, `question_9`, `question_10`) VALUES
(1, 1, 'A strong password should contain ?', 'Wich of the following passwords is least likely to appear in a passwordbank of commonly used passwords?', 'What is one way to defend against password spraying attacks?', '.What is the main risk associated with successful password spraying attacks?', 'Why is user education important in preventing password spraying attacks?', 'What is the role of multi-factor authentication (MFA) in mitigating password spraying attacks?', 'How does password spraying differ from brute force attacks?', 'What is the primary goal of password spraying attacks?', 'How does password spraying differ from brute force attacks?', 'What is a common mitigation strategy against password spraying attacks?');

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
  `topic_register_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `topic`
--

INSERT INTO `topic` (`topic_id`, `topic_title`, `topic_description`, `topic_video`, `topic_upload_date`, `topic_register_by`) VALUES
(1, 'Password Spraying', 'Password spraying is a technique used by hackers to guess users’ passwords by attempting to log into their accounts with commonly used passwords, such as,”password1″. A secure method for password creation is to use a combination of letters, numbers and special characters. It’s also important to remember to not use the same password for multiple accounts.', '6139d9bf-5f5b-490f-aeca-adcfc60c7124.mp4', '2023-12-21', 1);

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
(1, 'azim', '$2b$12$qe9rTHHbwbVSP0AdWYualO8Qcq2pnLCxlfqLdTZOEA8VSt4mxa0ni', 'Muhamad Azim bin Mohd Fauzi', 'azimm0044@gmail.com', 1),
(6, 'somi', '$2b$12$C1xfxUJiE7GtQgUpqA61COJhvHHdimilJO96INjbKgagAiDX.CfeC', 'Muhamad Haikal bin Mustaza', 'somi@gmail.com', 1);

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
-- AUTO_INCREMENT for table `topic`
--
ALTER TABLE `topic`
  MODIFY `topic_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

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
-- Constraints for table `topic`
--
ALTER TABLE `topic`
  ADD CONSTRAINT `topic_ibfk_1` FOREIGN KEY (`topic_register_by`) REFERENCES `admin` (`admin_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
