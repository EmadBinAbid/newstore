create user stellic with password 'stellic';
drop database if exists newstore;
create database newstore owner stellic encoding 'UTF-8';
\c newstore
create extension "uuid-ossp";
