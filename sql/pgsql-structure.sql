/*****************************************************
 * @software: PyCharm
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-08-04 16:20:52 UTC+08:00
 *****************************************************/

create schema if not exists public_dev_test authorization austin;

create table if not exists public_dev_test.publish
(
    id      serial primary key,
    name    varchar unique not null,
    area    varchar,
    existed boolean        not null default true,
    created timestamp      not null default current_timestamp,
    updated timestamp      not null default current_timestamp
);
comment on table public_dev_test.publish is '出版社表';
comment on column public_dev_test.publish.id is 'ID';
comment on column public_dev_test.publish.name is '出版社名字';
comment on column public_dev_test.publish.area is '出版社地区';
comment on column public_dev_test.publish.existed is '数据状态';
comment on column public_dev_test.publish.created is '创建时间';
comment on column public_dev_test.publish.updated is '修改时间';

create table if not exists public_dev_test.author
(
    id          serial primary key,
    name        varchar   not null,
    gender      boolean   not null,
    birthday    date      not null,
    description text,
    existed     boolean   not null default true,
    created     timestamp not null default current_timestamp,
    updated     timestamp not null default current_timestamp
);
comment on table public_dev_test.author is '作者表';
comment on column public_dev_test.author.id is 'ID';
comment on column public_dev_test.author.name is '作者名字';
comment on column public_dev_test.author.gender is '作者性别, true=1=男, false=0=女';
comment on column public_dev_test.author.birthday is '作者出生日期';
comment on column public_dev_test.author.description is '作者描述';
comment on column public_dev_test.author.existed is '数据状态';
comment on column public_dev_test.author.created is '创建时间';
comment on column public_dev_test.author.updated is '修改时间';
