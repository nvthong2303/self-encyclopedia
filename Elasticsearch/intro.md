# Elasticsearch

- Công cụ tìm kiếm, phân tích dữ liệu JSON, được thiết kế để scale theo chiều ngang, khả dụng cao, quản lý thuận tiện.
- Được xây dựng dựa trên apache lucene.
- Phù hợp với hầu hết các loại dữ liệu : văn bản, số, không gian địa lý, dữ liệu sql - nosql.
- Hỗ trợ rest API.
- Là thành phần cốt lõi của ELK (Elastic Stack - Bộ công cụ phân tích, thu thập, lưu trữ, trực quan hóa, ... dữ liệu. Bao gồm Elasticsearch - Logstash - Kibaka).
- Full-text search là tìm kiếm một lượng lớn văn bản không chỉ dựa trên việc so khớp chính xác, còn dựa trên việc phân tích và hiểu nghĩa của văn bản. ES hỗ trợ điều này bằng tokenizers, filters, analyzers.


## Query:

### Leaf query:

- Match query: So khớp 1 từ khóa với 1 trường cụ thể, dùng để tìm kiếm văn bản và phân tích từ khóa. Phù hợp full-text search.
	```
	{
		"query": {
			"match": {
			"title": "quick brown"
			}
		}
	}
	```
- Term query: Tìm kiếm chính xác, không phân tích từ khóa, phù hợp với các giá trị cố định.
- Range query: Tìm kiếm trong khoảng giá trị, dùng cho các trường số, ngày tháng.
	```
	{
		"query": {
			"range": {
			"age": { "gte": 18, "lt": 30 }
			}
		}
	}
	```
- Exists query: Kiếm tra trường có tồn tại hay không.
- Prefix, WildCard and Regular Expression: Tìm kiếm các ký tự đại diện và biểu thức chính quy.
- Fuzzy query: tìm kiếm gần đúng với lỗi chính tả hoặc khác biệt nhỏ giữa các từ.

### Compound query:

- Bool query: Kết hợp nhiều điều kiện tìm kiếm lại với nhau (must, must_not, should, filter).
	```
	{
		"query": {
			"bool": {
				"must": { "match": { "title": "quick" }},
				"must_not": { "match": { "title": "lazy" }}
			}
		}
	}
	```
- Dis Max query: tìm kiếm tài liệu phù hợp nhất từ nhiều truy vấn con, dùng tìm kiếm maximum score
- Multi-match query: So khớp một từ khóa với nhiều trường khác nhau.
- Function Score query: Tính điểm dựa trên các hàm để tạo điểm.
- Constant Score query: Gán một điểm cố định cho tất cả các tài liệu với điều kiện truy vấn.
- Filter query:
	```
	{
		"query": {
			"bool": {
				"filter": {
					"term": { "status": "published" }
				}
			}
		}
	}
	```
- Boosting query:

### Specialized Query:

### Aggregation Query:

## Documents:
- Tương tự 1 bản ghi trong db khác, mỗi document có 1 id duy nhất.
- Là dữ liệu cơ bản mà ES tìm kiếm và lưu trữ.
- Thường được lưu trữ dưới dạng JSON.
### Data type:
- String:
- Numerics:
- Date:
- Boolean:
- Binary types:
- Range types:
- Geospatial types:
- Array types:
- Joining types:
- Complex types:
- Others:

## Fields:
- Là các thành phần cơ bản của một documents. Là các thuộc tính hoặc trường thông tin về một documents.
- Mỗi Field có thể chứa một loạt các giá trị như chuỗi ký tự số, ngày, tháng, ...


## Mapping:
- Định nghĩa cấu trúc dữ liệu của 1 index, tương tự schema trong csdl. Mapping xác định các document được lưu trữ, index, query.
- DataType: text, keyword, interger, date, float, boolean, object, ...
-


## Index:
- là một ctdl quan trọng, tương tự như một csdl quan hệ.
- là nơi lưu trữ các document đc tổ chức theo dạng có thể tim kiếm và truy vấn.
- là tập hợp các document có các đặc điểm tương tự như nhau.
- các document trong 1 index có thể có các trường khác nhau, nhưng có cùng cấu trúc hoặc định dạng.
- mapping trong index: mapping xác định ctdl của các document trong index, bgom các trường và datatype.
--> Index là 1 cấu trúc dữ liệu quan trọng, dùng để tổ chức và truy vấn các tài liệu một các hiệu quả.

## Analyzer:
- Các thành phần của analyzer:
	- Character Filter: nó thực hiện thay thế hoặc loại bỏ các ký tự trước khi chia văn bản thành các token.
	- Tokenizer: là thành phần chia văn bản thành các token dựa trên các quy tắc cụ thể.
		- Standard tokenizer:
		- Whitespace tokenizer:
		- Keyword tokenizer:
		- Pattern tokenizer:
	- Token Filter: có thể thay đổi cách biểu diễn của token hoặc loại bỏ token không cần thiết.
		- Lowercase filter:
		- Stop filter:
		- Aynonym filter:


## Inverted Index:
- là thành phần cốt lõi trong ES, đc thiết kế để tối ưu hóa việc tìm kiếm văn bản.
- là ctdl chính giúp ES thực hiện truy vấn một cách nhanh chóng và hiệu quả trên các tập dữ liệu lớn.
- là ctdl lưu trữ ánh xạ giữa các từ (terms) và vị trí của chúng trong các document.
- thay vì lưu trữ theo thứ tự thông thường, Inverted index sẽ lưu trữ từng từ và ds các document chứa nó.
- inverted index được xây dựng khi thêm 1 document vào ES.
	- văn bản được phân tích bởi các analyzer, chuyển thành các token.
	- mỗi token sẽ được thêm vào các inverted index dưới dạng 1 từ.


## Aggregation:







## Câu hỏi:
### Điều gì làm cho ElasticSearch trở thành một công cụ tìm kiếm mạnh mẽ?
- ElasticSearch sử dụng Lucene dưới hạ tầng, hỗ trợ tìm kiếm full-text, cung cấp các công cụ như tokenizers, filters và analyzers để phân tích văn bản, và có khả năng mở rộng lớn.

### Trong ElasticSearch, match query dùng để làm gì?
- Match query dùng để so khớp một từ khóa với một trường cụ thể trong văn bản

### Bool query trong ElasticSearch dùng với mục đích gì?
- Bool query dùng để kết hợp nhiều điều kiện tìm kiếm lại với nhau.

### Khi nào nên sử dụng wildcard query trong ElasticSearch?
- Khi muốn tìm kiếm dựa trên các ký tự đại diện hoặc không biết chính xác từ khóa.

### Trong ví dụ minh họa, làm thế nào để tìm tất cả các sách có tiêu đề chứa từ khóa "Elastic"?
- Sử dụng phương thức searchByTitleContaining("Elastic") từ BookService.
