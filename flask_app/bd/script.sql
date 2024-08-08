-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema repartes
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `repartes` ;

-- -----------------------------------------------------
-- Schema repartes
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `repartes` DEFAULT CHARACTER SET utf8 ;
USE `repartes` ;

-- -----------------------------------------------------
-- Table `repartes`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `repartes`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(100) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(250) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `repartes`.`vehicle`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `repartes`.`vehicle` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `plate` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  `version` VARCHAR(45) NULL,
  `displacement` VARCHAR(45) NULL,
  `year` VARCHAR(45) NULL,
  `vin` VARCHAR(250) NULL,
  `motor_number` VARCHAR(250) NULL,
  `brand_name` VARCHAR(45) NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_vehicle_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_vehicle_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `repartes`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
