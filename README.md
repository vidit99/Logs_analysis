LOGS ANALYSIS UDACITY PROJECT 

This project requires virtual environment so you need to download virtual box and vagrant on your laptop.

In this we have a out file which shows the output of the project.

We have a analysis.py file which have all the queries .

Installation process /  steps required for the project

1) Clone the logs analysis project repository 

 `$ git clone https://github.com/mlupin/fullstack-nanodegree-logs-analysis.git`
 
2) Go to the repository you just clonned 

`$ cd fullstack-nanodegree-logs-analysis`

3) vagrant up 

4) Now you have to log into the virtual machine by typing the command :

vagrant ssh 

5) Now type cd/vagrant 

6) Now load newsdata.sql file 

7) Now load psql -d news -f newsdata.sql

8) now run the python file by typing command:

python analysis.py

9) you will get the output desired.

Database views referred in the python file:

->Gives a list of article title 
create or replace view article_view as select 
articles.title,count(case when log.status like '%200%' then 1 end) 
as view from articles left join log on log.path like '%' || articles.slug group by articles.title;


->Gives a list of all title
create or replace view arti as select substring(path,10) as path from log
	where path like '/arti%'

->Gives count of number of times article was viewed 	
create or replace view total_count as select articles.author , count(*) from
articles join arti on articles.slug = arti.path group by 
articles.author order by count(*) desc

	
->Gives popular authors	
create or replace view popular_author as select authors.name, authors.id
from authors join articles on articles.author = authors.id group by authors.id


->Gives total request,fail.
create or replace view mistake as select time::timestamp::date as date,COUNT(case 
when status like '%200%' then 1 end) as success, COUNT(case when status like 
'%404%' then 1 end)as fail, COUNT(method) as total from log group by date