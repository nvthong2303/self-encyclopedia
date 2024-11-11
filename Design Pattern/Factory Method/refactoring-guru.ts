// /**
//  * Lớp Creator khai báo một phương thức factory method được cho là
//  * trả về một đối tượng của lớp Product.
//  * Các lớp con của Creator cung cấp các implementation của phương thức này
// */
// abstract class Creator {
//     // Lưu ý là Creator cũng có thể cung cấp một số implementation mặc định của factory method
//     public abstract factoryMethod(): Product;

//     // lưu ý rằng, mặc dù có tên như vậy nhưng nhiệm vụ chính của Creator 
//     // không phải là tạo ra sản phẩm. Thông thường nó chứa một số logic kinh doanh quan trọng
//     // dựa vào các đối tượng Product trả về từ factory method
//     // Từ đó, các lớp con có thể gián tiếp thay đổi logic kinh doanh bằng cách ghi đè
//     // phương thức factory method và trả về một số product khác từ đó
//     public someOperation(): string {
//         // Call the factory method to create a Product object.
//         const product = this.factoryMethod();
//         // Now, use the product.
//         return "Creator: The same creator's code has just worked with " + product.operation();
//     }
// }


// // ConcreteCreators ghi đè phương thức factory method để thay đổi loại sản phẩm được tạo ra
// class ConcreteCreator1 extends Creator {
//     public factoryMethod(): Product {
//         return new ConcreteProduct1();
//     }
// }
// class ConcreteCreator2 extends Creator {
//     public factoryMethod(): Product {
//         return new ConcreteProduct2();
//     }
// }

// // Định nghĩa interface Product mà tất cả các sản phẩm cụ thể đều implement
// interface Product {
//     operation(): string;
// }

// // Các sản phẩm cụ thể cung cấp các implementation của phương thức operation
// class ConcreteProduct1 implements Product {
//     public operation(): string {
//         return '{Result of the ConcreteProduct1}';
//     }
// }
// class ConcreteProduct2 implements Product {
//     public operation(): string {
//         return '{Result of the ConcreteProduct2}';
//     }
// }

// // Client code
// function clientCode(creator: Creator) {
//     // ...
//     console.log('Client: I\'m not aware of the creator\'s class, but it still works.');
//     console.log(creator.someOperation());
//     // ...
// }

// /**
//  * Ứng dụng chọn loại creator và sử dụng nó
//  */
// console.log('App: Launched with the ConcreteCreator1.');
// clientCode(new ConcreteCreator1());
// console.log('');

// console.log('App: Launched with the ConcreteCreator2.');
// clientCode(new ConcreteCreator2());


abstract class Creator {
    public abstract factoryMethod(): Product;

    public someOperation(): string {
        // Call the factory method to create a Product object.
        const product = this.factoryMethod();
        // Now, use the product.
        return "Creator: The same creator's code has just worked with " + product.operation();
    }
}

class ConcreteCreator1 extends Creator {
    public factoryMethod(): Product {
        return new ConcreteProduct1();
    }
}
class ConcreteCreator2 extends Creator {
    public factoryMethod(): Product {
        return new ConcreteProduct2();
    }
}

interface Product {
    operation(): string;
}

class ConcreteProduct1 implements Product {
    public operation(): string {
        return '{Result of the ConcreteProduct1}';
    }
}
class ConcreteProduct2 implements Product {
    public operation(): string {
        return '{Result of the ConcreteProduct2}';
    }
}

function clientCode(creator: Creator) {
    // ...
    console.log('Client: I\'m not aware of the creator\'s class, but it still works.');
    console.log(creator.someOperation());
    // ...
}

console.log('App: Launched with the ConcreteCreator1.');
clientCode(new ConcreteCreator1());
console.log('');

console.log('App: Launched with the ConcreteCreator2.');
clientCode(new ConcreteCreator2());