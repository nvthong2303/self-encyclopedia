# Upstreams

```
"healthchecks": {
	"passive": {
		"unhealthy": { // 
			"tcp_failures": 0, // 
			"http_statuses": [],
			"http_failures": 0,
			"timeouts": 0
		},
		"type": "http",
		"healthy": { // điều kiện xác định upstreams là healthy
			"successes": 0, // số lần thành công để tính là healthy
			"http_statuses": []
		}
	},
	"active": {
		"headers": {}, // Headers có thể đc gửi kèm theo các request health-check
		"http_path": "/",
		"https_sni": null,
		"https_verify_certificate": true,
		"healthy": { // điều kiện để xác định upstreams đang health
			"interval": 5, // khoảng thời gian giữa mỗi lần check
			"http_statuses": [], // http code tính là healthy
			"successes": 5 // số lần thành công liên tiếp cần thiết để đánh dấu upstreams là healthy
		},
		"unhealthy": { // điều kiện xác định upstream unhealthy
			"interval": 5,
			"tcp_failures": 0, // số lần thất bại tcp liên tiếp để đánh dấu upstreams là unhealthy
			"timeouts": 0, 
			"http_failures": 5, // số lần thất bại http liên tiếp để đánh dấu upstreams là unhealthy
			"http_statuses": [] // http code tính là unhealthy 
		},
		"type": "http",
		"timeout": 1, // 
		"concurrency": 10 // số lượng request health-check có thể thực hiện đồng thời
	},
	"threshold": 2 // Số lần upstream bị đánh dấu là unhealthy trước khi nó bị loại khỏi danh sách upstream hoạt động.
},
```


- Cách UI nhận biết active / deactive health-checks:
	- cả 2 __interval__: --> deactive.

