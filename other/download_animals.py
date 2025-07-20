import os
import requests

# أنشئ مجلد لتخزين الصور
os.makedirs("bird_icons", exist_ok=True)

# قائمة أسماء الطيور بناءً على data-type (بدون animal_ في البداية لأنه سيتم إضافتها تلقائيًا)
bird_names = [
    "bluejay", "cardinal", "chicken_leghorn", "prairiechicken", "californiancondor",
    "cormorant_doublecrested", "cormorant_neotropic", "cranewhooping_whooping", "crow",
    "eagle_golden", "egret_reddish", "goosecanada", "hawk_ferruginous", "heron_greatblue",
    "loon_pacific", "oriole_baltimore", "oriole_hooded", "owl_great", "owl_californian",
    "pelican_white", "pheasant_ringneck", "pigeon_bandtailed", "quail", "raven", "robin",
    "rooster_dominique", "seagull_herring", "songbird_scarlet", "songbird_western",
    "sparrow_eurasian", "roseatespoonbill", "turkey_eastern", "vulture_eastern",
    "vulture_western", "cedarwaxwing", "woodpecker_redbellied"
]

base_url = "https://jeanropke.github.io/RDOMap/assets/images/icons/game/animals/"

for name in bird_names:
    file_name = f"animal_{name}.png"
    url = base_url + file_name
    dest = os.path.join("bird_icons", file_name)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(dest, "wb") as f:
                f.write(response.content)
            print(f"✅ Saved: {file_name}")
        else:
            print(f"❌ Failed: {file_name} (Not Found)")
    except Exception as e:
        print(f"⚠️ Error downloading {file_name}: {e}")
