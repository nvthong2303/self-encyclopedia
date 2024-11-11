class Singleton {
    private static instance: Singleton;

    private constructor() {
        // do something
    }

    public static getInstance(): Singleton {
        if (!Singleton.instance) {
            Singleton.instance = new Singleton();
        }

        return Singleton.instance;
    }

    public doSomething() {
        console.log('do something');
    }
}

const singleton1 = Singleton.getInstance();
const singleton2 = Singleton.getInstance();

singleton1.doSomething();

console.log(singleton1 === singleton2);