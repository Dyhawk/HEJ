from inventory.models import Inventory


def internal_sku(sup_num):
    qs = Inventory.objects.filter(internalsku__startswith=str(sup_num))
    sku_list = []
    if len(qs)>0:
        for item in qs:
            sku_list.append(item.internalsku)
        highest = max(sku_list)
        highest_value = str(int(highest[3:])+1)
        zeros = (8 - len(highest_value))-3
        string = str(sup_num)+'0'*zeros+highest_value
        return str(string)
    else:
        string = str(sup_num)+'00001'
        return str(string)

def totals(entry_cost, inv_list):
    total_num = 0
    total_cost = 0.00
    for item in inv_list:
        total_num += int(item.quantity)
    for item in inv_list:
        total_cost += float(item.cost)

    dif = float(entry_cost) - total_cost

    totals = {'total_num': total_num, 'total_cost':total_cost,
     'difference': dif}

    return totals
