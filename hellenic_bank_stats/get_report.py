# -*- coding: utf-8 -*-

import xlrd


wb = xlrd.open_workbook('download.xls')
ws = wb.sheet_by_index(0)
reason = 'report'
i = 1
total_sum = 0
total_sum_not_parced = 0

groups = [{'search': 'ATM ', 'total': 0, 'reason': 'ATM, cash'},
          {'search': 'EDCY', 'total': 0, 'reason': 'ATM, cash'},
          {'search': 'ENCY', 'total': 0, 'reason': 'ATM, cash'},
          {'search': 'CASH ADVANCE', 'total': 0, 'reason': 'commision'},
          {'search': 'Currency Conversion', 'total': 0, 'reason': 'commision'},
          {'search': 'BOLT.EU', 'total': 0, 'reason': 'Taxi'},
          {'search': 'FRENCH DEPOT', 'total': 0, 'reason': 'Wine (FrenchDeport)'},
          {'search': 'WWW.FOODY.COM.CY', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'GLORIA JEANS', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'THIMARI', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'RIO BRAVO', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'PIZZA HUT', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'LAVERANDA RESTAURANT', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'LAVERANDA RESTAURANT', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'THE WOODMAN (PUBS)', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'PAGODA', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'ORDER WO', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'SALUT', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'SYRIAN RESTAURANT', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'STEPHANOS OASIS', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'DO WINE & DINE', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'SCANDINAVIA', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'MOLLY MA', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'MEZEDOPOLIO', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'COLUMBIA BEACH', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'BISTROT 55', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'DA & COV', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'OINEAS', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'TEPEE ROCK CLUB', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'TO KAFE TIS CHRYSANT', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'NERO ELEFTHERIAS', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'KAMARA', 'total': 0, 'reason': 'Restaurants'},
          {'search': 'LC IN TOWN', 'total': 0, 'reason': 'Launch at work'},
          {'search': 'ALPHAMEGA', 'total': 0, 'reason': 'ALPHAMEGA'},
          {'search': 'KOUZINA LINOPETRA', 'total': 0, 'reason': 'Launch at work'},
          {'search': 'PETROXTISTO', 'total': 0, 'reason': 'Business launch'},
          {'search': 'COYA RESTAURANT', 'total': 0, 'reason': 'Business launch'},
          {'search': 'MANNEKEN', 'total': 0, 'reason': 'Business launch'},
          {'search': 'HOMUTO V', 'total': 0, 'reason': 'Business launch'},
          {'search': 'V Kolkov', 'total': 0, 'reason': 'Business launch'},
          {'search': 'JSC LENR', 'total': 0, 'reason': 'Business launch'},
          {'search': 'BOHO RESTOBAR', 'total': 0, 'reason': 'Business launch'},
          {'search': 'BRUXX', 'total': 0, 'reason': 'Business launch'},
          {'search': 'BRYNZA', 'total': 0, 'reason': 'Business launch'},
          {'search': 'RUMOURS', 'total': 0, 'reason': 'Business launch'},
          {'search': 'TSEH 85', 'total': 0, 'reason': 'Launch at work'},
          {'search': '"TSEH 85', 'total': 0, 'reason': 'Launch at work'},
          {'search': 'CYTA', 'total': 0, 'reason': 'CYTA mobile'},
          {'search': 'YPERAGORA', 'total': 0, 'reason': 'Market'},
          {'search': 'PAPAS HYPERMARKET', 'total': 0, 'reason': 'Market'},
          {'search': 'PERIPTERO', 'total': 0, 'reason': 'Market'},
          {'search': 'SKLAVENITIS COLUMBIA', 'total': 0, 'reason': 'Market'},
          {'search': 'MAGAZIN', 'total': 0, 'reason': 'Market'},
          {'search': 'SHOP & GO', 'total': 0, 'reason': 'SHOP & GO'},
          {'search': 'ELECTROLINE', 'total': 0, 'reason': 'ELECTROLINE shop'},
          {'search': 'NETFLIX', 'total': 0, 'reason': 'Netflix'},
          {'search': 'PHARMA', 'total': 0, 'reason': 'Pharmacy'},
          {'search': 'WATERBOARD', 'total': 0, 'reason': 'Common expenses'},
          {'search': 'EAC ', 'total': 0, 'reason': 'Common expenses'},
          {'search': 'CABLENET', 'total': 0, 'reason': 'Common expenses'},
          {'search': 'AEROFLOT', 'total': 0, 'reason': 'Travels'},
          {'search': 'LOKAL HOTEL', 'total': 0, 'reason': 'Hotels'},
          {'search': 'LONDA HOTEL', 'total': 0, 'reason': 'Hotels'},
          {'search': 'LOUIS LEDRA BEACH', 'total': 0, 'reason': 'Hotels'},
          {'search': 'CRYSTAL COVE HOTEL', 'total': 0, 'reason': 'Hotels'},
          {'search': 'HYPNOS BY', 'total': 0, 'reason': 'Hotels'},
          {'search': 'Classic ', 'total': 0, 'reason': 'Hotels'},
          {'search': 'NETFIXED', 'total': 0, 'reason': 'Saved money'},
          {'search': 'INVITRO', 'total': 0, 'reason': 'Invitro'},
          {'search': 'RIO CINE', 'total': 0, 'reason': 'Ignore, refunded'},
          {'search': 'SEAFARE RESTAURANT', 'total': 0, 'reason': 'Ignore, refunded'},
          {'search': 'RIO CINE', 'total': 0, 'reason': 'Ignore, refunded'},
          {'search': 'LIMASSOL SPORTING', 'total': 0, 'reason': 'Ignore, refunded'},]

while reason:
    reason = None

    try:
        reason = ws.cell(i, 4).value
        price = ws.cell(i, 5).value

        total_sum += price
        reason_found = False

        for r, _ in enumerate(groups):
            if reason.startswith(groups[r]['search']):
                groups[r]['total'] += price
                reason_found = True
                break

        if not reason_found:
            total_sum_not_parced += price
            print(reason, price)
    except:
        pass

    i += 1

print('Total sum:', total_sum)
print('Total sum not parsed:', total_sum_not_parced)

titled = {}

for g in groups:
    r = g['reason']
    p = g['total']
    if r in titled:
        titled[r] += p
    else:
        titled[r] = p

titled['Other'] = total_sum_not_parced

for k, v in sorted(titled.items(), key=lambda x: x[1], reverse=True):
    if 'Ignore' not in k:
        print('{0:30} | {1:7.0f} euro  | {2:.2f}%'.format(k, v, 100.0*v/total_sum))

