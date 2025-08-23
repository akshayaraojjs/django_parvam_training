import heapq

class TreatPatient:
    def __init__(self):
        self.patientsQueue = []
        
    def add_patient(self, priority, problem):
        # heappush(list, (priority, problem))
        heapq.heappush(self.patientsQueue, (priority, problem))
        print(f"Patient with {problem} with priority {priority} has been enrolled")
        
    def check_patient(self):
        if self.patientsQueue:
            # heappop(list)
            priority, problem = heapq.heappop(self.patientsQueue)
            print(f"Treating patient with {problem} - Priority {priority}")
        else:
            print("All patients has been treated!")
    
    def patient_queue(self):
        print(f"Patients in the queue: {len(self.patientsQueue)} and their details are as follows:")
        print("Patients: ",self.patientsQueue)   
         
pq = TreatPatient()
pq.add_patient(3, "Headache")
pq.add_patient(4, "Sneezing")
pq.add_patient(2, "High Fever")
pq.add_patient(1, "Head Injury")

pq.patient_queue()

pq.check_patient()
pq.check_patient()
pq.check_patient()
pq.check_patient()