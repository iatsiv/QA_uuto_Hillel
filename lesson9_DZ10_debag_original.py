"""
симулятор каси магазину
код, наведений нижче, приймає від покупця наступну інформацію
про закупівлю 2-х товарів
- назва
- кількість (ціле число)
- ціна за одиницю
на підставі отриманих даних формується чек
всі ціни та вартість мають бути виведені в форматі з копійками,
кількість - цілі числа
програма розрахована на використання на території України
"""
import textwrap
from datetime import datetime
from decimal import Decimal

def cash_register():
    # goods 1 section
    item_1_title = textwrap.shorten(input('Введіть назву першого товару: '),
                                    width=20, placeholder='...').ljust(20, ' ')
    item_1_quantity = int(input('Введіть бажаєму кількість першого товару: '))
    item_1_price = input('Введіть ціну першого товару, грн: ')

    # goods 2 section
    item_2_title = textwrap.shorten(input('Введіть назву другого товару: '),
                                    width=20, placeholder='...').ljust(20, ' ')
    item_2_quantity = int(input('Введіть бажаєму кількість другого товару: '))
    item_2_price = input('Введіть ціну другого товару, грн: ')

    item_1_total_cost = Decimal(item_1_quantity) * Decimal(item_1_price)
    item_1_total_cost_right_format = item_1_total_cost.quantize(Decimal('0.01'))

    item_2_total_cost = Decimal(item_2_quantity) * Decimal(item_2_price)
    item_2_total_cost_right_format = item_2_total_cost.quantize(Decimal('0.01'))

    total_cost_right_format = item_1_total_cost_right_format + \
                              item_2_total_cost_right_format
    total_quantity = item_1_quantity + item_2_quantity

    printing_template = '{}\t\t\t\t\t{}\t\t\t\t{}\t\t\t{}'

    # printing receipt
    print('\n\n\n')
    print('фіскальний чек'.capitalize().center(80, '~'))
    print('магазин "все для дому"'.upper().center(80))
    print('Товар\t\t\t\t\t\t\t\t\tкількість\t\tціна\t\tвартість')
    print(printing_template.format(item_1_title, item_1_quantity,
                                   item_1_price, item_1_total_cost_right_format))
    print(printing_template.format(item_2_title, item_2_quantity,
                                   item_2_price, item_2_total_cost_right_format))
    print('~' * 80)
    print(printing_template.format(
        'ВСЬОГО'.ljust(20),
        total_quantity,
        'x',
        total_cost_right_format
        )
    )
    print(datetime.now().strftime('%d-%m-%Y %H:%M:%S').rjust(80))
    print('\n\n')


cash_register()