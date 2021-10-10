-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 10, 2019 at 04:26 PM
-- Server version: 5.1.36
-- PHP Version: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `speedex`
--
CREATE DATABASE `speedex` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `speedex`;

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

CREATE TABLE IF NOT EXISTS `adminlogin` (
  `aid` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`aid`, `password`) VALUES
('admin@gmail.com', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE IF NOT EXISTS `city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cityname` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`id`, `cityname`) VALUES
(1, 'varanasi'),
(2, 'LUCKNOW'),
(4, 'LUKNOW NR'),
(5, 'kanpur'),
(6, 'Mirjapur'),
(7, 'Allahabad'),
(8, 'Chandauli'),
(9, 'khusinagar'),
(10, 'Punjab'),
(11, 'ambla');

-- --------------------------------------------------------

--
-- Table structure for table `complain`
--

CREATE TABLE IF NOT EXISTS `complain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `mobileno` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `refno` int(11) NOT NULL,
  `ctext` varchar(600) NOT NULL,
  `cdate` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `complain`
--

INSERT INTO `complain` (`id`, `name`, `mobileno`, `email`, `refno`, `ctext`, `cdate`) VALUES
(3, 'Arbind ', '986876346', 'a@gmail.com', 12890, 'no complain', '2019-08-06 21:28:19'),
(4, 'Vinod Kumar', '7890045789', 'v@gmail.com', 2345, 'weldone for complain\r\n\r\n\r\n\r\n', '2019-08-10 07:09:35');

-- --------------------------------------------------------

--
-- Table structure for table `consignment`
--

CREATE TABLE IF NOT EXISTS `consignment` (
  `refno` int(11) NOT NULL,
  `sname` varchar(100) NOT NULL,
  `saddress` varchar(300) NOT NULL,
  `scontact` varchar(15) NOT NULL,
  `rname` varchar(100) NOT NULL,
  `raddress` varchar(300) NOT NULL,
  `rcontact` varchar(15) NOT NULL,
  `source` varchar(100) NOT NULL,
  `curcity` varchar(100) NOT NULL,
  `desination` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  `postdate` varchar(50) NOT NULL,
  PRIMARY KEY (`refno`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `consignment`
--

INSERT INTO `consignment` (`refno`, `sname`, `saddress`, `scontact`, `rname`, `raddress`, `rcontact`, `source`, `curcity`, `desination`, `status`, `postdate`) VALUES
(123, 'prakash yadav', 'azamgarh', '5742578754', 'PRAVEEN', 'lucknow', '245788', 'varanasi', 'LUCKNOW', 'varanasi', 'Delivered', '2019-08-07 16:26:58'),
(2345, 'Ritesh Kumar', 'Kanpur', '78095435', '7646', 'Gorkhpur', '7890002337', 'varanasi', 'LUCKNOW', 'LUKNOW NR', 'Delivered', '2019-08-10 07:13:29');

-- --------------------------------------------------------

--
-- Table structure for table `contactus`
--

CREATE TABLE IF NOT EXISTS `contactus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `mobileno` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(300) NOT NULL,
  `purpose` varchar(500) NOT NULL,
  `curdate` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `contactus`
--

INSERT INTO `contactus` (`id`, `name`, `mobileno`, `email`, `address`, `purpose`, `curdate`) VALUES
(1, 'PRAVIN YADAV', '4565763536474', 'praveenyadav9838@gmail.com', 'VIJAYIPURA KONIA  VARANASI\r\nVIJAYIPURA KONIA VARANASI\r\nVIJAYIPURA KONIA VARANASI', 'i am not sure', '2019-08-03 09:18:17'),
(4, 'monu', '235678909876', 'm@gmail.com', 'kanpur', 'i cghj\r\n', '2019-08-08 15:34:02'),
(5, 'Aman Yadav', '8906478889', 'ab@gmail.com', 'surhbhjss', 'cvghjjkjkk\r\n', '2019-08-08 19:00:58'),
(6, 'Servesh Yadav', '789043256', 's@gmail.com', 'Azamgarh', 'hii hiii hii', '2019-08-09 07:13:26'),
(7, 'Ritesh Kumar', '90998754567', 'ra@gmail.com', 'Azamagarh', 'hii Welcome', '2019-08-10 07:07:57');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE IF NOT EXISTS `register` (
  `name` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `mobileno` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(300) NOT NULL,
  `pinno` varchar(10) NOT NULL,
  `regdate` varchar(50) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`name`, `gender`, `mobileno`, `email`, `address`, `pinno`, `regdate`) VALUES
('ashok', 'male', '42562288', 's@gmail.com', 'lucknow', '4567', '2019-08-08 11:19:32'),
('Amit kumar', 'male', '90067879575677', 'ra@gmail.com', 'VARANASI', '56546', '2019-08-09 18:42:29'),
('Rohit ', 'male', '12344444', 'b@gmail.com', 'dyuyjfjgkuhgjfyj', '22344', '2019-08-01 12:25:31'),
('Jhon', 'male', '98989797', 'praveenyadav9838@gmail.com', 'VIJAYIPURA KONIA  VARANASI\r\nVIJAYIPURA KONIA VARANASI\r\nVIJAYIPURA KONIA VARANASI', '221001', '2019-08-08 11:18:11'),
('kl Yadav', 'male', '314168986', 'kl@gmail.com', 'ygehasihaejuehd', '12345', '2019-08-04 10:09:30');
