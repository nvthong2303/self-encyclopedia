interface Chair {
    hasLegs(): void;
    sitOn(): void;
}
interface Table {
    hasLegs(): void;
    putOn(): void;
}

class ModernChair implements Chair {
    hasLegs(): void {
        console.log('ModernChair has 4 legs');
    }
    sitOn(): void {
        console.log('You can sit on ModernChair');
    }
}
class VictorianChair implements Chair {
    hasLegs(): void {
        console.log('VictorianChair has 4 legs');
    }
    sitOn(): void {
        console.log('You can sit on VictorianChair');
    }
}
class ModernTable implements Table {
    hasLegs(): void {
        console.log('ModernTable has 4 legs');
    }
    putOn(): void {
        console.log('You can put on ModernTable');
    }
}
class VictorianTable implements Table {
    hasLegs(): void {
        console.log('VictorianTable has 4 legs');
    }
    putOn(): void {
        console.log('You can put on VictorianTable');
    }
}

// Abstract Factory
interface FurnitureFactory {
    createChair(): Chair;
    createTable(): Table;
}

class ModernFurnitureFactory implements FurnitureFactory {
    createChair(): Chair {
        return new ModernChair();
    }
    createTable(): Table {
        return new ModernTable();
    }
}
class VictorianFurnitureFactory implements FurnitureFactory {
    createChair(): Chair {
        return new VictorianChair();
    }
    createTable(): Table {
        return new VictorianTable();
    }
}

function clientCodeAbtractFactory(factory: FurnitureFactory) {
    const chair = factory.createChair();
    const table = factory.createTable();

    chair.hasLegs();
    chair.sitOn();
    table.hasLegs();
    table.putOn();
}

console.log("Client: Testing client code with the ModernFurnitureFactory:");
clientCodeAbtractFactory(new ModernFurnitureFactory());

console.log("");

console.log("Client: Testing client code with the VictorianFurnitureFactory:");
clientCodeAbtractFactory(new VictorianFurnitureFactory());
