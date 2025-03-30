
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plant_disease_detector.settings')
django.setup()

from disease_app.models import PlantDisease

# Sample disease data
disease_data = [
    {
        'name': 'Apple___Apple_scab',
        'plant_type': 'Apple',
        'symptoms': 'Olive-green to brown spots on leaves and fruit. Infected leaves may twist, curl, and fall early. Fruit may be deformed and crack.',
        'causes': 'Fungal pathogen Venturia inaequalis. Favored by cool, wet weather during spring and early summer.',
        'treatment': 'Apply fungicides early in the growing season. Remove and destroy fallen leaves in autumn. Prune the tree to improve air circulation.',
        'prevention': 'Select resistant apple varieties. Apply fungicidal spray according to a regular schedule starting at bud break. Ensure proper spacing between trees for good air circulation.',
    },
    {
        'name': 'Apple___Black_rot',
        'plant_type': 'Apple',
        'symptoms': 'Circular purple spots on leaves. Rotting fruit with concentric rings of black pycnidia. Cankers on branches and limbs.',
        'causes': 'Fungal pathogen Botryosphaeria obtusa. Often enters through wounds or dead tissue.',
        'treatment': 'Prune out dead or diseased wood. Apply fungicides during the growing season. Remove mummified fruit and cankers.',
        'prevention': 'Maintain tree vigor with proper fertilization. Remove wild brambles near the orchard. Control insects that create wounds. Prune trees during dry weather.',
    },
    {
        'name': 'Corn_(maize)___Common_rust_',
        'plant_type': 'Corn (Maize)',
        'symptoms': 'Small, circular to elongated, powdery, cinnamon-brown pustules on both leaf surfaces. Severe infections can cause leaves to yellow and die early.',
        'causes': 'Fungal pathogen Puccinia sorghi. Spores are windborne from southern regions. Favored by humid conditions and moderate temperatures (60-77°F).',
        'treatment': 'Apply fungicides when disease first appears. In commercial settings, foliar fungicides may be economically justified.',
        'prevention': 'Plant resistant corn hybrids. Early planting can help avoid severe infections. Crop rotation may provide limited benefits since spores can travel long distances.',
    },
    {
        'name': 'Corn_(maize)___Northern_Leaf_Blight',
        'plant_type': 'Corn (Maize)',
        'symptoms': 'Long, elliptical, grayish-green to tan lesions on leaves. Lesions typically begin on lower leaves and work upward. Under humid conditions, dark olive-green spores form on lesions.',
        'causes': 'Fungal pathogen Exserohilum turcicum. Disease development favored by moderate temperatures (65-80°F) and extended periods of leaf wetness.',
        'treatment': 'Apply fungicides when disease symptoms first appear. In severe cases, multiple applications may be necessary.',
        'prevention': 'Plant resistant hybrids. Practice crop rotation with non-host crops. Tillage to bury infected crop residue. Early planting to avoid favorable conditions during critical growth stages.',
    },
    {
        'name': 'Apple___healthy',
        'plant_type': 'Apple',
        'symptoms': 'No disease symptoms present. Leaves appear normal with vibrant green color. No spots, lesions, or abnormal growth patterns.',
        'causes': 'Not applicable - this is a healthy plant.',
        'treatment': 'No treatment necessary. Continue regular orchard management practices.',
        'prevention': 'Maintain good orchard hygiene. Ensure proper nutrition and watering. Monitor for early signs of disease or pest problems.',
    },
    {
        'name': 'Corn_(maize)___healthy',
        'plant_type': 'Corn (Maize)',
        'symptoms': 'No disease symptoms present. Leaves show normal green coloration with no lesions or discoloration. Plant exhibits normal growth pattern.',
        'causes': 'Not applicable - this is a healthy plant.',
        'treatment': 'No treatment necessary. Continue regular crop management practices.',
        'prevention': 'Maintain good field hygiene. Ensure proper nutrition and irrigation. Regular monitoring for early detection of potential issues.',
    },
]

def populate_database():
    print("Populating database with plant disease information...")
    
    for disease_info in disease_data:
        disease, created = PlantDisease.objects.get_or_create(
            name=disease_info['name'],
            defaults={
                'plant_type': disease_info['plant_type'],
                'symptoms': disease_info['symptoms'],
                'causes': disease_info['causes'],
                'treatment': disease_info['treatment'],
                'prevention': disease_info['prevention'],
            }
        )
        
        if created:
            print(f"Added: {disease.name}")
        else:
            print(f"Already exists: {disease.name}")
    
    print("Database population completed!")

if __name__ == '__main__':
    populate_database()