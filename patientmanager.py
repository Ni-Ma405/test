for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return n <= from queue import Queue

patient_name = Queue()
current_patient_name = None

while True:
    print("Desk Manager - Patient Registration and Appointment System")
    print("1.Register patient")
    print("2.Remove Patient after Meeting Doctor")
    print("3.Display Patient Queue")
    print("4.Exit")

    task = int(input("Enter your choice (just enter the option number): "))
    if task == 1:
        name = input("Enter Patient name: ")
        patient_name.put(name)
        current_patient_name = name
        print(f"Patient {name} regitered")

    elif task == 2:
        patient_name.get()
        print(f"Patient {patient_name} removed after meeting the doctor")
    elif task == 3:
        print("Current Patient Queue: ")
        print(patient_name.queue)
    elif task == 4:
        print("Exiting program...")
    else:
        print("Invalid Input")   
