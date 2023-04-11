-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 11-04-2023 a las 09:45:23
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `article`
--

INSERT INTO `article` (`id`, `authors`, `year`, `title`, `journal`, `issue`, `place`, `doi`, `genreId`, `pdf`) VALUES
(3, 'Nombre del autorasd', 2022, 'Título del artículo', 'Nombre de la revista', 1, 'Lugar de publicación', '12345', 1, 'ruta/al/archivo.pdf'),
(4, 'Nombre del autorerfg', 2022, 'Título del artículo', 'Nombre de la revista', 1, 'Lugar de publicación', '12345', 1, 'ruta/al/archivo.pdf'),
(9, '123', 123, '123', '123', 123, '123', '123', 2, '123');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genre`
--

CREATE TABLE `genre` (
  `id` int(11) NOT NULL,
  `genre` varchar(250) NOT NULL,
  `color` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `genre`
--

INSERT INTO `genre` (`id`, `genre`, `color`) VALUES
(1, 'Photography', 'black'),
(2, 'Egyptology', 'yellow'),
(3, 'cosas mariposas', 'red'),
(7, 'Nombre del género', 'Color del género'),
(9, 'asd', 'asd'),
(10, 'dasf', 'sdf');

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
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `article`
--
ALTER TABLE `article`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `genre`
--
ALTER TABLE `genre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

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
