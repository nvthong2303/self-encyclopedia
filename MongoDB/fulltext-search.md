## Full text search

- create index trước khi sử dụng full-text search.

- tìm kiếm toàn văn bản, nhận lệnh khớp các cụm từ tìm kiếm trên: "chan,va,bang,dau"
```
db.players.find({ $text:{ $search: 'chan va bang dau'} })
```

- tìm kiếm chính xác "chan va bang dau"
```
db.players.find({ $text:{ $search: '\"chan va bang dau\"'} })
```

```

```
