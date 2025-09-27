-- Data Cleaning Project

select * from layoffs;

-- Step to follow Data Cleaing
 -- 1) Remove Dublicates
 -- 2) Standardize the Data
 -- 3) Null Values or Blank values
 -- 4) Remove any columns
 
 
 -- Raw Data Copy to past into Another Table
 create table layoffs_staging
 like layoffs; 
 
 -- Just Select the Column of table 
 select * from layoffs;
 
 -- Now Copying Data from layoffs to layoffs
 insert layoffs_staging
 select * from layoffs;
 
 select * from layoffs_staging;
 -- NOw We have Copy data from raw to layoffs_staging
 
  -- 1) Remove Dublicates
  select * ,
  ROW_NUMBER() OVER(
  PARTITION BY company,industry,total_laid_off, percentage_laid_off, `date`
  ) as row_num
  from layoffs_staging;
  
  -- to get the dublicate data is here
  WITH CTE_dublicates As
  (
  select * ,
  ROW_NUMBER() OVER(PARTITION BY company,location,industry,total_laid_off, percentage_laid_off, `date`,stage,country,funds_raised_millions) as row_num
  from layoffs_staging
  )
  select * from CTE_dublicates
  where row_num > 1;
  
  select * from layoffs_staging
  where company = 'hibob';
  
  -- now delete Dublicate Rows but here we get error The target table CTE_dublicates of the DELETE is not updatable
WITH CTE_dublicates As
  (
  select * ,
  ROW_NUMBER() OVER(PARTITION BY company,location,industry,total_laid_off, percentage_laid_off, `date`,stage,country,funds_raised_millions) as row_num
  from layoffs_staging
  )
  delete from CTE_dublicates
  where row_num > 1;
  
  -- SOLVE this by Add new Column row_num so we create new table layoffs_staging2
  create table layoffs_staging2
  (
   `company` TEXT,
  `location` TEXT,
  `industry` TEXT,
  `total_laid_off` INT DEFAULT NULL,
  `percentage_laid_off` TEXT,
  `date` TEXT,
  `stage` TEXT,
  `country` TEXT,
  `funds_raised_millions` INT DEFAULT NULL,
  `row_num` INT
  )
  
select * from layoffs_staging2;

insert into layoffs_staging2
select * ,
ROW_NUMBER() OVER(PARTITION BY company,location,industry,total_laid_off, percentage_laid_off, `date`,stage,country,funds_raised_millions) as row_num
  from layoffs_staging;

-- Now Deleted Dublicated Record
delete from layoffs_staging2
where row_num > 1;
  
select * from layoffs_staging2;

-- standardizing data
select company, trim(company)  from layoffs_staging2;

update layoffs_staging2
set company = TRIM(company);
  
select DISTINCT industry from layoffs_staging2 order by 1;

select * from layoffs_staging2 where industry like 'Crypto%';

-- update industry name repeat same name with actual orginal name 
update layoffs_staging2
set industry = 'Crypto'
where industry like 'Crypto%';

select * from layoffs_staging2;

-- united states country ok, But Data Format is not Good United State. This Dote is bad or Wrong Country
select * from layoffs_staging2
where country like 'united states.';

-- remove this .from country extra for Good Format
-- update Query
update layoffs_staging2 set country  =  TRIM(TRAILING '.' FROM country)
where country like 'United States%';

-- date format Correct it 
select `date`,STR_TO_DATE(`date`,'%m/%d/%Y')
from layoffs_staging2;

-- update formate 
update layoffs_staging2
set `date` = STR_TO_DATE(`date`,'%m/%d/%Y');


-- change date Data Type Date -> TEXT TO date
Alter table layoffs_staging2
MODIFY COLUMN  `date` DATE;

 -- 3) Null Values or Blank values
 select * from layoffs_staging2
 where total_laid_off is null and percentage_laid_off is null;

-- check industry is null or blank
select industry from layoffs_staging2;

select * from layoffs_staging2
where industry is null or industry = '';

-- we check Airbnb is related to which indusdry to  so that same company industry should be same which one is null or blank
select * from layoffs_staging2 where company = 'Airbnb';

select t1.industry, t2.industry from layoffs_staging2 t1
join layoffs_staging2 t2
on t1.company = t2.company
where (t1.industry is null or t1.industry = '')
and t2.industry is not null;


update layoffs_staging2 t1
join layoffs_staging2 t2
on t1.company = t2.company
set t1.industry  =  t2.industry
where (t1.industry is null or t1.industry = '')
and t2.industry is not null;

-- this query did not work properly because some data is blank so convert that data in to null then apply query this let 
update layoffs_staging2
set industry = null
where industry = '';

-- Delete Data which one is null, LIKE -  total_laid_off is null and percentage_liad_off is null
delete from layoffs_staging2
where total_laid_off is null
and percentage_laid_off is null;

 -- 4) Remove any columns
 
 ALTER TABLE layoffs_staging2
 drop column row_num;

select * from layoffs_staging2;

-- ------------- THI IS COMPLETE DATA CLEANING PROJECT IN MYSQL--------------