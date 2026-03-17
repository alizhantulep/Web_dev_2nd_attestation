
from models import Vehicle, Car, Motorcycle

def main():
    v1 = Vehicle("Generic", "Transporter", 2010)
    c1 = Car("Tesla", "Model S", 2023, doors=4, electric=True)
    c2 = Car("Toyota", "Corolla", 2020, doors=4)
    m1 = Motorcycle("Yamaha", "MT-07", 2022, cc=689)

    vehicles = [v1, c1, c2, m1]

    for v in vehicles:
        print(v)            
        print(v.start())        
        print(v.stop())         
        if isinstance(v, Car):
            print(v.honk())
        elif isinstance(v, Motorcycle):
            print(v.wheelie())
        
        print("-" * 40)

if __name__ == "__main__":
    main()