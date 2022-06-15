-- sample flask app database initer.  for postgres, massage as needed for other sql dialects

drop database if exists my_flask_sample_app;

create database my_flask_sample_app;

\c my_flask_sample_app

set statement_timeout = 0;
set lock_timeout = 0;
set client_encoding = 'UTF8';
set standard_conforming_strings = on;
set check_function_bodies = false;
set client_min_messages = warning;
set default_tablespace = '';
set default_with_oids = false;
