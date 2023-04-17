-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-04-2023 a las 10:16:34
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `shelf`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `article`
--

CREATE TABLE `article` (
  `id` int(11) NOT NULL,
  `authors` varchar(250) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `title` varchar(1000) DEFAULT NULL,
  `journal` varchar(250) DEFAULT NULL,
  `issue` int(250) DEFAULT NULL,
  `place` varchar(250) DEFAULT NULL,
  `doi` varchar(1000) DEFAULT NULL,
  `genreId` int(11) DEFAULT NULL,
  `pdf` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `article`
--

INSERT INTO `article` (`id`, `authors`, `year`, `title`, `journal`, `issue`, `place`, `doi`, `genreId`, `pdf`) VALUES
(9, '1234sazxdc', 123, '123', '123', 123, '123', '123', 2, '123'),
(11, '123', 123, '123', '123', 123, '123', '123', 1, '123'),
(55, 'Maria Hernandez', 2020, 'La vida en el campo', 'El Pais', 6, 'Madrid', '9876543', 1, 'field_life.pdf'),
(56, 'Juan Perez', 2019, 'Historias de la ciudad', 'La Vanguardia', 3, 'Barcelona', '1357986', 3, 'city_stories.pdf'),
(57, 'Jose Torres', 2018, 'El pincipe pequeñito', 'ABC', 12, 'Santiago de Compostela', '1234579', 2, 'archive.pdf'),
(58, 'Maria Hernandez', 2020, 'La vida en el campo', 'El Pais', 6, 'Madrid', '9876543', 1, 'field_life.pdf'),
(59, 'Juan Perez', 2019, 'Historias de la ciudad', 'La Vanguardia', 3, 'Barcelona', '1357986', 3, 'city_stories.pdf'),
(60, 'Jose Torres', 2018, 'El pincipe pequeñito', 'ABC', 12, 'Santiago de Compostela', '1234579', 2, 'archive.pdf'),
(61, 'Maria Hernandez', 2020, 'La vida en el campo', 'El Pais', 6, 'Madrid', '9876543', 1, 'field_life.pdf'),
(62, 'Juan Perez', 2019, 'Historias de la ciudad', 'La Vanguardia', 3, 'Barcelona', '1357986', 3, 'city_stories.pdf'),
(63, 'Jose Torres', 2018, 'El pincipe pequeñito', 'ABC', 12, 'Santiago de Compostela', '1234579', 2, 'archive.pdf'),
(64, 'Maria Hernandez', 2020, 'La vida en el campo', 'El Pais', 6, 'Madrid', '9876543', 1, 'field_life.pdf'),
(65, 'Juan Perez', 2019, 'Historias de la ciudad', 'La Vanguardia', 3, 'Barcelona', '1357986', 3, 'city_stories.pdf'),
(66, 'Jose Torres', 2018, 'El pincipe pequeñito', 'ABC', 12, 'Santiago de Compostela', '1234579', 2, 'archive.pdf'),
(67, 'Maria Hernandez', 2020, 'La vida en el campo', 'El Pais', 6, 'Madrid', '9876543', 1, 'field_life.pdf'),
(68, 'Juan Perez', 2019, 'Historias de la ciudad', 'La Vanguardia', 3, 'Barcelona', '1357986', 3, 'city_stories.pdf'),
(69, 'Jose Torres', 2018, 'El pincipe pequeñito', 'ABC', 12, 'Santiago de Compostela', '1234579', 2, 'archive.pdf'),
(70, 'Maria Hernandez', 2020, 'La vida en el campo', 'El Pais', 6, 'Madrid', '9876543', 1, 'field_life.pdf'),
(71, 'Juan Perez', 2019, 'Historias de la ciudad', 'La Vanguardia', 3, 'Barcelona', '1357986', 3, 'city_stories.pdf'),
(72, 'Jose Torres', 2018, 'El pincipe pequeñito', 'ABC', 12, 'Santiago de Compostela', '1234579', 2, 'archive.pdf'),
(73, 'Maria Hernandez', 2020, 'La vida en el campo', 'El Pais', 6, 'Madrid', '9876543', 1, 'field_life.pdf'),
(74, 'Juan Perez', 2019, 'Historias de la ciudad', 'La Vanguardia', 3, 'Barcelona', '1357986', 3, 'city_stories.pdf'),
(75, 'Jose Torres', 2018, 'El pincipe pequeñito', 'ABC', 12, 'Santiago de Compostela', '1234579', 2, 'archive.pdf'),
(76, 'Maria Hernandez', 2020, 'La vida en el campo', 'El Pais', 6, 'Madrid', '9876543', 1, 'field_life.pdf'),
(77, 'Juan Perez', 2019, 'Historias de la ciudad', 'La Vanguardia', 3, 'Barcelona', '1357986', 3, 'city_stories.pdf'),
(78, 'Jose Torres', 2018, 'El pincipe pequeñito', 'ABC', 12, 'Santiago de Compostela', '1234579', 2, 'archive.pdf'),
(79, 'Maria Hernandez', 2020, 'La vida en el campo', 'El Pais', 6, 'Madrid', '9876543', 1, 'field_life.pdf'),
(80, 'Juan Perez', 2019, 'Historias de la ciudad', 'La Vanguardia', 3, 'Barcelona', '1357986', 3, 'city_stories.pdf'),
(81, 'Jose Torres', 2018, 'El pincipe pequeñito', 'ABC', 12, 'Santiago de Compostela', '1234579', 2, 'archive.pdf'),
(82, 'Maria Hernandez', 2020, 'La vida en el campo', 'El Pais', 6, 'Madrid', '9876543', 1, 'field_life.pdf'),
(83, 'Juan Perez', 2019, 'Historias de la ciudad', 'La Vanguardia', 3, 'Barcelona', '1357986', 3, 'city_stories.pdf'),
(84, 'Jose Torres', 2018, 'El pincipe pequeñito', 'ABC', 12, 'Santiago de Compostela', '1234579', 2, 'archive.pdf'),
(85, '456', 456, '456', '456', 456, '456', '456', 7, '456'),
(86, '678', 678, '678', '678', 678, '678', '678', 2, ''),
(87, '234', 234, '324', '', 234, '', '234', 2, '234'),
(88, '234', 324, '234', '324', 234, '234', '234', 1, '234'),
(90, '123', 123, '123', '123123', 123123, '123', '123', 3, '123'),
(91, '123', 123, '123', '123123', 123123, '123', '123', 3, '123'),
(92, '123', 123, '123', '123123', 123123, '123', '123', 3, '123');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genre`
--

CREATE TABLE `genre` (
  `id` int(11) NOT NULL,
  `genre` varchar(250) NOT NULL,
  `color` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `genre`
--

INSERT INTO `genre` (`id`, `genre`, `color`) VALUES
(1, 'Photography', 'black'),
(2, 'Egyptology', 'yellow'),
(3, 'cosas mariposas', 'red'),
(7, 'Nombre del género', 'Color del género'),
(9, 'asd', 'asd'),
(10, 'dasf', 'sdf'),
(13, 'sdf', 'sdf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `user` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `user`, `email`, `password`) VALUES
(5, 'example_user', 'example_email', 'example_password'),
(7, 'jose', 'jose@jhg', '12345'),
(8, 'pepe', 'joseasd@jhg', '12345'),
(10, 'pepasdasde', 'josasdeasd@jhg', '123asd45'),
(11, 'a21cesargm', 'guerramendezcesar@gmail.com', 'abc123.');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `article`
--
ALTER TABLE `article`
  ADD PRIMARY KEY (`id`),
  ADD KEY `genre_fk` (`genreId`);

--
-- Indices de la tabla `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `user` (`user`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `article`
--
ALTER TABLE `article`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;

--
-- AUTO_INCREMENT de la tabla `genre`
--
ALTER TABLE `genre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `article`
--
ALTER TABLE `article`
  ADD CONSTRAINT `genre_fk` FOREIGN KEY (`genreId`) REFERENCES `genre` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
