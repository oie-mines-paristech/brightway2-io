GEO_UPDATE = {
    "Al producing Area 2, North America": "IAI Area 2, North America",
    "IAI Area 2, North America": "IAI Area 2, North America",
    "IAI Area, North America, without Quebec": "IAI Area 2, without Quebec",
    "IAI Area 1": "IAI Area 1, Africa",
    "IAI Area, Africa": "IAI Area 1, Africa",
    "IAI Area 3": "IAI Area, South America",
    "IAI Area, South America": "IAI Area, South America",
    "IAI Area 4&5 without China": "IAI Area 4&5, without China",
    "IAI Area, Asia, without China and GCC": "IAI Area 4&5, without China",
    "IAI Area 6A": "IAI Area 6, Europe",
    "IAI Area, Europe outside EU & EFTA": "IAI Area 6, Europe",
    "IAI Area 8": "IAI Area 8, Gulf",
    "IAI Area, Gulf Cooperation Council": "IAI Area 8, Gulf",
    "IAI Area, West Europe": "IAI Area, EU27 & EFTA",
    "IAI Area, Russia & RER w/o EU27 & EFTA": "IAI Area, Europe outside EU & EFTA",
    "Ashmore and Cartier Islands": "AUS-AC",
    "Indian Ocean Territories": "AUS-IOT",
    "CC": "AUS-IOT",
    "CX": "AUS-IOT",
    "ROC": "Canada without Quebec",
    "MRO, US only": "US-MRO",
    "NPCC, US only": "US-NPCC",
    "WECC, US only": "US-WECC",
    "CSG": "CN-CSG",
    "SGCC": "CN-SGCC",
    "FRCC": "US-FRCC",
    "HICC": "US-HICC",
    "RFC": "US-RFC",
    "SERC": "US-SERC",
    "SPP": "US-SPP",
    "TRE": "US-TRE",
    "ASCC": "US-ASCC",
}


def update_ecoinvent_locations(db):
    """Update old ecoinvent location codes"""
    for ds in db:
        if 'location' in ds:
            ds['location'] = GEO_UPDATE.get(ds['location'], ds['location'])
    return db
