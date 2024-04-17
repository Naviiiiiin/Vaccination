# your_app/management/commands/import_data.py

from django.core.management.base import BaseCommand
from register.models import Area, Hospitals

class Command(BaseCommand):
    help = 'Import data into the database'

    def handle(self, *args, **options):
        data = {
           "Mumbai": ["Lilavati Hospital", "Kokilaben Dhirubhai Ambani Hospital", "Bombay Hospital", "Hinduja Hospital", "Nanavati Super Speciality Hospital", "Jaslok Hospital", "Tata Memorial Hospital", "Breach Candy Hospital", "Wockhardt Hospital", "Saifee Hospital"],
                "Delhi": ["AIIMS", "Apollo Hospital", "Fortis Hospital", "Max Hospital", "Medanta - The Medicity", "Sir Ganga Ram Hospital", "BLK Super Speciality Hospital", "Indraprastha Apollo Hospital", "Safdarjung Hospital", "Moolchand Hospital"],
                "Bangalore": ["Apollo Hospital", "Fortis Hospital", "Manipal Hospital", "Columbia Asia Referral Hospital", "Narayana Multispeciality Hospital", "Sakra World Hospital", "BGS Gleneagles Global Hospital", "St. John's Medical College and Hospital", "Narayana Institute of Cardiac Sciences", "Ramaiah Memorial Hospital"],
                "Kolkata": ["Apollo Gleneagles Hospital", "Medica Superspecialty Hospital", "AMRI Hospital", "Ruby General Hospital", "Woodlands Hospital", "Rabindranath Tagore International Institute of Cardiac Sciences", "Belle Vue Clinic", "Fortis Hospital", "Peerless Hospital", "B. P. Poddar Hospital & Medical Research Ltd"],
                "Chennai": ["Apollo Hospital", "Fortis Malar Hospital", "MIOT International", "Kauvery Hospital", "Billroth Hospital", "Sri Ramachandra Medical Center", "Madras Medical Mission", "Chettinad Hospital", "Government General Hospital", "Madurai Medical College Hospital"],
                "Hyderabad": ["Apollo Hospital", "Yashoda Hospital", "Care Hospitals", "KIMS Hospital", "Sunshine Hospitals", "Virinchi Hospitals", "Continental Hospitals", "MaxCure Hospitals", "Aware Global Hospitals", "Aster Prime Hospitals"],
                "Ahmedabad": ["Apollo Hospital", "Sterling Hospital", "CIMS Hospital", "Shalby Hospitals", "Narayana Multispeciality Hospital", "Zydus Hospital", "HCG Cancer Centre", "SAL Hospital", "GCS Medical College, Hospital & Research Centre", "HCG Hospitals"],
                "Pune": ["Sahyadri Hospital", "Ruby Hall Clinic", "Jehangir Hospital", "Deenanath Mangeshkar Hospital", "KEM Hospital", "Columbia Asia Hospital", "Poona Hospital and Research Centre", "Inlaks and Budhrani Hospital", "Noble Hospital", "Surya Hospital"],
                "Jaipur": ["Apollo Hospital", "Fortis Escorts Hospital", "Manipal Hospital", "Eternal Hospital", "Bhandari Hospital and Research Centre", "Narayana Multispeciality Hospital", "Sawai Man Singh Hospital", "SMS Hospital", "Monilek Hospital and Research Centre", "Metro MAS Hospital"],
                "Lucknow": ["Apollo Hospital", "Ram Manohar Lohia Hospital", "King George's Medical University", "Dr. Ram Manohar Lohia Institute of Medical Sciences", "Samar Hospital", "Shalimar Hospital", "Shekhar Hospital", "Uma Hospital", "Raj Hospital", "Brijraj Hospital"],
                "Surat": ["Apollo Hospital", "Dhiraj Hospital", "Dhanvantari Hospital", "Sahara Hospital", "Kiran Hospital", "Anand Hospital", "Vivekanand Hospital", "Sanjivani Hospital", "Apple Hospital", "Prannath Hospital"],
                "Nagpur": ["W ockhardt Hospitals", "Orange City Hospital & Research Institute", "CIIMS Hospital", "KRIMS Hospital", "Neuron Hospital", "New Era Hospital", "Guruji Hospital", "Ikon Hospital", "Avanti Institute of Cardiology Pvt. Ltd.", "Krishna Hospital & ICU"],
                "Indore": ["Bombay Hospital", "Apollo Hospitals", "CHL Hospitals", "Medanta Hospital", "Choithram Hospital and Research Centre", "Sudarshan Hospital", "Shreemati Laxmibai Institute of Medical Science", "Index Hospital", "Mayank Hospital", "Arihant Hospital"],
                "Thane": ["Jupiter Hospital", "Bethany Hospital", "Currae Hospital", "Fortis Hospital", "Hiranandani Hospital", "Kaushalya Medical Foundation Trust Hospital", "Noble Hospital", "Bethesda Hospital", "Horizon Prime Hospital", "Highland Super Speciality Hospital"],
                "Bhopal": ["Bansal Hospital", "Chirayu Medical College and Hospital", "Bhopal Memorial Hospital & Research Centre", "Noble Multispeciality Hospital", "Jawaharlal Nehru Cancer Hospital & Research Centre", "Care Hospitals", "Narmada Trauma Centre", "RKDF Medical College Hospital & Research Centre", "Peoples General Hospital", "Navodaya Cancer Hospital & Research Institute"],
                "Visakhapatnam": ["Apollo Hospital", "Seven Hills Hospital", "Care Hospitals", "Queen's NRI Hospitals", "Indus Hospital", "Sanghvi Institute of Management & Science Hospital", "NRI Hospitals", "Bloom Hospitals", "Mahatma Gandhi Cancer Hospital & Research Institute", "M.K.G. Memorial Multispeciality Hospital"],
                "Pimpri-Chinchwad": ["Yashwantrao Chavan Memorial Hospital", "Aditya Birla Memorial Hospital", "Chaitanya Hospital", "Spandan Hospital", "Vatsalya Hospital", "Lifeline Multispeciality Hospital", "Surya Hospital", "Om Hospital", "Sterling Multispeciality Hospital", "Pune Hospital"],
                "Patna": ["AIIMS Patna", "Jawaharlal Nehru Medical College & Hospital", "Patna Medical College and Hospital", "Nalanda Medical College and Hospital", "Indira Gandhi Institute of Medical Sciences", "Ford Hospital", "Ruban Memorial Hospital", "Rajeshwar Hospital", "Panacea Hospital", "Sanjeevani Hospital"],
                "Vadodara": ["Sterling Hospital", "Nirmal Hospital", "Spandan Hospital", "Apex Hospital", "Dhruvin Hospital", "Kailash Hospital", "Gandhi Hospital", "The General Hospital", "Vadodara Institute of Neurological Sciences", "Vadodara Institute of Ophthalmology"],
                "Ghaziabad": ["Yashoda Super Speciality Hospital", "Columbia Asia Hospital", "Shanti Gopal Hospital", "Sanjeevani Hospital", "Sarvodaya Hospital & Research Centre", "Pushpanjali Crosslay Hospital", "MMG Hospital", "Max Super Speciality Hospital", "Narinder Mohan Hospital & Heart Centre", "Gargi Hospital"],
                "Ludhiana": ["Christian Medical College & Hospital", "Dayanand Medical College & Hospital", "Fortis Hospital", "Sarabha Dental College & Hospital", "Satguru Partap Singh Apollo Hospitals", "Deep Hospital", "Rattan Multispeciality Hospital", "Suman Hospital", "Ivy Hospital", "Guru Teg Bahadur Hospital"],
                "Agra": ["Pushpanjali Hospital and Research Centre", "UP Rural Institute of Medical Sciences & Research", "Paras JK Hospital", "Manas Hospital", "Ankur Hospital", "Mansarovar Hospital", "Om Hospital", "Pawan Hospital", "Shanti Mangalick Hospital", "Lotus Super Speciality Hospital"],
                "Nashik": ["Wockhardt Hospital", "Apollo Hospital", "Chaitanya Hospital", "Lilavati Hospital", "Suyash Hospital", "Pooja Hospital", "Pranav Hospital", "Krishna Hospital", "Arihant Hospital", "Life Care Hospital"],
                "Faridabad": ["Fortis Escorts Hospital", "Asian Institute of Medical Sciences", "Sarvodaya Hospital & Research Centre", "Qrg Central Hospital & Research Centre", "Metro Hospital & Heart Institute", "Royal Hospital", "Park Hospital", "Esi Hospital", "Gulab Devi Chest Hospital", "Amrit Dhara Hospital"],
                "Meerut": ["Chameli Devi Hospital", "Subharti Medical College", "Agrawal Eye Hospital", "Lisie Hospital", "Anand Hospital", "Kishan Eye Hospital", "Lions Eye Hospital", "Radhika Hospital", "Sona Eye Hospital", "Sita Eye Hospital"],
                "Rajkot": ["Sterling Hospital", "Pandit Deendayal Upadhyay Hospital", "Ami Surgical Hospital", "Bhakti Multispeciality Hospital", "Punit Hospital", "Nirali Hospital", "Niramaya Hospital", "Punjabi Surgical Hospital", "Bhagwat Hospital", "Raj Surgical Hospital"],
                "Kalyan-Dombivli": ["Balaji Hospital", "Davakhar Hospital", "Icon Hospital", "Matoshree Hospital", "Ratnadeep Hospital", "Sanjeevani Hospital", "Siddhivinayak Hospital", "Shree Hospital", "Vedant Hospital", "Vimal Hospital"],
                "Vasai-Virar": ["Aadinath ENT Surgical Hospital", "BAPS Pramukh Swami Hospital", "Dahisar Accident Hospital", "Dr. Sonawane Hospital", "Golden Park Hospital", "Kasliwal's Cardiac Care Hospital", "Mediworld Multi-speciality Hospital", "Pragati Hospital", "Sanjivani Children Hospital", "Suyash Surgical and Maternity Hospital"],
                "Varanasi": ["Heritage Hospital", "Kashi Hospital", "Lahiri Mahasaya Hospital", "Maa Gayatri Hospital", "Pandit Deendayal Upadhyay Hospital", "Prime Hospital", "Saket Hospital", "Shree Mahadev Hospital", "Sri Anand Hospital", "Tirupati Hospital"],
                "Srinagar": ["Sher-i-Kashmir Institute of Medical Sciences", "Soura Institute of Medical Sciences", "Jhelum Valley Medical College", "Government Medical College", "SKIMS Medical College", "Bone and Joint Hospital", "Al-Amin Hospital", "Khyber Medical Institute", "Dr. Irfan Hospital", "SMHS Hospital"]
            
        }

        for area, hospitals in data.items():
            area, created = Area.objects.get_or_create(name=area)
            for hospital_name in hospitals:
                Hospitals.objects.get_or_create(text=hospital_name, area=area)

        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
# class Area(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Hospitals(models.Model):
#     area = models.ForeignKey(Area, on_delete=m