CREATE TABLE `exception`(
	`topic` varchar(10000) NOT NULL,
	`description` varchar(10000) NOT NULL,
	`fix` varchar(10000) NOT NULL
);

CREATE TABLE `command`(
	`topic` varchar(10000) NOT NULL,
	`description` varchar(10000) NOT NULL,
	`matching` varchar(10000) NOT NULL,
	`args` varchar(10000) NOT NULL,
	`returns` varchar(10000) NOT NULL,
	`link` varchar(10000) NOT NULL
);

CREATE TABLE `flagged_user`(
	`user_number` bigint auto_increment,
	`user_id` bigint primary key,
	`num_of_warnings` bigint
);

CREATE TABLE `example`(
	`function` varchar(10000),
	`example` varchar(10000),
	`comment` varchar(10000)
);
