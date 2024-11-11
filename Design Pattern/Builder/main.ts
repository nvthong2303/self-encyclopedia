class House {
    public doors: number = 0;
    public windows: number = 0;
    public roof: boolean = false;
    public garage: boolean = false;

    public description(): string {
        return `This house has ${this.doors} doors, ${this.windows} windows, ${this.roof} roof and ${this.garage} garage.`;
    }
}

interface HouseBuilder {
    reset(): void;
    setDoors(doors: number): void;
    setWindows(windows: number): void;
    setRoof(roof: boolean): void;
    setGarage(garage: boolean): void;
    getResult(): House;
}

class ConcreteHouseBuilder implements HouseBuilder {
    private house: House;
    
    constructor() {
        this.reset();
    }
    public reset(): void {
        this.house = new House();
    }
    public setDoors(doors: number): void {
        this.house.doors = doors;
    }
    public setWindows(windows: number): void {
        this.house.windows = windows;
    }
    public setRoof(roof: boolean): void {
        this.house.roof = roof;
    }
    public setGarage(garage: boolean): void {
        this.house.garage = garage;
    }
    public getResult(): House {
        const result = this.house;
        this.reset();
        return result;
    }
}

class Director {
    private builder: HouseBuilder;

    public setBuilder(builder: HouseBuilder): void {
        this.builder = builder;
    }

    public constructSimpleHouse(): void {
        this.builder.setDoors(1);
        this.builder.setWindows(2);
        this.builder.setRoof(true);
    }

    public constructLuxuryHouse(): void {
        this.builder.setDoors(4);
        this.builder.setWindows(8);
        this.builder.setRoof(true);
        this.builder.setGarage(true);
    }
}

function clientCode(director: Director) {
    const builder = new ConcreteHouseBuilder();
    director.setBuilder(builder);

    console.log("Building a simple house:");
    director.constructSimpleHouse();
    console.log(builder.getResult().description());

    console.log("Building a luxury house:");
    director.constructLuxuryHouse();
    console.log(builder.getResult().description());
}

const director = new Director();
clientCode(director);