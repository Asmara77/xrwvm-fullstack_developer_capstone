from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    # Create CarMake instances and store them in a dictionary for easy access
    car_make_instances = {}
    for data in car_make_data:
        car_make = CarMake.objects.create(
            name=data['name'], 
            description=data['description']
        )
        car_make_instances[data['name']] = car_make

    # Create CarModel instances using the corresponding CarMake instances
    car_model_data = [
        {
            "name": "Pathfinder",
            "type": "SUV",
            "year": 2023, 
            "car_make": "NISSAN"
        },
        {
            "name": "Qashqai", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": "NISSAN"
        },
        {
            "name": "XTRAIL", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": "NISSAN"
        },
        {
            "name": "A-Class", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": "Mercedes"
        },
        {
            "name": "C-Class", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": "Mercedes"
        },
        {
            "name": "E-Class", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": "Mercedes"
        },
        {
            "name": "A4", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": "Audi"
        },
        {
            "name": "A5",
            "type": "SUV", 
            "year": 2023, 
            "car_make": "Audi"
        },
        {
            "name": "A6", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": "Audi"
        },
        {
            "name": "Sorrento", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": "Kia"
        },
        {
            "name": "Carnival", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": "Kia"
        },
        {
            "name": "Cerato", 
            "type": "Sedan", 
            "year": 2023, 
            "car_make": "Kia"
        },
        {
            "name": "Corolla",
            "type": "Sedan", 
            "year": 2023, 
            "car_make": "Toyota"
        },
        {
            "name": "Camry", 
            "type": "Sedan", 
            "year": 2023, 
            "car_make": "Toyota"
        },
        {
            "name": "Kluger", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": "Toyota"
        },
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=car_make_instances[data['car_make']],
            type=data['type'],
            year=data['year']
        )
