# Cheat sheet


## Quản lý role
- xem thông tin role: ```select * from pg_roles;``` hoặc ```\du+```
- tạo mới role: ```CREATE ROLE <name>;```,
    - nếu thêm password: ```create role <name> login password <password>;```
    - 

- gán quyền cho role: 
    - ```GRANT CONNECT ON DATABASE postgres TO <name>;```
    - ```GRANT USAGE, CREATE ON SCHEMA public TO <name>;```
    - ```GRANT INSERT ON CUSTOMER TO <name>;```
    - ```alter role <name> superuser;```
    - ```Alter role <name> password 'Abcd1234';```
- INHERIT và NOINHERIT: 
    - inherit: option, nó cho phép grant quyền mà nó đang có cho 1 role khác. ```alter role <name> inherit;```
    - noinherit: ngược lại, nó không thể grant những quyền nó đang có cho role khác. ```alter role <name> noinherit;```
- xóa role: 
    ```
    REASSIGN OWNED BY <name> to postgres;
    DROP OWNED BY <name>;
    drop role <name>;
    ```

- Danh sách permission:

    | Permission    | Description |
    | -------- | ------- |
    | ---------------- database --------------- |
    | CONNECT  | quyền kết nối    |
    | CREATE | quyền tạo schema   |
    | TEMP   | quyền tạo bảng tạm thời    |
    | ---------------- schema --------------- |
    | USAGE   | quyền sử dụng nhưng không thao tác dịch vụ    |
    | CREATE   | quyền tạo    |
    | ---------------- table --------------- |
    | SELECT   | quyền truy vấn   |
    | INSERT   | quyền thêm data  |
    | UPDATE   | quyền sửa data  |
    | DELETE   | quyền xóa data  |
    | TRUNCATE   | quyền xóa bảng  |
    | REFERENCES   | quyền thêm foreign key  |
    | TRIGGER   | quyền tạo trigger lên bảng  |
    | ---------------- sequence --------------- |
    | ---------------- function --------------- |
    | ---------------- others --------------- |
    | SUPERUSER   | quyền root  |
    | CREATEDB   | quyền tạo db  |
    | CREATEROLE   | quyền tạo role  |


## Quản lý schema:
- Schema là tập hợp các đối tượng (table, index, view, function, ...).
- Schema: dùng để nhóm các đối tượng liên quan đến nhau, dùng để phân quyền hoặc quản lý.
- Sử dụng ```\dn+``` để liệt kế ds các schema trong dababase.
- Xóa schema: ```drop schema <tên schema> cascade;```


## Quản lý số lượng client, table, records:
- List client: ```SELECT COUNT(*) FROM pg_stat_activity WHERE state = 'active';```
- List client theo role: ```SELECT COUNT(*) FROM pg_stat_activity WHERE usename = 'postgres';```

- List table: ```SELECT COUNT(*) FROM information_schema.tables WHERE table_type = 'BASE TABLE';```
- Count record: ```SELECT table_name, (xpath('//row/text()', xml_count))[1]::text::int AS row_count
FROM (
  SELECT table_name, query_to_xml(format('SELECT COUNT(*) FROM %I.%I', table_schema, table_name), false, true, '') AS xml_count
  FROM information_schema.tables
  WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
) AS t;```