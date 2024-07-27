# invox技術テスト

### 環境構築
- docker-compose build
```console
docker-compose build
```
- docker-compose up
```console
docker-compose up
```
- DBマイグレーション実行
```console
sh ./scripts/migrate_up.sh
```

### 実行結果
<details>
<summary>実行ログ</summary>

```console
(invox) riku@MacBook-Air invox % date;curl -X POST -H "Content-Type: application/json" -d '{"image_path": "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"}' localhost:5001/register | jq;date;
2024年 7月27日 土曜日 23時23分31秒 JST
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   102  100    30  100    72   1002   2405 --:--:-- --:--:-- --:--:--  4250
{
  "message": "ok",
  "status": 200
}
2024年 7月27日 土曜日 23時23分31秒 JST
(invox) riku@MacBook-Air invox % date;curl -X POST -H "Content-Type: application/json" -d '{"image_path": "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"}' localhost:5001/register | jq;date;
2024年 7月27日 土曜日 23時23分35秒 JST
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   102  100    30  100    72    935   2245 --:--:-- --:--:-- --:--:--  3923
{
  "message": "ok",
  "status": 200
}
2024年 7月27日 土曜日 23時23分35秒 JST
(invox) riku@MacBook-Air invox % date;curl -X POST -H "Content-Type: application/json" -d '{"image_path": "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"}' localhost:5001/register | jq;date;
2024年 7月27日 土曜日 23時23分37秒 JST
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   102  100    30  100    72   1161   2787 --:--:-- --:--:-- --:--:--  5100
{
  "message": "ok",
  "status": 200
}
2024年 7月27日 土曜日 23時23分37秒 JST
(invox) riku@MacBook-Air invox % date;curl -X POST -H "Content-Type: application/json" -d '{"image_path": "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"}' localhost:5001/register | jq;date;
2024年 7月27日 土曜日 23時24分34秒 JST
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   102  100    30  100    72    848   2035 --:--:-- --:--:-- --:--:--  3642
{
  "message": "ok",
  "status": 200
}
2024年 7月27日 土曜日 23時24分34秒 JST
(invox) riku@MacBook-Air invox % date;curl -X POST -H "Content-Type: application/json" -d '{"image_path": "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"}' localhost:5001/register | jq;date;
2024年 7月27日 土曜日 23時24分35秒 JST
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   102  100    30  100    72   1151   2764 --:--:-- --:--:-- --:--:--  4857
{
  "message": "ok",
  "status": 200
}
2024年 7月27日 土曜日 23時24分35秒 JST
```

</details>

<details>
<summary>ai_analysis_logテーブル</summary>

```mysql
mysql> desc ai_analysis_log;
+--------------------+--------------+------+-----+---------+----------------+
| Field              | Type         | Null | Key | Default | Extra          |
+--------------------+--------------+------+-----+---------+----------------+
| id                 | int          | NO   | PRI | NULL    | auto_increment |
| image_path         | varchar(255) | YES  |     | NULL    |                |
| success            | tinyint(1)   | NO   |     | NULL    |                |
| message            | varchar(255) | YES  |     | NULL    |                |
| class              | int          | YES  |     | NULL    |                |
| confidence         | decimal(5,4) | YES  |     | NULL    |                |
| request_timestamp  | datetime(6)  | YES  |     | NULL    |                |
| response_timestamp | datetime(6)  | YES  |     | NULL    |                |
+--------------------+--------------+------+-----+---------+----------------+
8 rows in set (0.01 sec)

mysql> select * from ai_analysis_log;
+----+--------------------------------------------------------+---------+--------------+-------+------------+----------------------------+----------------------------+
| id | image_path                                             | success | message      | class | confidence | request_timestamp          | response_timestamp         |
+----+--------------------------------------------------------+---------+--------------+-------+------------+----------------------------+----------------------------+
|  1 | /image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg |       1 | success      |   154 |     0.9109 | 2024-07-27 23:23:31.677096 | 2024-07-27 23:23:31.684895 |
|  2 | /image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg |       1 | success      |   432 |     0.2010 | 2024-07-27 23:23:35.200926 | 2024-07-27 23:23:35.213070 |
|  3 | /image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg |       1 | success      |   794 |     0.3847 | 2024-07-27 23:23:37.717780 | 2024-07-27 23:23:37.727768 |
|  4 | /image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg |       1 | success      |   159 |     0.7302 | 2024-07-27 23:24:34.104040 | 2024-07-27 23:24:34.115438 |
|  5 | /image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg |       0 | Error:E50011 |  NULL |       NULL | 2024-07-27 23:24:35.754708 | 2024-07-27 23:24:35.761946 |
+----+--------------------------------------------------------+---------+--------------+-------+------------+----------------------------+----------------------------+
5 rows in set (0.00 sec)
```

</details>