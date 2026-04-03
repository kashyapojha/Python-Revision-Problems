import tkinter as tk
from tkinter import ttk, scrolledtext
import threading

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

# ── State data ─────────────────────────────────────────────────────────────────

STATES = {
    "Rajasthan": {
        "emoji": "🏯", "tag": "Forts & Deserts",
        "Overview": "Rajasthan — the Land of Kings — is India's largest state by area, sprawling over 342,239 sq km. It is famed for massive forts, colorful culture, golden deserts and royal palaces. The state greets visitors with its traditional welcome song 'Padhaaro Maare Desh.' Its folk dance, music, turbans and camels create a living cultural spectacle unlike anywhere else in the world.",
        "Food": "Must-try dishes: Dal Baati Churma, Laal Maas, Ghewar, Ker Sangri, Bajre ki Khichdi, Pyaaz Kachori, Gatte ki Sabzi.\n\nRajasthani cuisine is rich, spicy and designed for desert survival. Dal Baati Churma is the state's most iconic dish — baked wheat balls served with lentils and sweet churma. Laal Maas is a fiery red mutton curry. Ghewar is a honeycomb-shaped dessert popular at festivals.",
        "Places to Visit": "Top places: Amber Fort (Jaipur), Hawa Mahal, Jaisalmer Fort, Mehrangarh Fort (Jodhpur), Udaipur City Palace, Ranthambore National Park, Pushkar Lake, Chokhi Dhani.\n\nJaipur — the Pink City — is the crown jewel. Jaisalmer's golden sandstone fort rises from the Thar Desert. Udaipur, the City of Lakes, is among the most romantic cities in India. Ranthambore is one of the best places to spot tigers in the wild.",
        "Best Time": "October to March is ideal — cool and pleasant. Avoid May–June when temperatures soar above 45°C. The Pushkar Camel Fair (November) and Jaipur Literature Festival (January) are unmissable events.",
        "Fun Facts": "• India's largest state by area\n• Home to the only hill fort listed as a UNESCO World Heritage Site — Chittorgarh\n• The Thar Desert covers 60% of Rajasthan\n• Jaipur was the world's first planned city (1727 AD)\n• Rajasthan has more forts and palaces than any other Indian state",
    },
    "Gujarat": {
        "emoji": "🦁", "tag": "Desert & Lions",
        "Overview": "Situated at India's extreme western boundary, Gujarat is the only home of pure Asiatic Lions in the world, houses the world's largest salt desert (Rann of Kutch), and is the birthplace of both Mahatma Gandhi and Sardar Vallabhbhai Patel. Its coastline stretches over 1,600 km — the longest of any Indian state.",
        "Food": "Must-try dishes: Dhokla, Thepla, Fafda-Jalebi, Undhiyu, Khandvi, Gujarati Thali, Mohanthal.\n\nGujarati cuisine is predominantly vegetarian, subtly sweet and beautifully balanced. The classic Gujarati Thali is a feast of small portions covering every taste. Undhiyu — a mixed vegetable dish slow-cooked underground — is prepared especially in winter. Fafda-Jalebi is the beloved Sunday morning breakfast.",
        "Places to Visit": "Top places: Gir National Park, Rann of Kutch, Dwarka Temple, Somnath Temple, Statue of Unity, Rani ki Vav (Patan), Sabarmati Ashram, Marine National Park (Jamnagar).\n\nThe Rann of Kutch transforms into a dazzling white salt desert in winter. The Statue of Unity — the world's tallest statue — stands at 182 metres. Rani ki Vav is a UNESCO-listed stepwell of breathtaking intricacy.",
        "Best Time": "October to March is perfect. The Rann Utsav (November–February) is a cultural highlight. Navratri (September/October) is celebrated with the Garba dance — now a UNESCO Intangible Cultural Heritage.",
        "Fun Facts": "• Gujarat has India's longest coastline at over 1,600 km\n• Home to the world's only wild Asiatic Lions\n• The Statue of Unity is the world's tallest statue at 182 metres\n• Surat processes 90% of the world's diamonds\n• First Indian state to prohibit alcohol (1960)",
    },
    "Kerala": {
        "emoji": "🌴", "tag": "Backwaters & Beaches",
        "Overview": "Kerala — 'God's Own Country' — stretches along India's southwestern Malabar Coast. Named one of the ten paradises of the world by National Geographic Traveler, it is a treasure of backwaters, tea gardens, spice plantations, tropical beaches and ancient Ayurveda tradition. It consistently tops India's Human Development Index and literacy rankings.",
        "Food": "Must-try dishes: Sadya (Kerala feast on banana leaf), Appam with Stew, Fish Molee, Karimeen Pollichathu, Puttu and Kadala Curry, Kerala Prawn Curry, Payasam.\n\nKerala cuisine is defined by coconut, spices and seafood. The Sadya — a traditional vegetarian feast served on a banana leaf with 20+ dishes — is the pinnacle of Kerala culinary art. Karimeen Pollichathu (pearl spot fish wrapped in banana leaf) is a local delicacy.",
        "Places to Visit": "Top places: Alleppey Backwaters, Munnar Tea Gardens, Periyar Wildlife Sanctuary, Kovalam Beach, Varkala Cliff Beach, Fort Kochi, Wayanad, Thekkady.\n\nAlleppey — the 'Venice of the East' — is famous for houseboat cruises through tranquil backwaters. Munnar's rolling hills of emerald tea gardens are breathtaking. Fort Kochi blends Portuguese, Dutch and British colonial heritage.",
        "Best Time": "September to March is peak season. Onam festival (August/September) is the grandest celebration — snake boat races, flower rangoli and feasts. The monsoon (June–August) is great for Ayurveda treatments.",
        "Fun Facts": "• 100% literacy rate — highest in India\n• Named 'God's Own Country' by the tourism board\n• Kalaripayattu (world's oldest martial art) originated in Kerala\n• Kerala produces 97% of India's rubber\n• Kathakali dance form is one of India's classical dance traditions",
    },
    "Uttar Pradesh": {
        "emoji": "🕌", "tag": "Taj Mahal & Heritage",
        "Overview": "Uttar Pradesh — India's most populous state — is home to the Taj Mahal and the ancient city of Varanasi — one of the oldest continuously inhabited cities on earth. It is the origin of both Buddhism and Jainism. Cities like Lucknow preserve the refined Nawabi culture of the Mughal era.",
        "Food": "Must-try dishes: Lucknowi Biryani (Dum Biryani), Tunday Kabab, Petha (Agra), Banarasi Paan, Malai Makhan, Bedai Sabzi, Tehri.\n\nUP cuisine is a glorious blend of Mughal grandeur and rustic cooking. Lucknow's Dum Biryani and Tunday Kabab are internationally famous. Agra's Petha — a translucent sweet made from white pumpkin — is a must-buy souvenir.",
        "Places to Visit": "Top places: Taj Mahal (Agra), Varanasi Ghats, Agra Fort, Fatehpur Sikri, Sarnath Buddhist Site, Vrindavan & Mathura, Lucknow Bara Imambara, Dudhwa National Park.\n\nThe Taj Mahal needs no introduction. Varanasi's ghats at sunrise are a profoundly spiritual experience. Fatehpur Sikri is a ghost Mughal city frozen in the 16th century.",
        "Best Time": "October to March is ideal. The Taj Mahal on a full moon night is a once-in-a-lifetime experience. Kumbh Mela at Prayagraj (every 12 years) is the world's largest human gathering.",
        "Fun Facts": "• Uttar Pradesh is India's most populous state\n• The Taj Mahal took 22 years and 20,000 workers to build\n• Varanasi is one of the world's oldest living cities (3,000+ years)\n• Buddha delivered his first sermon at Sarnath in UP\n• UP produces the most sugarcane in India",
    },
    "Goa": {
        "emoji": "🏖️", "tag": "Beaches & Nightlife",
        "Overview": "India's smallest state by area, Goa is a former Portuguese colony that has become India's premier beach and party destination. Its unique Indo-Portuguese culture, vibrant nightlife, stunning churches and golden beaches attract over 8 million tourists annually. Goa is visibly different from the rest of India — in food, architecture and attitude.",
        "Food": "Must-try dishes: Fish Curry Rice, Prawn Balchão, Bebinca, Xacuti, Chouriço, Feni (cashew liquor), Pork Vindaloo.\n\nGoan food is a tantalising marriage of Indian spices and Portuguese techniques. Fish Curry Rice is the everyday staple. Bebinca is a layered coconut dessert and the queen of Goan sweets. Feni — distilled from cashew apples or coconut — is Goa's beloved local spirit.",
        "Places to Visit": "Top places: Calangute & Baga Beach, Palolem Beach, Old Goa Churches (UNESCO), Dudhsagar Waterfalls, Fort Aguada, Anjuna Flea Market, Spice Plantations, Chapora Fort.\n\nPalolem is Goa's most picturesque crescent beach. Old Goa's Bom Jesus Basilica is a UNESCO World Heritage Site. Dudhsagar Falls is one of India's tallest waterfalls.",
        "Best Time": "November to February is peak season. The Goa Carnival (February/March) is a riot of colour and music. Monsoon brings lush greenery but most beach shacks close.",
        "Fun Facts": "• Goa has the highest per capita income among Indian states\n• Two UNESCO World Heritage Sites — Old Goa churches and convents\n• Feni is the only Indian spirit with a Geographical Indication tag\n• Goa was under Portuguese rule for 451 years (1510–1961)\n• The state has 30+ beaches — a beach for every day of the month",
    },
    "Jammu & Kashmir": {
        "emoji": "🏔️", "tag": "Paradise Valley",
        "Overview": "Jammu & Kashmir — the crown of India — is a breathtaking tapestry of snow-capped peaks, serene lakes, fragrant saffron fields and Mughal gardens. Known as 'Paradise on Earth,' the Kashmir Valley sits at about 1,600m elevation. Ladakh, its eastern region, is a stark and magnificent high-altitude desert.",
        "Food": "Must-try dishes: Rogan Josh, Wazwan (36-course feast), Yakhni, Dum Aloo, Kahwa (saffron tea), Modur Pulao, Seekh Kabab.\n\nKashmiri cuisine is a rich aromatic tradition centred on slow-cooked meats in yoghurt and spice gravies. The Wazwan is a ceremonial 36-course feast — the ultimate expression of Kashmiri hospitality. Kahwa — saffron, cardamom and almond tea — is perfect for the cold mountain air.",
        "Places to Visit": "Top places: Dal Lake & Shikara Rides, Gulmarg (skiing & gondola), Pahalgam Valley, Sonamarg Glacier, Leh Palace (Ladakh), Pangong Lake, Vaishno Devi Temple, Mughal Gardens.\n\nDal Lake with floating gardens and wooden houseboats is Kashmir's most iconic image. Gulmarg has Asia's highest gondola and is India's premier ski resort. Pangong Lake changes colour from blue to green throughout the day.",
        "Best Time": "April–June and September–October for the valley. December–February for skiing at Gulmarg. Ladakh is best from June to September.",
        "Fun Facts": "• Kashmir produces over 90% of India's saffron\n• Dal Lake is home to 50,000+ people living on floating houseboats\n• Gulmarg has Asia's highest and longest cable car\n• Pangong Lake sits at 4,350m altitude\n• Kashmir's Pashmina wool is among the world's finest textiles",
    },
    "Karnataka": {
        "emoji": "🏛️", "tag": "Silk & Sandalwood",
        "Overview": "Karnataka — the land of sandalwood, silks and spices — is a vibrant mosaic of ancient temple towns, cosmopolitan IT hubs, misty hill stations and pristine coastline. It is home to the UNESCO-listed ruins of Hampi, the magnificent Mysore Palace, and the tech metropolis of Bengaluru. Karnataka produces 70% of India's coffee.",
        "Food": "Must-try dishes: Bisi Bele Bath, Masala Dosa (originated here), Ragi Mudde, Coorg Pandi Curry, Mysore Pak, Neer Dosa, Mangalorean Fish Curry.\n\nKarnataka's cuisine varies dramatically by region. Udupi gave the world the masala dosa. Mysore Pak — a rich ghee-and-gram flour fudge — was invented in the Mysore royal kitchen. Coorg's Pandi (pork) Curry is a bold tribal specialty.",
        "Places to Visit": "Top places: Hampi (UNESCO), Mysore Palace, Coorg (Kodagu), Jog Falls, Badami Caves, Chikmagalur Coffee Estates, Bandipur National Park, Gokarna Beach.\n\nHampi — the ruined capital of the Vijayanagara Empire — is a surreal landscape of boulder-strewn hills and magnificent stone temples. Jog Falls is India's second highest waterfall.",
        "Best Time": "October to March. Mysore's Dasara festival (October) is Karnataka's grandest spectacle — the Mysore Palace is illuminated by 100,000 light bulbs.",
        "Fun Facts": "• Karnataka produces 70% of India's coffee\n• Bengaluru is Asia's fastest growing tech city\n• Hampi was the second largest city in the world in the 14th century\n• ISRO (Indian Space Research Organisation) is headquartered in Bengaluru\n• Karnataka has the highest number of UNESCO World Heritage Sites in South India",
    },
    "Himachal Pradesh": {
        "emoji": "❄️", "tag": "Snow & Temples",
        "Overview": "Himachal Pradesh — 'the Land of Snow-capped Mountains' — offers everything from apple orchards and cedar forests to alpine meadows and glaciated peaks. It is called 'Dev Bhoomi' (Land of Gods) for its extraordinary density of ancient temples. The state is also the adventure capital of India.",
        "Food": "Must-try dishes: Dham (Himachali feast), Siddu (steamed bread), Chha Gosht, Babru (black gram kachori), Aktori (buckwheat pancake), Madra (chickpea curry), Kullu Trout.\n\nHimachali cuisine is hearty mountain food. The Dham is a traditional feast served at celebrations — rice, dal, rajma, curd and meetha — always cooked by Brahmin cooks. Siddu is a steamed bread stuffed with poppy seeds or walnuts, eaten with ghee.",
        "Places to Visit": "Top places: Shimla, Manali & Rohtang Pass, Dharamsala & McLeodGanj, Spiti Valley, Kullu Valley, Kasol, Great Himalayan National Park, Khajjiar (Mini Switzerland).\n\nShimla, the former summer capital of British India, retains its colonial charm. Spiti Valley is a remote high-altitude cold desert. McLeodGanj is the residence of the Dalai Lama.",
        "Best Time": "March–June for hill stations and trekking. December–February for snow and skiing at Solang Valley. Spiti is only accessible May–October.",
        "Fun Facts": "• Himachal produces 25% of India's apples\n• The Kugti Wildlife Sanctuary shelters the rare snow leopard\n• Khajjiar is known as India's Mini Switzerland\n• Shimla was the summer capital of British India\n• The state has over 2,000 temples and monasteries",
    },
    "Punjab": {
        "emoji": "⚔️", "tag": "Five Rivers & Sikhs",
        "Overview": "Punjab — the land of five rivers — is the agricultural powerhouse of India, producing 40–50% of India's wheat and rice. It is the spiritual home of Sikhism and the birthplace of Guru Nanak Dev Ji. The Golden Temple in Amritsar is the holiest Sikh shrine and reportedly the most visited place in India — surpassing even the Taj Mahal.",
        "Food": "Must-try dishes: Makki di Roti & Sarson da Saag, Amritsari Kulcha, Butter Chicken (invented in Punjab), Chole Bhature, Lassi, Dal Makhani, Pindi Chhole.\n\nPunjabi food is rich, generous and unapologetic. Butter Chicken and Dal Makhani — now global sensations — were invented in Punjab. The classic winter meal of Makki di Roti and Sarson da Saag with white butter is the soul of rural Punjab.",
        "Places to Visit": "Top places: Golden Temple (Amritsar), Jallianwala Bagh, Wagah Border Ceremony, Anandpur Sahib, Qila Mubarak (Patiala), Maharaja Ranjit Singh Museum, Gobindgarh Fort.\n\nThe Golden Temple — covered in 750 kg of gold — feeds 100,000 people daily for free. The Wagah Border ceremony at sunset is a spectacular display of nationalism.",
        "Best Time": "October to March. Lohri (January) and Baisakhi (April 13) are Punjab's most vibrant festivals — celebrated with Bhangra dancing and bonfires.",
        "Fun Facts": "• The Golden Temple feeds 100,000 people free daily — the world's largest free kitchen\n• Punjab contributes 40–50% of India's wheat to the national grain pool\n• Butter Chicken was invented at Moti Mahal restaurant by a Punjabi migrant\n• Bhangra dance originated in Punjab and is now a global phenomenon\n• Punjab has one of the highest tractor densities in the world",
    },
    "West Bengal": {
        "emoji": "🍵", "tag": "Darjeeling & Culture",
        "Overview": "West Bengal is the cultural capital of India — the home of Rabindranath Tagore, Satyajit Ray and Amartya Sen. It stretches from the Himalayan foothills of Darjeeling to the mangrove forests of the Sundarbans Delta. Kolkata's Durga Puja is a UNESCO Intangible Cultural Heritage.",
        "Food": "Must-try dishes: Rosogolla (originated here), Macher Jhol (fish curry), Shorshe Ilish (hilsa in mustard), Luchi & Aloor Dom, Mishti Doi (sweet yoghurt), Kolkata Biryani, Puchka.\n\nBengali cuisine is an art form built around fish, mustard oil, panch phoron spices and milk-based sweets. Ilish (hilsa) is worshipped as a delicacy. Kolkata's puchka (pani puri) is considered the best in India.",
        "Places to Visit": "Top places: Darjeeling (toy train + tea estates), Sundarbans National Park, Victoria Memorial (Kolkata), Howrah Bridge, Bishnupur Terracotta Temples, Digha & Mandarmani Beach, Hazarduari Palace, Kalimpong.\n\nThe Sundarbans is the world's largest mangrove delta and home to the Royal Bengal Tiger. The Darjeeling Himalayan Railway (toy train) is a UNESCO World Heritage Site.",
        "Best Time": "October to March. Durga Puja (October) is Kolkata's grandest festival — the city transforms into an open-air art gallery with spectacular pandals.",
        "Fun Facts": "• Kolkata's Durga Puja is a UNESCO Intangible Cultural Heritage\n• The Sundarbans has the world's largest tiger reserve\n• West Bengal produces 25% of India's rice\n• The Howrah Bridge has no nuts and bolts — held together by rivets\n• Darjeeling tea holds a Geographical Indication tag",
    },
    "Andhra Pradesh": {
        "emoji": "🏺", "tag": "Temples & Coastline",
        "Overview": "Andhra Pradesh is the land of spices, temples and the world's most visited pilgrimage site. Tirupati's Venkateswara Temple draws more visitors per day than the Vatican. The state has the longest eastern coastline in India and rich Buddhist heritage.",
        "Food": "Must-try dishes: Pesarattu (moong dal dosa), Gongura Mutton, Pulihora (tamarind rice), Bobbatlu (sweet flatbread), Kodi Pulusu (chicken curry), Chegodilu (rice crackers), Hyderabadi Biryani.\n\nAndhra cuisine is arguably the spiciest in India. Gongura (sorrel leaf) is unique to AP and used in chutneys, meats and pickles. Pesarattu — a green moong dal crepe — is the classic breakfast.",
        "Places to Visit": "Top places: Tirupati Venkateswara Temple, Araku Valley, Borra Caves, Visakhapatnam Beach, Amaravati Stupa, Nagarjunasagar Dam, Sri Sailam Wildlife Sanctuary, Lepakshi Temple.\n\nTirupati is the world's richest and most visited religious site. Araku Valley is a stunning hill station accessible by one of India's most scenic train journeys.",
        "Best Time": "October to March. Ugadi (Telugu New Year, March/April) and Sankranti (January) are the state's biggest festivals.",
        "Fun Facts": "• Tirupati is the world's richest temple, earning over ₹650 crore annually\n• Andhra Pradesh has the longest eastern coastline in India\n• Kuchipudi classical dance form originated in AP\n• The state produces the most chillies in India\n• AP was the first state to implement e-governance in India",
    },
    "Arunachal Pradesh": {
        "emoji": "🌿", "tag": "Hidden Shangri-La",
        "Overview": "Called 'The Land of the Dawn-Lit Mountains,' Arunachal Pradesh is India's largest north-eastern state and one of the most biodiverse regions on Earth. It is home to 26 major tribes and over 100 sub-tribes. Sunrise here is the first in India — the state sits at the easternmost tip of the country.",
        "Food": "Must-try dishes: Apong (rice beer), Thukpa (noodle soup), Pika Pila (bamboo shoot), Smoked Pork with Bamboo, Zan (finger millet porridge), Lukter (dried beef), Marua (millet beer).\n\nArunachali cuisine is flavoured by bamboo shoots, fermented foods and smoked meats — techniques born of the forest. Apong (rice beer) is central to every tribal celebration. The food is simple, earthy and deeply connected to the land.",
        "Places to Visit": "Top places: Tawang Monastery, Ziro Valley (UNESCO tentative), Namdapha National Park, Sela Pass, Mechuka Valley, Dirang, Pasighat, Daporijo.\n\nTawang Monastery — at 10,000 ft — is the largest in India and the second largest Buddhist monastery in the world. Ziro Valley is a picturesque plateau nominated for UNESCO World Heritage.",
        "Best Time": "October to April. Protected Area Permits are required for non-Indian nationals. The Ziro Music Festival (September) is a cult event for independent music lovers.",
        "Fun Facts": "• Arunachal Pradesh receives the first sunrise in India\n• Home to 26 major tribes each with distinct languages\n• Tawang Monastery is the second largest Buddhist monastery in the world\n• The state has over 500 species of orchids\n• Namdapha NP is one of the world's biodiversity hotspots",
    },
    "Assam": {
        "emoji": "🦏", "tag": "Rhinos & Brahmaputra",
        "Overview": "Assam — the Gateway to North-East India — is a land of mighty rivers, lush tea gardens, one-horned rhinos and extraordinary biodiversity. The Brahmaputra River is considered male in Hindu tradition. Assam tea is served in 150+ countries and the state produces 55% of India's total tea output.",
        "Food": "Must-try dishes: Masor Tenga (sour fish curry), Duck Meat Curry, Khar (alkaline curry), Pitha (rice cake), Bamboo Shoot Pickle, Jolpan (traditional breakfast), Assam Laksa.\n\nAssamese cuisine is light, minimal in spices but bold in flavour. Khar — an alkaline preparation made from banana peels — is uniquely Assamese. Masor Tenga is a sour fish curry made with tomatoes or elephant apple. Pitha rice cakes are made in dozens of varieties.",
        "Places to Visit": "Top places: Kaziranga National Park (UNESCO), Majuli River Island, Kamakhya Temple, Manas National Park, Sivasagar, Haflong Hill Station, Dibru-Saikhowa NP, Pobitora Wildlife Sanctuary.\n\nKaziranga is home to two-thirds of the world's one-horned rhinos. Majuli is the world's largest river island. Kamakhya Temple is one of the 51 Shakti Peethas.",
        "Best Time": "November to April. Bihu festival (April) is Assam's most joyous celebration — celebrated three times a year, it marks the Assamese New Year with dance, music and feasts.",
        "Fun Facts": "• Assam produces 55% of India's total tea\n• Kaziranga has 2,500+ one-horned rhinos — 70% of world's population\n• Majuli is the world's largest river island\n• The Brahmaputra is one of only three rivers to cross the Himalayas\n• Assam is home to the largest population of wild water buffalo",
    },
    "Bihar": {
        "emoji": "🕉️", "tag": "Buddhist Circuit",
        "Overview": "Bihar — derived from 'Vihara' (monastery) — was the cradle of two great religions (Buddhism and Jainism), the birthplace of India's first empire (Maurya), and home to the world's first university (Nalanda). The Buddha attained enlightenment at Bodh Gaya, right here in Bihar.",
        "Food": "Must-try dishes: Litti Chokha, Sattu Paratha, Dal Pitha, Makhana Kheer, Tilkut (sesame sweet), Chura Dahi, Khaja (flaky sweet).\n\nBihari cuisine is rustic, wholesome and deeply satisfying. Litti Chokha — roasted wheat balls stuffed with sattu served with charred brinjal chokha — is Bihar's most iconic dish. Bihar produces 90% of the world's makhana (fox nuts).",
        "Places to Visit": "Top places: Bodh Gaya (Buddha's enlightenment site), Nalanda University ruins, Rajgir, Vaishali, Vikramshila, Mahabodhi Temple (UNESCO), Patna Sahib Gurudwara, Valmiki National Park.\n\nThe Mahabodhi Temple is a UNESCO World Heritage Site. The Bodhi tree here is a direct descendant of the original tree under which the Buddha attained enlightenment.",
        "Best Time": "October to March. Chhath Puja (October/November) is Bihar's most sacred festival — celebrated on riverbanks at sunrise and sunset in a deeply moving ritual.",
        "Fun Facts": "• Bihar was home to Nalanda — world's first residential university\n• Bodh Gaya is one of the four holiest sites in Buddhism\n• Bihar produces 90% of the world's makhana (fox nuts)\n• Chandragupta Maurya founded India's first empire in Bihar\n• Vaishali is considered the world's first republic (6th century BC)",
    },
    "Chhattisgarh": {
        "emoji": "🌊", "tag": "Waterfalls & Tribes",
        "Overview": "Chhattisgarh — India's 10th largest state — is the country's tribal heartland. With 44% forest cover and 32% tribal population, it is one of India's most ecologically rich and culturally authentic destinations, home to the widest waterfall in India and the most diverse tribal arts in the country.",
        "Food": "Must-try dishes: Chila (rice flour crepe), Muthia (steamed rice dumplings), Fara, Bafauri (split pea fritters), Aamat (tribal curry), Bore Baasi (fermented rice), Sabudana Khichdi.\n\nChhattisgarhi cuisine is simple tribal food — largely rice-based, light on spices. Bore Baasi — overnight-soaked cooked rice eaten with curd and onion — is the tribal breakfast. Aamat is a tangy stew made with local vegetables and bamboo shoots.",
        "Places to Visit": "Top places: Chitrakote Falls (India's widest), Bastar, Kanker Palace, Sirpur Buddhist Site, Barnawapara Wildlife Sanctuary, Achanakmar Tiger Reserve, Bhoramdeo Temple, Tirathgarh Falls.\n\nChitrakote Falls — often called India's Niagara — swells to nearly 300 metres wide during monsoon. Bastar is a tribal cultural destination unlike anywhere else.",
        "Best Time": "October to March. The Bastar Dussehra (October) is unique — lasting 75 days, it is the world's longest festival rooted in tribal goddess tradition.",
        "Fun Facts": "• Chhattisgarh has India's widest waterfall — Chitrakote Falls\n• Bastar Dussehra is the world's longest festival (75 days)\n• The state has over 80% of flora not found elsewhere in India\n• Chhattisgarh produces 15% of India's steel\n• Home to rare tribal art forms including Gond and Baiga painting",
    },
    "Haryana": {
        "emoji": "🌾", "tag": "Battlefields & Culture",
        "Overview": "Haryana — the 'Abode of God' — is both ancient and modern. The battlefield of Kurukshetra, where the Mahabharata war was fought, lies in Haryana. Yet the state is also home to Gurugram (Gurgaon), one of India's fastest-growing tech and financial hubs. Haryana has produced more Olympic medals per capita than any other Indian state.",
        "Food": "Must-try dishes: Bajra Khichdi, Hara Dhania Cholia, Singri ki Sabzi, Methi Gajar, Kachri ki Chutney, Besan Masala Roti, Alsi ki Pinni.\n\nHaryanvi cuisine is simple, agricultural and deeply nourishing. It relies on seasonal produce, dairy and millets. Bajra (pearl millet) is the staple grain. Alsi ki Pinni — a sweet made from flaxseeds, jaggery and ghee — is a winter energy booster.",
        "Places to Visit": "Top places: Kurukshetra, Sultanpur National Park, Pinjore Gardens, Morni Hills, Panipat Museum, Surajkund Craft Fair, Tilyar Lake, Farrukhnagar Step Well.\n\nKurukshetra is one of India's most sacred sites. Surajkund Crafts Mela (February) is one of Asia's largest craft fairs. Sultanpur National Park near Gurugram is a birder's paradise with 250+ species.",
        "Best Time": "October to March. Geeta Jayanti at Kurukshetra (November/December) is a major spiritual event. Surajkund Crafts Mela (February) is unmissable for art and culture lovers.",
        "Fun Facts": "• Haryana is India's top producer of milk\n• The state won 8 of India's 12 medals at the 2020 Tokyo Olympics\n• Panipat witnessed three decisive battles that shaped Indian history\n• Gurgaon (Gurugram) hosts over 250 Fortune 500 companies\n• Haryana is home to India's largest solar power plant",
    },
    "Jharkhand": {
        "emoji": "💧", "tag": "Waterfalls & Forests",
        "Overview": "Jharkhand — 'Land of the Forest' — is one of India's richest states in minerals while also being home to some of the most beautiful waterfalls, dense Sal forests and vibrant tribal traditions. It is called the 'Ruhr of India' for its industrial wealth.",
        "Food": "Must-try dishes: Dhuska (rice & lentil pancake), Rugra (forest mushroom curry), Chilka Roti, Litti Chokha, Bamboo Shoot Curry, Handia (rice beer), Maro (millet porridge).\n\nJharkhand tribal cuisine is earthy and forest-dependent. Rugra — a wild mushroom found only in Sal forests — is a seasonal delicacy. Handia (rice beer) is consumed at every tribal celebration. Dhuska is a crispy fried bread made from soaked rice and lentils.",
        "Places to Visit": "Top places: Hundru Falls, Betla National Park, Netarhat (Queen of Chotanagpur), Jonha Falls, Deoghar Baidyanath Dham, Rajmahal Hills, Parasnath Hill, Dasam Falls.\n\nHundru Falls — 98 metres high — is one of India's most dramatic waterfalls. Netarhat is called the 'Queen of Chotanagpur' for its sweeping sunrises. Baidyanath Dham in Deoghar is one of the 12 Jyotirlingas.",
        "Best Time": "October to March for waterfalls and wildlife. Sarhul (March/April) and Karma (August/September) are the major tribal festivals — celebrated with singing, dancing and nature worship.",
        "Fun Facts": "• Jharkhand has the richest mineral reserves in India\n• Hundru Falls drops 98 metres — one of India's highest\n• The state has 28% of India's coal reserves\n• Parasnath Hill is the holiest site for Jains\n• Jharkhand produces the most lac (shellac) in the world",
    },
    "Madhya Pradesh": {
        "emoji": "🐯", "tag": "Tigers & Temples",
        "Overview": "Madhya Pradesh — the 'Heart of India' — has more UNESCO World Heritage Sites than any other Indian state and more tiger reserves than any other state. The Narmada River, one of India's seven sacred rivers, flows entirely through MP for 1,077 km.",
        "Food": "Must-try dishes: Dal Bafla, Poha Jalebi (Indore's famous breakfast), Bhutte ki Kees (grated corn), Chakki ki Shaak, Mawa Bati (sweet), Sabudana Khichdi, Shikanji (lemon cooler).\n\nIndore's food scene is legendary — Sarafa Bazaar and Chappan Dukan are famous food streets. Poha-Jalebi is Indore's signature breakfast. Dal Bafla is the local cousin of Rajasthan's Dal Baati.",
        "Places to Visit": "Top places: Khajuraho Temples (UNESCO), Sanchi Stupa (UNESCO), Bhimbetka Rock Caves (UNESCO), Kanha Tiger Reserve, Bandhavgarh National Park, Pachmarhi Hill Station, Mandu, Omkareshwar Jyotirlinga.\n\nKhajuraho's 10th-century temple sculptures are among the world's finest medieval Indian art. Bandhavgarh has the highest density of tigers in India.",
        "Best Time": "October to March. Tiger sighting is best in April–June. Khajuraho Dance Festival (February) is a classical arts extravaganza.",
        "Fun Facts": "• MP has 3 UNESCO World Heritage Sites — more than any other state\n• Bandhavgarh has the world's highest density of Bengal tigers\n• MP has the most tiger reserves in India (7 reserves)\n• Bhimbetka cave paintings are 30,000 years old\n• The Narmada River flows entirely through MP for 1,077 km",
    },
    "Maharashtra": {
        "emoji": "🏰", "tag": "Forts & Festivals",
        "Overview": "Maharashtra — India's second most populous and wealthiest state — is an extraordinary blend of Maratha glory, Bollywood glamour, Konkan coastline and the financial might of Mumbai. Shivaji Maharaj built a network of 300+ forts across the Western Ghats that remain symbols of pride.",
        "Food": "Must-try dishes: Vada Pav (Mumbai's burger), Misal Pav, Puran Poli, Modak (Ganesh's favourite), Kolhapuri Chicken, Sol Kadhi, Thali Peeth.\n\nVada Pav — a deep-fried potato dumpling in a bread roll — is Mumbai's beloved street food. Modak — a steamed rice dumpling stuffed with coconut and jaggery — is Lord Ganesha's favourite prepared by millions during Ganesh Chaturthi.",
        "Places to Visit": "Top places: Ajanta & Ellora Caves (UNESCO), Gateway of India (Mumbai), Lonavala & Mahabaleshwar, Shirdi, Kolhapur, Daulatabad Fort, Nashik (wine country), Tadoba Tiger Reserve.\n\nAjanta and Ellora — 2nd century BC to 10th century AD cave temples — are among humanity's greatest artistic achievements. Nashik is India's wine capital and also hosts the Kumbh Mela.",
        "Best Time": "October to February. Ganesh Chaturthi (August/September) is Maharashtra's most spectacular festival — Mumbai celebrates for 11 days with processions and immersion of thousands of Ganesha idols.",
        "Fun Facts": "• Maharashtra is India's wealthiest state by GDP\n• Mumbai is home to Bollywood — producing 1,000+ films per year\n• Ajanta Caves have paintings 2,000 years old, preserved without artificial light\n• Maharashtra has more Shiva temples than any other state\n• The Wari pilgrimage to Pandharpur draws 10 million people annually",
    },
    "Manipur": {
        "emoji": "🌺", "tag": "Polo & Floating Park",
        "Overview": "Manipur — 'the Jewel of India' — is celebrated for its classical dance (Manipuri dance), unique cuisine, spectacular landscapes and the world's only floating national park. The Loktak Lake is the largest freshwater lake in north-east India and home to the endangered Sangai deer.",
        "Food": "Must-try dishes: Eromba (fermented fish stew), Singju (raw salad), Chamthong (vegetable stew), Ngari (fermented fish), Paknam (steamed cake), Chak-hao Kheer (black rice pudding), Morok Metpa (chilli chutney).\n\nManipuri cuisine features fermented foods and fresh vegetables. Ngari (fermented fish) is the backbone of Manipuri cooking. Chak-hao (black rice) is a GI-tagged variety unique to Manipur.",
        "Places to Visit": "Top places: Loktak Lake, Keibul Lamjao (floating NP), Kangla Fort, Ima Keithel (women's market), Shirui Lily Festival (Ukhrul), Dzüko Valley, Moirang, Khonghampat Orchidarium.\n\nIma Keithel in Imphal is the world's only all-women market — over 3,000 women vendors — in operation for over 500 years. Dzüko Valley is a pristine alpine valley blanketed in seasonal wildflowers.",
        "Best Time": "October to February. The Shirui Lily Festival (May) celebrates the state flower found only in Shirui Hills. Yaosang (February/March) is Manipur's version of Holi — celebrated for 5 days.",
        "Fun Facts": "• Polo — the sport — originated in Manipur (1st century AD)\n• Keibul Lamjao is the world's only floating national park\n• Ima Keithel is the world's only all-women market (500+ years old)\n• Chak-hao (black rice) has a GI tag from Manipur\n• Manipuri dance is one of India's 8 classical dance forms",
    },
    "Meghalaya": {
        "emoji": "🌧️", "tag": "Wettest Place on Earth",
        "Overview": "Meghalaya — 'Abode of the Clouds' — is India's wettest state. Cherrapunjee (Sohra) and Mawsynram compete for the title of the world's wettest place. The state is home to the unique matrilineal Khasi, Jaintia and Garo tribes and the miraculous living root bridges.",
        "Food": "Must-try dishes: Jadoh (rice and pork), Tungrymbai (fermented soya beans), Doh Khleh (pork salad), Nakham Bitchi (dried fish soup), Putharo (rice cake), Minil Songa (steamed sticky rice), Sakin Gata (rice with sesame).\n\nMeghalayan cuisine is tribal and forest-based — pork, fermented soya beans and bamboo shoots dominate. Jadoh — a one-pot rice and pork dish — is the staple of the Khasi community. Tungrymbai has a pungent, deeply savoury flavour.",
        "Places to Visit": "Top places: Living Root Bridges (Cherrapunjee), Dawki River (crystal clear), Mawlynnong (Asia's cleanest village), Elephant Falls (Shillong), Ward's Lake, Nohkalikai Falls, Umiam Lake, Balpakram National Park.\n\nThe living root bridges — grown over 500 years by training tree roots — are remarkable bio-engineering. The Dawki River is so clear you can see the riverbed from a boat.",
        "Best Time": "October to May. Avoid monsoon for trekking but waterfalls are at their most dramatic. The Shillong Autumn Festival (October) and Cherry Blossom Festival (November) are beautiful cultural events.",
        "Fun Facts": "• Mawsynram and Cherrapunjee are the world's two wettest places\n• The living root bridges are grown, not built — over 500 years old\n• Meghalaya is one of three Indian states with a matrilineal society\n• Dawki River is so clear boats appear to float on air\n• Krem Puri is the world's longest sandstone cave at 31 km",
    },
    "Mizoram": {
        "emoji": "🎋", "tag": "Bamboo Forests & Mist",
        "Overview": "Mizoram — 'Land of the Hill People' — is a remote, pristine and deeply fascinating state in India's far north-east. Its rolling hills covered in bamboo and pine, clean towns and remarkably high literacy rate (91%+) make it feel unlike any other Indian state. The Mizo people are warm, deeply Christian and extraordinarily musical.",
        "Food": "Must-try dishes: Bai (boiled greens with pork), Vawksa Rep (smoked pork), Mizo Sawhchiar (rice porridge), Bamboo Shoot Fry, Chhum Han (steamed vegetables), Arsa Buhchiar (chicken porridge), Zu (rice wine).\n\nVawksa Rep — smoked pork — is the cornerstone of Mizo cooking. Bai is the everyday staple — boiled vegetables and pork with fermented soya beans. Zu (rice wine) is prepared at home for every festival.",
        "Places to Visit": "Top places: Phawngpui (Blue Mountain), Vantawng Falls (Mizoram's highest), Reiek Heritage Village, Champhai Valley, Palak Lake, Murlen National Park, Aizawl city views, Tam Dil Lake.\n\nPhawngpui — the Blue Mountain — is Mizoram's highest peak (2,157m) and sacred to the Mizo people. The Champhai Valley is a stunning highland plain known as the 'Rice Bowl of Mizoram.'",
        "Best Time": "October to March. Chapchar Kut (March) — Mizoram's most important festival — celebrates with traditional Cheraw (bamboo) dance. Mim Kut (October) marks the maize harvest.",
        "Fun Facts": "• Mizoram has 91%+ literacy — second highest in India\n• The state is over 90% Christian\n• Cheraw (bamboo dance) is Mizoram's most iconic cultural art form\n• Mizoram experiences the rare Mautam — bamboo flowering every 48 years\n• Phawngpui is called the Blue Mountain and is sacred to the Mizo people",
    },
    "Nagaland": {
        "emoji": "🦅", "tag": "Hornbill Festival",
        "Overview": "Nagaland — 'Land of the Nagas' — is a cultural treasure chest of 16 major tribes, each with distinct languages, dress, food and traditions. Known as the 'Land of Festivals,' it hosts the Hornbill Festival — one of Asia's most spectacular cultural events.",
        "Food": "Must-try dishes: Smoked Pork with Bamboo Shoot, Axone (fermented soya bean), Galho (rice-vegetable porridge), Zutho (rice beer), Akhuni Chutney, Naga Chilli (Raja Mircha) dishes.\n\nNaga cuisine is bold, smoky and intensely flavoured. Axone (fermented soya bean) is the foundation. The Bhut Jolokia (Ghost Pepper) — once the world's hottest chilli — grows here. Smoked meat is everywhere, with smoking techniques unique to each tribe.",
        "Places to Visit": "Top places: Hornbill Festival (Kisama), Kohima War Cemetery, Dzüko Valley, Pfütsero (highest town), Khonoma Green Village, Japfu Peak Trek, Longwa Village, Touphema Village Resort.\n\nThe Kohima War Cemetery honours Allied soldiers from WWII's fiercest battles. Khonoma is India's first green village. Longwa Village straddles the India-Myanmar border.",
        "Best Time": "October to March. The Hornbill Festival (December 1–10) is the unmissable event. Pre-book accommodation months in advance.",
        "Fun Facts": "• Nagaland is home to 16 major tribes each with distinct culture\n• The Ghost Pepper (Bhut Jolokia) — once world's hottest chilli — is from Nagaland\n• Kohima War Cemetery is one of the most moving WWII memorials in Asia\n• Khonoma is India's first green village\n• Longwa Village chief's house straddles the India-Myanmar international border",
    },
    "Odisha": {
        "emoji": "🎭", "tag": "Temples & Odissi Dance",
        "Overview": "Odisha — formerly Orissa — is home to the sacred Jagannath Temple at Puri, the erotic masterpieces of Konark Sun Temple and the serene Buddhist stupa at Dhauli. Odisha's Pattachitra paintings, Odissi classical dance and tribal crafts are internationally recognised art forms.",
        "Food": "Must-try dishes: Dalma (lentils with vegetables), Pakhala Bhaat (fermented rice), Machha Besara (fish in mustard), Chhena Poda (burnt cheese dessert), Rasgulla (GI tag), Santula (stir-fried vegetables), Mudhi Mansa (puffed rice with mutton).\n\nOdia cuisine is mild, health-conscious and flavoured by mustard and coconut. Pakhala Bhaat — rice soaked overnight in water — is one of the world's oldest fermented foods. Chhena Poda is a caramelised cottage cheese dessert — one of India's most unique sweets.",
        "Places to Visit": "Top places: Puri Jagannath Temple, Konark Sun Temple (UNESCO), Chilika Lake, Bhubaneswar (City of Temples), Simlipal National Park, Dhauli Buddhist Stupa, Bhitarkanika Mangroves, Rath Yatra (Puri).\n\nThe Konark Sun Temple — a 13th-century chariot-shaped temple — is one of the world's greatest architectural achievements. Chilika Lake is Asia's largest brackish water lake.",
        "Best Time": "October to February. Rath Yatra in Puri (June/July) is a once-in-a-lifetime spectacle. Konark Dance Festival (December) showcases classical Indian dance against the temple backdrop.",
        "Fun Facts": "• The English word 'Juggernaut' comes from Jagannath\n• Konark Sun Temple is called the 'Black Pagoda' by sailors\n• Odisha has 242 temples in Bhubaneswar alone\n• Odisha Rasagola has a GI tag separate from Bengal's Rosogolla\n• Chilika Lake hosts 160 species of migratory birds in winter",
    },
    "Sikkim": {
        "emoji": "🌸", "tag": "Himalayan Wonderland",
        "Overview": "Sikkim — India's smallest state by area — is arguably its most naturally spectacular. Sandwiched between Nepal, Bhutan, Tibet and West Bengal, it is home to Kangchenjunga — the world's third highest mountain. Sikkim was an independent Buddhist kingdom until 1975 and became India's first fully organic state in 2016.",
        "Food": "Must-try dishes: Phagshapa (pork with radish), Gundruk (fermented leafy greens), Momo (steamed dumplings), Thukpa (noodle soup), Chhurpi (hard cheese), Sel Roti (rice doughnut), Tongba (millet beer).\n\nSikkimese cuisine reflects its Nepali, Tibetan and Lepcha roots. Momo — steamed dumplings — are everywhere and deeply addictive. Tongba is a unique fermented millet drink served hot in a bamboo mug — ideal for cold mountain evenings.",
        "Places to Visit": "Top places: Kangchenjunga (world's 3rd highest peak), Gurudongmar Lake, Rumtek Monastery, Pelling & Kanchenjunga view, Tsomgo Lake (Changu Lake), Yumthang Valley (Valley of Flowers), Namchi, Ravangla Buddha Park.\n\nGurudongmar Lake at 17,100 ft is one of the world's highest lakes — sacred to Buddhists and Hindus. Yumthang Valley bursts into colour with rhododendrons in spring.",
        "Best Time": "March–May (rhododendron bloom) and October–December (clear mountain views). Losar (Tibetan New Year, February/March) is the biggest festival.",
        "Fun Facts": "• Sikkim was an independent Buddhist kingdom until 1975\n• India's first fully organic farming state (2016)\n• Kangchenjunga is the world's third highest mountain at 8,586m\n• Gurudongmar Lake is one of the world's highest lakes at 17,100 ft\n• Sikkim has over 600 species of orchids — highest density in India",
    },
}

TABS = ["Overview", "Food", "Places to Visit", "Best Time", "Fun Facts"]

# ── App ────────────────────────────────────────────────────────────────────────

class TourismApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Incredible India — State Tourism Guide")
        self.root.geometry("980x660")
        self.root.configure(bg="#f5f4f0")
        self.root.resizable(True, True)
        self.tts_engine = None
        self.speaking = False
        self.current_state = None
        self.current_tab = "Overview"
        self.filtered_names = list(STATES.keys())
        self._build_ui()

    def _build_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#1a3d2b", pady=14)
        header.pack(fill="x")
        tk.Label(header, text="🇮🇳  Incredible India — State Tourism Guide",
                 font=("Helvetica", 17, "bold"), bg="#1a3d2b", fg="white").pack()
        tk.Label(header, text="Overview · Food · Places to Visit · Best Time · Fun Facts",
                 font=("Helvetica", 10), bg="#1a3d2b", fg="#9fcfb5").pack()

        # Search bar
        sf = tk.Frame(self.root, bg="#f5f4f0", pady=8, padx=16)
        sf.pack(fill="x")
        tk.Label(sf, text="Search:", bg="#f5f4f0", font=("Helvetica", 11)).pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda *a: self._filter_list())
        tk.Entry(sf, textvariable=self.search_var, font=("Helvetica", 11),
                 relief="solid", bd=1, width=32).pack(side="left", padx=8)

        # Main layout
        main = tk.Frame(self.root, bg="#f5f4f0")
        main.pack(fill="both", expand=True, padx=16, pady=(0, 10))

        # Left pane — state list
        left = tk.Frame(main, bg="#f5f4f0")
        left.pack(side="left", fill="y")
        tk.Label(left, text="States", font=("Helvetica", 12, "bold"),
                 bg="#f5f4f0", anchor="w").pack(anchor="w", pady=(0, 6))
        lf = tk.Frame(left, bd=1, relief="solid", bg="white")
        lf.pack(fill="y", expand=True)
        sb = tk.Scrollbar(lf, orient="vertical")
        self.listbox = tk.Listbox(lf, yscrollcommand=sb.set, font=("Helvetica", 12),
                                  width=24, activestyle="none",
                                  selectbackground="#1D9E75", selectforeground="white",
                                  bd=0, highlightthickness=0, bg="white")
        sb.config(command=self.listbox.yview)
        sb.pack(side="right", fill="y")
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind("<<ListboxSelect>>", self._on_select)
        self._populate_list(list(STATES.keys()))

        # Right pane — detail
        right = tk.Frame(main, bg="#f5f4f0", padx=14)
        right.pack(side="left", fill="both", expand=True)

        # State title
        self.title_lbl = tk.Label(right, text="← Select a state to begin",
                                  font=("Helvetica", 16, "bold"), bg="#f5f4f0",
                                  fg="#1a3d2b", anchor="w", wraplength=520, justify="left")
        self.title_lbl.pack(anchor="w", pady=(0, 2))
        self.tag_lbl = tk.Label(right, text="", font=("Helvetica", 11, "italic"),
                                bg="#f5f4f0", fg="#5a8a6a", anchor="w")
        self.tag_lbl.pack(anchor="w", pady=(0, 8))

        # Tab bar
        self.tab_frame = tk.Frame(right, bg="#f5f4f0")
        self.tab_frame.pack(fill="x", pady=(0, 6))
        self.tab_btns = {}
        for t in TABS:
            btn = tk.Button(self.tab_frame, text=t, font=("Helvetica", 10),
                            relief="flat", bd=0, padx=10, pady=5,
                            bg="#e0ddd5", fg="#444", cursor="hand2",
                            command=lambda tab=t: self._switch_tab(tab))
            btn.pack(side="left", padx=2)
            self.tab_btns[t] = btn

        # Text area
        tf = tk.Frame(right, bd=1, relief="solid")
        tf.pack(fill="both", expand=True)
        self.text_area = scrolledtext.ScrolledText(
            tf, wrap="word", font=("Helvetica", 12), relief="flat",
            bg="white", fg="#222", padx=14, pady=12, state="disabled"
        )
        self.text_area.pack(fill="both", expand=True)

        # Speak buttons
        bf = tk.Frame(right, bg="#f5f4f0", pady=8)
        bf.pack(fill="x")
        self.speak_btn = tk.Button(
            bf, text="🔊  Read Aloud", font=("Helvetica", 11),
            bg="#1D9E75", fg="white", relief="flat", padx=14, pady=6,
            cursor="hand2", command=self._speak, state="disabled"
        )
        self.speak_btn.pack(side="left")
        self.stop_btn = tk.Button(
            bf, text="⏹  Stop", font=("Helvetica", 11),
            bg="#c0392b", fg="white", relief="flat", padx=12, pady=6,
            cursor="hand2", command=self._stop_speaking, state="disabled"
        )
        self.stop_btn.pack(side="left", padx=8)
        if not TTS_AVAILABLE:
            tk.Label(bf, text="Install pyttsx3 for text-to-speech",
                     font=("Helvetica", 9), bg="#f5f4f0", fg="#999").pack(side="left")

    def _populate_list(self, names):
        self.listbox.delete(0, "end")
        for name in names:
            s = STATES[name]
            self.listbox.insert("end", f"  {s['emoji']}  {name}")

    def _filter_list(self):
        q = self.search_var.get().lower()
        self.filtered_names = [
            n for n in STATES
            if q in n.lower() or q in STATES[n]["tag"].lower()
            or any(q in STATES[n][t].lower() for t in TABS)
        ]
        self._populate_list(self.filtered_names)

    def _on_select(self, event):
        sel = self.listbox.curselection()
        if not sel:
            return
        name = self.filtered_names[sel[0]]
        self._show_state(name)

    def _show_state(self, name):
        self._stop_speaking()
        self.current_state = name
        s = STATES[name]
        self.title_lbl.config(text=f"{s['emoji']}  {name}")
        self.tag_lbl.config(text=s["tag"])
        self.current_tab = "Overview"
        self._highlight_tab("Overview")
        self._render_tab("Overview")
        if TTS_AVAILABLE:
            self.speak_btn.config(state="normal")

    def _switch_tab(self, tab):
        self.current_tab = tab
        self._highlight_tab(tab)
        self._render_tab(tab)

    def _highlight_tab(self, active):
        for t, btn in self.tab_btns.items():
            if t == active:
                btn.config(bg="#1D9E75", fg="white")
            else:
                btn.config(bg="#e0ddd5", fg="#444")

    def _render_tab(self, tab):
        if not self.current_state:
            return
        content = STATES[self.current_state].get(tab, "")
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", content)
        self.text_area.config(state="disabled")

    def _speak(self):
        if not self.current_state or self.speaking:
            return
        self.speaking = True
        self.speak_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        text = STATES[self.current_state].get(self.current_tab, "")
        t = threading.Thread(target=self._tts_thread, args=(text,), daemon=True)
        t.start()

    def _tts_thread(self, text):
        try:
            engine = pyttsx3.init()
            self.tts_engine = engine
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass
        finally:
            self.speaking = False
            self.tts_engine = None
            self.root.after(0, self._reset_speak_btn)

    def _stop_speaking(self):
        if self.tts_engine:
            try:
                self.tts_engine.stop()
            except Exception:
                pass
        self.speaking = False
        self._reset_speak_btn()

    def _reset_speak_btn(self):
        if TTS_AVAILABLE and self.current_state:
            self.speak_btn.config(state="normal")
        self.stop_btn.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = TourismApp(root)
    root.mainloop()