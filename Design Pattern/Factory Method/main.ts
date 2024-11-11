// interface Product cho tất cả các sp cụ thể đều phải cài đặt với phương thức use()
interface ProductX {
    use(): void;
}

// Cài đặt các sản phẩm cụ thể
// Mỗi class có cách thực hiện use() khác nhau
class ConcreteProductA implements ProductX {
    use(): void {
        console.log('use ConcreteProduct A');
    }
}
class ConcreteProductB implements ProductX {
    use(): void {
        console.log('use ConcreteProduct B');
    }
}

// lớp Creator cơ sở với phương thức factoryMethod
abstract class CreatorX {
    // phương thức factoryMethod
    public abstract factoryMethod(): ProductX;

    public doSomething(): void {
        const product = this.factoryMethod();
        product.use();
    }
}

// các creator cụ thể tạo ra các sản phẩm cụ thể
// các lớp con của Creator mỗi lớp sẽ tạo ra một sản phẩm cụ thể
class ConcreteCreatorA extends CreatorX {
    public factoryMethod(): ProductX {
        return new ConcreteProductA();
    }
}
class ConcreteCreatorB extends CreatorX {
    public factoryMethod(): ProductX {
        return new ConcreteProductB();
    }
}

// tạo ra các instance của ConcreteCreatorA và ConcreteCreatorB
// sau đó gọi doSomething() để tạo ra sản phẩm cụ thể
const creatorA = new ConcreteCreatorA();
creatorA.doSomething();

const creatorB = new ConcreteCreatorB();
creatorB.doSomething();