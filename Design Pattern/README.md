# Design Pattern

## Creational Patterns

#### Singleton
Đảm bảo một lớp chỉ có một thể hiện duy nhất và cung cấp điểm truy cập toàn cục cho thể hiện đó.

- Trong NestJs, decorator: @Injectable() chính là thể hiển của singleton, đảm bảo rằng mỗi class chỉ có 1 instance và nó có thể truy cập từ bất cứ đâu trong ứng dụng.
- Trong NestJS:
    ```
    @Injectable({ scope: Scope.DEFAULT })
    export class LoggerService {
        log(message: string) {
            console.log(message);
        }
    }
    ```

#### Factory Method
- Biến một yêu cầu thành một đối tượng độc lập để có thể tham số hóa các khách hàng với các yêu cầu khác nhau, hàng đợi hoặc ghi lại các yêu cầu.

- Factory Pattern là một trong những Pattern phổ biến trong lập trình hướng đối tượng. Nhiệm vụ của Factory Pattern là quản lý và trả về các đối tượng theo yêu cầu, giúp cho việc khởi tạo đổi tượng một cách linh hoạt hơn.

- Factory Method cung cấp một interface, phương thức trong việc tạo và quản lý các object trong class. Nhưng để cho class con kế thừa của nó có thể ghi đè để chỉ rõ object nào được tạo. Factory method giao việc việc khởi tạo một object cụ thể cho lớp con. ==> Giảm sự phụ thuộc, dễ dàng mở rộng, Che giấu logic của phương thức khởi tạo.

![image info](./Factory%20Method/model.webp)
- Các thành phần của Factory Method:
    - Product: khuôn mẫu (interface) của các đối tượng mà Factory Method tạo ra.
    - ConcreteProduct: các Lớp được cài đặt khuôn mẫu Product.
    - Creator: Lớp cơ sở với phương thức Factory Method.
    - khai báo Factory Method: trả về kiểu đối tượng kiểu Product, Creator cũng có thể định nghĩa một cài đặt mặc định của Factory Method mà giá trị trả về là một đối tượng ConcreteProduct mặc định.
    - gọi Factory Method để tạo đối tượng kiểu Product
    - ConCreteCreator: Ghi đè Factory Method để trả về một instance của ConcreteProduct


- Trong NestJS:
    ```
    export interface IProduct {
        name: string;
        price: number;
    }

    @Injectable()
    export class ProductFactory {
        createProduct(type: string): IProduct {
            if (type === 'book') {
            return new Book();
            } else if (type === 'movie') {
            return new Movie();
            } else if (type === 'music') {
            return new Music();
            } else {
            throw new Error(`Invalid product type: ${type}`);
            }
        }
    }

    export class Book implements IProduct {
        name = 'Book';
        price = 10;
    }

    export class Movie implements IProduct {
        name = 'Movie';
        price = 20;
    }

    export class Music implements IProduct {
        name = 'Music';
        price = 5;
    }
    ```
    
#### Abstract Factory
- Cung cấp một interface cho việc khởi tạo các tập hợp của những object có đặc điểm giống nhau mà khong cần quan tâm object đó là gì, không cần xác định lớp cụ thể. Đảm bảo rằng các product mà bạn nhận được từ một factory đều tương thích, hạn chế sự phục thuộc giữa creator và concreteProduct.

#### Builder
- Tách biệt việc xây dựng một object phức tạp khỏi biểu diễn của nó để cùng 1 quá trình xây dựng có thể tạo ra các biểu diễn khác nhau.
- Cho phép xây dựng các object phức tạp bằng cách sử dụng các đối tượng đơn giản và sử dụng tiếp cận từng bước. 
- Trong NestJS:
    ```
    @Injectable()
    export class DatabaseConnectionBuilder {
        private host: string;
        private port: number;
        private username: string;
        private password: string;
        private database: string;

        setHost(host: string) {
            this.host = host;
            return this;
        }

        setPort(port: number) {
            this.port = port;
            return this;
        }

        setUsername(username: string) {
            this.username = username;
            return this;
        }

        setPassword(password: string) {
            this.password = password;
            return this;
        }

        setDatabase(database: string) {
            this.database = database;
            return this;
        }

        build() {
            return new DatabaseConnection(
            this.host,
            this.port,
            this.username,
            this.password,
            this.database,
            );
        }
    }

    export class DatabaseConnection {
        constructor(
            private readonly host: string,
            private readonly port: number,
            private readonly username: string,
            private readonly password: string,
            private readonly database: string,
        ) {
            // connect to database
        }

        // other methods
    }
    ```

#### Prototype

## Structural Patterns

#### Adapter
#### Bridge
#### Composite
#### Decorator
#### Facade
#### Flyweight
#### Proxy

## Behavioral Patterns