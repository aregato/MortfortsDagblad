-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Värd: 127.0.0.1
-- Tid vid skapande: 05 maj 2017 kl 15:33
-- Serverversion: 10.1.21-MariaDB
-- PHP-version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databas: `loggilue`
--

-- --------------------------------------------------------

--
-- Tabellstruktur `lectures`
--

CREATE TABLE `lectures` (
  `bokning_id` varchar(50) NOT NULL,
  `program_id` int(50) NOT NULL,
  `datum` int(50) NOT NULL,
  `start_tid` varchar(50) NOT NULL,
  `slut_tid` varchar(50) NOT NULL,
  `dagnamn` varchar(50) NOT NULL,
  `veckonummer` int(50) NOT NULL,
  `moment` text,
  `kurskod` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumpning av Data i tabell `lectures`
--

INSERT INTO `lectures` (`bokning_id`, `program_id`, `datum`, `start_tid`, `slut_tid`, `dagnamn`, `veckonummer`, `moment`, `kurskod`) VALUES
('BokningsId_20160426_000002505', 1, 170420, '14:15', '17:15', 'Tor', 16, 'Omtentamen 2', 'DA153A'),
('BokningsId_20160512_000000479', 1, 170217, '08:15', '12:15', 'Fre', 7, 'Omtentamen 2 1202', 'DA156A'),
('BokningsId_20160512_000000705', 1, 170110, '08:15', '12:00', 'Tis', 2, 'Laboration', 'DA354A'),
('BokningsId_20160512_000000707', 1, 170113, '08:15', '12:00', 'Fre', 2, 'Laboration', 'DA354A'),
('BokningsId_20160608_000000939', 1, 170105, '11:59', '12:00', 'Tor', 1, 'Examinering:Intro övningar, designprojekt', 'DA157A'),
('BokningsId_20160608_000000943', 1, 170113, '17:59', '18:00', 'Fre', 2, 'Dealine: Hemtentamen', 'DA157A'),
('BokningsId_20160608_000000945', 1, 170213, '17:59', '18:00', 'Mån', 7, 'Omexamination 1', 'DA157A'),
('BokningsId_20160608_000000947', 1, 170313, '17:59', '18:00', 'Mån', 11, 'Omexamination 2', 'DA157A'),
('BokningsId_20161031_000000771', 1, 170116, '10:15', '12:00', 'Mån', 3, 'FI: Kursintroduktion', 'DA336A'),
('BokningsId_20161031_000000777', 1, 170117, '13:15', '15:00', 'Tis', 3, 'FII: Information om projektförslag och projekt', 'DA336A'),
('BokningsId_20161031_000000779', 1, 170119, '08:15', '10:00', 'Tor', 3, 'F1: Introduktion till Software Engineering', 'DA336A'),
('BokningsId_20161031_000000787', 1, 170124, '10:15', '12:00', 'Tis', 4, 'F2: Processmodeller', 'DA336A'),
('BokningsId_20161031_000000789', 1, 170124, '13:15', '15:00', 'Tis', 4, 'F3: Agila processer', 'DA336A'),
('BokningsId_20161031_000000881', 1, 170130, '10:15', '12:00', 'Mån', 5, 'F4: Krav 1', 'DA336A'),
('BokningsId_20161031_000000885', 1, 170131, '13:15', '15:00', 'Tis', 5, 'F5: Krav 2', 'DA336A'),
('BokningsId_20161031_000000887', 1, 170206, '08:15', '10:00', 'Mån', 6, 'F6: Arkitektur', 'DA336A'),
('BokningsId_20161031_000000889', 1, 170206, '10:15', '12:00', 'Mån', 6, 'Presentation projektförslag OBLIGATORISKT för presenterande grupper, presentationsschema via kursplats, del av provkod 1504 Presenterande grupper: Grupper från Spel: 50-65, 80-83', 'DA336A'),
('BokningsId_20161031_000000891', 1, 170207, '13:15', '15:00', 'Tis', 6, 'F7: Design och metrics', 'DA336A'),
('BokningsId_20161031_000000893', 1, 170207, '15:15', '17:00', 'Tis', 6, 'Presentation projektförslag OBLIGATORISKT för presenterande grupper, presentationsschema via kursplats, del av provkod 1504 Presenterande grupper: Grupper från IA och några blandgrupper med App/Sys/IA: 1-7, 10-21, 79', 'DA336A'),
('BokningsId_20161031_000000895', 1, 170214, '08:15', '10:00', 'Tis', 7, 'Presentation projektförslag OBLIGATORISKT för presenterande grupper, presentationsschema via kursplats, del av provkod 1504 Presenterande grupper: Grupper från App och Sys med främst Android/app-förslag: 30-45, 84-85', 'DA336A'),
('BokningsId_20161031_000000899', 1, 170214, '13:15', '15:00', 'Tis', 7, 'F9: Processförbättring, kvalitetshantering, riskhantering', 'DA336A'),
('BokningsId_20161031_000000901', 1, 170214, '15:15', '17:00', 'Tis', 7, 'Presentation projektförslag OBLIGATORISKT för presenterande grupper, presentationsschema via kursplats, del av provkod 1504 Presenterande grupper: Grupper från App och Sys: 70-78', 'DA336A'),
('BokningsId_20161031_000000911', 1, 170217, '13:15', '15:00', 'Fre', 7, 'F10: Test 1', 'DA336A'),
('BokningsId_20161031_000000913', 1, 170220, '08:15', '10:00', 'Mån', 8, 'F11: Test 2', 'DA336A'),
('BokningsId_20161031_000000917', 1, 170223, '10:15', '12:00', 'Tor', 8, 'F12: Test 3', 'DA336A'),
('BokningsId_20161031_000000923', 1, 170228, '08:15', '10:00', 'Tis', 9, 'Frågor inför tentamen', 'DA336A'),
('BokningsId_20161031_000000927', 1, 170228, '10:15', '12:00', 'Tis', 9, 'Kick-off projekt! Presentation av projektgrupper', 'DA336A'),
('BokningsId_20161031_000000945', 1, 170302, '08:15', '13:15', 'Tor', 9, 'Tentamen provkod 1501', 'DA336A'),
('BokningsId_20161031_000000953', 1, 170306, '08:15', '12:00', 'Mån', 10, 'Tentamensrättning och genomgång OBLIGATORISK NÄRVARO FÖR GODKÄND TENTAMEN, del av provkod 1501', 'DA336A'),
('BokningsId_20161031_000000955', 1, 170307, '13:15', '17:00', 'Tis', 10, 'FP1: ProjektprocessFP2: Gruppdynamik', 'DA336A'),
('BokningsId_20161031_000000963', 1, 170612, '08:15', '13:15', 'Mån', 24, 'Tentamen provkod 1501, omtillfälle 1', 'DA336A'),
('BokningsId_20161031_000000971', 1, 170613, '13:15', '17:00', 'Tis', 24, 'Tentamensrättning och genomgång, omtillfälle 1, OBLIGATORISK NÄRVARO FÖR GODKÄND TENTAMEN, del av provkod 1501', 'DA336A'),
('BokningsId_20161031_000000983', 1, 170126, '10:15', '12:00', 'Tor', 4, 'Seminarium F1-3', 'DA336A'),
('BokningsId_20161031_000000991', 1, 170202, '08:15', '10:00', 'Tor', 5, 'Seminarium F4-5', 'DA336A'),
('BokningsId_20161031_000000997', 1, 170209, '10:15', '12:00', 'Tor', 6, 'Seminarium F6-7', 'DA336A'),
('BokningsId_20161031_000001001', 1, 170216, '08:15', '10:00', 'Tor', 7, 'Seminarium F8-9', 'DA336A'),
('BokningsId_20161031_000001007', 1, 170224, '13:15', '15:00', 'Fre', 8, 'Seminarium F10-12', 'DA336A'),
('BokningsId_20161031_000001011', 1, 170328, '10:15', '12:00', 'Tis', 13, 'Föreläsning 1', 'DA127A'),
('BokningsId_20161031_000001013', 1, 170329, '13:15', '15:00', 'Ons', 13, 'Föreläsning 2', 'DA127A'),
('BokningsId_20161031_000001015', 1, 170404, '10:15', '12:00', 'Tis', 14, 'Föreläsning 3', 'DA127A'),
('BokningsId_20161031_000001017', 1, 170405, '13:15', '15:00', 'Ons', 14, 'Föreläsning 4', 'DA127A'),
('BokningsId_20161031_000001019', 1, 170418, '10:15', '12:00', 'Tis', 16, 'Föreläsning 5', 'DA127A'),
('BokningsId_20161031_000001021', 1, 170421, '10:15', '12:00', 'Fre', 16, 'Föreläsning 6', 'DA127A'),
('BokningsId_20161031_000001023', 1, 170425, '10:15', '12:00', 'Tis', 17, 'Föreläsning 7', 'DA127A'),
('BokningsId_20161031_000001025', 1, 170428, '10:15', '12:00', 'Fre', 17, 'Föreläsning 8', 'DA127A'),
('BokningsId_20161031_000001027', 1, 170502, '10:15', '12:00', 'Tis', 18, 'Föreläsning 9', 'DA127A'),
('BokningsId_20161031_000001029', 1, 170505, '10:15', '12:00', 'Fre', 18, 'Föreläsning 10', 'DA127A'),
('BokningsId_20161031_000001039', 1, 170509, '10:15', '12:00', 'Tis', 19, 'Föreläsning 11', 'DA127A'),
('BokningsId_20161031_000001041', 1, 170516, '10:15', '12:00', 'Tis', 20, 'Föreläsning 12', 'DA127A'),
('BokningsId_20161031_000001043', 1, 170517, '13:15', '17:00', 'Ons', 20, 'Föreläsning 13', 'DA127A'),
('BokningsId_20161031_000001045', 1, 170524, '14:15', '18:15', 'Ons', 21, 'Tentamen', 'DA127A'),
('BokningsId_20161101_000000941', 1, 170126, '08:15', '10:00', 'Tor', 4, 'Handledning projektförslag, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000000949', 1, 170127, '10:15', '12:00', 'Fre', 4, 'Handledning projektförslag, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000000955', 1, 170307, '08:15', '12:00', 'Tis', 10, 'Verktygslabbar, gruppschema via kursplats', 'DA336A'),
('BokningsId_20161101_000000959', 1, 170308, '13:15', '17:00', 'Ons', 10, 'Verktygslabbar, gruppschema via kursplats', 'DA336A'),
('BokningsId_20161101_000000961', 1, 170309, '08:15', '12:00', 'Tor', 10, 'Verktygslabbar, gruppschema via kursplats', 'DA336A'),
('BokningsId_20161101_000000989', 1, 170313, '08:15', '12:00', 'Mån', 11, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000000991', 1, 170314, '13:15', '17:00', 'Tis', 11, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000000993', 1, 170314, '15:15', '17:00', 'Tis', 11, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000000995', 1, 170315, '13:15', '17:00', 'Ons', 11, 'Handledning projektgrupper, gruppschema via handledare Farid: sal A0304 Kristian: sal A0305', 'DA336A'),
('BokningsId_20161101_000000997', 1, 170316, '08:15', '12:00', 'Tor', 11, 'Specialisttider 8.15-11.00Kristina i NI:A0502: Frågor om dokumentation och testningRolf i NI:A0513: Frågor om Andriod eller annan Java-programmering och kodstruktur för detta', 'DA336A'),
('BokningsId_20161101_000000999', 1, 170317, '08:15', '12:00', 'Fre', 11, 'Specialisttider 8.15-11.00Anton i NI:A0513: Frågor relaterade till webbprogrammering, HTML och CSS samt användbarhet.', 'DA336A'),
('BokningsId_20161101_000001001', 1, 170320, '08:15', '12:00', 'Mån', 12, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001003', 1, 170322, '13:15', '17:00', 'Ons', 12, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001005', 1, 170323, '08:15', '12:00', 'Tor', 12, 'Specialisttider 8-11', 'DA336A'),
('BokningsId_20161101_000001007', 1, 170324, '08:15', '12:00', 'Fre', 12, 'Specialisttider 8-11', 'DA336A'),
('BokningsId_20161101_000001009', 1, 170321, '15:15', '17:00', 'Tis', 12, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001011', 1, 170321, '13:15', '17:00', 'Tis', 12, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001013', 1, 170324, '12:59', '13:00', 'Fre', 12, 'Deadline inlämning Sprint 1', 'DA336A'),
('BokningsId_20161101_000001067', 1, 170328, '13:15', '15:00', 'Tis', 13, 'Retrospekt 1, gruppschema via handledaredare', 'DA336A'),
('BokningsId_20161101_000001073', 1, 170328, '13:15', '17:00', 'Tis', 13, 'Retrospekt 1, gruppschema via handledaredare', 'DA336A'),
('BokningsId_20161101_000001079', 1, 170328, '15:15', '17:00', 'Tis', 13, 'Retrospekt 1, gruppschema via handledaredare', 'DA336A'),
('BokningsId_20161101_000001083', 1, 170329, '15:15', '17:00', 'Ons', 13, 'Retrospekt 1, gruppschema via handledaredare', 'DA336A'),
('BokningsId_20161101_000001085', 1, 170331, '10:15', '15:00', 'Fre', 13, 'Retrospekt1 Grupp 1-6', 'DA336A'),
('BokningsId_20161101_000001089', 1, 170412, '13:15', '17:00', 'Ons', 15, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001091', 1, 170419, '08:15', '12:00', 'Ons', 16, 'Retrospekt 2, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001093', 1, 170424, '08:15', '12:00', 'Mån', 17, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001095', 1, 170504, '13:15', '17:00', 'Tor', 18, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001097', 1, 170406, '08:15', '12:00', 'Tor', 14, 'Specialisttider 8-11', 'DA336A'),
('BokningsId_20161101_000001099', 1, 170413, '08:15', '12:00', 'Tor', 15, 'Specialisttider 8-11', 'DA336A'),
('BokningsId_20161101_000001101', 1, 170420, '08:15', '12:00', 'Tor', 16, 'Specialisttider 8-11', 'DA336A'),
('BokningsId_20161101_000001103', 1, 170427, '08:15', '12:00', 'Tor', 17, 'Specialisttider 8-11', 'DA336A'),
('BokningsId_20161101_000001105', 1, 170504, '08:15', '12:00', 'Tor', 18, 'Specialisttider 8-11', 'DA336A'),
('BokningsId_20161101_000001107', 1, 170404, '13:15', '17:00', 'Tis', 14, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001109', 1, 170406, '13:15', '17:00', 'Tor', 14, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001111', 1, 170404, '13:15', '15:00', 'Tis', 14, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001113', 1, 170404, '15:15', '17:00', 'Tis', 14, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001115', 1, 170411, '15:15', '17:00', 'Tis', 15, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001117', 1, 170411, '13:15', '17:00', 'Tis', 15, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001119', 1, 170411, '13:15', '15:00', 'Tis', 15, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001121', 1, 170418, '13:15', '15:00', 'Tis', 16, 'Retrospekt 2, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001123', 1, 170418, '15:15', '17:00', 'Tis', 16, 'Retrospekt 2, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001125', 1, 170418, '13:15', '17:00', 'Tis', 16, 'Retrospekt 2, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001127', 1, 170425, '13:15', '17:00', 'Tis', 17, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001129', 1, 170425, '13:15', '15:00', 'Tis', 17, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001131', 1, 170425, '15:15', '17:00', 'Tis', 17, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001133', 1, 170502, '13:15', '17:00', 'Tis', 18, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001135', 1, 170502, '13:15', '15:00', 'Tis', 18, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001137', 1, 170502, '08:15', '10:00', 'Tis', 18, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001157', 1, 170413, '12:59', '13:00', 'Tor', 15, 'Deadline inlämning Sprint 2', 'DA336A'),
('BokningsId_20161101_000001159', 1, 170504, '12:59', '13:00', 'Tor', 18, 'Deadline inlämning Sprint 3', 'DA336A'),
('BokningsId_20161101_000001161', 1, 170510, '08:15', '12:00', 'Ons', 19, 'Retrospekt 3, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001163', 1, 170511, '08:15', '12:00', 'Tor', 19, 'Specialisttider 8-11', 'DA336A'),
('BokningsId_20161101_000001165', 1, 170510, '13:15', '17:00', 'Ons', 19, 'Retrospekt 3, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001167', 1, 170509, '13:15', '15:00', 'Tis', 19, 'Retrospekt 3, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001169', 1, 170509, '13:15', '17:00', 'Tis', 19, 'Retrospekt 3, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001171', 1, 170516, '13:15', '17:00', 'Tis', 20, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001173', 1, 170518, '08:15', '12:00', 'Tor', 20, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001175', 1, 170518, '08:15', '12:00', 'Tor', 20, 'Specialisttider 8-11', 'DA336A'),
('BokningsId_20161101_000001177', 1, 170518, '13:15', '17:00', 'Tor', 20, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001179', 1, 170522, '08:15', '12:00', 'Mån', 21, 'Specialisttider 8-11', 'DA336A'),
('BokningsId_20161101_000001183', 1, 170523, '08:15', '17:00', 'Tis', 21, 'Utställningsdag, OBLIGATORISK NÄRVARO, del av provkod 1504. Öppna ytor våning 5 och 6', 'DA336A'),
('BokningsId_20161101_000001187', 1, 170526, '12:59', '13:00', 'Fre', 21, 'Deadline Slutinlämning projekt, del av provkod 1502, 1503', 'DA336A'),
('BokningsId_20161101_000001191', 1, 170529, '15:15', '17:00', 'Mån', 22, 'Retrospekt 4, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001195', 1, 170530, '13:15', '17:00', 'Tis', 22, 'Retrospekt 4, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001199', 1, 170531, '08:15', '12:00', 'Ons', 22, 'Retrospekt 4, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001201', 1, 170601, '08:15', '12:00', 'Tor', 22, 'Retrospekt 4, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001205', 1, 170601, '13:15', '17:00', 'Tor', 22, 'Retrospekt 4, gruppschema via handledare', 'DA336A'),
('BokningsId_20161101_000001207', 1, 170602, '12:59', '13:00', 'Fre', 22, 'Deadline inlämning av reflektionsrapport, del av provkod 1502', 'DA336A'),
('BokningsId_20161101_000001251', 1, 170331, '08:15', '10:00', 'Fre', 13, 'Övning 1', 'DA127A'),
('BokningsId_20161101_000001261', 1, 170407, '10:15', '12:00', 'Fre', 14, 'Övning 2', 'DA127A'),
('BokningsId_20161101_000001271', 1, 170419, '13:15', '17:00', 'Ons', 16, 'Datorövning 1', 'DA127A'),
('BokningsId_20161101_000001279', 1, 170426, '13:15', '17:00', 'Ons', 17, 'Datorövning 2', 'DA127A'),
('BokningsId_20161101_000001281', 1, 170503, '13:15', '17:00', 'Ons', 18, 'Datorövning 3', 'DA127A'),
('BokningsId_20161101_000001283', 1, 170519, '08:15', '12:00', 'Fre', 20, 'Datorövning 4', 'DA127A'),
('BokningsId_20161101_000001291', 1, 170510, '13:15', '15:00', 'Ons', 19, 'Övning 3', 'DA127A'),
('BokningsId_20161125_000000145', 1, 170116, '08:15', '10:00', 'Mån', 3, 'Kursintroduktion', 'DA155A'),
('BokningsId_20161125_000000147', 1, 170119, '13:15', '15:00', 'Tor', 3, 'Digital materialitet', 'DA155A'),
('BokningsId_20161125_000000149', 1, 170125, '13:15', '15:00', 'Ons', 4, 'Designmetodik', 'DA155A'),
('BokningsId_20161125_000000151', 1, 170130, '13:15', '15:00', 'Mån', 5, 'Perception', 'DA155A'),
('BokningsId_20161125_000000153', 1, 170202, '13:15', '15:00', 'Tor', 5, 'Utvärdering av IT-system och artefakter', 'DA155A'),
('BokningsId_20161125_000000155', 1, 170208, '08:15', '12:00', 'Ons', 6, 'Workshop med CheckUP- Projektarbete inleds. Kl. 09.00-12.00', 'DA155A'),
('BokningsId_20161125_000000157', 1, 170213, '13:15', '15:00', 'Mån', 7, 'Minne och Kognition', 'DA155A'),
('BokningsId_20161125_000000159', 1, 170216, '13:15', '15:00', 'Tor', 7, 'Human Computer Interaction', 'DA155A'),
('BokningsId_20161125_000000161', 1, 170222, '10:15', '12:00', 'Ons', 8, 'Handledning kan bokas', 'DA155A'),
('BokningsId_20161125_000000165', 1, 170227, '13:15', '15:00', 'Mån', 9, 'Möte med CheckUP', 'DA155A'),
('BokningsId_20161125_000000169', 1, 170308, '10:15', '12:00', 'Ons', 10, 'Digitala plattformar', 'DA155A'),
('BokningsId_20161125_000000171', 1, 170309, '13:15', '15:00', 'Tor', 10, 'Workshop', 'DA155A'),
('BokningsId_20161125_000000175', 1, 170313, '13:15', '15:00', 'Mån', 11, 'Workshop', 'DA155A'),
('BokningsId_20161125_000000177', 1, 170315, '10:15', '12:00', 'Ons', 11, 'Frågestund', 'DA155A'),
('BokningsId_20161125_000000179', 1, 170320, '13:15', '17:00', 'Mån', 12, 'Presentationer av projektarbete', 'DA155A'),
('BokningsId_20161125_000000181', 1, 170323, '13:15', '17:00', 'Tor', 12, 'Presentationer av projektarbete', 'DA155A'),
('BokningsId_20161209_000000447', 1, 170112, '13:15', '15:00', 'Tor', 2, 'Omtillfälle 2 Etik-seminarium INGEN ANMÄLD TILL TILLFÄLLET', 'DA153A'),
('BokningsId_20161213_000000995', 1, 170329, '08:15', '12:00', 'Ons', 13, 'Retrospekt 1, gruppschema via handledaredare', 'DA336A'),
('BokningsId_20161213_000000997', 1, 170328, '13:15', '17:00', 'Tis', 13, 'Retrospekt 1, gruppschema via handledaredare', 'DA336A'),
('BokningsId_20161213_000001001', 1, 170404, '13:15', '17:00', 'Tis', 14, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161213_000001005', 1, 170403, '10:15', '12:00', 'Mån', 14, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161213_000001009', 1, 170418, '13:15', '17:00', 'Tis', 16, 'Retrospekt 2, gruppschema via handledare', 'DA336A'),
('BokningsId_20161213_000001011', 1, 170418, '08:15', '10:00', 'Tis', 16, 'Retrospekt 2, gruppschema via handledare', 'DA336A'),
('BokningsId_20161213_000001013', 1, 170425, '13:15', '17:00', 'Tis', 17, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161213_000001015', 1, 170424, '10:15', '12:00', 'Mån', 17, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161213_000001017', 1, 170502, '13:15', '17:00', 'Tis', 18, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161213_000001019', 1, 170502, '08:15', '10:00', 'Tis', 18, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161213_000001025', 1, 170509, '13:15', '17:00', 'Tis', 19, 'Retrospekt 3, gruppschema via handledare', 'DA336A'),
('BokningsId_20161213_000001027', 1, 170509, '08:15', '10:00', 'Tis', 19, 'Retrospekt 3, gruppschema via handledare', 'DA336A'),
('BokningsId_20161213_000001029', 1, 170519, '13:15', '17:00', 'Fre', 20, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20161213_000001053', 1, 170329, '23:54', '23:55', 'Ons', 13, 'Deadline inlämning kamratgranskning omtillfälle 2', 'DA153A'),
('BokningsId_20161213_000001055', 1, 170409, '23:54', '23:55', 'Sön', 14, 'Deadline Slutinlämning Skrivuppgift omtillfälle 2', 'DA153A'),
('BokningsId_20161213_000001057', 1, 170403, '08:15', '10:00', 'Mån', 14, 'Kamratgranskning Skrivuppgift: Omtillfälle 2', 'DA153A'),
('BokningsId_20161213_000001063', 1, 170413, '13:15', '17:00', 'Tor', 15, 'Återkopplingsmöten Skrivuppgift omtillfälle 2 bokning via doodle-länk i svar på inlämning', 'DA153A'),
('BokningsId_20161213_000001349', 1, 170214, '10:15', '12:00', 'Tis', 7, 'F8: Implementation, Configuration Management och underhåll', 'DA336A'),
('BokningsId_20161215_000000379', 1, 170104, '13:15', '15:00', 'Ons', 1, 'Föreläsning: Programeringsparadigmer med Python', 'DA354A'),
('BokningsId_20161215_000000381', 1, 170105, '13:15', '17:00', 'Tor', 1, 'Laboration: Extra', 'DA354A'),
('BokningsId_20161222_000000841', 1, 170110, '12:15', '13:00', 'Tis', 2, 'Tentavisning omtentamen 1', 'DA153A'),
('BokningsId_20170111_000000539', 1, 170122, '23:54', '23:55', 'Sön', 3, 'Deadline för inlämning av anmälan av projektförslagsgrupp. Del av provkod 1503 och 1504', 'DA336A'),
('BokningsId_20170111_000000541', 1, 170201, '23:54', '23:55', 'Ons', 5, 'Deadline inlämning av projektförslag och presentationsbilder. Del av provkod 1503', 'DA336A'),
('BokningsId_20170111_000000543', 1, 170216, '23:54', '23:55', 'Tor', 7, 'Deadline för inlämning av projektanmälan. Del av provkod 1502, 1503, 1504', 'DA336A'),
('BokningsId_20170112_000000259', 1, 170131, '15:15', '17:00', 'Tis', 5, 'Frågestund logik (inför omtillfälle)', 'DA153A'),
('BokningsId_20170112_000000261', 1, 170206, '08:15', '10:00', 'Mån', 6, 'Logik omtillfälle 2', 'DA153A'),
('BokningsId_20170124_000000145', 1, 170127, '15:15', '18:00', 'Fre', 4, 'Handledning projektförslag, gruppschema via handledare', 'DA336A'),
('BokningsId_20170125_000000429', 1, 170127, '08:15', '12:00', 'Fre', 4, 'Handledning projektförslag, gruppschema via handledare', 'DA336A'),
('BokningsId_20170126_000000231', 1, 170329, '15:00', '21:00', 'Ons', 13, 'IA-dag', 'TS - D'),
('BokningsId_20170126_000000385', 1, 170127, '08:15', '12:00', 'Fre', 4, 'Handledning projektförslag, gruppschema via handledare', 'DA336A'),
('BokningsId_20170210_000000197', 1, 170215, '08:15', '10:00', 'Ons', 7, 'Seminarium F6-7', 'DA336A'),
('BokningsId_20170309_000000207', 1, 170314, '13:15', '17:00', 'Tis', 11, 'Tentavisning', 'DA336A'),
('BokningsId_20170314_000000905', 1, 170320, '10:15', '12:00', 'Mån', 12, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20170314_000000907', 1, 170517, '10:15', '12:00', 'Ons', 20, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20170323_000000417', 1, 170502, '15:15', '17:00', 'Tis', 18, 'Föreläsning om att skapa affischer till utställning', 'DA336A'),
('BokningsId_20170323_000000575', 1, 170329, '15:15', '17:00', 'Ons', 13, 'Retrospekt 1, gruppschema via handledaredare', 'DA336A'),
('BokningsId_20170323_000000577', 1, 170328, '13:15', '15:00', 'Tis', 13, 'Retrospekt 1, gruppschema via handledaredare', 'DA336A'),
('BokningsId_20170330_000000261', 1, 170330, '08:15', '12:00', 'Tor', 13, 'Specialisttider 8-11', 'DA336A'),
('BokningsId_20170405_000000249', 1, 170516, '13:15', '17:00', 'Tis', 20, 'Handledning projektgrupper, gruppschema via handledare', 'DA336A'),
('BokningsId_20170407_000000267', 1, 170425, '08:15', '10:00', 'Tis', 17, 'Gästföreläsning: \"Testning in Agile Environments\" av Aneta Poniszewska-Mara&#324;da', 'DA336A'),
('BokningsId_20170420_000000171', 1, 170421, '08:15', '10:00', 'Fre', 16, 'Retrospekt 2', 'DA336A'),
('BokningsId_20170425_000001549', 1, 170608, '08:15', '12:00', 'Tor', 23, 'Hjälp inför omtenta', 'DA336A');

-- --------------------------------------------------------

--
-- Tabellstruktur `notes`
--

CREATE TABLE `notes` (
  `note_id` int(50) NOT NULL,
  `bokning_id` varchar(50) NOT NULL,
  `user_id` int(50) NOT NULL,
  `points` int(100) NOT NULL DEFAULT '0',
  `text` text NOT NULL,
  `rubrik` varchar(50) NOT NULL,
  `path` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumpning av Data i tabell `notes`
--

INSERT INTO `notes` (`note_id`, `bokning_id`, `user_id`, `points`, `text`, `rubrik`, `path`) VALUES
(1, 'BokningsId_20161031_000001027', 50, 0, 'Hejehhjehje\r\n', 'Heeeej', ''),
(2, 'BokningsId_20161101_000001137', 50, 1, 'asddsaad', 'Aasdasd', ''),
(3, 'BokningsId_20161101_000001137', 50, 0, 'asdasdsadljkhaskdljasldhhaskljdhalskd', 'adsfgrwewasd', ''),
(4, 'BokningsId_20161101_000001137', 50, 20, 'adsadsasdsa', 'dasfsdfs', ''),
(5, 'BokningsId_20161101_000001137', 50, 5, 'Heeej', 'Hejhej', ''),
(6, 'BokningsId_20161101_000001137', 50, 0, 'adyiguhijklöä\r\n', 'tfgyhujklö', ''),
(7, 'BokningsId_20161101_000001137', 50, 0, 'ewrthyjyuytyrterty', 'wqerty77564', ''),
(8, 'BokningsId_20161101_000001137', 50, 0, '12345678', 'aadsads', ''),
(9, 'BokningsId_20161101_000001137', 50, 0, 'YEEESSS', 'HHHHEEEEJ', ''),
(14, 'BokningsId_20161213_000001019', 50, 0, 'Japp', 'Test1', 'Designdokument.docx'),
(15, 'BokningsId_20161213_000001019', 50, 0, 'Yep', 'Test2', 'Kravdokument.docx'),
(16, 'BokningsId_20161213_000001019', 50, 0, 'Såhär vi rullar', 'Test3', 'Projektplan.pdf'),
(17, 'BokningsId_20161213_000001019', 50, 4, 'Upvota denna kommentaren era nååbs', 'Test4', 'VoVdokument.pdf');

-- --------------------------------------------------------

--
-- Tabellstruktur `programs`
--

CREATE TABLE `programs` (
  `program_id` int(11) NOT NULL,
  `program_name` varchar(65) NOT NULL,
  `program_code` varchar(65) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumpning av Data i tabell `programs`
--

INSERT INTO `programs` (`program_id`, `program_name`, `program_code`) VALUES
(1, 'Informationsarkitekt HT16', 'TGIAA16h'),
(2, 'Informationsarkitekt HT15', 'TGIAA15h');

-- --------------------------------------------------------

--
-- Tabellstruktur `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(150) NOT NULL,
  `program_id` int(11) DEFAULT NULL,
  `points` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumpning av Data i tabell `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `program_id`, `points`) VALUES
(35, 'imeal', 'imreal@gmail.com', '$2b$12$KLSmWfbqWQUehnCmPOwyn.pnv6TLzvByn97sGSRNuYP', 2, 0),
(38, 'Hannes123', 'u@gmail.com', '$2b$12$aKK.XFfQtkRA8tFrbBohqOZPNwti1X0GZAhW5j8h.nSQjJk3QWXnC', 1, 0),
(39, 'hannes', 'Fuser@gmail.com', '$2b$12$SK.5eJZ5l.xtH4NNeWi8juknt4GL.wxF1s4PlOqp7WPpL9wTfS6Ca', 1, 0),
(41, 'testUser', 'test@gmail.com', '$2b$12$WBXMcR9YUof251YxK7gZhO9hydk0LmArB2mlwSw6WTeqACyLyHiba', 2, 0),
(42, 'lol', 'lol@gmail.com', '$2b$12$njRyIe9ul8ZHrFeY8F/Loebg6qABzkhgeGLbfsLDtkMCkncMV/.PO', 1, 0),
(46, 'asdqwe123', 'asd@gmail.com', '$2b$12$9qVU/WdnmWA6FvTKSjvfl.4N29ytZ9uwBVk2QL3ZBfhxEAaF8JK9S', 1, 0),
(48, 'Jan', 'j@gmail.com', '$2b$12$ey7fYUdJDzWxeUi90QL41u6SgAM/pIBNu03do8jQ8mjcGF1y1Yzhy', 1, 0),
(49, 'Alfred', 'a@gmail.com', '$2b$12$./KyfMRVBTxDWVJR1dYiN.yAOuVdeXs3rlB5Xaz71UemplgqHU8CK', 1, 0),
(50, 'david', 'davidhurtig95@hotmail.com', '$2b$12$vBydg.A7hopNUL3zs9GO9uf3bQ5/9XRhd0iHE2cz6xCKo4fYRFWbC', 1, 27);

--
-- Index för dumpade tabeller
--

--
-- Index för tabell `lectures`
--
ALTER TABLE `lectures`
  ADD PRIMARY KEY (`bokning_id`),
  ADD KEY `program_id->program_id` (`program_id`);

--
-- Index för tabell `notes`
--
ALTER TABLE `notes`
  ADD PRIMARY KEY (`note_id`),
  ADD KEY `bokning->Lectures` (`bokning_id`),
  ADD KEY `user->user_id` (`user_id`);

--
-- Index för tabell `programs`
--
ALTER TABLE `programs`
  ADD PRIMARY KEY (`program_id`);

--
-- Index för tabell `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `fk` (`program_id`);

--
-- AUTO_INCREMENT för dumpade tabeller
--

--
-- AUTO_INCREMENT för tabell `notes`
--
ALTER TABLE `notes`
  MODIFY `note_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT för tabell `programs`
--
ALTER TABLE `programs`
  MODIFY `program_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT för tabell `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
--
-- Restriktioner för dumpade tabeller
--

--
-- Restriktioner för tabell `lectures`
--
ALTER TABLE `lectures`
  ADD CONSTRAINT `prog_id` FOREIGN KEY (`program_id`) REFERENCES `programs` (`program_id`);

--
-- Restriktioner för tabell `notes`
--
ALTER TABLE `notes`
  ADD CONSTRAINT `bokning->Lectures` FOREIGN KEY (`bokning_id`) REFERENCES `lectures` (`bokning_id`),
  ADD CONSTRAINT `user->user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Restriktioner för tabell `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`program_id`) REFERENCES `programs` (`program_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
