# populate_db.py

from register.models import Area, Hospital

data = {
    "Faridabad": ["Fortis Escorts Hospital", "Asian Institute of Medical Sciences", "Sarvodaya Hospital & Research Centre", "Qrg Central Hospital & Research Centre", "Metro Hospital & Heart Institute", "Royal Hospital", "Park Hospital", "Esi Hospital", "Gulab Devi Chest Hospital", "Amrit Dhara Hospital"],
    "Meerut": ["Chameli Devi Hospital", "Subharti Medical College", "Agrawal Eye Hospital", "Lisie Hospital", "Anand Hospital", "Kishan Eye Hospital", "Lions Eye Hospital", "Radhika Hospital", "Sona Eye Hospital", "Sita Eye Hospital"],
}

for city, hospitals in data.items():
    area, created = Area.objects.get_or_create(name=city)
    for hospital_name in hospitals:
        Hospital.objects.create(name=hospital_name, area=area)
