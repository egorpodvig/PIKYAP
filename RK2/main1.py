from operator import itemgetter

class Detail:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Supplier:
    def __init__(self, id, name, salary, detail_id):
        self.id = id
        self.name = name
        self.salary = salary
        self.detail_id = detail_id

class SupplierDetail:
    def __init__(self, supplier_id, detail_id):
        self.supplier_id = supplier_id
        self.detail_id = detail_id



def task1(details, suppliers):
    result = [(detail.name, supplier.name)
              for detail in details
              for supplier in suppliers
              if supplier.detail_id == detail.id]
    return sorted(result, key=itemgetter(0))

def task2(details, suppliers):
    result = []
    for detail in details:
        total_salary = sum(supplier.salary for supplier in suppliers if supplier.detail_id == detail.id)
        result.append((detail.name, total_salary))
    return sorted(result, key=itemgetter(1), reverse=True)

def task3(details, suppliers, supplier_details):
    result = []
    for detail in details:
        if "деталь" in detail.name.lower():
            suppliers_in_detail = [supplier.name
                                   for supplier in suppliers
                                   for sd in supplier_details
                                   if sd.detail_id == detail.id and sd.supplier_id == supplier.id]
            result.append((detail.name, suppliers_in_detail))
    return result




def main():
    details = [
        Detail(1, "Деталь 1"),
        Detail(2, "Деталь 2"),
        Detail(3, "Сложная деталь"),
        Detail(4, "Простая деталь"),
    ]

    suppliers = [
        Supplier(1, "Поставщик А", 5000, 1),
        Supplier(2, "Поставщик Б", 3000, 2),
        Supplier(3, "Поставщик В", 4000, 3),
        Supplier(4, "Поставщик Г", 2000, 1),
        Supplier(5, "Поставщик Д", 2500, 4),
    ]

    supplier_details = [
        SupplierDetail(1, 1),
        SupplierDetail(2, 2),
        SupplierDetail(3, 3),
        SupplierDetail(4, 1),
        SupplierDetail(5, 4),
    ]

    print("Задание 1: Список связанных поставщиков и деталей, отсортированный по деталям:")
    print(task1(details, suppliers))

    print("\nЗадание 2: Список деталей с суммарной зарплатой поставщиков, отсортированный по суммарной зарплате:")
    print(task2(details, suppliers))

    print("\nЗадание 3: Список деталей, содержащих слово 'деталь', и работающих в них поставщиков:")
    print(task3(details, suppliers, supplier_details))

if __name__ == '__main__':
    main()
