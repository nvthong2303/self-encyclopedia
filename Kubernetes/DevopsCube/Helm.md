# Helm
- Là một trình quản lý gói và quản lý ứng dụng cho K8s, đóng gói nhiều tài nguyên k8s vào 1 đơn vị triển khai duy nhất, được gọi là **Chart**
- cấu trúc thư mục helm:
```
    └── Example project
        ├── Chart.yaml # mô tả chart
        ├── values.yaml # các giá trị mặc định, có thể thay đổi
        ├── chart/ # subcharts
        └── templates/ # template files
```
- lợi ích khi dùng helm: 


# Cheat sheet:
## Chart management:
```
# create new chart directory
helm create <name>

# packages chart into a version chart archivec file
helm package <chart-path>

# run test and identify possible issue
helm lint <chart>

# inspect chart and list content
helm show all <char>

# display content of values.yaml file
helm show values <chart>

# download / pull chart
helm pull <chart>

# if set to true, will untar the chart after download
helm pull <chart> --untar=true

# verify package before use it
helm pull <chart> --verify


```

