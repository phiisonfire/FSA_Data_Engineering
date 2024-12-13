CREATE DATABASE itversity_retail_db;

create user itversity_retail_user with encrypted password 'itversity';

grant all on database itversity_retail_db to itversity_retail_user;