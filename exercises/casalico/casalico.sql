-- MySQL Script generated by MySQL Workbench
-- Wed Mar  9 11:46:38 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema casalico
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema casalico
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `casalico` DEFAULT CHARACTER SET latin1 ;
-- -----------------------------------------------------
-- Schema new_schema1
-- -----------------------------------------------------
USE `casalico` ;

-- -----------------------------------------------------
-- Table `casalico`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `casalico`.`user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `user_type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `realtor id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `casalico`.`property`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `casalico`.`property` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `owner_id` INT(11) NOT NULL,
  `number_of_rooms` INT NOT NULL,
  `number_of_bathrooms` INT(11) NOT NULL,
  `sqft` INT NOT NULL,
  `lote` VARCHAR(45) NOT NULL,
  `price` INT NOT NULL,
  `street` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `zip_code` INT NULL,
  `create_date` DATETIME NULL,
  `realtor_id` INT NULL,
  `user_type` VARCHAR(45) NOT NULL,
  `year_of_construction` INT NULL,
  `status` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idnew_table_UNIQUE` (`id` ASC),
  INDEX `fk_property_person_idx` (`owner_id` ASC),
  INDEX `fk_property_person_realtor_idx` (`realtor_id` ASC),
  CONSTRAINT `fk_property_person`
    FOREIGN KEY (`owner_id`)
    REFERENCES `casalico`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_property_person_realtor`
    FOREIGN KEY (`realtor_id`)
    REFERENCES `casalico`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `casalico`.`sales_record`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `casalico`.`sales_record` (
  `property_id` INT(11) NULL,
  `realtor_id` INT(11) NULL DEFAULT NULL,
  `sale_price` VARCHAR(45) NULL,
  `month_of_sale` VARCHAR(45) NULL DEFAULT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  INDEX `realtor_idx` (`realtor_id` ASC),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  CONSTRAINT `fk_property_sales_record`
    FOREIGN KEY (`property_id`)
    REFERENCES `casalico`.`property` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_realtor_sales_record`
    FOREIGN KEY (`realtor_id`)
    REFERENCES `casalico`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `casalico`.`photos_property`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `casalico`.`photos_property` (
  `property_id` INT(11) NOT NULL,
  `image_path` VARCHAR(2000) NULL DEFAULT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  INDEX `id_idx` (`property_id` ASC),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  CONSTRAINT `fk_property_photos_property`
    FOREIGN KEY (`property_id`)
    REFERENCES `casalico`.`property` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
